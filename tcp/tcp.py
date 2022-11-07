import socket
import sys

from pathlib import Path

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir + '\console')
sys.path.append(parent_dir + '\define')

from console import Console
from define import Define

#  _   _ _  _   _              _              _      _  _   _
# | | | | || | | |            / \   _ __   __| |_ __| || | | |_
# | |_| | || |_| |  _____    / _ \ | '_ \ / _` | '__| || |_| __|
# |  _  |__   _| | |_____|  / ___ \| | | | (_| | |  |__   _| |_
# |_| |_|  |_| |_|         /_/   \_\_| |_|\__,_|_|     |_|  \__|
#                                                   coded by H4l

class Socket:
    def __init__(self, ip, port) -> None:
        """コンストラクタ

        Args:
            ip (any): ipアドレス
            port (any): ポート
        """
        self.ip = ip
        self.port = port
        self.socket = socket.socket(type=socket.SOCK_STREAM)
            
    def start(self) -> bool:
        """バインド

        Returns:
            bool: 成功または失敗
        """
        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.ip, int(self.port)))
            Console.printl(Define.LogType.SUCCESS, "succeed bind socket!")
            return True
        except Exception as e:
            Console.printl(Define.LogType.ERROR, e)
            return False
