from dbconnection.dbconnector import DBConnector
import utils.function as fn

class FinCheckRepositories:

    @staticmethod
    def SavePersonalInfo(data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_personal = """
            INSERT INTO personal_info (name_title_eng, name_title_thai, dob, email, english_name, gender, job, password, thai_name)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)  RETURNING id
            """
            cursor = con.cursor()
            personal_values = (
                data['Name_title_eng'], data['Name_title_thai'], data['dob'],
                data['email'], data['english_name'], data['gender'],
                data['job'], data['password'], data['thai_name']
            )
            cursor.execute(sql_personal, personal_values)
            con.commit()
            last_inserted_id = cursor.fetchone()[0]
            print("last_inserted_id: ", last_inserted_id)
            cursor.close()
            con.close()
            return True , last_inserted_id
        except Exception as e:
            print(f"Error SavePersonalInfo: {e}")
            return False , "0"
        
    @staticmethod
    def GetPersonalInfo(id):
        try:
            print("start GetPersonalInfo :" , id)
            con = DBConnector.connect()
            cursor = con.cursor()
            cursor.execute("SELECT name_title_eng, name_title_thai, dob, email, english_name, gender, job, password, thai_name FROM personal_info WHERE id = %s", (id,))
            row = cursor.fetchone()

            if row is None:
                return {}
            
            result = {
                "name_title_eng": row[0],
                "name_title_thai": row[1],
                "dob": row[2],
                "age" : fn.calculate_age_new(row[2]),
                "email": row[3],
                "english_name": row[4],
                "gender": row[5],
                "job": row[6],
                "password": row[7],
                "thai_name": row[8],
            }
            
            cursor.close()
            con.close()

            return result
        except Exception as e:
            print("error GetPersonalInfo : " , e)
            return {}
        
    @staticmethod
    def GetPersonalInfoAll():
        try:
            print("start GetPersonalInfoAll :" , id)
            con = DBConnector.connect()
            cursor = con.cursor()
            cursor.execute("SELECT id,name_title_eng, name_title_thai, thai_name FROM personal_info")
            rows = cursor.fetchall()
            
            if not rows:
                return []

            result = [
                { 
                    "id" : row[0],
                    "name_title_eng": row[1],
                    "name_title_thai": row[2],
                    "thai_name": row[3],
                 } for row in rows]
            

            cursor.close()
            con.close()

            return result
        except Exception as e:
            print("error GetPersonalInfoAll : " , e)
            return []

        
    @staticmethod
    def SaveFinancialInfo(data,personal_info_id):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_financial = """
                INSERT INTO financial_info (personal_info_id, current_assets, debt_payments, life_expectancy, monthly_expenses, 
            monthly_income, retirement_age, savings, total_assets, total_liabilities)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor = con.cursor()
            financial_values = (
                personal_info_id, str(data['current_assets']), str(data['debt_payments']),
                str(data['life_expectancy']), str(data['monthly_expenses']),
                str(data['monthly_income']), str(data['retirement_age']),
                str(data['savings']), str(data['total_assets']),
                str(data['total_liabilities'])
            )
            cursor.execute(sql_financial, financial_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveFinancialInfo: {e}")
            return False 
        
    @staticmethod
    def GetFinancialInfo(id):
        try:
            print("start GetFinancialInfo :" , id)
            con = DBConnector.connect()
            cursor = con.cursor()

            select_query = """
            SELECT current_assets, debt_payments, life_expectancy, monthly_expenses, 
                monthly_income, retirement_age, savings, total_assets, total_liabilities 
            FROM financial_info 
            WHERE personal_info_id = %s
            """

            cursor.execute(select_query, (id,))
            
            row = cursor.fetchone()

            if row is None:
                return {}

            result = {
                "current_assets": row[0],
                "debt_payments": row[1],
                "life_expectancy": row[2],
                "monthly_expenses": row[3],
                "monthly_income": row[4],
                "retirement_age": row[5],
                "savings": row[6],
                "total_assets": row[7],
                "total_liabilities": row[8],
            }

            cursor.close()
            con.close()

            return result
        except Exception as e:
            print("error GetFinancialInfo :" , e)
            return {}

    
    @staticmethod
    def SaveFinancialImage(personal_info_id,data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO financial_image (mode, url_name , personal_info_id) VALUES (%s, %s, %s)"
            data_values = (data['mode'], data['url_name'], int(personal_info_id))
            cursor.execute(sql_data, data_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveFinancialImage: {e}")
            return False 
        
    @staticmethod
    def GetFinancialImages(id):
        try:
            print("start GetFinancialImage :" , str(id))
            con = DBConnector.connect()
            cursor = con.cursor()
            select_query = """
                SELECT mode, url_name
                FROM financial_image
                WHERE personal_info_id = %s
            """
            cursor.execute(select_query, (id,))

            rows = cursor.fetchall()

            if not rows:
                return []

            result = [{"mode": row[0], "url_name": row[1]} for row in rows]

            cursor.close()
            con.close()
            return result
        except Exception as e:
            print(f"Error GetFinancialImage: {e}")
            return [] 

    
