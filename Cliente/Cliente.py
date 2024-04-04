import socket
import sys
import os

# Configuração da Porta
PORTA = 25565

if len(sys.argv) != 3:
    print('\n Chamada incorreta, use o seguinte formato: "python3 cliente.py <ip-do-servidor> <arquivo>"\n')
    sys.exit(1)

IP = sys.argv[1]
ARQUIVO = sys.argv[2]


if not os.path.exists(ARQUIVO):
    print(f"O arquivo '{ARQUIVO}' não foi encontrado no diretório atual. Não foi possível fazer o envio do arquivo.")
    sys.exit(1) 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    
    client_socket.connect((IP, PORTA))
    print(f'Conexao estabelecida com o servidor {IP}')

    client_socket.send(ARQUIVO.encode('utf-8'))

    with open(ARQUIVO, 'rb') as arquivo:
        data = arquivo.read(4096)
        while data:
            client_socket.send(data)
            data = arquivo.read(4096)
    print(f'Arquivo {ARQUIVO} enviado com sucesso.')
except ConnectionRefusedError:
    print('Erro de conexão. Verifique se o servidor está escutando ou se o endereco esta correto.')
finally:
    client_socket.close()
    print('Finalizando execução.')
