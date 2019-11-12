from flask import Blueprint

from infrastructure.view_modifiers import response
from services import card_service, player_service

blueprint = Blueprint('card', __name__)


@blueprint.route('/card')
@response(template_file='card.html')
def card_get():
    card = player_service.get_card()
    card_alt = card_service.extract_card_alt(card)
    description = card_service.get_description(card)
    return {
        'card': card,
        'card_alt': card_alt,
        'description': description,
    }
