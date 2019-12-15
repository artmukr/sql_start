import sqlite3


def read_all():
	with sqlite3.connect('untitled.db') as conn:
		curs = conn.cursor()
		curs.execute('''select * from users''')
		result = curs.fetchall()
	return result


def read_on_id(id_: int):
	with sqlite3.connect('untitled.db') as conn:
		id_1 = (id_,)
		curs = conn.cursor()
		curs.execute('''select * from users where "id"=?''', id_1)
		return curs.fetchall()


def post_data(*args):
	with sqlite3.connect('untitled.db') as conn:
		curs = conn.cursor()
		for args_dict in args:
			curs.execute(
				'''insert into Users values 
				(:id, :username, :email, :password,:age, :city)''',
				{
					"id": None,
					"username": args_dict["username"],
					"email": args_dict["email"],
					"password": args_dict["password"],
					"age": args_dict["age"],
					"city": args_dict["city"]
				}
			)

	return curs.lastrowid


def put_data(*args):
	with sqlite3.connect('untitled.db') as conn:
		curs = conn.cursor()
		user_id = args[0]
		args_dict = args[1]
		curs.execute(
			'''update Users set
			username = :username, email = :email, password = :password,
			age = :age, city = :city where id = :id''',
			{
				"id": user_id,
				"username": args_dict["username"],
				"email": args_dict["email"],
				"password": args_dict["password"],
				"age": args_dict["age"],
				"city": args_dict["city"]
			}
		)
	return read_all()


def remove_data(user_id):
	with sqlite3.connect('untitled.db') as conn:
		curs = conn.cursor()
		curs.execute(
			"delete from Users where id = :user_id",
			{"user_id": user_id}
		)
	return read_all()
