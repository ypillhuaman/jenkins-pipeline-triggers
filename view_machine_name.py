import socket

def main():
    hostname = socket.gethostname()
    print(f"Name of the server: {hostname}")

if __name__ == "__main__":
    main()
        