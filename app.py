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


def register_blueprints():
    app.register_blueprint(create_view)
    app.register_blueprint(index_view)
    app.register_blueprint(join_view)
    app.register_blueprint(room_view)
    app.register_blueprint(card_view)


def setup_db():
    folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(0, folder)
    db_file = os.path.join(os.path.dirname(__file__), 'db', 'treachery.sqlite')
    db_session.global_init(db_file)


def configure():
    register_blueprints()
    setup_db()


def main():
    configure()
    app.run(debug=True)


if __name__ == '__main__':
    main()
else:
    configure()
