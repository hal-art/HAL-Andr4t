import socket


class GhostClient:
    """
    TCPクライアント(Android端末)の代用とする。
    現段階では、Android側のserviceが未完成の為、実端末と通信が出来ない。
    
    そのため、GhostClientクラスをAndroid端末の代用とし、このプログラムをTCPクライアントとする。
    
    Android serviceが完成するまでの間の為、
    Android service完成後は使用を禁止する。
    """
    def __init__(self) -> None:
        """
        コンストラクタ
        """
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect((socket.gethostname(), 1234))
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    def receive(self) -> None:
        """
        受信処理[無限ループ]
        """
        while True:
            msg = self.__socket.recv(1024)
            print(msg.decode("utf-8"))
        
    def send(self) -> None:
        """
        送信処理[無限ループ]
        
        Remarks:
            コンソール入力されたものを送信する
        """
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
