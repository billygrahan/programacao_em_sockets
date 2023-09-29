import socket
import threading
import time
import os

def listar_arquivos(client_conexao, diretorio):
    try:
        arquivos = os.listdir(diretorio)
        lista_arquivos = "\n".join(arquivos)
        client_conexao.sendall(lista_arquivos.encode())
    except FileNotFoundError:
        resposta = "Diretório não encontrado."
        client_conexao.sendall(resposta.encode())
    except BrokenPipeError:
        print("Conexão com o cliente foi encerrada prematuramente.")

def enviar_img(client_conexao, nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'rb') as file:
            img_data = file.read()
            img_size = len(img_data).to_bytes(4, byteorder='big')  # Envia o tamanho da imagem como 4 bytes
            client_conexao.send(img_size)
            client_conexao.send(img_data)
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
            elif mensagem == "listar":
                listar_arquivos(client_conexao, "arquivos")
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