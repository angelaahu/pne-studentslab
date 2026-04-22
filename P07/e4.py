from Seq1 import Seq
import http.server
import json

genes = {"FRAT1": "ENSG00000165879",
         "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552",
         "TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052",
         "ANK2": "ENSG00000145362"
         }

try:
    gene_name = input("Write the gene name: ").upper()
    if gene_name in genes:
        SERVER = "rest.ensembl.org"
        ENDPOINT = "/sequence/id"
        GENE = "/" + genes[gene_name]
        PARAMS = "?content-type=application/json"

        print()
        print("Server:", SERVER)
        print("URL:", SERVER + ENDPOINT + GENE + PARAMS)
        conn = http.client.HTTPSConnection(SERVER)
        conn.request("GET", ENDPOINT + GENE + PARAMS)
        r1 = conn.getresponse()
        print(f"Response received!: {r1.status} {r1.reason}\n")
        data1 = r1.read().decode("utf-8")
        response = json.loads(data1)

        seq = response["seq"]
        s = Seq(seq)
        seq_len = s.len()
        print(f"Gene: {gene_name}\n"
              f"Description: {response["desc"]}\n"
              f"Total length: {seq_len}")

        bases_info = s.count()
        for key, value in bases_info.items():
            percentage = round((value / seq_len) * 100, 1)
            print(f"{key}: {value} ({percentage})%")






    else:
        print(f"{gene_name} not a valid gene name")


except KeyError:
    print("Not valid")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

