from flask import Blueprint, request, redirect

from infrastructure.view_modifiers import response
from services import room_service, player_service

blueprint = Blueprint('create', __name__)


@blueprint.route('/create', methods=['GET'])
@response(template_file='create.html')
def create_get():
    return {}


@blueprint.route('/create', methods=['POST'])
@response(template_file='create.html')
def create_post():
    r = request.form

    num_players = int(r['num_players'])
    rarity = r['rarity']

    room_code = room_service.create_room(num_players, rarity)
    player_id = player_service.create_player()

    room_service.add_player_to_room(player_id, room_code)

    return redirect('/room/{}'.format(room_code))
