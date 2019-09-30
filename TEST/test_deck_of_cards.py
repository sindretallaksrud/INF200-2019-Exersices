from ..deck_by_comp import deck_comp


def test_deck_har_52_cards():

    assert len(deck_comp()) == 52

def test_deck_of_cards_have_4_suits():
    deck = deck_comp
    suits = (suit for suit, value in deck)
    assert len(suits) == 4

