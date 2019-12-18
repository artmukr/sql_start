# Flask Restful
from flask import Flask
from flask_restful import Api, reqparse
from database.core import Users, DetailedUser, Posts, Comments, CommentsPosts, \
	Stats

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

api.add_resource(Users, '/users')
api.add_resource(DetailedUser, '/users/<int:user_id>')
api.add_resource(Posts, '/users/<int:user_id>/posts')
api.add_resource(Comments, '/users/<int:user_id>/comments')
api.add_resource(CommentsPosts, '/posts/<int:post_id>/comments')
api.add_resource(Stats, '/users/stats')

if __name__ == '__main__':
	app.run(debug=True, port=5003)
