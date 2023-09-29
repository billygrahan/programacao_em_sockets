import socket
import threading
import time

def enviar_img(client_conexao, nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'rb') as file:
            while True:
                chunk = file.read(5 * 1024 * 1024)  # Leitura em pedaços de 1 MB
                if not chunk:
                    break
                client_conexao.send(chunk)
    except FileNotFoundError:
        resposta = "Arquivo não encontrado."
        client_conexao.sendall(resposta.encode())
    except BrokenPipeError:
        print("Conexão com o cliente foi encerrada prematuramente.")

def arquivo(nome_do_arquivo):
    conteudo_binario = b""
    with open(nome_do_arquivo, 'rb') as arquivo:
        conteudo_binario = arquivo.read()
    return conteudo_binario

def cliente(client_conexao, client_endereco):
    if client_conexao:
        print(f"Conexão de {client_endereco}")

        while True:
            mensagem = client_conexao.recv(1000000).decode()

            if mensagem == "exit":
                client_conexao.close()
                print("Conexão encerrada!")
                break
            elif mensagem == "poema":
                try:
                    client_conexao.sendall(arquivo(f"arquivos/{mensagem}.txt"))
                except FileNotFoundError:
                    resposta = "Arquivo não encontrado."
                    client_conexao.sendall(resposta.encode())
                except BrokenPipeError:
                    print("Conexão com o cliente foi encerrada prematuramente.")
                    break
            elif mensagem == "imagem":
                enviar_img(client_conexao, "arquivos/imagem.png")
            elif mensagem == "tempo":
                current_time = time.ctime(time.time())
                client_conexao.sendall(current_time.encode())
            else:
                try:
                    resposta = "tuacha"
                    client_conexao.sendall(resposta.encode())
                except BrokenPipeError:
                    print("Conexão com o cliente foi encerrada prematuramente.")
                    break

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(5)

while True:
    print("Servidor aguardando conexões...")

    client_conexao, client_endereco = server_socket.accept()

    client_handler = threading.Thread(target=cliente, args=(client_conexao, client_endereco))
    client_handler.start()