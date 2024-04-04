import socket

# Configuração do servidor, 
# Configure a porta e o IP
IP = '192.168.1.101'
PORTA = 25565

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((IP, PORTA))

server_socket.listen(1)
print(f'Servidor inicado em {IP}:{PORTA} \n')

try:
    while True:
        conexao, ip = server_socket.accept()
        print(f'Conexão de: {ip[0]}')

        file_name = conexao.recv(4096).decode('utf-8')
        if not file_name:
            print("Nenhum nome de arquivo recebido. Fechando conexão.")
            conexao.close()
            continue
        print(f'Recebendo o arquivo: {file_name}')

        with open(file_name, 'wb') as arquivo:
            while True:
                dado = conexao.recv(4096)
                if not dado:
                    break  
                arquivo.write(dado)
        print(f'Arquivo "{file_name}" recebido com sucesso.')
        conexao.close()  
except KeyboardInterrupt:
    print("\nServidor interrompido manualmente.")
finally:
    server_socket.close()
    print("Servidor fechado.")
