import sqlite3

conn = sqlite3.connect('untitled.db')

with conn:
	conn.execute('''create table Users (
	id integer unique primary key autoincrement,
	username varchar(50) not null,
	email varchar(50) not null,
	password varchar(15) not null,
	age smallint,
	city varchar(25)
)''')


with conn:
	conn.execute('''create table Posts (
	id integer unique primary key,
	posts varchar(500)
)''')
