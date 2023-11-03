import socket


def start_server(local_ip='localhost', port=4242):
    """
    Start a TCP server that listens for incoming client connections.
    """
    # Create a TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the local_ip and port
    server_address = (local_ip, port)
    server.bind(server_address)

    while True:
        # Listen for incoming client connections
        server.listen(1)

        print('Waiting for a client to connect...')
        client, client_address = server.accept()
        print(f'Connection from client {client_address[0]}:{client_address[1]}')

        # Receive request from the client
        request = client.recv(100)
        print(f'Client sent: "{request.decode()}"')
        reply = b"Who's there?"
        print(f'Server replies: "{reply.decode()}"\n')
        client.sendall(reply)

        # Close the connection
        client.close()


def main():
    """"""
    local_ip = 'SERVER IP ADDRESS'
    start_server(local_ip)


if __name__ == '__main__':
    main()
