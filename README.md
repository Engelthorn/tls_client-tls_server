# tls_client-tls_server
A secure model of Client/Server. Client sends an encrypted message to the server. The server will listen for incoming connections. Configured to support only one connection.Don't forget to generate keys and certificates to both sides. Ex: openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 ➥ -keyout server.key -out server.crt. 
