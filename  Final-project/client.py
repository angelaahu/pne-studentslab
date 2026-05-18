import http.client
import json


PORT = 8080
SERVER = "localhost"

print(f"\nConnecting to server: {SERVER}:{PORT}\n")


url_list = ["/listSpecies?limit=10",
"/listSpecies?",
"/karyotype?species=mouse",
"/karyotype?species=Shrew+mouse",
"/chromosomeLength?species=mouse&chromo=18",
"/geneLookup?gene=FRAT1",
"/geneSeq?gene=FRAT1",
"/geneInfo?gene=FRAT1",
"/geneCalc?gene=FRAT1",
"/geneList?chromo=9&start=22125500&end=22136000"]


for index, url in enumerate(url_list):
    conn = http.client.HTTPConnection(SERVER, PORT)
    url_json = f"{url}&json=1"

    try:
        conn.request("GET", url_json)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    response_num = r1.status

    print(f"Response received!: {response_num} {r1.reason}\n")


    if response_num == 200:
        data1 = r1.read().decode("utf-8")
        data_dict = json.loads(data1)
        count = index + 1

        print(f"Response {count}: {url_json}")

        for key, value in data_dict.items():
            print(f"{key}:")
            if type(value) is list:
                for item in value:
                    print(f"{item}")

            else:
                print(f"{value}")

    elif response_num == 400:
        print("ERROR! Cannot connect to the Server")
        exit()


