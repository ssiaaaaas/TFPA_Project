from flask import jsonify , render_template , send_file, request , url_for , redirect , session
from werkzeug.utils import secure_filename
from repositories.crm_repositories import CRMRepositories
from repositories.fincheck_repositories import FinCheckRepositories
from repositories.userdata_repositories import UserDataRepositories
import utils.function as fn
import utils.calculate as calculate
import os
from decimal import Decimal, InvalidOperation

crm_repo = CRMRepositories()
fincheck_repo = FinCheckRepositories()
userdata_repo = UserDataRepositories()

class CRMService:

    @staticmethod
    def Home():
        if request.method == "POST":
            data = request.form.to_dict()
            print("data : " , data)
            status , user = crm_repo.Login(data)
            if status == True:
                session["id"] = {
                        "job" : user[2],
                        "id" : user[3],
                        "name" : user[4]
                    }
                return redirect(url_for("crm.Dashboard"))

        return render_template("CRM/Login_CRM.html")
    
    @staticmethod
    def Dashboard():
        personal_info = session.get("id", {})
        if personal_info == {}:
            return redirect(url_for("crm.Home"))
        
        print("start")
        data = {
            "personal_info" : fincheck_repo.GetPersonalInfo(personal_info['id']),
            "financial_info" : fincheck_repo.GetFinancialInfo(personal_info['id']),
            "financial_images" : fincheck_repo.GetFinancialImages(personal_info['id'])
        }
        print("data : " , data)
        return render_template("CRM/User_CRM.html" , user=personal_info)
    
    @staticmethod
    def Dashboard1():
        id = request.args.get('id')
        print("id : " , id)
        personal_info = fincheck_repo.GetPersonalInfo(id)
        print("personal_info :" , personal_info)
        income = userdata_repo.GetIncome(id)[0]
        expense = userdata_repo.GetExpenseDetail(id)
        financial = fincheck_repo.GetFinancialInfo(id)

        asset = userdata_repo.GetAsset(id)
        asset_detail = userdata_repo.GetAssetDetail(id)
        expense_detail = userdata_repo.GetExpenseDetail(id)
        goal = userdata_repo.GetGoalInput1(id)
        
        print("asset: ", asset)
        print("asset_detail :" , asset_detail)    
        print("financial :" , financial)
        print("expense_detail : ", expense_detail)
        personal_assets = 0
        investment_assets = 0
        expense_sum = 0

        if len(expense_detail) > 0:
            for item in expense_detail:
                if item['fix_cf_value'] != "":
                    expense_sum = expense_sum + int(item['fix_cf_value'])

        if len(asset_detail) > 0:
            for item in asset_detail:
                print("item :", item)
                if item['asset_type'] == "personal_asset":
                    personal_assets = personal_assets + int(item['asset_value'])
                elif item['asset_type'] in ["bonds" , "perferred_shares" , "common_shares" , "funds" , "investment"]:
                    investment_assets = investment_assets + int(item['asset_value'])
        print("------")
        print("personal_assets :", personal_assets)
        print("investment_assets :", investment_assets)
        print("income: ", income)
        print("expense_sum :" , expense_sum)


        sum_asset = int(asset['number_bank']) + int(asset['fixedDeposit'])

        income_1  =float(income['income_1']) if income['income_1'] != "" else 0
        income_2  =float(income['income_2']) if income['income_2'] != "" else 0
        income_3  =float(income['income_3']) if income['income_3'] != "" else 0
        income_4  =float(income['income_4']) if income['income_4'] != "" else 0
        income_5  =float(income['income_5']) if income['income_5'] != "" else 0
        income_6  =float(income['income_6']) if income['income_6'] != "" else 0
        income_7  =float(income['income_7']) if income['income_7'] != "" else 0
        income_8  =float(income['income_8']) if income['income_8'] != "" else 0
        
        sum_income = income_1 + income_2 +income_3 +income_4 +income_5 +income_6 +income_7 +income_8
        sumall = (sum_income - expense_sum)
        print("start ")

        yearly_expenses = expense_sum
        years_before_retirement = int(financial['retirement_age']) - int(personal_info['age'])
        fund_on_retirement = fn.calculate_investment(
            principal=Decimal(yearly_expenses),
            annual_contribution=Decimal(0),
            annual_rate=3,  # Convert to percentage if applicable
            years=years_before_retirement
        )

        print("fund_on_retirement:" , fund_on_retirement)
        will_have_fund_on_retirment = calculate.will_have_fund_on_retirment(sum_asset , sumall, financial['retirement_age'], personal_info['age'] )
        fix_percent = 5 / 100  #
        fix_data = 3 / 100  

        # คำนวณ
        result = ((1 + fix_percent) / (1 + fix_data)) - 1
        must_have_fund_on_retirment = calculate.must_have_fund_on_retirment(financial['retirement_age'] , financial['life_expectancy'] , fund_on_retirement , result)
        print("start end ")
        print("will_have_fund_on_retirment: ", will_have_fund_on_retirment)
        print("goal :", goal)

        goalData = []
        goal_sum = 0

        

        for i in range(len(goal)):
            if i == 0:
                arr = {
                    "title" : "เป้าหมายหลัก",
                    "name_goal" : goal[i]['financial_goal'],
                    "value" : str("{:,.2f}".format(float(goal[i]['amount'])))
                }
                goal_sum = goal_sum + int(goal[i]['amount'])
            else:
                arr = {
                    "title" : "เป้าหมายรอง",
                    "name_goal" : goal[i]['financial_goal'],
                    "value" : str("{:,.2f}".format(float(goal[i]['amount']))) 
                }
                goal_sum = goal_sum + int(goal[i]['amount'])

            goalData.append(arr)

        fix = 0
        varSum = 0
        insurance = 0
        expense_sum = 0
        sumother = 0

        print("--------!!!!")
        for item in expense_detail:
            if item['fix_cf_value'] != "":
                expense_sum = expense_sum + int(item['fix_cf_value'])
            if item['fix_cf_mode'] == "fix":
                if item['fix_cf_value'] != "":
                    fix = fix +  float(item['fix_cf_value'])
            if item['fix_cf_mode'] == "insurance":
                if item['fix_cf_value'] != "":
                    insurance = insurance +  float(item['fix_cf_value'])
            if item['fix_cf_mode'] == "var":
                if item['fix_cf_value'] != "":
                    varSum = varSum +  float(item['fix_cf_value'])

        data_goal = []
        for item in goal:
            print("item : " ,item)
            if item['payment_type'] == "annual":
                data_goal.append([item['financial_goal'] , item['amount'] , item['amount'] , item['amount'] , item['amount'] , item['amount'] , item['amount']])
            if item['payment_type'] == "one-time":
                rowData = ["0"] * 7  
                rowData[0] = item['financial_goal']  
                print("item['time_period']: ", item['time_period'])
                if 1 <= int(item['time_period']) <= 6:
                    rowData[int(item['time_period'])+1] = item['amount']  
                
                print("rowData: ", rowData)
                data_goal.append(rowData)

        sum_columns = [sum(int(row[i]) for row in data_goal) for i in range(1, 7)]

        sumother = income_2 + income_3 + income_5 + income_6 +income_7 + income_8
        sum_all = (income_1 + sumother + income_4) - ((fix + insurance) + varSum)


        sum_all -sum_columns[0]

        data = {
            "income_expense" :  {
                "income_sum" : str(sum_income),
                "expense_sum" : str(expense_sum)
            },
            "assets" : {
                "liquid_assets" : str(int(asset['number_bank']) + int(asset['fixedDeposit'])),
                "investment_assets": str(personal_assets),
                "personal_assets" : str(investment_assets)
            },
            "retirement_plan": {
                "expected_retirement_savings" : str("{:,.2f}".format(will_have_fund_on_retirment)),
                "recommended_retirement_savings" : str("{:,.2f}".format(fund_on_retirement)),
                "additional_monthly_savings" : str("{:,.2f}".format(must_have_fund_on_retirment))
            },
            "financial_planning" : {
                "goal" : goalData,
                "financial_sum" : str("{:,.2f}".format(goal_sum)),
                "financial_amount" : str("{:,.2f}".format(float(sum_all) -float(sum_columns[0])))
            }
        }
        print("data :", data)
        return render_template("CRM/User1_Dashboard1.html" , user=personal_info , data=data)
    
    @staticmethod
    def Dashboard2():
        id = request.args.get('id')
        print("id : " , id)
        personal_assets = 0
        investment_assets = 0
        asset = userdata_repo.GetAsset(id)
        asset_detail = userdata_repo.GetAssetDetail(id)
        income = userdata_repo.GetIncome(id)[0]
        expense_detail = userdata_repo.GetExpenseDetail(id)
        liabilities = userdata_repo.GetLiabilities(id)

        asset_sum_total = 0
        if asset['number_bank'] != "" and asset['fixedDeposit'] != 0:
            asset_sum_total = asset_sum_total + (int(asset['number_bank']) + int(asset['fixedDeposit']))
       
        print("asset_detail :" , asset_detail)
        if len(asset_detail) > 0:
            for item in asset_detail:
                print("item :", item)
                asset_sum_total = asset_sum_total + int(item['asset_value'])
                if item['asset_type'] == "personal_asset":
                    personal_assets = personal_assets + int(item['asset_value'])
                elif item['asset_type'] in ["bonds" , "perferred_shares" , "common_shares" , "funds" , "investment"]:
                    investment_assets = investment_assets + int(item['asset_value'])

        income_1  =float(income['income_1']) if income['income_1'] != "" else 0
        income_2  =float(income['income_2']) if income['income_2'] != "" else 0
        income_3  =float(income['income_3']) if income['income_3'] != "" else 0
        income_4  =float(income['income_4']) if income['income_4'] != "" else 0
        income_5  =float(income['income_5']) if income['income_5'] != "" else 0
        income_6  =float(income['income_6']) if income['income_6'] != "" else 0
        income_7  =float(income['income_7']) if income['income_7'] != "" else 0
        income_8  =float(income['income_8']) if income['income_8'] != "" else 0

        fix = 0
        varSum = 0
        insurance = 0
        expense_sum = 0
        sumother = 0

        for item in expense_detail:
            if item['fix_cf_value'] != "":
                expense_sum = expense_sum + int(item['fix_cf_value'])
            if item['fix_cf_mode'] == "fix":
                if item['fix_cf_value'] != "":
                    fix = fix +  float(item['fix_cf_value'])
            if item['fix_cf_mode'] == "insurance":
                if item['fix_cf_value'] != "":
                    insurance = insurance +  float(item['fix_cf_value'])
            if item['fix_cf_mode'] == "var":
                if item['fix_cf_value'] != "":
                    varSum = varSum +  float(item['fix_cf_value'])
            

        sumother = income_2 + income_3 + income_5 + income_6 +income_7 + income_8
        print("fix + insurance :", fix + insurance)

        liability_sum_short_trem = 0
        liability_sum_long_trem = 0
        liability_sum = 0

        for item in liabilities:
            if item['liability_type'] == "short-term":
                liability_sum_short_trem = liability_sum_short_trem +  int(item['amount_due'])
            if item['liability_type'] == "long-term":
                liability_sum_long_trem = liability_sum_long_trem +  int(item['amount_due'])
        
        liability_sum = liability_sum_long_trem + liability_sum_short_trem
        
        data = {
            "cash_flow" : {
                "salary" : int(income_1),
                "sumother" : int(sumother),
                "fixed_expenses" : int(fix) + int(insurance),
                "variable_expenses" : int(varSum)
            },
            "balance" : [
                {
                    "name_one" : "สภาพคล่อง",
                    "bath_one" : str("{:,.2f}".format(float(int(asset['number_bank']) + int(asset['fixedDeposit'])))),
                    "ratio_one" : "0%",
                    "type" : "ระยะสั้น",
                    "bath_two" :  str("{:,.2f}".format(float(liability_sum_short_trem))),
                    "ratio_two" : "0%"
                },
                {
                    "name_one" : "การลงทุน",
                    "bath_one" : str("{:,.2f}".format(float(investment_assets))),
                    "ratio_one" : "0%",
                    "type" : "ระยะยาว",
                    "bath_two" : str("{:,.2f}".format(float(liability_sum_long_trem))),
                    "ratio_two" : "0%"
                },
                {
                    "name_one" : "ส่วนบุคคล",
                    "bath_one" : str("{:,.2f}".format(float(personal_assets))),
                    "ratio_one" : "0%",
                    "type" : "รวม",
                    "bath_two" : str("{:,.2f}".format(float(liability_sum_long_trem) + float(liability_sum_short_trem))),
                    "ratio_two" : "0%"
                }
            ],
            "balance_sum" : {
                    "bath_one" : str("{:,.2f}".format(float(personal_assets) +  float(investment_assets) + float(int(asset['number_bank']) + int(asset['fixedDeposit'])))),
                    "ratio_one" : "0%",
                    "bath_two" : str("{:,.2f}".format(float(asset_sum_total) - float(liability_sum))) ,
                    "ratio_two" : "0%"
                }
        }
        return render_template("CRM/User1_Dashboard2.html" , data=data)
    
    @staticmethod
    def Dashboard3():
        id = request.args.get('id')
        print("id : " , id)

        asset_detail = userdata_repo.GetAssetDetail(id)
        income = userdata_repo.GetIncome(id)[0]
        expense_detail = userdata_repo.GetExpenseDetail(id)
        work_detail = userdata_repo.GetWorkdetail(id)

        fix = 0
        varSum = 0
        insurance = 0
        expense_sum = 0
        sumother = 0

        for item in expense_detail:
            if item['fix_cf_value'] != "":
                expense_sum = expense_sum + int(item['fix_cf_value'])
            if item['fix_cf_mode'] == "fix":
                if item['fix_cf_value'] != "":
                    fix = fix +  float(item['fix_cf_value'])
            if item['fix_cf_mode'] == "insurance":
                if item['fix_cf_value'] != "":
                    insurance = insurance +  float(item['fix_cf_value'])
            if item['fix_cf_mode'] == "var":
                if item['fix_cf_value'] != "":
                    varSum = varSum +  float(item['fix_cf_value'])
        
        inflation = 3

        inflation_set = (1 + (inflation/100))

        fix_2568  = (fix * float(inflation_set))
        fix_2569  = (fix_2568 * float(inflation_set))
        fix_2570  = (fix_2569 * float(inflation_set))
        fix_2571  = (fix_2570 * float(inflation_set))

        insurance_2568  = (insurance * float(inflation_set))
        insurance_2569  = (insurance_2568 * float(inflation_set))
        insurance_2570  = (insurance_2569 * float(inflation_set))
        insurance_2571  = (insurance_2570 * float(inflation_set))

        varSum_2568  = (varSum * float(inflation_set))
        varSum_2569  = (varSum_2568 * float(inflation_set))
        varSum_2570  = (varSum_2569 * float(inflation_set))
        varSum_2571  = (varSum_2570 * float(inflation_set))
       
        income_1  =float(income['income_1']) if income['income_1'] != "" else 0
        income_2  =float(income['income_2']) if income['income_2'] != "" else 0
        income_3  =float(income['income_3']) if income['income_3'] != "" else 0
        income_4  =float(income['income_4']) if income['income_4'] != "" else 0
        income_5  =float(income['income_5']) if income['income_5'] != "" else 0
        income_6  =float(income['income_6']) if income['income_6'] != "" else 0
        income_7  =float(income['income_7']) if income['income_7'] != "" else 0
        income_8  =float(income['income_8']) if income['income_8'] != "" else 0
        

        salary_growth = (float(work_detail['salary_growth']) / 100) + 1
        growth_rate = 0.00
        growth_rate_order = 0.0
        inflation = 3

        inflation_set = (1 + (inflation/100))

        for item in asset_detail:
            # print("asset_detail : " , item['growth_rate'])
            if item['growth_rate'] != "":
                growth_rate = growth_rate + float(item['growth_rate'])
                growth_rate_order = growth_rate_order + 1

        print("growth_rate", growth_rate)
        print("salary_growth :" , salary_growth)
        print("growth_rate_order: " , growth_rate_order)
        # print("growth_rate / growth_rate_order" , (growth_rate / growth_rate_order))
        if growth_rate_order == 0:
            dividend_growth = 0.0
        else:
            dividend_growth = (float(growth_rate) / float(growth_rate_order))
            
        print("dividend_growth : ", dividend_growth)
        growth_rate_sum = (1 + (dividend_growth/100))
        
        print("growth_rate_sum :" , growth_rate_sum)
        income_1_2568  = ( income_1 * (float(salary_growth)))
        print("------ " , income_1_2568)
        income_1_2569  = (income_1_2568 * float(salary_growth))
        income_1_2570  = (income_1_2569 * float(salary_growth))
        income_1_2571  = (income_1_2570 * float(salary_growth))
        income_1_2572  = (income_1_2571 * float(salary_growth))

        income_4_2568  = (income_4 * float(growth_rate_sum))
        income_4_2569  = (income_4_2568 * float(growth_rate_sum))
        income_4_2570  = (income_4_2569 * float(growth_rate_sum))
        income_4_2571  = (income_4_2570 * float(growth_rate_sum))
        


        sum_income = income_1 + income_2 +income_3 +income_4 +income_5 +income_6 +income_7 +income_8
        
        sumall = (sum_income - expense_sum)

        sumall_2568  = (sumall * float(inflation_set))
        sumall_2569  = (sumall_2568 * float(inflation_set))
        sumall_2570  = (sumall_2569 * float(inflation_set))
        sumall_2571  = (sumall_2570 * float(inflation_set))

        data = [
            {
                "name" : "รวมรายรับ",
                "value1" : "{:,.2f}".format(income_1 + sumother + income_4) ,
                "value2" : "{:,.2f}".format(income_1_2568 + sumother + income_4_2568),
                "value3" : "{:,.2f}".format(income_1_2569 + sumother + income_4_2569) ,
                "value4" : "{:,.2f}".format(income_1_2570 + sumother + income_4_2570),
                "value5" : "{:,.2f}".format(income_1_2571 + sumother + income_4_2571),
            },
            {
                "name" : "รายจ่าย",
                "value1" : "{:,.2f}".format((fix + insurance) + varSum),
                "value2" : "{:,.2f}".format((fix_2568 + insurance_2568) + varSum_2568) ,
                "value3" : "{:,.2f}".format((fix_2569 + insurance_2569) + varSum_2569) ,
                "value4" : "{:,.2f}".format((fix_2570 + insurance_2570) + varSum_2570) ,
                "value5" : "{:,.2f}".format((fix_2571 + insurance_2571) + varSum_2571) ,
            },
            {
                "name" : "กระแสเงินสดสุทธิ",
                "value1" : "{:,.2f}".format(sumall),
                "value2" : "{:,.2f}".format(sumall_2568),
                "value3" : "{:,.2f}".format(sumall_2569),
                "value4" : "{:,.2f}".format(sumall_2570),
                "value5" : "{:,.2f}".format(sumall_2571),
            }
        ]
        return render_template("CRM/User1_Dashboard3.html" , data=data)
    
    @staticmethod
    def DownloadCashFlows():
        id = request.args.get('id') 
        output = f"static/file/Cash-flows-{id}.xlsx"
        asset = userdata_repo.GetAsset(id)
        asset_detail = userdata_repo.GetAssetDetail(id)
        income = userdata_repo.GetIncome(id)
        work_detail = userdata_repo.GetWorkdetail(id)
        expense_detail = userdata_repo.GetExpenseDetail(id)
        goal_input1 = userdata_repo.GetGoalInput1(id)
        personal_info = fincheck_repo.GetPersonalInfo(id)
        financial_info = fincheck_repo.GetFinancialInfo(id)
        fn.create_cash_flow_excel(asset , asset_detail, income[0] , work_detail , expense_detail ,goal_input1 , personal_info , financial_info ,  output)
        print("output DownloadFinStatement: " , output)
        return send_file(output)
        # return "ok"

        # fn.create_cash_flow_excel(output)
        # print("output DownloadCashFlows: ", output)
        # return send_file(output)
    
    @staticmethod
    def DownloadFinStatement():
        id = request.args.get('id')
        output = "static/file/Fin-statement-"+id+".xlsx"
        asset = userdata_repo.GetAsset(id)
        asset_detail = userdata_repo.GetAssetDetail(id)
        liabilities = userdata_repo.GetLiabilities(id)
        income = userdata_repo.GetIncome(id)
        expense_detail = userdata_repo.GetExpenseDetail(id)
        fn.create_budget_excel(asset ,asset_detail, liabilities , income[0] ,expense_detail , output)
        print("output DownloadFinStatement: " , output)
        return send_file(output)
        # return "ok"