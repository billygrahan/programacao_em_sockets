import socket


def menu(num):
    if num == 0:
        print("- Digite o nome do arquivo:")
        print("- Digite 'tempo' para obter a hora do servidor.")
        print("- Digite 'imagem' para receber uma imagem PNG.")
        print("- Digite 'poema' para receber uma poema.")
        print("- Digite 'listar' para listar os arquivos.")
        print("- Digite 'exit' para sair.")

def save_txt(resposta, mensagem):
    with open(f'{mensagem}.txt', 'w') as file:
        file.write(resposta)

def listar_arquivos(cliente_socket):
    cliente_socket.send("listar".encode())
    lista_arquivos = cliente_socket.recv(1000000).decode()
    print(f'Arquivos no diretório do servidor:\n{lista_arquivos}')

def receber_imagem(cliente_socket):
    img_size = int.from_bytes(cliente_socket.recv(4), byteorder='big')
    img_data = cliente_socket.recv(img_size)
    with open('imagem_recebida.png', 'wb') as file:
        file.write(img_data)
    print("\n\nImagem recebida e salva como 'imagem_recebida.png'.\n\n")

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente_socket.connect(('localhost', 12345))
    print("Conectado ao servidor!")
except ConnectionError:
    print("Não foi possível conectar ao servidor.")
    exit()

while True:
    menu(0)
    mensagem = str(input("> "))

    if mensagem == "exit":
        break
    elif mensagem == "tempo":
        cliente_socket.send(mensagem.encode())
        resposta = cliente_socket.recv(1024).decode()
        print(f'Tempo do servidor: {resposta}')
    elif mensagem == "imagem":
        cliente_socket.send(mensagem.encode())
        receber_imagem(cliente_socket)
    elif mensagem == "lista":
        listar_arquivos(cliente_socket)
    else:
        cliente_socket.send(mensagem.encode())
        resposta = cliente_socket.recv(10000000).decode()

        if resposta != "tuacha":
            save_txt(resposta, mensagem)
            print("\n\nArquivo criado!\n\n")
        else:
            print(resposta)

print("Fim")