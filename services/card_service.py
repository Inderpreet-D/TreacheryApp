import random
from random import shuffle
from typing import Dict, List

_CARDS: Dict[str, Dict[str, List[str]]] = {
    'Guardian': {
        'Mythic': ['The Great Martyr.jpg', 'The Oracle.jpg', 'The Warlock.jpg'],
        'Rare': ['The Aetherist.jpg', 'The Augur.jpg', 'The Cryomancer.jpg', 'The Immortal.jpg', 'The Marshal.jpg',
                 'The Summoner.jpg', 'The Supplier.jpg'],
        'Uncommon': ['The Bodyguard.jpg', 'The Cathar.jpg', 'The Flickering Mage.jpg', 'The Golem.jpg',
                     'The Hieromancer.jpg', 'The Spellsnatcher.jpg']
    },
    'Assassin': {
        'Mythic': ['The Bio-Engineer.jpg', 'The Depths Caller.jpg', 'The Shapeshifting Slayer.jpg'],
        'Rare': ['The Ambitious Queen.jpg', 'The Corpse Snatcher.jpg', 'The Madwoman.jpg', 'The Necromancer.jpg',
                 'The Rebel General.jpg', 'The War Shaman.jpg'],
        'Uncommon': ['The Beastmaster.jpg', 'The Demon.jpg', 'The Pyromancer.jpg', 'The Seer.jpg', 'The Sigil Mage.jpg',
                     'The Sorceress.jpg', 'The Witch.jpg']
    },
    'Traitor': {
        'Mythic': ['The Ferryman.jpg', 'The Metamorph.jpg', 'The Puppet Master.jpg', 'The Wearer of Masks.jpg'],
        'Rare': ['The Cleaner.jpg', 'The Reflector.jpg', 'The Time Bender.jpg'],
        'Uncommon': ['The Banisher.jpg', 'The Gatekeeper.jpg', 'The Grenadier.jpg', 'The Oneiromancer.jpg']
    },
    'Leader': {
        'Mythic': ['His Beloved Majesty.jpg', 'The Corrupted Regent.jpg', 'The Gathering.jpg'],
        'Rare': ['The Chaos Bringer.jpg', 'The King over the Scrapyard.jpg', 'The Twin Princesses.jpg',
                 'The Void Tyrant.jpg'],
        'Uncommon': ['Her Seedborn Highness.jpg', 'The Blood Empress.jpg', 'The Old Ruler.jpg',
                     'The Queen of Light.jpg']
    }
}

_DESC = {
    'Guardian': 'The Guardians help the Leader, they win or lose with them.',
    'Assassin': 'The Assassins win if the Leader is eliminated.',
    'Traitor': 'The Traitor wins if they are the last player standing. (This implies killing the Assassins before the '
               'Leader, as well as other Traitors if there are more than one.)',
    'Leader': 'The Leader, and their Guardians, win if they are the last players standing.'
}


def _choose_n_from(card_type: str, rarity: str, amount: int) -> [str]:
    global _CARDS

    chosen = []
    cards = _CARDS[card_type][rarity]
    while len(chosen) != amount:
        item = card_type + '/' + rarity + '/' + random.choice(cards)
        if item not in chosen:
            chosen.append(item)
    return chosen


def get_cards(num_players: int, rarity: str) -> [str]:
    chosen = _choose_n_from('Leader', rarity, 1)

    if num_players == 8:
        chosen += _choose_n_from('Traitor', rarity, 2)
    else:
        chosen += _choose_n_from('Traitor', rarity, 1)

    if num_players >= 6:
        chosen += _choose_n_from('Assassin', rarity, 3)
    else:
        chosen += _choose_n_from('Assassin', rarity, 2)

    if num_players >= 7:
        chosen += _choose_n_from('Guardian', rarity, 2)
    elif num_players >= 5:
        chosen += _choose_n_from('Guardian', rarity, 1)

    shuffle(chosen)
    return chosen


def extract_card_alt(card_path: str) -> str:
    return card_path.split('/')[-1].split('.')[0]


def get_description(card_path: str) -> str:
    card_type = card_path.split('/')[0]
    return _DESC[card_type]
