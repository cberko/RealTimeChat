# RealTimeChat
Real Time Chat terminal application by using python.
# RealTimeChat
Real Time Chat terminal application by using python.
# Real-Time Chat Application

This is a simple Python-based real-time chat application using socket programming. It features a server (`server.py`) and a client (`client.py`) to demonstrate basic networking and communication in a chat application.

## Features

- **Server-Client Architecture**: Handles multiple client connections and broadcasts messages.
- **Real-Time Messaging**: Enables clients to send and receive messages instantly.
- **Chat History**: Clients maintain a simple history of their chat sessions.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your system.

### Installation

Clone the repository to your local machine:


### Running the Server

To start the chat server, run: python server.py

The server will start and listen for incoming client connections.

### Running the Client

To start a chat client, open a new terminal window and run: python client.py <username>

Replace `<username>` with your desired username. Repeat this step in separate terminals for multiple clients.

### Interacting in the Chat

- Type your message and hit Enter to send.
- Type `quit` and hit Enter to disconnect from the chat.

## Architecture

- **Server (`server.py`)**: Listens for incoming connections, manages active client sessions, and broadcasts messages to all connected clients.
- **Client (`client.py`)**: Connects to the server, sends messages, receives broadcasts from the server, and maintains a session chat history.






