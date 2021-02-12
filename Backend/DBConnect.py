import mysql.connector
import mysql.connector.errors
class DBConnect:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="123456789",
                                               database="assignment")
            self.cur = self.con.cursor()
            print('Sucess')

        except mysql.connector.Error as e:
            print(f"Unable to connect {e}")



    def insert(self,query,values):
        self.cur.execute(query,values)
        self.con.commit()

    def select(self,query,values):
        self.cur.execute(query, values)
        rows = self.cur.fetchall()
        return rows

    def update(self,query,values):
        self.cur.execute(query, values)
        self.con.commit()



DBConnect()