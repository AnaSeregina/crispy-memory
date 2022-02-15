
from typing import List


class Fish:
    def __init__(self, internal_timer: int) -> None:
        self.timer = internal_timer


    def get_timer(self) -> int:
        return self.timer

    def set_timer(self, internal_timer: int) -> None:
        self.timer = internal_timer


    
