import socket
import os

def main():
    hostname = socket.gethostname()
    print(f"Name of the server: {hostname}")
    print(f'The currect direcory is: {os.getcwd()}')

if __name__ == "__main__":
    main()
        