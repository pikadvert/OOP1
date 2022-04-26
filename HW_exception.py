from typing import Tuple, Dict


class InputException(Exception):
    def __init__(self, message):
        super().__init__(message)
    def __str__(self):
        return 'InputError'

def InputError(arg):
    if any(map(str.isdigit, arg)):
        raise InputException(arg)
    #else:
        #pass


def get_name() -> Tuple[str, str]:
    while True:
        try:
            fullname = input(str("Enter your fullname: "))
            InputError(fullname)
            fullname = fullname.split()
            first_name, last_name = fullname[0], fullname[1]
            return first_name, last_name
        except IndexError:
            pass
        except KeyboardInterrupt:
            pass
        except InputException:
            pass

#print(get_name())

def push() -> None:
    #ask for a key
    key = "first_name", "last_name"
    value = fullname[0], fullname[1]
    DATA_STACK[key] = value
    return DATA_STACK[value]


def pop() -> None:
    # ask for a key
    key = "first_name", "last_name"
    return DATA_STACK[key]

FUNC_CONTAINER = {
    "push": push,
    "pop": pop
}
DATA_STACK: Dict = {}

if __name__ == "__main__":
    fullname = get_name()
    while True:
        try: # push or pop
            choice = "push"
            func = FUNC_CONTAINER[choice]

        except KeyboardInterrupt:
            pass
