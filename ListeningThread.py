from nfstream import NFStreamer
import ModbusPlugin
import threading


class ListeningThread(threading.Thread):
    def __init__(self):
        super().__init__()
        print("NFStream thread created")

    def run(self):
        streamer = NFStreamer(source="lo0", udps=ModbusPlugin.Plugin())
        print("NFStream started successfully")
        for stream in streamer:
            None
