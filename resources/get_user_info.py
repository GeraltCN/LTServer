from flask_restful import fields, marshal_with, reqparse, Resource
from resources.database.database import LTDatabase
import base64
import time

valid_time = 7 * 24 * 3600


def check_token(token):
    text = base64.b64decode(token).decode()
    tt = text.split()
    id = tt[0]
    time_token = int(tt[-1])
    time_now = round(time.time())
    db = LTDatabase('USER')
    if db.get_info((id, ['*'])) and (time_now - time_token <= valid_time):
        return id
    else:
        return 0


post_parse = reqparse.RequestParser()
post_parse.add_argument(
    'token', type=str,
    dest='token',
)

# Output
user_info_fields = {
    # TODO blabla...
    'name': fields.String,
}


class get_user_info(Resource):
    @marshal_with(user_info_fields)
    def post(self):
        args = post_parse.parse_args()
        token = args.token
        id = check_token(token)
        if id:
            return {"THIS IS": "CONTENT"}
        else:
            return {"NOT": "OK"}
