import string
import traceback
import pymysql
import Myconstants

_DEBUG = True
TABLE_CONST = "employee"


class MysqlUtil(object):

    def __init__(self, databaseName=Myconstants.DATABASE_CONST):
        host = Myconstants.HOST_CONST
        user = Myconstants.USER_CONST
        port = Myconstants.PORT_CONST
        password = Myconstants.PASSWORD_CONST
        database = databaseName
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    @staticmethod
    def __phraseSQL(table, fields, condition="NULL"):
        sql = "SELECT "
        haveQuote = 0
        for i in fields:
            if haveQuote == 0:
                haveQuote = 1
            else:
                sql += ', '
            sql += i
        sql += " FROM " + table

        if condition != "NULL":
            sql += f' WHERE {condition}'
        sql += ';'
        if _DEBUG:
            print(sql)
        return sql

    def ChangeDatabase(self, databaseName):
        self.db.close()
        self.cursor.close()
        host = Myconstants.HOST_CONST
        user = Myconstants.USER_CONST
        port = Myconstants.PORT_CONST
        password = Myconstants.PASSWORD_CONST
        database = databaseName
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def insert(self, table=TABLE_CONST, fields_and_vals=None):
        if fields_and_vals is None:
            fields_and_vals = {}
        sql = "INSERT INTO " + table
        sql += '('
        haveQuote = 0
        for firstPart, secondPart in fields_and_vals:
            if haveQuote == 0:
                haveQuote = 1
            else:
                sql += ', '
            sql += f"{firstPart}"
        sql += ') VALUES ('
        haveQuote = 0
        for firstPart, secondPart in fields_and_vals:
            if haveQuote == 0:
                haveQuote = 1
            else:
                sql += ', '
            if type(secondPart) == string:
                sql += f'"{secondPart}"'
            else:
                sql += f"{secondPart}"

        sql += ');'
        if _DEBUG:
            print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except pymysql.DatabaseError:
            traceback.print_exc()
            self.db.rollback()
        finally:
            self.db.close()

    def fetchone(self, table, condition="NULL", *fields):
        # return with list<dictionary>
        sql = self.__phraseSQL(table=table, condition=condition, fields=fields)

        result = list()
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
        except pymysql.DatabaseError:
            traceback.print_exc()
            self.db.rollback()
        finally:
            self.db.close()
        return result

    def fetchall(self, table, condition="NULL", *fields):
        # return with list<dictionary>
        sql = self.__phraseSQL(table=table, condition=condition, fields=fields)
        results = list()
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except pymysql.DatabaseError:
            traceback.print_exc()
            self.db.rollback()
        finally:
            self.db.close()
        return results

    def delete(self, table, condition):
        sql = f"DELETE FROM {table} WHERE {condition}"
        if _DEBUG:
            print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except pymysql.DatabaseError:
            traceback.print_exc()
            self.db.rollback()
        finally:
            self.db.close()

    def update(self, condition="NULL", table=TABLE_CONST, **fields_and_vals):
        sql = f'UPDATE {table} SET '
        haveQuote = 0
        for firstVal, secondVal in fields_and_vals:
            if haveQuote == 0:
                haveQuote = 1
            else:
                sql += ', '
            sql += f"{firstVal}="
            if type(secondVal) == string:
                sql += f'"{secondVal}"'
            else:
                sql += f"{secondVal}"
        if condition != "NULL":
            sql += condition
        if _DEBUG:
            print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except pymysql.DatabaseError:
            traceback.print_exc()
            self.db.rollback()
        finally:
            self.db.close()