from flask_restful import fields, marshal_with, reqparse, Resource
from resources.database.database import LTDatabase


def create_user(username, password):
    # TODO REGISTER
    db = LTDatabase('USER')
    if not db.has_item():
        pass


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
    # TODO 注册
    pass


class user_register(Resource):
    def post(self):
        args = post_parse.parse_args()
        if create_user(args.username, args.password):
            return {'result': 1}
        else:
            return {'result': 0}

if __name__ == '__main__':
    db = LTDatabase('USER')
    print(db.get_info(['USERNAME','PASSWORD'], ("ID", 10000)))
