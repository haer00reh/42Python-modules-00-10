import functools
import operator
from functools import singledispatch
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int | str:
    operations = {
        "min": min,
        "max": max,
        "add": operator.add,
        "multiply": operator.mul
    }

    if operation not in operations:
        return "unknown operation"

    try:
        return functools.reduce(operations[operation], spells)
    except TypeError:
        return "unknown operation"


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment with power {power} cast on {target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire_enchant': functools.partial(base_enchantment, 50, "fire"),
        'ice_enchant': functools.partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': functools.partial(
            base_enchantment,
            50,
            'lightning',
        ),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast_spell(spell: object) -> str:
        return f"Unknown spell type: {type(spell).__name__}"

    @cast_spell.register
    def _(spell: int) -> str:
        return f"Damage spell deals {spell} damage"

    @cast_spell.register
    def _(spell: str) -> str:
        return f"Enchantment cast: {spell}"

    @cast_spell.register
    def _(spell: list) -> str:
        return (
            f"Multi-cast spells: "
            f"{', '.join(str(s) for s in spell)}"
        )

    return cast_spell


def test_functions() -> None:
    print("=== Testing partial_enchanter ===")
    enchants = partial_enchanter(base_enchantment)

    print(enchants['fire_enchant']("dragon"))
    print(enchants['ice_enchant']("goblin"))
    print(enchants['lightning_enchant']("wizard"))

    # import time
    # start = time.perf_counter()
    print("\n=== Testing memoized_fibonacci ===")
    print("fib(0):", memoized_fibonacci(0))
    print("fib(1):", memoized_fibonacci(1))
    print("fib(10):", memoized_fibonacci(10))
    print("fib(20):", memoized_fibonacci(20))
    # end = time.perf_counter()
    # print(f"Execution time: {end - start:.4f} seconds")

    print("\n=== Testing spell_dispatcher ===")
    dispatcher = spell_dispatcher()

    print(dispatcher(100))
    print(dispatcher("flame shield"))
    print(dispatcher(["fireball", "ice"]))
    print(dispatcher(3.14))


if __name__ == '__main__':
    test_functions()
