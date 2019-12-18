from flask import request
from flask_restful import Resource
from database.api \
	import \
	read_all, read_on_id, \
	post_data, put_data, \
	remove_data, read_on_user_id,\
	read_on_post_id, get_stats


class Users(Resource):
	def get(self):
		return read_all("Users")

	def post(self):
		args = request.get_json()
		return post_data("Users", args), 201


class DetailedUser(Resource):
	def get(self, user_id):
		return read_on_id('Users', user_id)

	def put(self, user_id):
		data = request.get_json()
		return put_data("Users", user_id, data), 204

	def delete(self, user_id):
		return remove_data('Users', user_id), 204


class Posts(Resource):
	def get(self, user_id):
		return read_on_id('Posts', user_id)

	def put(self, user_id):
		data = request.get_json()
		return put_data("Posts", user_id, data, ), 204

	def delete(self, user_id):
		return remove_data('Posts', user_id), 204


class Comments(Resource):
	def get(self, user_id):
		return read_on_user_id(user_id)


class CommentsPosts(Resource):
	def get(self, post_id):
		return read_on_post_id(post_id)


class Stats(Resource):
	def get(self):
		return get_stats()
