import http.server
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"

print()
print("Server:", SERVER)
print("URL:", SERVER + ENDPOINT + PARAMS)

print(f"\nConnecting to server: {SERVER}")

# Connect with the server
conn = http.client.HTTPSConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")
# -- Read the response's body
data1 = r1.read().decode("utf-8")
# -- Create a variable with the data,
# -- form the JSON received
response = json.loads(data1)

if response["ping"] == 1:
    print("ALIVE! PING OK! The database is running")