import sys

from pathlib import Path

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir + r'\tcp')
from tcp import Socket

#  _   _ _  _   _              _              _      _  _   _
# | | | | || | | |            / \   _ __   __| |_ __| || | | |_
# | |_| | || |_| |  _____    / _ \ | '_ \ / _` | '__| || |_| __|
# |  _  |__   _| | |_____|  / ___ \| | | | (_| | |  |__   _| |_
# |_| |_|  |_| |_|         /_/   \_\_| |_|\__,_|_|     |_|  \__|
#                                                   coded by H4l


class Andr4t:
    def __init__(self, ip, port) -> None:
        self.socket = Socket(ip, port)
        self.socket.start()
    
    def get_shell(self) -> None:
        if (not self.socket.send(bytes("Hello World", 'utf-8'))):
            return


# TODO デバッグコード(通信相手設定処理)
if (__debug__):
    andr4t = Andr4t("xxx.xxx.xx.x", 0000)
    andr4t.get_shell()
