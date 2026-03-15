from typing import Callable


def mage_counter() -> Callable:
    x = 0

    def foo() -> int:
        nonlocal x
        x += 1
        return x

    return foo


def spell_accumulator(initial_power: int) -> Callable:

    def foo(accum: int) -> int:
        nonlocal initial_power
        initial_power += accum
        return initial_power

    return foo


def enchantment_factory(enchantment_type: str) -> Callable:
    def foo(enchantment: str) -> str:
        return f"{enchantment_type} {enchantment}"

    return foo


def memory_vault() -> dict[str, Callable]:
    spell_mem = {}

    def store(key: str, value: str) -> None:
        spell_mem[key] = value

    def recall(key: str) -> str:
        if key not in spell_mem:
            return "Memory not found"
        return spell_mem[key]

    return {'store': store, 'recall': recall}


def test_closures() -> None:
    print("Testing mage_counter...")
    counter = mage_counter()
    print(counter())
    print(counter())
    print(counter())

    print("\nTesting spell_accumulator...")
    accumulator = spell_accumulator(10)
    print(accumulator(5))
    print(accumulator(3))
    print(accumulator(7))

    print("\nTesting enchantment_factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Axe"))

    print("\nTesting memory_vault...")
    vault = memory_vault()
    print(vault["recall"]("spell"))
    vault["store"]("spell", "Fireball")
    vault["store"]("weapon", "Staff")
    print(vault["recall"]("spell"))
    print(vault["recall"]("weapon"))
    print(vault["recall"]("mana"))


if __name__ == '__main__':
    test_closures()
