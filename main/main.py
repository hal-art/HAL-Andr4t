import sys
from pathlib import Path

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir + r'\andr4t')
from andr4t import Andr4t

#  _   _ _  _   _              _              _      _  _   _
# | | | | || | | |            / \   _ __   __| |_ __| || | | |_
# | |_| | || |_| |  _____    / _ \ | '_ \ / _` | '__| || |_| __|
# |  _  |__   _| | |_____|  / ___ \| | | | (_| | |  |__   _| |_
# |_| |_|  |_| |_|         /_/   \_\_| |_|\__,_|_|     |_|  \__|
#                                                   coded by H4l


def main() -> None:
    """
    メイン処理
    """
    
    # TODO args parserを用いて、socket通信用のip, portを指定する。
    android = Andr4t("xxx", 9999)
    android.get_shell()


if (__name__ == "__main__"):
    main()
