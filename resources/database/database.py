import os
import sqlite3


def split_content(content):
    # TODO 解析文本
    pass

def execute(cr, code):
    if hasattr(cr, 'execute') & hasattr(cr, 'fetchall'):
        cr.execute(code)
        return cr.fetchall()


def executemany(cr, code):
    if hasattr(cr, 'executemany'):
        cr.executemany(code)


def executescript(cr, code):
    if hasattr(cr, 'executescript'):
        cr.executescript(code)


class LTDatabase(object):

    ways = {
        "ONE": execute,
        "MANY": executemany,
        "SCRIPT": executescript,
    }

    def __init__(self, type):
        self.type = type

    def execute(self, code, way):
        rv = sqlite3.connect('database.db')
        cr = rv.cursor()
        away = self.ways[way]
        away(cr, code)
        cr.close()
        rv.commit()
        rv.close()

    def init_db(self):
        with open('ltdb.sql', 'r') as f:
            code = f.read()
            self.execute(code, 'SCRIPT')

    def create_db(self):
        with open('LTDB.sql', 'r') as f:
            code = f.read()
            self.execute(code, 'SCRIPT')

    def save_db(self):
        rv = sqlite3.connect('database.db')
        with open('backup.sql', 'w') as f:
            for line in rv.iterdump():
                f.write('%s\n' % line)

    def get_info(self, content):
        id = 1
        items = split_content(content)
        items = 'A, B, C, D'
        self.execute('SELECT %s FROM %s WHERE ID = %s;' % (self.type, items, id), "ONE")

    def add_info(self, content):
        # items, data = split_content(content)
        items = "(A, B)"
        data = "(1, 2)"
        self.execute('INSERT INTO %s %s VALUES %s;' % (self.type, items, data), 'ONE')

    def set_info(self, content):
        id = 1
        sets = ''
        items, data = split_content(content)
        for i in range(len(items)):
            sets = sets + '%s = %s' % (items[i], data[i])
        self.execute('UPDATE %s SET %s WHERE ID = %s;' % (self.type, sets, id), 'ONE')

    def has_item(self):
        # useless
        self.execute('do sth here')

    # !!!
    def del_info(self, id):
        self.execute('DELETE FROM %s WHERE ID = %s;' % (self.type, id), "ONE")


'''
    def getSth(self, sth):
        # TODO 待完善
        self.__execute(sth)
'''

# demo
if __name__ == '__main__':
    db = LTDatabase('USER')
    db.create_db()
    db.save_db()
    os.system('rm database.db')