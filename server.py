import socket
import jwt

SECRET_KEY = 'ab'

#decoding the token back to data
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
