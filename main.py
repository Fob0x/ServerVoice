
import socket
import threading
import pyaudio

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024

def handle_client(conn, addr):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)
    while True:
        try:
            data = conn.recv(CHUNK)
            if not data:
                break
            stream.write(data)
        except:
            break
    conn.close()

def start_server():
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    print(f'Server listening on {host}:{port}')
    while True:
        conn, addr = s.accept()
        print(f'Connected by {addr}')
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == '__main__':
    start_server()

