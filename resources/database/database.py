import sqlite3

dataBase = {
    'USER': 'users',
    'DRIVER': 'drives',
    'ORDER': 'orders',
}


class LTDatabase(object):
    def __init__(self, type):
        self.type = dataBase[type]


    def __execute(self, code):
        rv = sqlite3.connect(self.__as_db())
        cr = rv.cursor()
        cr.executescript(code)
        cr.close()
        rv.commit()
        rv.close()


    def init_db(self):
        with open(self.__as_sql(self.type), 'r') as f:
            code = f.read()
            self.__execute(code)

    def save_db(self):
        rv = sqlite3.connect(self.__as_db())
        with open('users.sql','w') as f:
            for line in rv.iterdump():
                f.write('%s\n' % line)

    def __as_db(self):
        return self.type+'.db'

    def __as_sql(self, str):
        return self.type+'.sql'


    def getSth(self, sth):
        # TODO 待完善
        self.__execute(sth)



if __name__ == '__main__':
    print('?')

