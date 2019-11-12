from flask import Blueprint, request, redirect

from infrastructure.view_modifiers import response
from services import player_service, cookie_service

blueprint = Blueprint('index', __name__)


@blueprint.route('/', methods=['GET'])
@response(template_file='index.html')
def index_get():
    return {}


@blueprint.route('/', methods=['POST'])
@response(template_file='index.html')
def index_post():
    button_name = request.form['submit_button']

    resp = redirect('/{}'.format(button_name))
    player_id = player_service.create_player()

    cookie_service.set_player_id(resp, player_id)
    return resp
