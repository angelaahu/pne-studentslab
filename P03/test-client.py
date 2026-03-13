from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 8080
IP = "127.0.0.1"

c = Client(IP, PORT)
print(str(c))

commands = ["GET", "INFO", "COMP", "REV", "GENE"]
genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]

print("* Testing PING...")
response = c.talk("PING")
print(response)

for command in commands:
    if command == "GET":
        print("* Testing GET...")
        for i in range(0,5):
            response = c.talk(f"GET {i}").strip()
            print(f"GEN {i}: {response}")

            if i == 0:
                seq0 = response
                seq = seq0
        print()

    elif command == "INFO" or command == "COMP" or command == "REV":
        print(f"* Testing {command}...")
        response = c.talk(f"{command} {seq}")
        print(response)


    elif command == "GENE":
        print("\n* Testing GENE...")
        for gene in genes:
            response = c.talk(f"GENE {gene}")
            print(f"GENE {gene}\n{response}")