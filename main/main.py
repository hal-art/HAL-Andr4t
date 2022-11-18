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

    if(not args.arg1 is ARG_IP_ADDRESS_PREFIX):
        console.print('Please enter "-a" as the first character.')
        return False

    iplist=args.arg2.split('.')

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

    if(not args.arg3 is ARG_port_ADDRESS_PREFIX):
        Console.print('Please enter "-p" as the first character.')
        return False
    
    try:
        int(args.arg4)
    except:
        Console.print("Please enter only numerical values for the port number")
        return False
    
    return True


def main() -> None:
    """
    メイン処理
    """
    #args = sys.argv   #sysによる引数の取得。argsにリストで格納
    # TODO args parserを用いて、socket通信用のip, portを指定する。
    parser = argparse.ArgumentParser(description="Get command line arguments")   #パーサー作成
    parser.add_argument("arg1",help="-a",type=str)   #引数設定
    parser.add_argument("arg2",help="IP address",type=str)
    parser.add_argument("arg3",help="-p",type=str)
    parser.add_argument("arg4",help="TCP port number",type=str)
    args = parser.parse_args( )   #引数解析

    if(not __args_analyze_ip(args) or
        not __args_analyze_port(args)):
        return False

    ip=args.arg2
    port=int(args.arg4)
    
    android = Andr4t(ip,port) #androidはAndr4tのインスタンス
    android.get_shell()

if (__name__ == "__main__"):
    main()
