import traceback

import pymysql

HOST_CONST = "localhost"
USER_CONST = "root"
PORT_CONST = 3306
PASSWORD_CONST = "Gz8ymJMXfbr#3*5"
DATABASE_CONST = "test_db"


class MysqlUtil(object):

    def __init__(self, databaseName=DATABASE_CONST):
        host = HOST_CONST
        user = USER_CONST
        port = PORT_CONST
        password = PASSWORD_CONST
        database = databaseName
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def ChangeDatabase(self, databaseName):
        self.db.close()
        self.cursor.close()
        host = HOST_CONST
        user = USER_CONST
        port = PORT_CONST
        password = PASSWORD_CONST
        database = databaseName
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def insert(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            traceback.print_exc()
            self.db.rollback()
        finally:
            self.db.close()

    def fetchone(self, sql):
        # return with list<dictionary>
        result = list()
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
        except:
            traceback.print_exc()
            self.db.rollback()
        finally:
            self.db.close()
        return result

    def fetchall(self, sql):
        # return with list<dictionary>
        result = list()
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except:
            traceback.print_exc()
            self.db.rollback()
        finally:
            self.db.close()
        return results

    def delete(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            traceback.print_exc()
            self.db.rollback()
        finally:
            self.db.close()

    def update(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            traceback.print_exc()
            self.db.rollback()
        finally:
            self.db.close()
