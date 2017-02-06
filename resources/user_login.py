from flask_restful import fields, marshal_with, reqparse, Resource
from resources.database.database import LTDatabase

post_parse = reqparse.RequestParser()
post_parse.add_argument(
    'username', type= str,
    dest = 'username',
)
post_parse.add_argument(
    'password', type= str,
    dest = 'password',
)

def login(username, password,):
    # TODO 登陆

    udb = LTDatabase('USER')



    pass

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

