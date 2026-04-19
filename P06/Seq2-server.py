import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
from Seq1 import Seq

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path
        print(path)
        arguments = parse_qs(url_path.query)
        print(arguments)


        status_num = 200
        if path == "/":
            contents = Path("html/index.html").read_text()

        elif path == "/ping":
            contents = Path("html/ping.html").read_text()

        elif path == "/get":
            sequences = ["ACCCCGGTAGACTA", "GGACCGTTATGAAC", "CCCTTTGAAAAGATAA",
                         "AGACGCACATAAAA", "TTTTTTAATGGAAAAA"]

            if "operation" in arguments:
                number = int(arguments["operation"][0])
                seq = sequences[number]
                dct = {"operation": number, "seq": seq}
                contents = read_html_file("get.html").render(dct)

        elif path == "/gene":
            U5 = Path("sequences/U5.txt").read_text()
            ADA = Path("sequences/ADA.txt").read_text()
            FRAT1 = Path("sequences/FRAT1.txt").read_text()
            RNU6_269P = Path("sequences/RNU6_269P.txt").read_text()
            FXN = Path("sequences/FXN.txt").read_text()

            genes = {"U5": U5, "ADA": ADA, "FRAT1": FRAT1, "RNU6_269P": RNU6_269P, "FXN": FXN}
            if "name" in arguments:
                gene_name = arguments["name"]
                gene_name = gene_name[0]

                if gene_name in genes:
                    seq = genes[gene_name].split("\n")
                    sequences = seq[1:]
                    gene_seq = "".join(sequences)
                    contents = read_html_file("gene.html").render(name=gene_name, gene=gene_seq)

        elif path == "/operate":
            seq = arguments["msg"][0]
            operation = arguments["operation"][0]
            sequence = Seq(seq)

            if operation == "Rev":
                result = seq[::-1]

            elif operation == "Comp":
                seq_comp = sequence.complement()
                result = seq_comp

            elif operation == "Info":
                seq_len = sequence.len()
                result = (f"Total length: {seq_len}\n")
                bases_info = sequence.count()
                for key, value in bases_info.items():
                    percentage = round((value / seq_len) * 100, 1 )
                    result += (f"\t{key}: {value} ({percentage})%\n")

            contents = read_html_file("operation.html").render(sequence=seq, operation=operation, result=result)

        else:
            status_num = 404
            contents = Path("html/error.html").read_text()

        # Generating the response message
        self.send_response(status_num)  # -- Status line: OK

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
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