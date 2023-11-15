import socket

host = '127.0.0.1'
port = 25565


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    while True:
        email_address = input("Enter email address ")
        email_password = input("Enter email password ")
        email_message = input("Enter email message ")
        encoded_message = bytes(f"address = {email_address}, password = {email_password}, message = {email_message}", 'UTF-8')
        sock.sendall(encoded_message)
        response = sock.recv(1024)

        status = response

        if status.decode('UTF-8') == "OK":
            print(status)
            break
        else:
            print(status)




