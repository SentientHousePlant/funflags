from attrs import define, field


@define
class Flag:

    #This enforces good flag naming conventions,
    #and excludes the status of a flag from eq's.
    name: str = field(eq=str.lower)
    status: bool = field(eq = False, default=False)

    def __hash__(self):
        return hash(self.name)



class FlagManager:

    flags : set[Flag] = set

    def add_flag(self, flag : Flag) -> None:

        pass

    def get_state(self, flag : Flag) -> bool:

        pass

    def set_state(self, flag : Flag) -> None:

        pass

if __name__=="__main__":

    print(Flag(name="Hello") == Flag(name="hello"))