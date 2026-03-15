import functools
import time
from typing import Any, Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def foo(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        print(f"Casting {func.__name__}...")
        try:
            return func(*args, **kwargs)
        finally:
            end = time.perf_counter()
            print(f"Spell completed in time seconds {end - start:.4f}")

    return foo


def power_validator(min_power: int) -> Callable:

    def foo(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapp(*args: Any, **kwargs: Any) -> Any:
            try:
                power = args[-1]
            except IndexError:
                return "Insufficient power for this spell"

            if power >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"

        return wrapp

    return foo


def retry_spell(max_attempts: int) -> Callable:

    def foo(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapp(*args: Any, **kwargs: Any) -> Any:
            print(f"trying spell {func.__name__}")
            i = 0
            while i < max_attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {i + 1}/{max_attempts})"
                    )
                i += 1
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapp

    return foo


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


def test_all_functional_mage_features() -> None:

    print("=== Testing spell_timer ===")

    @spell_timer
    def sample_spell(a: int, b: int) -> int:
        return a + b

    result = sample_spell(5, 7)
    print(result)
    print("\n=== Testing power_validator ===")

    @power_validator(10)
    def basic_spell(spell_name: str, power: int) -> str:
        return f"{spell_name} cast with power {power}"

    print(basic_spell("Fireball", 15))
    print(basic_spell("Spark", 5))

    print("\n=== Testing retry_spell ===")

    attempts = 0

    @retry_spell(3)
    def unstable_spell() -> str:
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ValueError("Spell fizzled")
        return "Spell succeeded"

    print(unstable_spell())

    @retry_spell(2)
    def always_fail_spell() -> str:
        raise RuntimeError("Always broken")

    print(always_fail_spell())

    print("\n=== Testing MageGuild.validate_mage_name ===")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))
    print(MageGuild.validate_mage_name("Merlin Wise"))
    print(MageGuild.validate_mage_name("Mage123"))

    print("\n=== Testing MageGuild.cast_spell ===")
    mage = MageGuild()

    print(mage.cast_spell("Lightning Bolt", 20))  # should work
    print(mage.cast_spell("Tiny Spark", 5))       # should fail


test_all_functional_mage_features()
