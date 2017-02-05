from flask_restful import fields, marshal_with, reqparse, Resource

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