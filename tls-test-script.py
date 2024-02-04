import socket
import ssl
import pprint

def get_server_certificate(host, port):
    # Create a socket and connect to server
    sock = socket.create_connection((host, port))

    # Wrap the socket with SSL/TLS
    context = ssl.create_default_context()
    tls_sock = context.wrap_socket(sock, server_hostname=host)

    # Retrieve the server's certificate
    cert = tls_sock.getpeercert()

    # Close the TLS connection and socket
    tls_sock.close()
    sock.close()

    return cert

def main():
    host = 'radsecproxy.seantech.info'  # Replace with the server's hostname or IP
    port = 2084            # Replace with the server's TLS port

    try:
        cert = get_server_certificate(host, port)
        print("Server's Certificate:")
        pprint.pprint(cert)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
