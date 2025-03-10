from dbconnection.dbconnector import DBConnector


class UserDataRepositories:

    @staticmethod
    def SaveUserPersonalinfo2(personal_info_id,data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO user_info (personal_info_id, id_number, current_address, postal_code, province, district, subdistrict, street, village, education ) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s)"
            data_values = (int(personal_info_id),data['id_number'],data['current_address'],data['postal_code'],data['province'],data['district'],data['subdistrict'],data['street'],data['village'],data['education'])
            cursor.execute(sql_data, data_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveUserPersonalinfo2: {e}")
            return False 
        

    @staticmethod
    def GetUserPersonalinfo2(id):
        try:
            print("start GetUserPersonalinfo2 :" , str(id))
            con = DBConnector.connect()
            cursor = con.cursor()
            select_query = """
                SELECT id_number, current_address, postal_code, province, district, subdistrict, street, village, education
                FROM user_info
                WHERE personal_info_id = %s
            """
            cursor.execute(select_query, (id,))

            row = cursor.fetchone()

            if row is None:
                return {}

            result = {
                "id_number": row[0],
                "current_address": row[1],
                "postal_code": row[2],
                "province": row[3],
                "district": row[4],
                "subdistrict": row[5],
                "street": row[6],
                "village": row[7],
                "education": row[8]
            }


            cursor.close()
            con.close()
            return result
        except Exception as e:
            print(f"Error GetUserPersonalinfo2: {e}")
            return []

    @staticmethod
    def SaveGoalInput1(personal_info_id,data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO goal_input1 (personal_info_id, amount , duration, financial_goal, other_factors , payment_type, time_period ) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data_values = (int(personal_info_id),data['amount'],data['duration'],data['financial_goal'],data['other_factors'],data['payment_type'],data['time_period'])
            cursor.execute(sql_data, data_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveGoalInput1: {e}")
            return False 
    
    @staticmethod
    def GetGoalInput1(id):
        try:
            print("start GetGoalInput1 :" , str(id))
            con = DBConnector.connect()
            cursor = con.cursor()
            select_query = """
                SELECT amount , duration, financial_goal, other_factors , payment_type, time_period 
                FROM goal_input1
                WHERE personal_info_id = %s
            """
            cursor.execute(select_query, (id,))

            # row = cursor.fetchone()

            # if row is None:
            #     return {}

            # result = {
            #     "mamount": row[0],
            #     "duration": row[1],
            #     "financial_goal": row[2],
            #     "other_factors": row[3],
            #     "payment_type": row[4],
            #     "time_period": row[5]
            # }

            rows = cursor.fetchall()

            if not rows:
                return []

            result = [
                {
                "amount": row[0],
                "duration": row[1],
                "financial_goal": row[2],
                "other_factors": row[3],
                "payment_type": row[4],
                "time_period": row[5]
            } for row in rows]


            cursor.close()
            con.close()
            return result
        except Exception as e:
            print(f"Error GetGoalInput1: {e}")
            return []
        
    
    @staticmethod
    def SaveGoalInput2(personal_info_id , key , sub_dict):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO goal_input2 (name_goal, priority , personal_info_id) VALUES (%s, %s, %s)"
            data_values = (key, sub_dict, int(personal_info_id))
            cursor.execute(sql_data, data_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveGoalInput2: {e}")
            return False
        
    @staticmethod
    def GetGoalInput2(id):
        try:
            print("start GetGoalInput2 :" , str(id))
            con = DBConnector.connect()
            cursor = con.cursor()
            select_query = """
                SELECT name_goal, priority
                FROM goal_input2
                WHERE personal_info_id = %s
            """
            cursor.execute(select_query, (id,))

            rows = cursor.fetchall()

            if not rows:
                return []

            result = [{"name_goal": row[0], "priority": row[1]} for row in rows]

            cursor.close()
            con.close()
            return result
        except Exception as e:
            print(f"Error GetGoalInput2: {e}")
            return []
        
    @staticmethod
    def SaveWorkdetail(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO work_detail (personal_info_id, job , work_place, department, job_title, salary, bonus, salary_growth, working_years, job_change_prop) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
            data_values = (int(personal_info_id), data['job'], data['work_place'],data['department'],data['job_title'],data['salary'],data['bonus'],data['salary_growth'],data['working_years'],data['job_change_prop'])
            cursor.execute(sql_data, data_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveWorkdetail: {e}")
            return False
        
    @staticmethod
    def GetWorkdetail(id):
        try:
            print("start GetWorkdetail :" , str(id))
            con = DBConnector.connect()
            cursor = con.cursor()
            select_query = """
                SELECT job , work_place, department, job_title, salary, bonus, salary_growth, working_years, job_change_prop
                FROM work_detail
                WHERE personal_info_id = %s
            """
            cursor.execute(select_query, (id,))

            row = cursor.fetchone()

            if row is None:
                return {}

            result = {
                "job": row[0],
                "work_place": row[1],
                "department": row[2],
                "job_title": row[3],
                "salary": row[4],
                "bonus": row[5],
                "salary_growth": row[6],
                "working_years": row[7],
                "job_change_prop": row[8]
            }

            cursor.close()
            con.close()
            return result
        except Exception as e:
            print(f"Error GetGoalInput2: {e}")
            return []
    
    @staticmethod
    def SaveAsset(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO asset (personal_info_id, number_bank , fixedDeposit) VALUES (%s, %s, %s)"
            data_values = (int(personal_info_id), data['number_bank'], data['fixedDeposit'])
            cursor.execute(sql_data, data_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveAsset: {e}")
            return False
        
    @staticmethod
    def GetAsset(id):
        try:
            print("start GetAsset :" , str(id))
            con = DBConnector.connect()
            cursor = con.cursor()
            select_query = """
                SELECT number_bank , fixedDeposit
                FROM asset
                WHERE personal_info_id = %s
            """
            cursor.execute(select_query, (id,))

            row = cursor.fetchone()

            if row is None:
                return {}

            result = {
                "number_bank": row[0],
                "fixedDeposit": row[1]
            }

            cursor.close()
            con.close()
            return result
        except Exception as e:
            print(f"Error GetAsset: {e}")
            return []
        
    @staticmethod
    def SaveAssetDetail(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO asset_detail (personal_info_id, asset_type , asset_name, asset_value, asset_cost, dividend, growth_rate , purchase_date, maturity_date) VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s)"
            data_values = (int(personal_info_id), data['asset_type'], data['asset_name'],data['asset_value'],data['asset_cost'],data['dividend'],data['growth_rate'],data['purchase_date'],data['maturity_date'])
            cursor.execute(sql_data, data_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveAssetDetail: {e}")
            return False
        
    @staticmethod
    def GetAssetDetail(id):
        try:
            print("start GetAssetDetail :" , str(id))
            con = DBConnector.connect()
            cursor = con.cursor()
            select_query = """
                SELECT  asset_type , asset_name, asset_value, asset_cost, dividend, growth_rate , purchase_date, maturity_date
                FROM asset_detail
                WHERE personal_info_id = %s
            """
            cursor.execute(select_query, (id,))

            rows = cursor.fetchall()

            if not rows:
                return []

            result = [
                {
                    "asset_type": row[0], 
                    "asset_name": row[1],
                    "asset_value": row[2],
                    "asset_cost": row[3],
                    "dividend": row[4],
                    "growth_rate": row[5],
                    "purchase_date": row[6],
                    "maturity_date": row[7]
                    
            } for row in rows]

            cursor.close()
            con.close()
            return result
        except Exception as e:
            print(f"Error GetAssetDetail: {e}")
            return []
        
    @staticmethod
    def SaveLiabilities(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO liabilities (personal_info_id, liability_type , liability_name, amount_due, interest_rate) VALUES (%s, %s, %s, %s, %s)"
            data_values = (int(personal_info_id), data['liability_type'], data['liability_name'],data['amount_due'],data['interest_rate'])
            cursor.execute(sql_data, data_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveLiabilities: {e}")
            return False
        

    @staticmethod
    def GetLiabilities(id):
        try:
            print("start GetLiabilities :" , str(id))
            con = DBConnector.connect()
            cursor = con.cursor()
            select_query = """
                SELECT  liability_type , liability_name, amount_due, interest_rate
                FROM liabilities
                WHERE personal_info_id = %s
            """
            cursor.execute(select_query, (id,))

            rows = cursor.fetchall()

            if not rows:
                return []

            result = [
                {
                    "liability_type": row[0], 
                    "liability_name": row[1],
                    "amount_due": row[2],
                    "interest_rate": row[3]
                    
            } for row in rows]

            cursor.close()
            con.close()
            return result
        except Exception as e:
            print(f"Error GetLiabilities: {e}")
            return []
        
    @staticmethod
    def SaveIncome(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO income (personal_info_id, income_1 , income_2, income_3, income_4,income_5,income_6,income_7,income_8) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)"
            data_values = (int(personal_info_id), data['income_1'], data['income_2'],data['income_3'],data['income_4'],data['income_5'],data['income_6'],data['income_7'],data['income_8'])
            cursor.execute(sql_data, data_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveIncome: {e}")
            return False
        
    @staticmethod
    def GetIncome(id):
        try:
            print("start GetIncome :" , str(id))
            con = DBConnector.connect()
            cursor = con.cursor()
            select_query = """
                SELECT  income_1 , income_2, income_3, income_4,income_5,income_6,income_7,income_8
                FROM income
                WHERE personal_info_id = %s
            """
            cursor.execute(select_query, (id,))

            rows = cursor.fetchall()

            if not rows:
                return []

            result = [
                {
                    "income_1": row[0], 
                    "income_2": row[1],
                    "income_3": row[2],
                    "income_4": row[3],
                    "income_5": row[4],
                    "income_6": row[5],
                    "income_7": row[6],
                    "income_8": row[7],
                    
            } for row in rows]

            cursor.close()
            con.close()
            return result
        except Exception as e:
            print(f"Error GetIncome: {e}")
            return []
        
    @staticmethod
    def SaveExpense(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO expense (personal_info_id, tax_income , tax_other) VALUES (%s, %s, %s)"
            data_values = (int(personal_info_id), data['tax_income'], data['tax_other'])
            cursor.execute(sql_data, data_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveExpense: {e}")
            return False
        
    @staticmethod
    def GetExpense(id):
        try:
            print("start GetExpense :" , str(id))
            con = DBConnector.connect()
            cursor = con.cursor()
            select_query = """
                SELECT tax_income , tax_other
                FROM expense
                WHERE personal_info_id = %s
            """
            cursor.execute(select_query, (id,))

            row = cursor.fetchone()

            if row is None:
                return {}

            result = {
                "tax_income": row[0],
                "tax_other": row[1]
            }

            cursor.close()
            con.close()
            return result
        except Exception as e:
            print(f"Error GetExpense: {e}")
            return []
        
    
        
    @staticmethod
    def SaveExpenseDetail(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO expense_detail (personal_info_id, fix_cf_name , fix_cf_value, fix_cf_mode) VALUES (%s, %s, %s, %s)"
            data_values = (int(personal_info_id), data['fix_cf_name'], data['fix_cf_value'],data['fix_cf_mode'])
            cursor.execute(sql_data, data_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveExpenseDetail: {e}")
            return False
        
    @staticmethod
    def GetExpenseDetail(id):
        try:
            print("start GetExpenseDetail :" , str(id))
            con = DBConnector.connect()
            cursor = con.cursor()
            select_query = """
                SELECT fix_cf_name , fix_cf_value, fix_cf_mode
                FROM expense_detail
                WHERE personal_info_id = %s
            """
            cursor.execute(select_query, (id,))

            rows = cursor.fetchall()

            if not rows:
                return []

            result = [
                {
                "fix_cf_name": row[0], 
                "fix_cf_value": row[1],
                "fix_cf_mode": row[2]
                    
            } for row in rows]

            cursor.close()
            con.close()
            return result
        except Exception as e:
            print(f"Error GetExpenseDetail: {e}")
            return []
        
    @staticmethod
    def SaveRisk1(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO risk1 (personal_info_id, insurance_date , insurance_type, policyholder, policy_number, insurance_company, insurance_premium, insurance_fund, cash_value, policy_age) VALUES (%s, %s, %s, %s, %s ,%s, %s,%s,%s,%s)"
            data_values = (int(personal_info_id), data['insurance_date'], data['insurance_type'],data['policyholder'],data['policy_number'],data['insurance_company'],data['insurance_premium'],data['insurance_fund'],data['cash_value'],data['policy_age'])
            cursor.execute(sql_data, data_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveRisk1: {e}")
            return False
        
    @staticmethod
    def GetRisk1(id):
        try:
            print("start GetRisk1 :" , str(id))
            con = DBConnector.connect()
            cursor = con.cursor()
            select_query = """
                SELECT  insurance_date , insurance_type, policyholder, policy_number, insurance_company, insurance_premium, insurance_fund, cash_value, policy_age
                FROM risk1
                WHERE personal_info_id = %s
            """
            cursor.execute(select_query, (id,))

            rows = cursor.fetchall()

            if not rows:
                return []

            result = [
                {
                "insurance_date": row[0], 
                "insurance_type": row[1],
                "policyholder": row[2],
                "policy_number": row[3],
                "insurance_company": row[4],
                "insurance_premium": row[5],
                "insurance_fund": row[6],
                "cash_value": row[7],
                "policy_age": row[8]
                    
            } for row in rows]

            cursor.close()
            con.close()
            return result
        except Exception as e:
            print(f"Error GetRisk1: {e}")
            return []
        
    @staticmethod
    def SaveRisk2(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO risk2 (personal_info_id, asset_insurance , insurance_type, policyholder, policy_number, insurance_company, insurance_premium, coverage_amount, coverage_period) VALUES (%s, %s, %s, %s, %s ,%s, %s,%s,%s)"
            data_values = (int(personal_info_id), data['asset_insurance'], data['insurance_type'],data['policyholder'],data['policy_number'],data['insurance_company'],data['insurance_premium'],data['coverage_amount'],data['coverage_period'])
            cursor.execute(sql_data, data_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveRisk2: {e}")
            return False
        
    @staticmethod
    def GetRisk2(id):
        try:
            print("start SaveRisk2 :" , str(id))
            con = DBConnector.connect()
            cursor = con.cursor()
            select_query = """
                SELECT  asset_insurance , insurance_type, policyholder, policy_number, insurance_company, insurance_premium, coverage_amount, coverage_period
                FROM risk2
                WHERE personal_info_id = %s
            """
            cursor.execute(select_query, (id,))

            rows = cursor.fetchall()

            if not rows:
                return []

            result = [
                {
                "asset_insurance": row[0], 
                "insurance_type": row[1],
                "policyholder": row[2],
                "policy_number": row[3],
                "insurance_company": row[4],
                "insurance_premium": row[5],
                "coverage_amount": row[6],
                "coverage_period": row[7]
                    
            } for row in rows]

            cursor.close()
            con.close()
            return result
        except Exception as e:
            print(f"Error SaveRisk2: {e}")
            return []
        
    @staticmethod
    def SaveRisk3(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO risk3 (personal_info_id , medical_expense, group_insurance) VALUES (%s, %s, %s)"
            data_values = (int(personal_info_id),  data['medical_expense'],data['group_insurance'])
            cursor.execute(sql_data, data_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveRisk3: {e}")
            return False
        
    @staticmethod
    def GetRisk3(id):
        try:
            print("start SaveRisk3 :" , str(id))
            con = DBConnector.connect()
            cursor = con.cursor()
            select_query = """
                SELECT   medical_expense, group_insurance
                FROM risk3
                WHERE personal_info_id = %s
            """
            cursor.execute(select_query, (id,))

            rows = cursor.fetchall()

            if not rows:
                return []

            result = [
                {
                "medical_expense": row[0], 
                "group_insurance": row[1]
                    
            } for row in rows]

            cursor.close()
            con.close()
            return result
        except Exception as e:
            print(f"Error SaveRisk3: {e}")
            return []
