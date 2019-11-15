from random import choice
from string import ascii_uppercase
from typing import Optional, Tuple

import data.db_session as db_session
from data.player import Player
from data.room import Room
from services.card_service import get_cards


def create_room(num_players: int, rarity: str) -> str:
    session = db_session.create_session()

    room_code = _generate_room_code()
    while session.query(Room).filter(Room.code == room_code).first() is not None:
        room_code = _generate_room_code()

    cards = get_cards(num_players, rarity)

    room = Room()
    room.code = room_code
    room.size = num_players
    room.cards = ':'.join(cards)

    session.add(room)
    session.commit()
    session.close()

    return room.code


def _generate_room_code() -> str:
    code = ''
    for i in range(4):
        code += choice(ascii_uppercase)
    return code


def get_room_by_code(room_code: str) -> Optional[Room]:
    session = db_session.create_session()
    room = session.query(Room).filter(Room.code == room_code).first()
    session.close()
    return room


def get_room_stats(room_code: str) -> Optional[Tuple[int, int]]:
    session = db_session.create_session()
    room = session.query(Room).filter(Room.code == room_code).first()
    if not room:
        session.close()
        return None
    num_players = session.query(Player).filter(Player.room_code == room.code).count()
    session.close()
    return room.size, num_players


def add_player_to_room(player_id: int, room_code: str):
    session = db_session.create_session()

    room = session.query(Room).filter(Room.code == room_code).first()
    player = session.query(Player).filter(Player.id == player_id).first()

    if player.room_code == room_code:
        session.close()
        return

    player.room_code = room_code

    cards = room.cards.split(':')
    player.card = choice(cards)
    cards.remove(player.card)
    room.cards = ':'.join(cards)

    session.add(player)
    session.add(room)
    session.commit()
    session.close()
