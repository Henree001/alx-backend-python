from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def float_multiplier(num: float) -> float:
        return num * multiplier

    return float_multiplier
