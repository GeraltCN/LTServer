from flask_restful import fields, marshal_with, reqparse, Resource
from resources.database.database import LTDatabase
from resources.token_lt import *

post_parse = reqparse.RequestParser()
post_parse.add_argument(
    'token', type=str,
    dest='token',
)

# Output
user_info_fields = {
    # TODO blabla...
    'id': fields.Integer,
    'name': fields.String,
}


class get_user_info(Resource):
    @marshal_with(user_info_fields)
    def get(self):
        args = post_parse.parse_args()
        token = args.token
        username = check_token(token)
        db = LTDatabase('USER')
        if id:
            _id, _username = db.get_info(['ID', 'USERNAME'], ('USERNAME', username))[0]
            return {'id': _id, 'name': _username}
        else:
            return {"NOT": "OK"}


if __name__ == '__main__':
    db = LTDatabase('USER')
    print(db.get_info(0, ('USERNAME','ljjjx1997')))