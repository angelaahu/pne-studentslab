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

gene_name = "MIR633"

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id"
GENE = "/" + genes[gene_name]
PARAMS = "?content-type=application/json"

print()
print("Server:", SERVER)
print("URL:", SERVER + ENDPOINT + GENE + PARAMS)

conn = http.client.HTTPSConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + GENE + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()

print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode("utf-8")
response = json.loads(data1)

print(f"Gene: {gene_name}\n"
      f"Description: {response["desc"]}\n"
      f"Bases: {response["seq"]}")
