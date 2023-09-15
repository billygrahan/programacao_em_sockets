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

1. Verifique se o cliente está configurado para se conectar ao mesmo endereço IP e porta em que o servidor está escutando. A linha a ser verificada é:
   ```python
      cliente_socket.connect(('localhost', 12345))

2. Certifique-se de que os valores correspondam aos configurados no servidor.

3. Inicie o cliente executando o arquivo `client.py`.

## Uso do Cliente
Ao iniciar o cliente, você será apresentado a um menu simples. Você pode inserir o nome de um arquivo (por exemplo, “poema”) para solicitar um arquivo de texto do servidor. O servidor procurará o arquivo no diretório “arquivos” e o enviará de volta ao cliente se existir.

Você também pode digitar “exit” para encerrar a conexão com o servidor e sair do cliente.

## Notas Adicionais
Os arquivos de texto solicitados pelo cliente são armazenados na pasta “arquivos” do servidor e enviados ao cliente quando solicitados.

O servidor é capaz de lidar com várias conexões de clientes simultaneamente por meio de threads.

Certifique-se de que os arquivos de texto existam no diretório “arquivos” antes de solicitar seu envio ao servidor.

Este é apenas um exemplo simples de comunicação cliente-servidor usando sockets e pode ser usado como base para construir aplicativos mais complexos.

Certifique-se de encerrar tanto o servidor quanto o cliente quando não estiver mais em uso.

## Autor
JVictor011 e billygrahan
