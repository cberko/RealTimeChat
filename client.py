# client.py
import socket
import threading
import sys

class EnhancedClient:
    def __init__(self, username, host='localhost', port=12345):
        self.username = username
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def connect(self):
        try:
            self.socket.connect((self.host, self.port))
            self.connected = True
            print(f"{self.username} connected to the chat server.")
            threading.Thread(target=self.listen_for_messages, daemon=True).start()
        except ConnectionError:
            print("Failed to connect to the server.")
            self.connected = False

    def send_message(self, message):
        if self.connected:
            try:
                full_message = f"{self.username}: {message}"
                self.socket.sendall(full_message.encode('utf-8'))
            except:
                print("Failed to send message.")
        else:
            print("You are not connected to the server.")

    def listen_for_messages(self):
        while self.connected:
            try:
                message = self.socket.recv(1024).decode('utf-8')
                if message:
                    print(f"\n{message}")
            except:
                print("An error occurred while receiving a message.")
                self.disconnect()

    def disconnect(self):
        if self.connected:
            self.socket.close()
            self.connected = False
            print(f"{self.username} disconnected from the server.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    client = EnhancedClient(username)
    client.connect()

    try:
        while True:
            message = input()
            if message.lower() == 'quit':
                client.disconnect()
                break
            client.send_message(message)
    except KeyboardInterrupt:
        client.disconnect()
