import socket
import os

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("localhost", 17209))
conn.listen(100)

while True:
    try:
        client, _ = conn.accept()
        while True:
            data = client.recv(100)
            print(data)
    except Exception:
        pass
