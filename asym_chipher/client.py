from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import socket
from cryptography.hazmat.primitives import serialization

# Загрузка публичного ключа сервера
with open("server_public_key.pem", "rb") as f:
    server_public_key = serialization.load_pem_public_key(f.read())

# Сообщение для отправки
message = "Привет, сервер!".encode()

# Шифрование сообщения
encrypted_message = server_public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    )
)

# Подключение к серверу
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

# Отправка зашифрованного сообщения
client.send(encrypted_message)

client.close()
