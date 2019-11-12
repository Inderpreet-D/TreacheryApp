from flask import Blueprint, redirect, jsonify, request

from infrastructure.view_modifiers import response
from services import room_service

blueprint = Blueprint('room', __name__)


@blueprint.route('/room/<room_code>')
@response(template_file='room.html')
def room_get(room_code):
    room_size, num_players = room_service.get_room_stats(room_code)

    if num_players == room_size:
        return redirect('/card')
    else:
        return {
            'room_code': room_code,
            'room_size': room_size,
            'num_players': num_players,
        }


@blueprint.route('/room/refresh')
def room_refresh():
    room_code = request.args['code'].split('/')[-1]
    room_size, num_players = room_service.get_room_stats(room_code)
    return jsonify({
        'room_size': room_size,
        'num_players': num_players,
        'done': num_players == room_size,
    })
