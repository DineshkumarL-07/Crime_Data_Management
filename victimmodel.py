from model.connection import Conn


class VictimModel:

    def __init__(self):
        self.connection = Conn.get_connection().connection
        self.cursor = self.connection.cursor()

    def view(self):
        query = """SELECT * FROM VICTIM"""
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        if rows:
            return rows
        else:
            return None

    def insert(self, name, age, gender, address, aadhaar, description):
        query = """INSERT INTO VICTIM(VICTIMNAME,VICTIMAGE,VICTIMGENDER,VICTIMADDRESS,VICTIMAADHAAR,VICTIMDESCRIPTION) VALUES (?, ?, ?, ?, ?, ?)"""
        try:
            self.cursor.execute(query, name, age, gender, address, aadhaar, description)
            self.connection.commit()
            return True
        except:
            return False

    def view_specific(self, col, val):
        query = f"SELECT * FROM VICTIM WHERE {col} LIKE '%{val}%'"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        if rows:
            return rows
        else:
            return None

    def delete_specific(self, id):
        query = """DELETE FROM VICTIM WHERE VICTIMID = ? OR VICTIMNAME = ?"""
        try:
            self.cursor.execute(query, id, id)
            self.connection.commit()
            return True
        except:
            return False

    def update(self,id,col,val):
        query = f"""UPDATE VICTIM SET {col}= ? WHERE VICTIMID = ? OR VICTIMNAME = ?"""
        try:
            self.cursor.execute(query,val,id,id)
            self.connection.commit()
            return True
        except:
            return False

    def get_id(self,name):
        query = """SELECT VICTIMID FROM VICTIM WHERE VICTIMNAME = ?"""
        self.cursor.execute(query,name)
        id = self.cursor.fetchone()
        if id:
            return id[0]
        else:
            return None

    def getid(self,id):
        query = """SELECT VICTIMNAME FROM VICTIM WHERE VICTIMID = (SELECT V_ID FROM CV WHERE C_ID = ?)"""
        self.cursor.execute(query,id)
        id = self.cursor.fetchone()
        if id:
            return id[0]
        else:
            return None
