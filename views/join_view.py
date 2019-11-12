from flask import Blueprint, request, redirect

from infrastructure.view_modifiers import response
from services import room_service, player_service

blueprint = Blueprint('join', __name__)


@blueprint.route('/join', methods=['GET'])
@response(template_file='join.html')
def join_get():
    return {}


@blueprint.route('/join', methods=['POST'])
@response(template_file='join.html')
def join_post():
    r = request.form
    room_code = r['room_code'].upper()

    room = room_service.get_room_by_code(room_code)
    if not room:
        return {
            'error': 'The room could not be found',
            'room_code': room_code,
        }

    player_id = player_service.create_player()
    room_service.add_player_to_room(player_id, room_code)

    return redirect('/room/{}'.format(room.code))
