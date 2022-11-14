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
    QUEUE_MAX_NUMBER = 1
    
    def __init__(self, ip: str, port: int) -> None:
        """コンストラクタ

        Args:
            ip (any): ipアドレス
            port (any): ポート
        """
        self.ip = ip
        self.port = port
        self.socket = socket.socket(type=socket.SOCK_STREAM)
        
        # TODO リリース時、消しておくこと　デバッグコード(通信相手設定処理)
        if (__debug__):
            self.ip = socket.gethostname()
            self.port = '1234'

    def start(self) -> bool:
        """バインド

        Returns:
            bool: 成功または失敗
        """
        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.ip, int(self.port)))
            self.socket.listen(Socket.QUEUE_MAX_NUMBER)
            Console.printl(f"Succeed to bind to {self.ip}", Define.LogType.SUCCESS)
            return True
        except Exception as e:
            Console.printl(e, Define.LogType.ERROR)
            return False
        
    def send(self) -> bool:
        while True:
            try:
                android_device, address = self.socket.accept()
                Console.printl(f"Succeed to connect to {address}", Define.LogType.SUCCESS)
                
                android_device.send(bytes("Hello World", 'utf-8'))
                Console.printl("Succeed to send bytes", Define.LogType.SUCCESS)
                
                android_device.close()
                Console.printl(f"Succeed to close connection from {address}", Define.LogType.SUCCESS)
                
            except Exception as e:
                Console.printl(e, Define.LogType.ERROR)
                return False
