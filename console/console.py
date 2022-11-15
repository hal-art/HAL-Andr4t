import sys
from pathlib import Path

from multipledispatch import dispatch

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir + r'\define')
sys.path.append(parent_dir + r'\date')
from date import Date
from define import Define

#  _   _ _  _   _              _              _      _  _   _
# | | | | || | | |            / \   _ __   __| |_ __| || | | |_
# | |_| | || |_| |  _____    / _ \ | '_ \ / _` | '__| || |_| __|
# |  _  |__   _| | |_____|  / ___ \| | | | (_| | |  |__   _| |_
# |_| |_|  |_| |_|         /_/   \_\_| |_|\__,_|_|     |_|  \__|
#                                                   coded by H4l


class Console:
    prefix_color_dict = {
        Define.LogType.INFO: "30m",
        Define.LogType.ERROR: "31m",
        Define.LogType.SUCCESS: "32m",
        Define.LogType.WARNING: "33m",
    }
    
    def __get_header(color: str, prefix: str) -> str:
        """
        ヘッダ文字列取得

        Args:
            color (str): カラーコード
            prefix (str): 先頭字

        Returns:
            str: ヘッダ文字列
        """
        header = "\033[1m[\033[31m\033[0m\033[1m\033[" + color + prefix + "\033[0m\033[1m]\033[0m " + Date.get_detail_date() + '\n'
        return header
    
    @dispatch(str, Define.LogType)
    def printl(message: str, log_type: Define.LogType) -> None:
        """ログ出力
        
        Args:
            message (str): メッセージ
            log_type (Define.LogType): ログ種
        """
        color = Console.prefix_color_dict[log_type]
        prefix = log_type.name
        header = Console.__get_header(color=color, prefix=prefix)
        print(header + message)
    
    @dispatch(Exception, Define.LogType)
    def printl(message: Exception, log_type: Define.LogType) -> None:
        """ログ出力(オーバーロード)

        Args:
            log_type (Define.LogType): ログ種
            message (str): メッセージ
        """
        color = Console.prefix_color_dict[log_type]
        prefix = log_type.name
        header = Console.__get_header(color=color, prefix=prefix)
        for arg in message.args:
            print(header + str(arg))
