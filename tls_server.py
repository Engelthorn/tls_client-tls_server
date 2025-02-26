#!/usr/bin/python3.12


from sys import argv
from ssl import *
from socket import socket, AF_INET, SOCK_STREAM

server_key = 'server.key'
server_cert = 'server.crt'

client_cert = 'client.crt'


def run_tls_server(port):
    context = create_default_context(Purpose.CLIENT_AUTH)
    context.verify_mode = CERT_REQUIRED
    context.load_verify_locations(cafile=client_cert)
    context.load_cert_chain(certfile=server_cert, keyfile=server_key)

    context.options |= OP_SINGLE_ECDH_USE
    context.options |= OP_NO_TLSv1 | OP_NO_TLSv1_1 | OP_NO_TLSv1_2

    with socket(AF_INET, SOCK_STREAM, 0) as tls_socket:
        tls_socket.bind(('', port))
        tls_socket.listen(1)
        print("\n----------------------------------------------------------"
              "\n [!] TLS Server is listening for the incoming connections..."
              "\n[!] Press CTRL + C to stop")

        with context.wrap_socket(tls_socket, server_side=True) as server_socket:
            client_connection, client_ip = server_socket.accept()
            print(f"\n\n\t[+] Get connection from: {client_ip[0]}: {client_ip[1]}!")

            message = client_connection.recv(1024).decode()
            message_for_client = message.upper()
            client_connection.send(message_for_client.encode())


run_tls_server(argv[1])         #In terminal example: sudo python tls_server.py 8080
