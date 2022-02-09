from dataclasses import dataclass


@dataclass
class Flag:

    name: str
    status: bool

class FlagManager:

    def add_flag(self, flag : Flag):

        pass

    def get_state(self, flag):

        pass
