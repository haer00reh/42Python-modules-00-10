from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    if not callable(spell1) or not callable(spell2):
        raise TypeError("spell1 or spell2 are not callable")

    def combined_spell(arg: object) -> tuple[object, object]:
        return (spell1(arg), spell2(arg))

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    if not callable(base_spell):
        raise TypeError("base_spell not callable")

    def amplifier(arg: object) -> object:
        res = base_spell(arg)
        return res * multiplier

    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise TypeError("condition or spell are not callable")

    def cond_cast(arg: object) -> object:
        if not condition(arg):
            return "Spell fizzled"
        else:
            return spell(arg)

    return cond_cast


def spell_sequence(spells: list[Callable]) -> Callable:

    for spell in spells:
        if not callable(spell):
            raise ValueError("spell is not callable")

    def foo(arg: object) -> list[object]:
        result_lst = list(map(lambda spell: spell(arg), spells))
        return result_lst

    return foo


def test_spells() -> None:

    def fireball(x: int) -> int:
        return x * 2

    def heal(x: int) -> int:
        return x + 10

    def lightning(x: int) -> int:
        return x * 3

    def enough_mana(x: int) -> bool:
        return x > 5

    print("Testing spell_combiner...")
    combined = spell_combiner(fireball, heal)
    print(combined(5))

    print("\nTesting power_amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball(5))

    print("\nTesting conditional_caster...")
    conditional_fireball = conditional_caster(enough_mana, fireball)
    print(conditional_fireball(10))
    print(conditional_fireball(3))

    print("\nTesting spell_sequence...")
    sequence = spell_sequence([fireball, heal, lightning])
    print(sequence(5))


if __name__ == '__main__':
    test_spells()
