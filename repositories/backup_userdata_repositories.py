from dbconnection.dbconnector import DBConnector


class BackupUserDataRepositories:

    @staticmethod
    def SaveUserPersonalinfo2(personal_info_id,data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO user_info_history (personal_info_id, id_number, current_address, postal_code, province, district, subdistrict, street, village, education ) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s)"
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
    def SaveGoalInput1(personal_info_id,data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO goal_input1_history (personal_info_id, amount , duration, financial_goal, other_factors , payment_type, time_period ) VALUES (%s, %s, %s, %s, %s, %s, %s)"
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
    def SaveGoalInput2(personal_info_id , key , sub_dict):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO goal_input2_history (name_goal, priority , personal_info_id) VALUES (%s, %s, %s)"
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
    def SaveWorkdetail(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO work_detail_history (personal_info_id, job , work_place, department, job_title, salary, bonus, salary_growth, working_years, job_change_prop) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
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
    def SaveAsset(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO asset_history (personal_info_id, number_bank , fixedDeposit) VALUES (%s, %s, %s)"
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
    def SaveAssetDetail(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO asset_detail_history (personal_info_id, asset_type , asset_name, asset_value, asset_cost, dividend, growth_rate , purchase_date, maturity_date) VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s)"
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
    def SaveLiabilities(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO liabilities_history (personal_info_id, liability_type , liability_name, amount_due, interest_rate) VALUES (%s, %s, %s, %s, %s)"
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
    def SaveIncome(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO income_history (personal_info_id, income_1 , income_2, income_3, income_4,income_5,income_6,income_7,income_8) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)"
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
    def SaveExpense(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO expense_history (personal_info_id, tax_income , tax_other) VALUES (%s, %s, %s)"
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
    def SaveExpenseDetail(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO expense_detail_history (personal_info_id, fix_cf_name , fix_cf_value, fix_cf_mode) VALUES (%s, %s, %s, %s)"
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
    def SaveRisk1(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO risk1_history (personal_info_id, insurance_date , insurance_type, policyholder, policy_number, insurance_company, insurance_premium, insurance_fund, cash_value, policy_age) VALUES (%s, %s, %s, %s, %s ,%s, %s,%s,%s,%s)"
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
    def SaveRisk2(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO risk2_history (personal_info_id, asset_insurance , insurance_type, policyholder, policy_number, insurance_company, insurance_premium, coverage_amount, coverage_period) VALUES (%s, %s, %s, %s, %s ,%s, %s,%s,%s)"
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
    def SaveRisk3(personal_info_id , data):
        try:
            con = DBConnector.connect()
            cursor = con.cursor()
            sql_data = "INSERT INTO risk3_history (personal_info_id , medical_expense, group_insurance) VALUES (%s, %s, %s)"
            data_values = (int(personal_info_id),  data['medical_expense'],data['group_insurance'])
            cursor.execute(sql_data, data_values)
            con.commit()
            cursor.close()
            con.close()
            return True
        except Exception as e:
            print(f"Error SaveRisk3: {e}")
            return False