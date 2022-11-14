from enum import Enum

#  _   _ _  _   _              _              _      _  _   _
# | | | | || | | |            / \   _ __   __| |_ __| || | | |_
# | |_| | || |_| |  _____    / _ \ | '_ \ / _` | '__| || |_| __|
# |  _  |__   _| | |_____|  / ___ \| | | | (_| | |  |__   _| |_
# |_| |_|  |_| |_|         /_/   \_\_| |_|\__,_|_|     |_|  \__|
#                                                   coded by H4l


class Define:
    class LogType(Enum):
        INFO = 1,
        SUCCESS = 2,
        WARNING = 3,
        ERROR = 4,

    class Command:
        HEADER = "H4L "
        CMD_GET_STATUS = "STATUS"
        CMD_GET_SCREEN_PICTURE = "SCREEN PICTURE"
