import sys
from pathlib import Path

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir + r'\define')

from define import Define


class Command:
    # TODO 戻り値は仮の為、コマンド仕様確定後必ず戻すこと
    # TODO 関数ヘッダを必ず記載すること
    def make_command() -> str:
        """
        コマンドデータ生成
        
        packet struct
        +-------------------------------------+
        | HEADER(H4L) | PAYLOAD(Command only) |
        +-------------------------------------+
        Returns:
            str: コマンドデータ
        """
        packet = bytes(Define.Command.HEADER + Define.Command.CMD_GET_STATUS)
        return packet
