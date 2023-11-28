import socket
import jwt

SECRET_KEY = 'ab'

# Define allowed IP addresses
allowed_ips = ['192.168.1.10', '192.168.1.20', '127.0.0.1']

def decode_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.exceptions.InvalidTokenError:
        print('Invalid token')
        return None

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    while True:
        conn, addr = server_socket.accept()

        # Check if the source IP address is allowed
        if addr[0] not in allowed_ips:
            print(f"Unauthorized connection from {addr[0]}")
            conn.close()
            continue

        print(f"Connection from {addr}")

        data = conn.recv(1024)
        if not data:
            break

        token = data.decode()
        decoded_data = decode_jwt(token)

        if decoded_data:
            user_id = decoded_data['user_id']
            print("Received request: ", decoded_data["action"])
            if user_id == "123":
                response_data = json.dumps(response).encode()
                conn.sendall(response_data)
        else:
            response = {"Verification incomplete"}

        conn.close()

if __name__ == "__main__":
    start_server()