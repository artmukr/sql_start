from flask import request
from flask_restful import Resource
from database.api import read_all, read_on_id, post_data, put_data, remove_data


class Users(Resource):
	def get(self):
		return read_all()

	def post(self):
		args = request.get_json()
		return post_data(args), 201


class DetailedUser(Resource):
	def get(self, user_id):
		return read_on_id(user_id)

	def put(self, user_id):
		data = request.get_json()
		return put_data(user_id, data), 204

	def delete(self, user_id):
		return remove_data(user_id), 204


# class Posts(Resource):
# 	def get(self, user_id):
# 		return read_on_id(user_id)
#
# 	def put(self, user_id):
# 		data = request.get_json()
# 		return put_data(user_id, data), 204
#
# 	def delete(self, user_id):
# 		return remove_data(user_id), 204