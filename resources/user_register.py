from flask_restful import fields, marshal_with, reqparse, Resource
from resources.database.database import LTDatabase


post_parse = reqparse.RequestParser()
post_parse.add_argument(
    'username', type=str,
    dest = 'username',
)
post_parse.add_argument(
    'password', type=str,
    dest = 'password',
)

#Output
register_fields = {
    'result' : fields.Integer,
}

def create_user(username, password):
    db = LTDatabase('USER')
    if not db.has_info(('USERNAME',username)):
        db.add_info({
            'USERNAME':username,
            'PASSWORD':password
        })
        return 1
    return 0


class user_register(Resource):
    @marshal_with(register_fields)
    def get(self):
        args = post_parse.parse_args()
        if create_user(args.username, args.password):
            return {'result': 1}
        else:
            return {'result': 0}

if __name__ == '__main__':
    create_user('ljjasda','asd')
