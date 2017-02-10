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
    'duty': fields.String,
}


class get_user_info(Resource):
    @marshal_with(user_info_fields)
    def get(self):
        args = post_parse.parse_args()
        token = args.token
        info = check_token(token)

        if info:
            _username = info[0]
            _duty = info[1]
            db = LTDatabase(_duty)
            _id, _username = db.get_info(['ID', 'USERNAME'], ('USERNAME', _username))[0]
            return {'id': _id, 'name': _username, 'duty': _duty}
        else:
            return {"NOT": "OK"}


if __name__ == '__main__':
    db = LTDatabase('USER')
    print(db.get_info(0, ('USERNAME','ljjjx1997')))