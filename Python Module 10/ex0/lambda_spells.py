import sys


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    try:
        return sorted(
            artifacts,
            key=lambda artifact: artifact['power'],
            reverse=True,
        )
    except (KeyError, TypeError) as err:
        print(
            f"an error occurred when trying to sort: {err}",
            file=sys.stderr,
        )
        return []


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    try:
        return list(filter(lambda mage: mage['power'] >= min_power, mages))
    except (KeyError, TypeError) as err:
        print(
            f"an error occurred when trying to filter: {err}",
            file=sys.stderr,
        )
        return []


def spell_transformer(spells: list[str]) -> list[str]:
    try:
        return list(map(lambda spell: f"* {spell} *", spells))
    except TypeError as err:
        print(
            f"an error occurred when trying to transform spell: {err}",
            file=sys.stderr,
        )
        return []


def mage_stats(mages: list[dict]) -> dict:
    try:
        powerful = max(mages, key=lambda mage: mage['power'])
        weakest = min(mages, key=lambda mage: mage['power'])
        avg_power = sum(map(lambda mage: mage['power'], mages)) / len(mages)
        return {
            'max_power': powerful['power'],
            'min_power': weakest['power'],
            'avg_power': round(avg_power, 2),
        }
    except (TypeError, ZeroDivisionError, ValueError, KeyError) as err:
        print(
            f"an error occurred when trying to get stats: {err}",
            file=sys.stderr,
        )
        return {}


def test_all_functions() -> None:
    artifacts = [
        {'name': 'Orb of Fire', 'power': 90, 'type': 'fire'},
        {'name': 'Crystal Wand', 'power': 70, 'type': 'arcane'},
        {'name': 'Shadow Dagger', 'power': 85, 'type': 'dark'}
    ]

    mages = [
        {'name': 'Aldor', 'power': 95, 'element': 'fire'},
        {'name': 'Lyra', 'power': 60, 'element': 'water'},
        {'name': 'Thane', 'power': 80, 'element': 'earth'},
        {'name': 'Zara', 'power': 40, 'element': 'air'}
    ]

    spells = ['fireball', 'ice shard', 'lightning strike']

    print("\nTesting artifact sorter...")
    print("artifact_sorter:", artifact_sorter(artifacts))
    print("\nTesting power filter...")
    print("power_filter:", power_filter(mages, 70))
    print("\nTesting spell transformer...")
    print("spell_transformer:", spell_transformer(spells))
    print("\nTesting mage stats...")
    print("mage_stats:", mage_stats(mages))


if __name__ == '__main__':
    test_all_functions()
