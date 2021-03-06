from typing import List


class InputDevice:
    name = ... # type: str
    handlers = ... # type: List[str]
    mapping = ... # type: str
    def __init__(self): ...
    def is_kbd(self) -> bool: ...
    def is_mouse(self) -> bool: ...
    def is_none_device(self) -> bool: ...
    def get_evdev(self) -> str: ...
