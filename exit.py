from enum import Enum

class ExitType(Enum):
    QUIT = 1;
    NORMAL = 2;
    WAIT_INPUT = 3;

class ExitUnit:
    def __init__(self, exit_type, rtn_msg) -> None:
        self.exit_type = exit_type
        self.rtn_msg = rtn_msg
