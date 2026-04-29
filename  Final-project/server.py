import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import json

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

        elif path == "/listSpecies":
            SERVER = "rest.ensembl.org"
            ENDPOINT = "/info/species"
            #VAR = "/species"
            PARAMS = "?content-type=application/json"
            URL = SERVER + ENDPOINT + PARAMS
            print("URL:", URL)

            conn = http.client.HTTPSConnection(SERVER)
            conn.request("GET", ENDPOINT + PARAMS)

            response = conn.getresponse()
            data = json.loads(response.read().decode())

            species = data["species"]
            species_dict = dict(enumerate(species))

            for key, value in species_dict:

                key["displa"]
                return key, value

            #value = species_dict["display_name"]
            contents = read_html_file("species.html").render(species=value)


            #if "number" in arguments:
             #   number = int(arguments["listSpecies"][0])
              #  print(number)
                #value = species[number]
                #contents = read_html_file("species.html").render(species=value)

            #for index, species_dict in enumerate(species):
             #   for key, value in species_dict.items:
              #      if key == "display_name":
               #         contents = read_html_file("species.html").render(species=value)
#
 #               return contents


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