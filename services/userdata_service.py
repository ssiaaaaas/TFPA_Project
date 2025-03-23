from flask import Flask, render_template, request, redirect, url_for, session , jsonify 
from repositories.fincheck_repositories import FinCheckRepositories
from repositories.userdata_repositories import UserDataRepositories
from repositories.backup_userdata_repositories import BackupUserDataRepositories
from repositories.crm_repositories import CRMRepositories

fincheck_repo = FinCheckRepositories()
userdata_repo = UserDataRepositories()
crm_repo = CRMRepositories()

class UserDataService:

    @staticmethod
    def Goal_input1():
        if request.method == "POST":
            # personal_info = session.get("personal_info", {})
            personal_info = session.get("personal_info", {})
            if personal_info == {}:
                return redirect(url_for("Fincheck.Personal_info"))
            
            # session["page2_data"] = request.form.get("data2")

            goals = []
    
            for key, value in request.form.items():
                if key.startswith('financial_goal_'):
                    index = key.split('_')[-1]
                    goals.append({
                        'financial_goal': value.strip(),
                        'time_period': request.form.get(f'time_period_{index}', '0').strip(),
                        'amount': request.form.get(f'amount_{index}', '0').strip(),
                        'payment_type': request.form.get(f'payment_type_{index}', 'one-time'),
                        'duration': request.form.get(f'duration_{index}', '').strip(),
                        'other_factors': request.form.get(f'other_factors_{index}', '').strip()
                    })
            
            print("Processed Goals:", goals) 
            
            priorities = range(1, len(goals) + 1)
            session["Goal_input1"] = goals
            return render_template("USER_Data_Collection/Goal_templates/Goal_input2.html" , financial_goal=goals , personal_info=personal_info, priorities=priorities)
            # return redirect(url_for("userdata.Goal_input2" , goals=goals))
        
        return render_template("USER_Data_Collection/Goal_templates/Goal_input1.html")
    

    @staticmethod
    def Goal_input2():
        if request.method == "POST":
            # personal_info = session.get("personal_info", {})
            personal_info = session.get("personal_info", {})
            if personal_info == {}:
                return redirect(url_for("Fincheck.Personal_info"))
            
            session["Goal_input2"] = request.form.to_dict()
            data = request.form
            print("data:" , data)
            session["Goal_input2"] = data
            # return jsonify({'message' : 'success'}) , 200
            return redirect(url_for("userdata.Pick_CFP"))
        
        # {"user": personal_info, "financial_goal": goals, "priorities": priorities}
        return render_template("USER_Data_Collection/Goal_templates/Goal_input2.html")
    

    @staticmethod
    def Pick_CFP():
        # personal_info = session.get("personal_info", {})
        personal_info = session.get("personal_info", {})
        if personal_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        
        return render_template("USER_Data_Collection/Pick_CFP.html")
    
    @staticmethod
    def User_Personal_info2():
        # personal_info = session.get("personal_info", {})
        personal_info = session.get("personal_info", {})
        print("personal_info: ", personal_info)
        if personal_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))


        if request.method == "POST":
            data = request.form
            print("data:" , data)
            session["User_Personal_info2"] = request.form.to_dict()


            jsonDataUser = {
                "personal_info" : session.get("personal_info", {}),
                "financial_info" : session.get("financial_info", {}),
                "data" : session.get("data", {}),
                "Goal_input1" : session.get("Goal_input1", {}),
                "Goal_input2" : session.get("Goal_input2", {}),
                "User_Personal_info2" : session.get("User_Personal_info2", {}),
            }
            print("jsonDataUser :", jsonDataUser)

            status_personal , personal_info_id = fincheck_repo.SavePersonalInfo(jsonDataUser['personal_info'])
            print("personal_info_id:" , personal_info_id)
            print("status_personal:" , status_personal)
            if status_personal == True:
                fincheck_repo.SaveFinancialInfo(jsonDataUser['financial_info'] , personal_info_id)
                fincheck_repo.SaveFinancialImage(personal_info_id,jsonDataUser['data'])
                userdata_repo.SaveUserPersonalinfo2(personal_info_id , jsonDataUser['User_Personal_info2'])
                for item in jsonDataUser['Goal_input1']:
                    userdata_repo.SaveGoalInput1(personal_info_id, item)

                for key, sub_dict in jsonDataUser['Goal_input2'].items():
                    print(f"Key: {key}, Value: {sub_dict}")
                    userdata_repo.SaveGoalInput2(personal_info_id , key , sub_dict)

            session["id"] = {
                "id" : personal_info_id
            }

            return jsonify({'message' : 'success'}) , 200

        return render_template("USER_Data_Collection/User_Personal_info2.html")
    
    @staticmethod
    def Work_detail():
        personal_info = session.get("personal_info", {})
        if personal_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        
        if request.method == "POST":
            data = request.form.to_dict()
            print("data:" , data)
            id = session.get("id", {})
            userdata_repo.SaveWorkdetail(id['id'],data)
            return redirect(url_for("userdata.Asset"))
        return render_template("USER_Data_Collection/Work_detail.html")
    
    @staticmethod
    def Asset():
        personal_info = session.get("personal_info", {})
        if personal_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        
        if request.method == "POST":
            data = request.get_json()
            print("data:" , data)
            id = session.get("id", {})
            userdata_repo.SaveAsset(id['id'],data[0])
            for item in data[0]['data']:
                if item['asset_name'] != "":
                    userdata_repo.SaveAssetDetail(id['id'],item)
            return jsonify({'message' : 'success'}) , 200
            # return redirect(url_for("userdata.Liabilities"))
        return render_template("USER_Data_Collection/Asset.html")
    
    @staticmethod
    def Liabilities():
        personal_info = session.get("personal_info", {})
        if personal_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        
        if request.method == "POST":
            data = request.get_json()
            print("data:" , data)
            id = session.get("id", {})
            for item in data:
                if item['amount_due'] != "":
                    userdata_repo.SaveLiabilities(id['id'],item)
            return jsonify({'message' : 'success'}) , 200
        return render_template("USER_Data_Collection/Liabilities.html")
    
    @staticmethod
    def Income():
        personal_info = session.get("personal_info", {})
        if personal_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        
        if request.method == "POST":
            data = request.get_json()
            print("data:" , data)
            id = session.get("id", {})
            for item in data:
                userdata_repo.SaveIncome(id['id'],item)
            return jsonify({'message' : 'success'}) , 200
        
        return render_template("USER_Data_Collection/Income.html")
    
    @staticmethod
    def Expense():
        personal_info = session.get("personal_info", {})
        if personal_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        
        if request.method == "POST":
            data = request.get_json()
            print("data:" , data)
            id = session.get("id", {})
            userdata_repo.SaveExpense(id['id'],data[0])
            for item in data[0]['data']:
                userdata_repo.SaveExpenseDetail(id['id'], item)
            return jsonify({'message' : 'success'}) , 200
        
        return render_template("USER_Data_Collection/Expense.html")
    
    @staticmethod
    def Risk1():
        personal_info = session.get("personal_info", {})
        if personal_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        

        personal_info = session.get("personal_info", {})
        if request.method == "POST":
            data = request.get_json()
            print("data:" , data)
            id = session.get("id", {})
            for item in data:
                userdata_repo.SaveRisk1(id['id'], item)

            return jsonify({'message' : 'success'}) , 200
        
        return render_template("USER_Data_Collection/Risk1.html")
    
    @staticmethod
    def Risk2():
        personal_info = session.get("personal_info", {})
        if personal_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        
        if request.method == "POST":
            data = request.get_json()
            print("data:" , data)
            id = session.get("id", {})
            for item in data:
                userdata_repo.SaveRisk2(id['id'], item)
            return jsonify({'message' : 'success'}) , 200
        
        return render_template("USER_Data_Collection/Risk2.html")
    
    @staticmethod
    def Risk3():
        personal_info = session.get("personal_info", {})
        if personal_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        
        if request.method == "POST":
            data = request.get_json()
            print("data:" , data)
            id = session.get("id", {})
            # for item in data:
            userdata_repo.SaveRisk3(id['id'], data)
            return jsonify({'message' : 'success'}) , 200
            # return redirect(url_for("crm.Home"))
        return render_template("USER_Data_Collection/Risk3.html")
    
