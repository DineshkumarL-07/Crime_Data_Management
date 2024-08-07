from model.connection import Conn

class CrimeModel:
    def __init__(self):
        self.connection = Conn.get_connection().connection
        self.cursor = self.connection.cursor()

    def view(self):
        query = """SELECT * FROM CRIME"""
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        if rows:
            return rows
        else:
            return None

    def insert(self,date,police,details,status,place,witness,evidence):
        query = """INSERT INTO CRIME(DATEOFCRIME,POLICESTATIONID,CRIMEDESCRIPTION,STATUSOFCRIME,PLACEOFCRIME,WITNESS,EVIDENCE) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        try:
            self.cursor.execute(query, date, police, details, status, place, witness, evidence)
            self.connection.commit()
            return True
        except:
            return False

    def view_specific(self,col,val):
        query = f"SELECT * FROM CRIME WHERE {col} LIKE '%{val}%'"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        if rows:
            return rows
        else:
            return None

    def delete_specific(self,id):
        query = """DELETE FROM CRIME WHERE CRIMEID = ?"""
        try:
            self.cursor.execute(query, id)
            self.connection.commit()
            return True
        except:
            return False

    def update(self,id,col,val):
        query = f"""UPDATE CRIME SET {col} = ? WHERE CRIMEID = ?"""
        try:
            self.cursor.execute(query,val,id)
            self.connection.commit()
            return True
        except:
            return False

    def report(self,id,c_id,v_id):
        query1 = """INSERT INTO CC VALUES (?,?)"""
        query2 = """INSERT INTO CV VALUES (?,?)"""
        try:
            self.cursor.execute(query1, id, c_id)
            self.connection.commit()
            self.cursor.execute(query2, id, v_id)
            self.connection.commit()
            return True
        except:
            return False
    def overview(self,id):
        query = """SELECT DATEOFCRIME,POLICESTATIONID,CRIMEDESCRIPTION,STATUSOFCRIME FROM CRIME WHERE CRIMEID  = ?"""
        self.cursor.execute(query,id)
        rows = self.cursor.fetchall()
        if rows:
            return rows
        else:
            return None