#!/usr/bin/python3.12

from sys import argv
from socket import create_connection
from ssl import *

client_key = 'client.key'
client_cert = 'client.crt'

server_cert = 'server.crt'


def run_tls_client(host, port):
    context = SSLContext(PROTOCOL_TLS, cafile=server_cert)
    context.load_cert_chain(certfile=client_cert, keyfile=client_key)

    context.load_verify_locations(cafile=server_cert)

    context.verify_mode = CERT_REQUIRED
    context.options |= OP_SINGLE_ECDH_USE
    context.options |= OP_NO_TLSv1 | OP_NO_TLSv1_1 | OP_NO_TLSv1_2

    with create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_side=False, server_hostname=host) as tls_socket:
            print(tls_socket.version())

        client_message = input("\n\tEnter your message: ")
        tls_socket.send(client_message.encode())

        received = tls_socket.recv(1024)
        print(received)


run_tls_client(argv[1], argv[2])        #In terminal example: sudo python tls_client.py <SERVER IP> 8080
