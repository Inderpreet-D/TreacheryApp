import os
import sys

from flask import Flask

import data.db_session as db_session
from views.card_view import blueprint as card_view
from views.create_view import blueprint as create_view
from views.index_view import blueprint as index_view
from views.join_view import blueprint as join_view
from views.room_view import blueprint as room_view

app = Flask(__name__)

app.register_blueprint(create_view)
app.register_blueprint(index_view)
app.register_blueprint(join_view)
app.register_blueprint(room_view)
app.register_blueprint(card_view)

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)
db_file = os.path.join(os.path.dirname(__file__), 'db', 'treachery.sqlite')
db_session.global_init(db_file)

if __name__ == '__main__':
    app.run(debug=True)
