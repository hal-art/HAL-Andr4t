import sys
from pathlib import Path

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir + r'\common\define')
sys.path.append(parent_dir + r'\common\console')

from define import Define
from console import Console


class Command:
    __command_dict = {
        "Status": Define.Command.CMD_GET_STATUS,
        "TakeScreenPicture": Define.Command.CMD_GET_SCREEN_PICTURE,
    }
    
    def make_command(command: str) -> str:
        """
        コマンドデータ生成
        
        Remarks:
            +-------------------------------------+
            | HEADER(H4L) | PAYLOAD(Command only) |
            +-------------------------------------+
            
            ヘッダ部とペイロード部で構成される。
            service側ではヘッダ情報を識別して正当なホストとのデータ通信かどうかを識別する。
            
        Returns:
            str: コマンドデータ
        """
        # 存在しないコマンドが指定された場合
        if not Command.__command_dict.__contains__(command):
            Console.printl(f"Not exists {command}", Define.LogType.ERROR)
            return None
        packet = bytes(Define.Command.HEADER + Command.__command_dict[command], 'utf-8')
        return packet
