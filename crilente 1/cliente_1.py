import socket

def menu(num):
    if num == 0:
        print("-ecreva o nome do arquivo:\n-para sair: exit")


def save_txt(resposta, mensagem):
    # Abra um arquivo de texto para escrita ('w' - write)
    with open(f'{mensagem}.txt', 'w') as file:
        file.write(resposta)
    # O arquivo é automaticamente fechado quando você sai do bloco "with"




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
    menu(0)

    mensagem = str(input("> "))
    

    if mensagem == "exit":
        break


    cliente_socket.send(mensagem.encode())  # encode transforma string em bytes

    resposta = cliente_socket.recv(10000000).decode()

    if resposta != "tuacha":
        save_txt(resposta, mensagem)
        print("\n\narquivo criado!\n\n")

    else:
        print(resposta)


print("fim")
