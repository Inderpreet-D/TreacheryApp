from flask import Blueprint

from infrastructure.view_modifiers import response
from services import card_service, player_service, room_service

blueprint = Blueprint('card', __name__)


@blueprint.route('/card')
@response(template_file='card.html')
def card_get():
    card = player_service.get_card()
    card_alt = card_service.extract_card_alt(card)
    description = card_service.get_description(card)
    room_info = room_service.get_room_info()
    return {
        'card': card,
        'card_alt': card_alt,
        'description': description,
        'room_info': room_info,
    }
