from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

import socket

# Загрузка приватного ключа
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# Создаем сервер
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)

print("Сервер ожидает подключения...")

conn, addr = server.accept()
print(f"Подключение от {addr}")

# Получение зашифрованного сообщения
encrypted_message = conn.recv(1024)

# Расшифровка сообщения
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    )
)

print(f"Расшифрованное сообщение: {decrypted_message.decode()}")

conn.close()
server.close()
