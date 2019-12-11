from typing import Optional

from flask import request

import data.db_session as db_session
from data.player import Player
from services import cookie_service


def create_player() -> int:
    player_id = cookie_service.get_player_id_via_cookie(request)

    session = db_session.create_session()
    player = session.query(Player).filter(Player.id == player_id).first()

    if player_id and player:
        return player_id

    player = Player()

    session.add(player)
    session.commit()
    session.close()

    return player.id


def get_player_by_id(player_id: int) -> Optional[Player]:
    session = db_session.create_session()
    player = session.query(Player).filter(Player.id == player_id).first()
    session.close()
    return player


def get_player_from_cookie() -> Player:
    player_id = cookie_service.get_player_id_via_cookie(request)
    return get_player_by_id(player_id)


def get_card() -> str:
    return get_player_from_cookie().card
