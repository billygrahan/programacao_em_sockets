import tkinter as tk
import socket

def get_time():
    cliente_socket.send("tempo".encode())
    resposta = cliente_socket.recv(1024).decode()
    result_label.config(text=f'Tempo do servidor: {resposta}')

def receive_image():
    filename = image_entry.get()  # Obtém o nome do arquivo da entrada de texto
    cliente_socket.send(f"imagem:{filename}".encode())  # Envia a mensagem com o nome do arquivo
    img_size = int.from_bytes(cliente_socket.recv(4), byteorder='big')
    img_data = cliente_socket.recv(img_size)
    resposta = b'ivo n\xc3\xa3o encontrado.'

    if img_data == resposta:
        result_label.config(text="Arq n encontrado!")
    else:
        with open(f'{filename}.png', 'wb') as file:
            file.write(img_data)
        result_label.config(text=f'Imagem recebida e salva como {filename}.png.')


def receive_poem():
    filename = poem_entry.get()
    cliente_socket.send(f"poema:{filename}".encode())
    resposta = cliente_socket.recv(10000000).decode()
    if resposta != "tuacha" and resposta != "Arquivo nao encontrado.":
        with open(f'{filename}.txt', 'w') as file:
            file.write(resposta)
        result_label.config(text=f"Poema recebido e salvo como '{filename}.txt'.")
    else:
        result_label.config(text=resposta)

def list_files():
    cliente_socket.send("listar".encode())
    lista_arquivos = cliente_socket.recv(1000000).decode()
    result_label.config(text=f'Arquivos no diretório do servidor:\n{lista_arquivos}')

def exit_program():
    cliente_socket.send("exit".encode())  # Envia uma mensagem de saída para o servidor
    cliente_socket.close()
    root.destroy()

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente_socket.connect(('localhost', 12345))
    print("Conectado ao servidor!")
except ConnectionError:
    print("Não foi possível conectar ao servidor.")
    exit()

root = tk.Tk()
root.title("Cliente de Servidor")

menu_label = tk.Label(root, text="Selecione uma opção:")
menu_label.pack()

time_button = tk.Button(root, text="Obter Hora do Servidor", command=get_time)
time_button.pack()

image_label = tk.Label(root, text="Nome do arquivo de imagem:")
image_label.pack()
image_entry = tk.Entry(root)
image_entry.pack()
image_button = tk.Button(root, text="Receber Imagem PNG", command=receive_image)
image_button.pack()

poem_label = tk.Label(root, text="Nome do arquivo de texto")
poem_label.pack()
poem_entry = tk.Entry(root)
poem_entry.pack()
poem_button = tk.Button(root, text="Receber Poema", command=receive_poem)
poem_button.pack()

list_button = tk.Button(root, text="Listar Arquivos no Servidor", command=list_files)
list_button.pack()

exit_button = tk.Button(root, text="Sair", command=exit_program)
exit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()