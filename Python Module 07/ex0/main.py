from ex0.CreatureCard import CreatureCard

try:
    fire_dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    print(f"""=== DataDeck Card Foundation ===

Testing Abstract Base Class Design:

CreatureCard Info:
{fire_dragon.get_card_info()}

Playing Fire Dragon with 6 mana available:
Playable: {fire_dragon.is_playable(6)}
Play result: {fire_dragon.play(fire_dragon.get_card_info())}
Fire Dragon attacks Goblin Warrior:
Attack result: {fire_dragon.attack_target()}

Testing insufficient mana (3 available):
Playable: {fire_dragon.is_playable(3)}

Abstract pattern successfully demonstrated!
""")
except Exception as e:
    print(f"Error in main execution: {e}")
