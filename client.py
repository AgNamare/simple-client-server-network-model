import socket
import jwt


SECRET_KEY = 'ab'

def generate_token(data):
    return jwt.encode(data, SECRET_KEY, algorithm='HS256')

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    request = {'action': 'getUserInfo', 'user_id': 523}

    token = generate_token(request)
    print(f"Token: {token}")
    client_socket.sendall(token.encode())
    print(f"Sent: {request}")

    # Receive response from server
    response_data = client_socket.recv(1024)
    decoded_response = response_data.decode()

    client_socket.close()

if __name__ == "__main__":
    start_client()
