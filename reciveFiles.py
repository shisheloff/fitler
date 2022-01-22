import os
import socket
import bin.syslog
print(os.path.abspath("auth_logs.txt"))
ip_host = "0.0.0.0"
server_port = 514
BufferSize = 4096
recived_filename = ""

def reciveFile():
    sc = socket.socket()

    sc.bind((ip_host, server_port))

    sc.listen(10)

    print(f"[INFO] Server listening as {ip_host}:{server_port}")

    client_socket, address = sc.accept()

    print(f"[+] {address} is connected.")

    recivedFilename = client_socket.recv(BufferSize).decode()

    recivedFilename = os.path.basename(recivedFilename)
    with open(recivedFilename, 'wb') as f:
        print(f"[INFO] reciving file: {recivedFilename} ")
        while True:
            bytesRead = client_socket.recv(BufferSize)
            if not bytesRead:
                break
            f.write(bytesRead)
        print(f"[INFO] recieved file {recivedFilename} successfully!")
    client_socket.close()
    sc.close()

    with open(recived_filename, "r") as f:
        data = f.readlines()
        for lines in data:
            print(bin.syslog.parser(lines))

reciveFile()