# /// 
    @staticmethod
    def Edit_User_Personal_info2():
        personal_info = session.get("id", {})
        if personal_info == {}:
            return redirect(url_for("crm.Home"))


        if request.method == "POST":
            print("personal_info Edit_User_Personal_info2 : ", personal_info)
            data = request.form.to_dict()
            print("data:" , data)
            crm_repo.DeletData("user_info" , personal_info['id'])

            userdata_repo.SaveUserPersonalinfo2(personal_info['id'] , data)
            # status_personal , personal_info_id = fincheck_repo.SavePersonalInfo(data)
            return jsonify({'message' : 'success'}) , 200

        data = userdata_repo.GetUserPersonalinfo2(personal_info['id'])
        print("data :" , data)
        return render_template("USER_Data_Collection_Edit/User_Personal_info2.html" , data=data)
    
    @staticmethod
    def Edit_Work_detail():
        personal_info = session.get("id", {})
        if personal_info == {}:
            return redirect(url_for("crm.Home"))
        
        if request.method == "POST":
            data = request.form.to_dict()
            print("data:" , data)
            id = session.get("id", {})
            crm_repo.DeletData("work_detail" , id['id'])
            userdata_repo.SaveWorkdetail(id['id'],data)
            return redirect(url_for("userdata.Edit_Asset"))
        # {"user": personal_info, "financial_goal": goals, "priorities": priorities}
        return render_template("USER_Data_Collection_Edit/Work_detail.html")
    
    @staticmethod
    def Edit_Asset():
        personal_info = session.get("id", {})
        if personal_info == {}:
            return redirect(url_for("crm.Home"))
        
        if request.method == "POST":
            data = request.get_json()
            print("data:" , data)
            id = session.get("id", {})
            crm_repo.DeletData("asset" , id['id'])
            crm_repo.DeletData("asset_detail" , id['id'])
            userdata_repo.SaveAsset(id['id'],data[0])
            for item in data[0]['data']:
                if item['asset_name'] != "":
                    userdata_repo.SaveAssetDetail(id['id'],item)
            return jsonify({'message' : 'success'}) , 200
            # return redirect(url_for("userdata.Liabilities"))
        return render_template("USER_Data_Collection_Edit/Asset.html")
    
    @staticmethod
    def Edit_Liabilities():
        personal_info = session.get("id", {})
        if personal_info == {}:
            return redirect(url_for("crm.Home"))
        
        if request.method == "POST":
            data = request.get_json()
            print("data:" , data)
            id = session.get("id", {})
            crm_repo.DeletData("liabilities" , id['id'])
            for item in data:
                if item['amount_due'] != "":
                    userdata_repo.SaveLiabilities(id['id'],item)
            return jsonify({'message' : 'success'}) , 200
        return render_template("USER_Data_Collection_Edit/Liabilities.html")
    
    @staticmethod
    def Edit_Income():
        personal_info = session.get("id", {})
        if personal_info == {}:
            return redirect(url_for("crm.Home"))
        
        if request.method == "POST":
            data = request.get_json()
            print("data:" , data)
            id = session.get("id", {})
            crm_repo.DeletData("income" , id['id'])
            for item in data:
                userdata_repo.SaveIncome(id['id'],item)
            return jsonify({'message' : 'success'}) , 200
        
        return render_template("USER_Data_Collection_Edit/Income.html")
    
    @staticmethod
    def Edit_Expense():
        personal_info = session.get("id", {})
        if personal_info == {}:
            return redirect(url_for("crm.Home"))
        
        if request.method == "POST":
            data = request.get_json()
            print("data:" , data)
            id = session.get("id", {})
            crm_repo.DeletData("expense" , id['id'])
            crm_repo.DeletData("expense_detail" , id['id'])
            userdata_repo.SaveExpense(id['id'],data[0])
            for item in data[0]['data']:
                userdata_repo.SaveExpenseDetail(id['id'], item)
            return jsonify({'message' : 'success'}) , 200
        
        return render_template("USER_Data_Collection_Edit/Expense.html")
    
    @staticmethod
    def Edit_Risk1():
        personal_info = session.get("id", {})
        if personal_info == {}:
            return redirect(url_for("crm.Home"))
        

        personal_info = session.get("personal_info", {})
        if request.method == "POST":
            data = request.get_json()
            print("data:" , data)
            id = session.get("id", {})
            crm_repo.DeletData("risk1" , id['id'])
            for item in data:
                userdata_repo.SaveRisk1(id['id'], item)

            return jsonify({'message' : 'success'}) , 200
        
        return render_template("USER_Data_Collection_Edit/Risk1.html")
    
    @staticmethod
    def Edit_Risk2():
        personal_info = session.get("id", {})
        if personal_info == {}:
            return redirect(url_for("crm.Home"))
        
        if request.method == "POST":
            data = request.get_json()
            print("data:" , data)
            id = session.get("id", {})
            crm_repo.DeletData("risk2" , id['id'])
            for item in data:
                userdata_repo.SaveRisk2(id['id'], item)
            return jsonify({'message' : 'success'}) , 200
        
        return render_template("USER_Data_Collection_Edit/Risk2.html")
    
    @staticmethod
    def Edit_Risk3():
        personal_info = session.get("id", {})
        if personal_info == {}:
            return redirect(url_for("crm.Home"))
        
        if request.method == "POST":
            data = request.get_json()
            print("data:" , data)
            id = session.get("id", {})
            # for item in data:
            crm_repo.DeletData("risk3" , id['id'])
            userdata_repo.SaveRisk3(id['id'], data)
            return jsonify({'message' : 'success'}) , 200
            # return redirect(url_for("crm.Home"))
        return render_template("USER_Data_Collection_Edit/Risk3.html")