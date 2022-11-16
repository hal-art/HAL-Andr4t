import socket


class GhostClient:
    def __init__(self) -> None:
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect((socket.gethostname(), 1234))
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    def receive(self) -> None:
        while True:
            msg = self.__socket.recv(1024)
            print(msg.decode("utf-8"))
        
    def send(self) -> None:
        while True:
            msg = input(">")
            self.__socket.send(msg.encode("utf-8"))


ghost_client = GhostClient()
menu = input("1:receive \n"
             "2:send \n"
             ">")
if (menu == "1"):
    ghost_client.receive()
    
elif (menu == "2"):
    ghost_client.send()
