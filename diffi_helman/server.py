import socket
import random

# Функция для вычисления возведения в степень по модулю
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Устанавливаем параметры p и g
p = 23  # Простое число
g = 5   # Основание

# Генерация секретного числа b
b = random.randint(1, 100)

# Создаем сервер
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)

print("Сервер ожидает подключения...")

conn, addr = server.accept()
print(f"Подключение от {addr}")

# Получаем от клиента p, g и A
client_data = conn.recv(1024).decode().split(',')
p, g, A = map(int, client_data)

# Вычисляем B = g^b mod p и K = A^b mod p
B = mod_exp(g, b, p)
K = mod_exp(A, b, p)

print(f"Секретный ключ на сервере: {K}")

# Отправляем B клиенту
conn.send(str(B).encode())

conn.close()
server.close()
