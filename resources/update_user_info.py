from flask_restful import fields, marshal_with, reqparse, Resource
from resources.database.database import LTDatabase
from resources.token_lt import *

post_parse = reqparse.RequestParser()
post_parse.add_argument(
    'token', type= str,
    dest= 'token',
)

post_parse.add_argument(
    'content', type= str,
    dest= 'content'
)


# Output
user_info_fields = {
    # TODO blabla...
    'result': fields.Integer,
    'test': fields.String,
}

class update_user_info(Resource):

    @marshal_with(user_info_fields)
    def get(self):
        args = post_parse.parse_args()
        token = args.token
        dict = args.dict
        return {'result':1, 'test':dict}