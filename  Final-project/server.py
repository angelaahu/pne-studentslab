import http.server
import socketserver
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import json
from Seq1 import Seq


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

def get_data(endpoint):
    SERVER = "rest.ensembl.org"
    PARAMS = "?content-type=application/json"
    conn = http.client.HTTPSConnection(SERVER)
    conn.request("GET", endpoint + PARAMS)
    response = conn.getresponse()
    dict_data = json.loads(response.read().decode())
    return dict_data

IP = "127.0.0.1"
PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        print(self.requestline)

        url_path = urlparse(self.path)
        path = url_path.path
        print(path)
        arguments = parse_qs(url_path.query)
        print(arguments)

        #JSON
        try:
            if "json" in arguments:
                json_arg = arguments["json"][0]
                if json_arg == "1":
                    content_type = "application/json"
                else:
                    content_type = "text/html"
            else:
                json_arg = "0"
                content_type = "text/html"

        except KeyError:
            json_arg = "0"
            content_type = "text/html"



        try:

            SERVER = "rest.ensembl.org"
            PARAMS = "?content-type=application/json"

            status_num = 200
            if path == "/":
                contents = Path("html/index.html").read_text()

            elif path == "/listSpecies":
                ENDPOINT = "/info/species"
                data = get_data(ENDPOINT)

                print("URL:", SERVER + ENDPOINT + PARAMS)

                species = data["species"]
                species_lst = []
                for index, dict in enumerate(species):
                    specie_name = dict["display_name"]
                    species_lst.append(specie_name)
                print(species_lst)

                if "limit" in arguments:
                    limit = arguments["limit"]
                    limit_number = int(limit[0])

                    if 1 <= limit_number <= len(species_lst):
                        selected_species = species_lst[:limit_number]
                    else:
                        selected_species = species_lst

                else:
                    # limit_number = len(species_lst)
                    selected_species = species_lst

                if json_arg == "1":
                    dct = {"Species": selected_species}
                    contents = json.dumps(dct)
                else:
                    contents = read_html_file("species.html").render(specie="<br>".join(selected_species), length=len(selected_species), total=len(species_lst))

            elif path == "/karyotype":
                if "species" in arguments:
                    species = str(arguments["species"][0])

                    ENDPOINT = "/info/assembly/"
                    SPECIES = species.replace(" ", "%20").lower()

                    print("URL:", SERVER + ENDPOINT + SPECIES + PARAMS)

                    data = get_data(ENDPOINT + SPECIES)

                    karyotype_list = data["karyotype"]
                    karyotype = ", ".join(karyotype_list)

                    if json_arg == "1":
                        dct = {"Specie": species,"Karyotype": karyotype}
                        contents = json.dumps(dct)

                    else:
                        contents = read_html_file("karyotype.html").render(karyotype="<br>".join(karyotype_list), specie=species)

                    # print(data)
                    # print(karyotype)



                else:
                    contents = Path("html/error.html").read_text()
                    content_type = "text/html"


            elif path == "/chromosomeLength":
                if "species" and "chromo" in arguments:
                    species = str(arguments["species"][0])
                    chromo = int(arguments["chromo"][0])

                    ENDPOINT = "/info/assembly/"
                    SPECIES = species.replace(" ", "%20").lower()
                    print("URL:", SERVER + ENDPOINT + SPECIES + PARAMS)

                    data = get_data(ENDPOINT + SPECIES)
                    # chromo_dict = {"chromosome": number, "name", top_level_region}

                    chromosomes_data = data["top_level_region"]
                    print(chromosomes_data)

                    chromosome = chromosomes_data[chromo - 1]
                    chromo_len = chromosome["length"]
                    # print(chromo_len)

                    if json_arg == "1":
                        dct = {"Chromosome": chromo, "Length": chromo_len}
                        contents = json.dumps(dct)
                    else:
                        contents = read_html_file("/chromosome-length.html").render(chromolen=chromo_len, chrome=chromo, species=species)

                else:
                    contents = Path("html/error.html").read_text()

                # MEDIUM EXERCISES FROM HERE
            elif path == "/geneLookup":

                if "gene" in arguments:
                    gene = arguments["gene"][0]
                    ENDPOINT = f"/lookup/symbol/homo_sapiens/{gene}"
                    print("URL:", SERVER + ENDPOINT + PARAMS)
                    data = get_data(ENDPOINT)
                    print(data)
                    ID = data["id"]

                    if json_arg == "1":
                        dct = {"Ensembl ID": ID}
                        contents = json.dumps(dct)

                    else:
                        contents = read_html_file("medium-gene-id.html").render(id=ID, gene=gene)


            elif path == "/geneSeq":
                if "gene" in arguments:
                    gene = arguments["gene"][0]

                    ENDPOINT_1 = f"/lookup/symbol/homo_sapiens/{gene}"
                    data1 = get_data(ENDPOINT_1)
                    ID = data1["id"]

                    ENDPOINT_2 = f"/sequence/id/{ID}"
                    print("URL:", SERVER + ENDPOINT_2 + PARAMS)
                    data2 = get_data(ENDPOINT_2)
                    # print(data2)

                    seq = data2["seq"]

                    if json_arg == "1":
                        dct = {"GeneSequence": seq}
                        contents = json.dumps(dct)
                    else:
                        contents = read_html_file("medium-sequence.html").render(sequence=seq)



            elif path == "/geneInfo":
                if "gene" in arguments:
                    gene = arguments["gene"][0]

                    ENDPOINT1 = f"/lookup/symbol/homo_sapiens/{gene}"
                    print("URL:", SERVER + ENDPOINT1 + PARAMS)

                    data = get_data(ENDPOINT1)

                    start = data["start"]
                    chromosome_number = data["seq_region_name"]
                    end = data["end"]
                    gene_name = data["display_name"]
                    gene_id = data["id"]

                    ENDPOINT_2 = f"/sequence/id/{gene_id}"
                    print("URL:", SERVER + ENDPOINT_2 + PARAMS)

                    data2 = get_data(ENDPOINT_2)

                    seq = data2["seq"]
                    chromo_name = data2["desc"]
                    gene_len = len(seq)

                    if json_arg == "1":
                        dct = {"Start": start,
                               "End": end,
                               "Length": gene_len,
                               "ID": gene_id,
                               "ChromosomeName": chromosome_number, }
                        contents = json.dumps(dct)
                    else:
                        contents = read_html_file("medium-info.html").render(start=start, end=end, length=gene_len, id=gene_id, chromo_name=chromosome_number, gene=gene_name)



            elif path == "/geneCalc":
                if "gene" in arguments:
                    gene = arguments["gene"][0]

                    ENDPOINT_1 = f"/lookup/symbol/homo_sapiens/{gene}"
                    data = get_data(ENDPOINT_1)
                    print("URL:", SERVER + ENDPOINT_1 + PARAMS)

                    gene_name = data["display_name"]
                    ID = data["id"]
                    ENDPOINT_2 = f"/sequence/id/{ID}"
                    print("URL:", SERVER + ENDPOINT_2 + PARAMS)
                    data2 = get_data(ENDPOINT_2)
                    # print(data2)

                    seq = data2["seq"]

                    sequence = Seq(seq)
                    seq_len = sequence.len()
                    seq_bases_count = sequence.count()

                    print(seq_bases_count)

                    result = ""
                    for key, value in seq_bases_count.items():
                        percentage = round((value / seq_len) * 100, 2)
                        result += f"Base: {key} - Percentage: {percentage}%<br>"

                    if json_arg == "1":
                        dct = {"GeneName": gene_name,
                               "Total length": seq_len,
                               "Percentage": seq_bases_count}
                        contents = json.dumps(dct)
                    else:
                        contents = read_html_file("medium-calculations.html").render(length=seq_len, percentage=result, gene=gene_name)



            elif path == "/geneList":
                if "chromo" and "start" and "end" in arguments:
                    chromosome_region = arguments["chromo"][0]
                    start_region = arguments["start"][0]
                    end_region = arguments["end"][0]

                    ENDPOINT = f"/overlap/region/human/{chromosome_region}:{start_region}-{end_region}"
                    FEATURES = f";feature=gene;feature=transcript;feature=cds;feature=exon"
                    print("URL:", SERVER + ENDPOINT + PARAMS + FEATURES)

                    conn = http.client.HTTPSConnection(SERVER)
                    conn.request("GET", ENDPOINT + PARAMS + FEATURES)
                    response = conn.getresponse()
                    dict_data = json.loads(response.read().decode())
                    print(dict_data)

                    gene_id_list = []
                    for i, item in enumerate(dict_data):
                        gene_id = item["id"]
                        gene_id_list.append(gene_id)

                    print(gene_id_list)

                    names_lst = []
                    for id in gene_id_list:
                        endpoint = f"/lookup/id/{id}"
                        print(SERVER + endpoint + PARAMS)
                        data = get_data(endpoint)
                        if "display_name" in data:
                            gene_name = data.get("display_name")
                        else:
                            gene_name = "Not found"

                        names_lst.append(gene_name)
                    print(names_lst)

                    names_of_the_genes = "<br>".join(names_lst)

                    # result = ""
                    # for gene_id, gene_name in zip(gene_id_list, names_lst):
                    #    result += f"ID: {gene_id} | Name: {gene_name} <br>"

                    # dct = {"id": "<br>".join(gene_id_list), "name": names_of_the_genes }
                    # result = f"ID: {dct['id']} | Name: {dct['name']} <br>"

                    if json_arg == "1":
                        dct = {"Chromosome": chromosome_region,
                               "Start": start_region,
                               "End": end_region,
                               "Genes": names_lst}
                        contents = json.dumps(dct)
                    else:
                        contents = read_html_file("medium-overlap-gene-list.html").render(chromo=chromosome_region, start=start_region, end=end_region, gene_list=names_of_the_genes)

            else:
                status_num = 404
                contents = Path("html/error.html").read_text()

        except KeyError:
            status_num = 404
            contents = Path("html/error.html").read_text()

        except ValueError:
            status_num = 404
            contents = Path("html/error.html").read_text()

            # Generating the response message
        self.send_response(status_num)  # -- Status line: OK

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()