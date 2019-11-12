import hashlib
from typing import Optional

from flask import Response, Request

auth_cookie_name = 'treachery_user'


def set_player_id(response: Response, player_id: int):
    hash_val = __hash_text(str(player_id))
    val = "{}:{}".format(player_id, hash_val)
    response.set_cookie(auth_cookie_name, val)


def __hash_text(text: str) -> str:
    text = 'mtg__' + text + '__treachery'
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_player_id_via_cookie(request: Request) -> Optional[int]:
    if auth_cookie_name not in request.cookies:
        return None

    val = request.cookies[auth_cookie_name]
    parts = val.split(':')
    if len(parts) != 2:
        return None

    user_id = parts[0]
    hash_val = parts[1]
    hash_val_check = __hash_text(user_id)
    if hash_val != hash_val_check:
        print("Warning: Hash mismatch, invalid cookie value")
        return None

    try:
        return int(user_id)
    except ValueError:
        return None
