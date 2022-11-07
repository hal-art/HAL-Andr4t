import sys

from pathlib import Path

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir + '\define')
from define import Define

#  _   _ _  _   _              _              _      _  _   _
# | | | | || | | |            / \   _ __   __| |_ __| || | | |_
# | |_| | || |_| |  _____    / _ \ | '_ \ / _` | '__| || |_| __|
# |  _  |__   _| | |_____|  / ___ \| | | | (_| | |  |__   _| |_
# |_| |_|  |_| |_|         /_/   \_\_| |_|\__,_|_|     |_|  \__|
#                                                   coded by H4l

class Console:
    prefix_color_dict = {
        Define.LogType.INFO : "30m",
        Define.LogType.ERROR : "31m",
        Define.LogType.SUCCESS : "32m",
        Define.LogType.WARNING : "33m",
    }
    
    def printl(log_type:Define.LogType, message:str) -> None:
        """ログ出力

        Args:
            log_type (Define.LogType): ログ種
            message (str): メッセージ
        """
        color = Console.prefix_color_dict[log_type]
        prefix = log_type.name
        header = "\033[1m[\033[31m\033[0m\033[1m\033["+color+prefix+"\033[0m\033[1m]\033[0m "
        print(header+message)