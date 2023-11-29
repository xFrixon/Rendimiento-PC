import socket
import psutil

def main():
    host = "200.12.169.186" # Cambia esta línea con la dirección IP de tu computador
    port = 80 # Cambia este valor con el puerto que deseas utilizar

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Obtiene el porcentaje de uso del CPU
    cpu_percent = psutil.cpu_percent()

    # Envía el porcentaje de uso del CPU al otro computador
    s.sendall(str(cpu_percent).encode())

    s.close()

if __name__ == "__main__":
    main()