from flask_restful import fields, marshal_with, reqparse, Resource
from resources.database.database import LTDatabase


post_parse = reqparse.RequestParser()
post_parse.add_argument(
    'token', type= str,
    dest= 'token',
)

# Output
user_info_fields = {
    # TODO blabla...
    'name' : fields.String,
}

class get_user_info(Resource):

    @marshal_with(user_info_fields)
    def post(self):
        pass