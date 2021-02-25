import mysql.connector
import mysql.connector.errors


class DBConnect:
    """This class serves as a bridge between our code and database. All CURD operation is performed through here"""
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="123456789",
                                               database="assignment")
            self.cur = self.con.cursor()

        except mysql.connector.Error as e:
            print(f"Unable to connect {e}")

    def insert(self, query, values):
        """This method validates query and insert values into respective database
        Here,
        Query = Query to execute
        value = Values supplied by user to be passed into database"""
        if type(query) is not str:
            raise TypeError("plz provide string ")
        self.cur.execute(query, values)
        self.con.commit()

    def select(self, query, values=None):
        """This method validates query and returns values from respective database
                Here,
                Query = Query to execute
                value = Values supplied by user to be passed into database (Optional)"""
        if type(query) is not str:
            raise TypeError("plz provide string ")
        self.cur.execute(query, values)
        rows = self.cur.fetchall()
        return rows

    def update(self, query, values):
        """This method validates query and updates values into respective database
                Here,
                Query = Query to execute
                value = Values supplied by user to be passed into database"""
        if type(query) is not str:
            raise TypeError("plz provide string ")
        self.cur.execute(query, values)
        self.con.commit()


    def delete(self, query, value):
        """This method validates query and removes values from respective database
                Here,
                Query = Query to execute
                value = Values supplied by user to be passed into database"""
        if type(query) is not str:
            raise TypeError("plz provide string ")
        self.cur.execute(query, value)
        self.con.commit()

    def __del__(self):
        if self.cur:
            self.cur.close()
        if self.con:
            self.con.close()
