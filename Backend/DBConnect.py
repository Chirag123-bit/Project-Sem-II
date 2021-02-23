import mysql.connector
import mysql.connector.errors


class DBConnect:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="123456789",
                                               database="assignment")
            self.cur = self.con.cursor()

        except mysql.connector.Error as e:
            print(f"Unable to connect {e}")

    def insert(self, query, values):
        if type(query) is not str:
            raise TypeError("plz provide string ")
        self.cur.execute(query, values)
        self.con.commit()

    def select(self, query, values=None):
        if type(query) is not str:
            raise TypeError("plz provide string ")
        self.cur.execute(query, values)
        rows = self.cur.fetchall()
        return rows

    def update(self, query, values):
        if type(query) is not str:
            raise TypeError("plz provide string ")
        self.cur.execute(query, values)
        self.con.commit()


    def delete(self, query, value):
        if type(query) is not str:
            raise TypeError("plz provide string ")
        self.cur.execute(query, value)
        self.con.commit()

    def __del__(self):
        if self.cur:
            self.cur.close()
        if self.con:
            self.con.close()
