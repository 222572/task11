import socket
import random

# Функция для вычисления возведения в степень по модулю
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Устанавливаем параметры p и g
p = 23  # Простое число
g = 5   # Основание

# Генерация секретного числа a
a = random.randint(1, 100)

# Вычисляем A = g^a mod p
A = mod_exp(g, a, p)

# Подключаемся к серверу
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

# Отправляем p, g и A серверу
client_data = f"{p},{g},{A}"
client.send(client_data.encode())

# Получаем B от сервера и вычисляем K = B^a mod p
B = int(client.recv(1024).decode())
K = mod_exp(B, a, p)

print(f"Секретный ключ на клиенте: {K}")

client.close()
