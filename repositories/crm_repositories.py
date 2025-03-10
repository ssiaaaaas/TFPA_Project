from dbconnection.dbconnector import DBConnector


class CRMRepositories:

    @staticmethod
    def Login(data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            query = "SELECT email, password,job,id,thai_name FROM personal_info WHERE email = %s"
            cursor.execute(query, (data['crm_user'],))
            user = cursor.fetchone()
            print("user: " , user)
            if user and user[1] == data['crm_pass']:
                print("Login successful")
                return True , user
            else:
                print("Invalid email or password")
                return False , None
            
        except Exception as e:
            print(f"Error Login: {e}")
            return False

    @staticmethod
    def Login(data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            query = "SELECT email, password,job,id,thai_name FROM personal_info WHERE email = %s"
            cursor.execute(query, (data['crm_user'],))
            user = cursor.fetchone()
            print("user: " , user)
            if user and user[1] == data['crm_pass']:
                print("Login successful")
                return True , user
            else:
                print("Invalid email or password")
                return False , None
            
        except Exception as e:
            print(f"Error Login: {e}")
            return False 
        
    @staticmethod
    def DeletData(table , personal_info_id_to_delete):
        try:
            print("start DeletData ", table)
            con = DBConnector.connect()
            cursor = con.cursor()
            if table == "user_info":
                cursor.execute(
                    "DELETE FROM user_info WHERE personal_info_id = %s", 
                    (personal_info_id_to_delete,)
                )
            if table == "work_detail":
                cursor.execute(
                    "DELETE FROM work_detail WHERE personal_info_id = %s", 
                    (personal_info_id_to_delete,)
                )
            if table == "asset":
                cursor.execute(
                    "DELETE FROM asset WHERE personal_info_id = %s", 
                    (personal_info_id_to_delete,)
                )
            if table == "asset_detail":
                cursor.execute(
                    "DELETE FROM asset_detail WHERE personal_info_id = %s", 
                    (personal_info_id_to_delete,)
                )
            if table == "liabilities":
                cursor.execute(
                    "DELETE FROM liabilities WHERE personal_info_id = %s", 
                    (personal_info_id_to_delete,)
                )
            if table == "income":
                cursor.execute(
                    "DELETE FROM income WHERE personal_info_id = %s", 
                    (personal_info_id_to_delete,)
                )
            if table == "expense":
                cursor.execute(
                    "DELETE FROM expense WHERE personal_info_id = %s", 
                    (personal_info_id_to_delete,)
                )
            if table == "expense_detail":
                cursor.execute(
                    "DELETE FROM expense_detail WHERE personal_info_id = %s", 
                    (personal_info_id_to_delete,)
                )
            if table == "risk1":
                cursor.execute(
                    "DELETE FROM risk1 WHERE personal_info_id = %s", 
                    (personal_info_id_to_delete,)
                )
            if table == "risk2":
                cursor.execute(
                    "DELETE FROM risk2 WHERE personal_info_id = %s", 
                    (personal_info_id_to_delete,)
                )
            if table == "risk3":
                cursor.execute(
                    "DELETE FROM risk3 WHERE personal_info_id = %s", 
                    (personal_info_id_to_delete,)
                )
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print("error : DeletData " ,table , " : " , e)
            return False

