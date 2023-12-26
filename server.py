# server.py
import socket
import threading

class ChatServer:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print("Server is listening for connections...")

        try:
            while True:
                conn, addr = self.server_socket.accept()
                self.clients.append(conn)
                print(f"Connection from {addr}")
                threading.Thread(target=self.client_thread, args=(conn, addr)).start()
        except KeyboardInterrupt:
            print("Shutting down the server...")
            for conn in self.clients:
                conn.close()
            self.server_socket.close()

    def client_thread(self, conn, addr):
        while True:
            try:
                message = conn.recv(1024)
                if message:
                    print(f"Message from {addr}: {message.decode('utf-8')}")
                    self.broadcast_message(message, conn)
                else:
                    break
            except:
                break

        self.clients.remove(conn)
        conn.close()

    def broadcast_message(self, message, sender_conn):
        for client in self.clients:
            if client != sender_conn:
                try:
                    client.sendall(message)
                except:
                    client.close()
                    self.clients.remove(client)

if __name__ == "__main__":
    server = ChatServer()
    server.start()
