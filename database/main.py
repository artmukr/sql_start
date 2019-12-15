# Flask Restful
from flask import Flask
from flask_restful import Api, reqparse
from database.users import Users, DetailedUser, Posts

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

api.add_resource(Users, '/users')
api.add_resource(DetailedUser, '/users/<int:user_id>')
api.add_resource(Posts, '/users/<int:user_id>/posts')

if __name__ == '__main__':
	app.run(debug=True, port=5002)
