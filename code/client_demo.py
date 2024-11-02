import socket


def start_client(server_ip="localhost", port=4242):
    """
    Start a TCP client that connects to a server.
    """
    # Create and connect the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        print(f"Connecting to server {server_ip}:{port}...")
        client.connect((server_ip, port))

        # Send request message
        message = b"Knock, knock"
        print(f'Client sending: "{message.decode()}"')
        client.sendall(message)

        # Receive reply from the server
        reply = client.recv(100)
        print(f'Client received: "{reply.decode()}"')


def main():
    server_ip = "SERVER IP ADDRESS"
    start_client(server_ip)


if __name__ == "__main__":
    main()
