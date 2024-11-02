import socket


def start_server(host=None, port=4242):
    """
    Start a TCP server that listens for incoming client connections.
    """
    # Automatically get the host IP if not provided
    if host is None:
        host = socket.gethostbyname(socket.gethostname())

    # Create and bind the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen(1)
        print(f"Server listening on {host}:{port}...")

        while True:
            print("Waiting for a client to connect...")
            client, client_address = server.accept()
            with client:
                print(f"Connection from client {client_address[0]}:{client_address[1]}")

                # Receive request from the client
                request = client.recv(100)
                print(f'Client sent: "{request.decode()}"')
                reply = b"Who's there?"
                print(f'Server replies: "{reply.decode()}"\n')
                client.sendall(reply)


def main():
    start_server()

    # server_ip = "localhost"  # Replace with your actual public IP address
    # start_server(host=server_ip)


if __name__ == "__main__":
    main()
