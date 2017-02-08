from flask_restful import fields, marshal_with, reqparse, Resource
from resources.database.database import LTDatabase
from resources.token_lt import *
import json

def content_analysis(content):
    info = base64.b64decode(content.encode()).decode()
    dict = json.loads(info)
    return dict

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
}

class update_user_info(Resource):

    @marshal_with(user_info_fields)
    def get(self):
        args = post_parse.parse_args()
        token = args.token
        dict = args.dict
        _username = check_token(token)
        if _username:
            db = LTDatabase('USER')
            db.set_info(dict, ('USERNAME', _username))
            return {'result':1}
        else:
            return 0


if __name__ == '__main__':
    info = base64.b64encode("{\"time\":\"now\"}".encode()).decode()
    print(type(content_analysis(info)))
