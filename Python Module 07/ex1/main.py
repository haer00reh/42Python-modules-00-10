from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard

try:
    decks = Deck()

    decks.add_card(SpellCard('Lightning Bolt', 3, 'Common', 'damage'))
    art_card = ArtifactCard(
        'Mana Crystal', 3, 'Epic', 1,
        'Permanent: +1 mana per turn')
    decks.add_card(art_card)
    decks.add_card(CreatureCard('Fire Dragon', 5, 'Legendary', 5, 4))

    print(f"""\n=== DataDeck Deck Builder ===

Building deck with different card types...
Deck stats: {decks.get_deck_stats()}
Drawing and playing cards:
""")
    c1 = decks.draw_card()
    print(f"Play result: {c1.play(c1.get_card_info())}\n")
    c2 = decks.draw_card()
    print(f"Play result: {c2.play(c2.get_card_info())}\n")
    c3 = decks.draw_card()
    print(f"Play result: {c3.play(c3.get_card_info())}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")
except Exception as e:
    print(f"Error in main execution: {e}")
