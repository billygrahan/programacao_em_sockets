import socket
import threading

def arquivo(nome_do_arquivo):
    conteudo_binario = b""
    with open(nome_do_arquivo, 'rb') as arquivo:
        # Leia o conteúdo do arquivo em binário
        conteudo_binario = arquivo.read()
    return conteudo_binario

def cliente(client_conexao):
    if client_conexao:
        print(f"Conexão de {client_endereco}")

        while True:
            # Recebendo arquivo do cliente
            mensagem = client_conexao.recv(1000000).decode()

            if mensagem == "exit":
                client_conexao.close()
                print("conexão encerrada!")
                break
            elif mensagem == "poema":
                try:
                    client_conexao.sendall(arquivo(f"arquivos/{mensagem}.txt"))
                except BrokenPipeError:
                    print("Conexão com o cliente foi encerrada prematuramente.")
                    break
            else:
                try:
                    resposta = "tuacha"
                    client_conexao.sendall(resposta.encode())
                except BrokenPipeError:
                    print("Conexão com o cliente foi encerrada prematuramente.")
                    break

# Crie um objeto socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associe o socket à porta e endereço desejados
server_socket.bind(('127.0.0.1', 12345))

# Comece a escutar por conexões
server_socket.listen(5)  # O argumento é o número máximo de conexões pendentes

while True:
    print("Servidor aguardando conexões...")

    # Aceitar uma conexão
    client_conexao, client_endereco = server_socket.accept()

    client_handler = threading.Thread(target=cliente, args=(client_conexao,))
    client_handler.start()



