# Servidor e Cliente Python usando Sockets

## Visão Geral

Este é um exemplo de um servidor e cliente Python que se comunicam por meio de sockets TCP/IP. O servidor recebe mensagens do cliente, processa-as e pode enviar arquivos de texto ou respostas simples de volta ao cliente. O cliente pode enviar mensagens para o servidor e receber arquivos de texto como resposta.

## Configuração do Servidor

1. Abra o arquivo `server.py` em um ambiente Python.

2. Certifique-se de que a porta e o endereço IP do servidor estejam configurados corretamente na linha:

   ```python
   server_socket.bind(('127.0.0.1', 12345))

Você pode modificar o endereço IP e a porta conforme necessário.

Inicie o servidor executando o arquivo `server.py`.

## Configuração do Cliente
Abra o arquivo `client.py` em um ambiente Python.

Verifique se o cliente está configurado para se conectar ao mesmo endereço IP e porta em que o servidor está escutando. A linha a ser verificada é:

```python
cliente_socket.connect(('localhost', 12345))
