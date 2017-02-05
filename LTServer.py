from flask import Flask
from flask_restful import Api

from resources.user_login import user_login
from resources.user_register import user_register
from resources.get_user_info import get_user_info

from resources.database.database import LTDatabase

# TODO TEST!
from resources.welcome import welcome
from resources.test import test

app = Flask(__name__)
api = Api(app)

api.add_resource(user_login, '/user_login')
api.add_resource(get_user_info, '/get_user_info')
api.add_resource(user_register, '/user_register')

'''

不完善

@app.cli.command('initdb')
def init_db():
    LTDatabase.init_db()

@app.cli.command('savedb')
def save_db():
    LTDatabase.save_db()
'''

# TODO TEST!
api.add_resource(welcome, '/')
api.add_resource(test, '/test')

if __name__ == "__main__":
    app.run(debug=True)