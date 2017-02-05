import sqlite3

rv = sqlite3.connect('test.db')
cr = rv.cursor()

def kk(cursor):
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    cursor.close()

kk(cr)

rv.commit()
rv.close()