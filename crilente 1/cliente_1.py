import socket

# Crie um objeto socket
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associe o socket à porta e endereço desejados

try:
    cliente_socket.connect(('localhost', 12345))
    print("conectado!")
except ConnectionError:
    print("não foi possível conectar ao servidor.")
    exit()

while True:
    mensagem = str(input("arquivo> "))

    cliente_socket.send(mensagem.encode())  # encode transforma string em bytes

    if mensagem == "exit":
        break

    """with open("arquivo_recebido.txt", 'wb') as file:  # wb escreve no arquivo
        while True:
            dados_recebidos = cliente_socket.recv(1024)  # Receba dados do servidor (1024 bytes por vez)
            if not dados_recebidos:
                break
            file.write(dados_recebidos)"""
    
    resposta = cliente_socket.recv(10000000).decode()

    print(resposta)

print("fim")
