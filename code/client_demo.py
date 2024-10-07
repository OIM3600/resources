import socket


def start_client(server_ip="localhost", port=4242):
    """
    Start a TCP client that connects to a server.
    """
    # Create a TCP/IP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server using the server_ip and port
    server_address = (server_ip, port)
    print(f"Connecting to server {server_address[0]}:{server_address[1]}")
    client.connect(server_address)

    # Send request message
    message = b"Knock, knock"
    print(f'Client sending: "{message.decode()}"')
    client.sendall(message)

    # Receive reply from the server
    reply = client.recv(100)
    print(f'Client received: "{reply.decode()}"')

    # Close the connection
    client.close()


def main():
    """"""
    server_ip = "SERVER IP ADDRESS"
    start_client(server_ip)


if __name__ == "__main__":
    main()
