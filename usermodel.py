from model.connection  import Conn

class UserModel:
    def __init__(self):
        self.connection = Conn.get_connection().connection
        self.cursor = self.connection.cursor()

    def login(self,username):
        query = 'SELECT pass,username FROM USER WHERE EMAILID=? or USERNAME=?'
        self.cursor.execute(query, username, username)
        password = self.cursor.fetchall()
        if password:
            return password
        else:
            return False

    def signup(self,username,pwd,email):
        query = """INSERT INTO USER(USERNAME,EMAILID,PASS) VALUES (?, ?, ?)"""
        try:
            self.cursor.execute(query, username, email, pwd)
            self.connection.commit()
            return True
        except:
            return False
