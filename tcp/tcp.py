import socket
import sys

from pathlib import Path

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir + r'\console')
sys.path.append(parent_dir + r'\define')

from console import Console
from define import Define

#  _   _ _  _   _              _              _      _  _   _
# | | | | || | | |            / \   _ __   __| |_ __| || | | |_
# | |_| | || |_| |  _____    / _ \ | '_ \ / _` | '__| || |_| __|
# |  _  |__   _| | |_____|  / ___ \| | | | (_| | |  |__   _| |_
# |_| |_|  |_| |_|         /_/   \_\_| |_|\__,_|_|     |_|  \__|
#                                                   coded by H4l


class Socket:
    
    def __init__(self, ip: str, port: int) -> None:
        """コンストラクタ

        Args:
            ip (any): ipアドレス
            port (any): ポート
        """
        "受信バッファの最大値"
        RECEIVE_BUFFER_NUMBER = 1024
    
        self.ip = ip
        self.port = port
        self.socket = socket.socket(type=socket.SOCK_STREAM)
        self.__blocker = False
        self.__read_size = RECEIVE_BUFFER_NUMBER
        
        # TODO リリース時、消しておくこと　デバッグコード(通信相手設定処理)
        if (__debug__):
            self.ip = socket.gethostname()
            self.port = 1234
            
    def start(self) -> bool:
        """接続の確立

        Returns:
            bool: 接続結果
        """
        "基本は、送信・受信の2つのキューを使用する"
        "エラー発生時に返答を返すためのキューとして + 1"
        QUEUE_MAX_NUMBER = 2 + 1
        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.ip, self.port))
            self.socket.listen(QUEUE_MAX_NUMBER)
            Console.printl(f"Succeed to bind to {self.ip}", Define.LogType.SUCCESS)
            
            self.handler = self.__accept()
            if self.handler is None:
                raise Exception("handler is None")
            return True
        except Exception as e:
            Console.printl(e, Define.LogType.ERROR)
            return False
        
    def send(self, send_data: bytes) -> bool:
        """
        データ送信

        Returns:
            bool: 送信結果
        """
        try:
            self.handler.send(send_data)
            Console.printl("Succeed to send bytes", Define.LogType.SUCCESS)
            
            self.handler.close()
            Console.printl("Succeed to close connection", Define.LogType.SUCCESS)
            return True
            
        except Exception as e:
            Console.printl(e, Define.LogType.ERROR)
            return False
        
    def receive(self) -> bytes:
        """
        データ受信

        Returns:
            bytes: 応答データ
        """
        while True:
            try:
                "#####  Socketクラスでは受信結果をバイナリデータで返却するだけ。#####"
                "#####           デシリアライズは受け手の責務とする            #####"
                
                "self.__blockerがTrueの場合は前回の処理を解析中なのでスルー"
                if self.__blocker is True:
                    self.send("ERROR __blocker flag is enable".encode('utf-8'))
                    continue
                
                self.buffer = self.handler.recv(self.__read_size)
            except Exception as e:
                Console.printl(e, Define.LogType.ERROR)
                return False
            
    def set_blocker(self, block: bool) -> None:
        """
        ブロッカーのフラグのセッター

        Args:
            block (bool): ブロックのオン・オフ
        """
        self.__blocker = block
        
    def __accept(self) -> socket:
        """
        接続処理

        Returns:
            socket: クライアント側ハンドラ
        """
        try:
            handle, address = self.socket.accept()
            Console.printl(f"Succeed to connect to {address}", Define.LogType.SUCCESS)
            return handle
        except Exception as e:
            Console.printl(e, Define.LogType.ERROR)
            return None
