from Client0 import Client

PORT = 8080
IP = "212.128.255.68"

c = Client(IP, PORT)

for i in range(5):
    msg = c.talk(f"Message{i}")
    print(f"To server: Message{i}")
    print(f"From server: ECHO: Message {msg}")