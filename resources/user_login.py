from flask_restful import fields, marshal_with, reqparse, Resource
from resources.database.database import LTDatabase
import base64
import time
import hashlib


def hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def accio_token(id):
    text = id + ' ' + str(round(time.time()))
    token = base64.b64encode(text.encode())
    return token.decode()

def login(username, password,):
    # TODO LOGIN
    udb = LTDatabase('USER')
    id, _password = udb.get_info(('ID', ['PASSWORD']))
    if password == _password:
        return accio_token(id)
    else:
        return 0


post_parse = reqparse.RequestParser()
post_parse.add_argument(
    'username', type= str,
    dest = 'username',
)
post_parse.add_argument(
    'password', type= str,
    dest = 'password',
)


#Output
login_fields = {
    'result': fields.Integer,
    'token': fields.String(default='default'),
}

def check():
    pass

class user_login(Resource):
    @marshal_with(login_fields)
    def post(self):
        args = post_parse.parse_args()
        answer =  login(args.username, args.password)
        if answer:
            return {'result': 1, 'token': answer}
        else:
            return {'result': 0, 'token': answer}


if __name__ == '__main__' :
    print(accio_token('asd1212axas222h22212aasdasj'))