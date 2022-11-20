import sys
from pathlib import Path

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir + r'\common\console')
sys.path.append(parent_dir + r'\common\utils')
sys.path.append(parent_dir + r'\andr4t')
from console import Console
from utils import Utils
from andr4t import Andr4t

#  _   _ _  _   _              _              _      _  _   _
# | | | | || | | |            / \   _ __   __| |_ __| || | | |_
# | |_| | || |_| |  _____    / _ \ | '_ \ / _` | '__| || |_| __|
# |  _  |__   _| | |_____|  / ___ \| | | | (_| | |  |__   _| |_
# |_| |_|  |_| |_|         /_/   \_\_| |_|\__,_|_|     |_|  \__|
#                                                   coded by H4l

def __check_ip_format(args) -> bool:
    """
    IPアドレスのフォーマットチェック

    Args:
        args (args): ユーザから受けとった引数配列

    Returns:
        bool: IPアドレスのフォーマットが正しいかどうか
    """
    # "-a"はIPアドレス引数の先頭字
    ARG_IP_ADDRESS_PREFIX = "-a"
    IP_ADDRESS_OCTET_MAX = 4
    IP_ADDRESS_MIN = 0
    IP_ADDRESS_MAX = 255
    
    ip_list=args.arg2.split('.')
    
    if(not args.arg1 == ARG_IP_ADDRESS_PREFIX):
        Console.printl("ipアドレス指定時は-aオプションを付けてください", Define.LogType.ERROR)
        return False

    if(not len(ip_list) is IP_ADDRESS_OCTET_MAX):
        Console.printl("IPアドレスはピリオド区切りで第4オクテットまで入力してください", Define.LogType.ERROR)
        return False

    for ip_str in ip_list:
        (result, ip_int) = Utils.int_try_parse(ip_str)
        if not result:
            Console.printl("数字以外の文字を指定しないでください", Define.LogType.ERROR)
            return False
        
        "各オクテットの値が0-255の範囲内かどうかをチェックする"
        if(IP_ADDRESS_MIN > ip_int or
            IP_ADDRESS_MAX < ip_int):
            Console.printl("アドレスの値が範囲外です", Define.LogType.ERROR)
            return False
    return True

def __check_port_format(args) -> bool:
    """
    ポート番号のフォーマットチェック

    Args:
        args (args): ユーザから受けとった引数配列

    Returns:
        bool: ポート番号の形式が正しいかどうか
    """
    # "-p"はport番号引数の先頭字
    ARG_port_ADDRESS_PREFIX = "-p"
    
    if(not args.arg3 == ARG_port_ADDRESS_PREFIX):
        Console.printl("ポート番号指定時は-pオプションを付けてください", Define.LogType.ERROR)
        return False
    
    (result, _) = Utils.int_try_parse(args.arg4)
    if not result:
        Console.printl("数字のみ入力を受け付けます", Define.LogType.ERRR)
        return False
    return True

def check_arg(args) -> bool:
    """
    引数チェック

    Args:
        args (args): ユーザから受けとった引数配列

    Returns:
        bool: 引数が正しく入力されているかどうか
    """
    expect_args_prefix = ["-a", "-p"]
    
    "expect_args_prefixの要素を1つずつ削除していく"
    for arg in args:
        if(not expect_args_prefix.__contains__(arg)):
            Console.printl("引数のフォーマットが正しくありません", Define.LogType.ERROR)
            return False
        expect_args_prefix.remove(arg)
        
    "1つでも余っていたら不足している引数があるため、エラー返却"
    if(expect_args_prefix.count() > 0):
        Console.printl("以下の引数の指定が不足しています", Define.LogType.ERROR)
        for prefix in expect_args_prefix:
            Console.printl(f"パラメータ：{prefix} \n", Define.LogType.INFO)
        return False
    
    return True

def main() -> None:
    """
    メイン処理
    """
    args = sys.argv()
    
    if not check_arg(args):
        return
    
    if(not __check_ip_format(args) or
        not __check_port_format(args)):
        return False
    
    "---- ここに来たら引数のフォーマットチェックは問題無いとする ----"
    
    ip=args.arg2
    port=int(args.arg4)
    
    android = Andr4t(ip,port)
    android.get_shell()

if (__name__ == "__main__"):
    main()
