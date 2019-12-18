import sqlite3


def read_all(table_name):
	with sqlite3.connect('untitled.db') as conn:
		curs = conn.cursor()
		curs.execute(f'select * from {table_name}')
	return curs.fetchall()


def read_on_id(table_name, id_: int):
	with sqlite3.connect('untitled.db') as conn:
		curs = conn.cursor()
		curs.execute(f'select * from {table_name} where "id"={id_}')

		return curs.fetchall()


def post_data(table_name, args):
	with sqlite3.connect('untitled.db') as conn:
		conn.row_factory = sqlite3.Row
		curs = conn.cursor()

		curs.execute(f'select * from {table_name}')
		columns = curs.fetchone().keys()
		num_of_col = len(columns) - 1
		string_of_q = ""
		i = 0
		while i < num_of_col:
			i += 1
			string_of_q += "?,"
		columns = ", ".join(columns[1:])

		curs.execute(
			f'insert into {table_name} ({columns}) values ({string_of_q[0:-1]})',
			tuple(args.values())
		)

	return curs.lastrowid


def put_data(table_name, id_, args):
	with sqlite3.connect('untitled.db') as conn:

		curs = conn.cursor()
		columns = list(args.keys())
		values = list(args.values())

		str_col_val = ''
		i = 0
		while i <= (len(args)-1):
			str_col_val += f'{columns[i]} = "{values[i]}", '
			i += 1
		str_col_val = str_col_val[:-2]
		curs.execute(
			f'update {table_name} set {str_col_val} where id = "{id_}";')

	return read_all(table_name)


def remove_data(table_name, user_id):
	with sqlite3.connect('untitled.db') as conn:
		curs = conn.cursor()
		curs.execute(
			f"delete from {table_name} where id = {user_id}"
		)
	return read_all(table_name)


def read_on_user_id(user_id):
	with sqlite3.connect('untitled.db') as conn:
		curs = conn.cursor()
		curs.execute(f'select * from Comments where "user_id"={user_id}')
		return curs.fetchall()


def read_on_post_id(post_id):
	with sqlite3.connect('untitled.db') as conn:
		curs = conn.cursor()
		curs.execute(f'select * from Comments where "post_id"={post_id}')
		return curs.fetchall()


def get_stats():
	with sqlite3.connect('untitled.db') as conn:
		curs = conn.cursor()
		curs.execute('select * from users order by age desc')
		return curs.fetchall()



