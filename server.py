import socket
import cv2
import pickle

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("HOST IP:", host_ip)
port = 10050
socket_address = (host_ip, port)
print("Socket created")
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1000000)
server_socket.bind(socket_address)
print("Socket bind complete")

vid = cv2.VideoCapture(0)
vid.set(3, 640)
vid.set(4, 480)

while vid.isOpened():
    address_client_socket = server_socket.recvfrom(1024)
    print("Connected to Client")
    message = address_client_socket[0]
    client_address = address_client_socket[1]
    print(message)
    img, frame = vid.read()
    _, buffer = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 30])
    img_as_bytes = pickle.dumps(buffer)
    server_socket.sendto(img_as_bytes, client_address)

    cv2.imshow("Sending...", frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cv2.destroyAllWindows()
vid.release()
