import sqlite3
import os

def execute(cr, code):
    if hasattr(cr, 'execute') & hasattr(cr, 'fetchall'):
        cr.execute(code)
        return cr.fetchall()

d = {"ONE": execute}

rv = sqlite3.connect('test.db')
cr = rv.cursor()

cr.executescript('''
create table users(id integer primary key,name text,level integer);
insert into users(name,level) values('李斯',2);
insert into users(name,level) values('张三',4);
insert into users(name,level) values('王五',3);
''')

print(d["ONE"](cr, "SELECT * FROM users"))


cr.close()
rv.commit()
rv.close()

os.system('rm test.db')