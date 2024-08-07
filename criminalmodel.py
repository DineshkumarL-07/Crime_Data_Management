from model.connection import Conn

class CriminalModel:
    def __init__(self):
        self.connection = Conn.get_connection().connection
        self.cursor = self.connection.cursor()

    def view(self):
        query = """SELECT * FROM CRIMINAL"""
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        if rows:
            return rows
        else:
            return None

    def insert(self,name,aadhaar,age,gender,address,police,birthmark):
        query = """INSERT INTO CRIMINAL(CRIMINALNAME,CRIMINALAADHAAR,CRIMINALAGE,CRIMINALGENDER,CRIMINALADDRESS,POLICESTATIONID,BIRTHMARK) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        try:
            self.cursor.execute(query, name, aadhaar, age, gender, address, police, birthmark)
            self.connection.commit()
            return True
        except:
            return False

    def view_specific(self,col,val):
        query = f"SELECT * FROM CRIMINAL WHERE {col} LIKE '%{val}%'"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        if rows:
            return rows
        else:
            return None

    def delete_specific(self,id):
        query = """DELETE FROM CRIMINAL WHERE CRIMINALID = ? OR CRIMINALNAME = ?"""
        try:
            self.cursor.execute(query, id, id)
            self.connection.commit()
            return True
        except:
            return False

    def update(self,id,col,val):
        query = f"""UPDATE CRIMINAL SET {col}= ? WHERE CRIMINALID = ? OR CRIMINALNAME = ?"""
        try:
            self.cursor.execute(query,val,id,id)
            self.connection.commit()
            return True
        except:
            return False

    def get_name(self,name):
        query = """SELECT CRIMINALID FROM CRIMINAL WHERE CRIMINALNAME = ?"""
        self.cursor.execute(query, name)
        id = self.cursor.fetchone()
        if id:
            return id[0]
        else:
            return None

    def get_id(self,id):
        query = """SELECT CRIMINALNAME FROM CRIMINAL WHERE CRIMINALID = (SELECT CRIMINAL_ID FROM CC WHERE CRIME_ID = ?)"""
        self.cursor.execute(query,id)
        id = self.cursor.fetchone()
        if id:
            return id[0]
        else:
            return None