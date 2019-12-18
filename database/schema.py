import sqlite3

conn = sqlite3.connect('untitled.db')

# with conn:
# 	conn.execute('''create table Users (
# 	id integer unique primary key autoincrement,
# 	username varchar(50) not null,
# 	email varchar(50) not null,
# 	password varchar(15) not null,
# 	age smallint,
# 	city varchar(25)
# )''')
#
#
# with conn:
# 	conn.execute('''create table Posts (
# 	id integer unique primary key,
# 	posts varchar(500),
# 	user_id integer,
# 	foreign key(user_id) references users(id))''')
#
#
with conn:
	conn.execute('''CREATE table comments (
	id integer primary key AUTOINCREMENT UNIQUE,
	data text, user_id integer,
	post_id integer,
	FOREIGN key(user_id) REFERENCES users(id),
	FOREIGN key(post_id) REFERENCES posts(id))''')
