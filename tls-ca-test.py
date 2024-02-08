import socket
import ssl
import pprint

# Path to the CA certificate
ca_certs_path = "/root/radsecproxy/radsecproxy_seantech_info.crt"  # Replace with the path to your ca.crt

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL, specifying the CA certificate
ssl_sock = ssl.wrap_socket(s,
                           ca_certs=ca_certs_path,
                           cert_reqs=ssl.CERT_REQUIRED)

# Connect to the server
ssl_sock.connect(('radsecproxy.seantech.info', 2084))  # Replace with your server details

pprint.pprint(ssl_sock.getpeercert())

ssl_sock.close()
