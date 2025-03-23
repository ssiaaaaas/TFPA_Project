from flask import Flask, render_template, request, redirect, url_for, session
import utils.function as fn
import utils.images as image
from decimal import Decimal, InvalidOperation

class FinCheckService:

    @staticmethod
    def Home():
        return render_template("Fincheck/UserDisclaimer.html")
    
    @staticmethod
    def Personal_info():
        if request.method == "POST":
            # session["page1_data"] = request.form.get("data1")
            session["personal_info"] = request.form.to_dict()
            return redirect(url_for("Fincheck.Financial_info"))
        return render_template("Fincheck/Personal_Information1.html")
    
    @staticmethod
    def Financial_info():
        if request.method == "POST":
            # session["page2_data"] = request.form.get("data2")

            personal_info = session.get("personal_info", {})
            if personal_info == {}:
                return redirect(url_for("Fincheck.Personal_info"))
            
            print("personal_info: " , personal_info)
           
            dob = personal_info['dob']
           
            age = fn.calculate_age(dob)

            retirement_age = request.form.get('retirement_age')
            monthly_expenses = request.form.get('monthly_expenses')
            savings = request.form.get('savings')
            current_assets = request.form.get('current_assets')
            total_assets = request.form.get('total_assets')
            total_liabilities = request.form.get('total_liabilities')
            debt_payments = request.form.get('debt_payments')
            monthly_income = request.form.get('monthly_income')

            r_after_retirement = Decimal(0.05)
            inflation = Decimal(0.03)
            print("retirement_age : ", retirement_age)
            print("age : ", age)
            years_before_retirement = int(retirement_age) - int(age)
            yearly_expenses = Decimal(monthly_expenses) * 12
            print("principal : ", Decimal(yearly_expenses))
            print("annual_contribution : ", Decimal(inflation *100))
            print("years : ", years_before_retirement)

            fund_on_retirement = fn.calculate_investment(
                principal=Decimal(yearly_expenses),
                annual_contribution=Decimal(0),
                annual_rate=Decimal(inflation *100),  
                years=years_before_retirement
            )

            print("fund_on_retirement: " , fund_on_retirement)
            print("r_after_retirement: " , r_after_retirement)
            needed_retirement_fund = fund_on_retirement / r_after_retirement
            print(needed_retirement_fund)
            print("needed_retirement_fund")
            will_have_fund = fn.calculate_investment(principal=current_assets,
                                                annual_contribution=savings,
                                                annual_rate=inflation /12,
                                                years=12*years_before_retirement)
            print(will_have_fund)
            missing_fund = int(needed_retirement_fund) - int(will_have_fund)
            if missing_fund < 0:
                missing_fund = 0
            print(missing_fund)

            calculated_data = {
                'age': int(age),
                'retirement_age': int(retirement_age),
                'monthly_expenses': int(monthly_expenses),
                'savings': int(savings),
                'needed_retirement_fund': int(needed_retirement_fund),
                'will_have_fund': int(will_have_fund),
                'missing_fund': int(missing_fund),
            }

            session["financial_info"] = request.form.to_dict()
            session["calculated_data"] = calculated_data

            Basic_Liquidity_Ratio = int(current_assets) / int(monthly_expenses)
            print(Basic_Liquidity_Ratio)
            L = 1 if Basic_Liquidity_Ratio >= 1 else 0
            Solvency_Ratio = (int(total_assets) - int(total_liabilities)) / int(total_assets)
            print(Solvency_Ratio)
            Debt_Service_Ratio = int(debt_payments) / int(monthly_income)
            print(Debt_Service_Ratio)
            D = 1 if (Solvency_Ratio >= 0.5 and Debt_Service_Ratio < 0.45) else 0
            Saving_Ratio = int(savings) / int(monthly_income)
            print(Saving_Ratio)
            S = 1 if Saving_Ratio >= 0.1 else 0
            print(L,D,S)

            # Decision logic for which page to show (based on your calculation rules)
            if L + D + S == 3: 
                return redirect(url_for("Fincheck.Future_Millionaire"))
            elif L == 0 and D == 0 and S == 1:
                return redirect(url_for("Fincheck.Savings_Starter_S"))
            elif L == 0 and D == 1 and S == 1:
                return redirect(url_for("Fincheck.Budget_Buddy_DS"))
            elif L == 1 and D == 1 and S == 0:
                return redirect(url_for("Fincheck.Budget_Buddy_LD"))
            elif L == 1 and D == 0 and S == 1:
                return redirect(url_for("Fincheck.Budget_Buddy_LS"))
            elif L == 0 and D == 1 and S == 0:
                return redirect(url_for("Fincheck.Savings_Starter_D"))
            elif L == 1 and D == 0 and S == 0:
                print("right")
                return redirect(url_for("Fincheck.Savings_Starter_L"))
            else:
                print("no")
                return redirect(url_for("Fincheck.Savings_Starter"))
            
            # return redirect(url_for("Fincheck.Budget_Buddy_LS"))
        return render_template("Fincheck/Financial_Information1.html")
    
    @staticmethod
    def Future_Millionaire():
        
        file_master = "static/media/analysis_images/Future_Millionaire.jpg"
        financial_info = session.get("calculated_data", {})
        if financial_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        
        print("financial_info : " , financial_info)
        text_positions = [
            (f"{financial_info['age']}", (160, 1060)),
            (f"{financial_info['retirement_age']}", (380, 1060)),
            (f"{financial_info['monthly_expenses']}", (120, 1140)),
            (f"{financial_info['savings']}", (340, 1140)),
            (f"{financial_info['needed_retirement_fund']}", (630, 1015)),
            (f"{financial_info['will_have_fund']}", (730, 1060)),
            (f"{financial_info['missing_fund']}", (615, 1100)),
        ]  
        url_name = image.generate_overlay_image_with_positions(file_master , text_positions)

        data = {
            'text_positions': text_positions,
            'url_name': url_name, 
            'mode' :  'Future_Millionaire'    
        }
        session["data"] = data
        
        return render_template("Fincheck/Future_Millionaire.html" , url_name=url_name)
    
    @staticmethod
    def Savings_Starter_S():
        
        file_master = "static/media/analysis_images/Savings_Starter_S.jpg"
        financial_info = session.get("calculated_data", {})
        if financial_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        print("financial_info : " , financial_info)
        text_positions = [
                (f"{financial_info['age']}", (160, 1060)),
                (f"{financial_info['retirement_age']}", (380, 1060)),
                (f"{financial_info['monthly_expenses']}", (120, 1140)),
                (f"{financial_info['savings']}", (340, 1140)),
                (f"{financial_info['needed_retirement_fund']}", (630, 1015)),
                (f"{financial_info['will_have_fund']}", (730, 1060)),
                (f"{financial_info['missing_fund']}", (615, 1100)),
            ]      
        url_name = image.generate_overlay_image_with_positions(file_master , text_positions)
        data = {
            'text_positions': text_positions,
            'url_name': url_name, 
            'mode' :  'Savings_Starter_S'    
        }
        session["data"] = data
        return render_template("Fincheck/Savings_Starter_S.html" , url_name=url_name)
    
    @staticmethod
    def Budget_Buddy_DS():
        
        file_master = "static/media/analysis_images/Budget_Buddy_SD.jpg"
        financial_info = session.get("calculated_data", {})
        if financial_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        print("financial_info : " , financial_info)
        text_positions = [
                (f"{financial_info['age']}", (160, 1060)),
                (f"{financial_info['retirement_age']}", (380, 1060)),
                (f"{financial_info['monthly_expenses']}", (120, 1140)),
                (f"{financial_info['savings']}", (340, 1140)),
                (f"{financial_info['needed_retirement_fund']}", (630, 1015)),
                (f"{financial_info['will_have_fund']}", (730, 1060)),
                (f"{financial_info['missing_fund']}", (615, 1100)),
            ]    
        url_name = image.generate_overlay_image_with_positions(file_master , text_positions)
        data = {
            'text_positions': text_positions,
            'url_name': url_name, 
            'mode' :  'Budget_Buddy_DS'    
        }
        session["data"] = data
        return render_template("Fincheck/Budget_Buddy_DS.html" , url_name=url_name)
    
    @staticmethod
    def Budget_Buddy_LD():
        
        file_master = "static/media/analysis_images/Budget_Buddy_LD.jpg"
        financial_info = session.get("calculated_data", {})
        if financial_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        print("financial_info : " , financial_info)
        text_positions = [
            (f"{financial_info['age']}", (160, 1060)),
            (f"{financial_info['retirement_age']}", (380, 1060)),
            (f"{financial_info['monthly_expenses']}", (120, 1140)),
            (f"{financial_info['savings']}", (340, 1140)),
            (f"{financial_info['needed_retirement_fund']}", (630, 1015)),
            (f"{financial_info['will_have_fund']}", (730, 1060)),
            (f"{financial_info['missing_fund']}", (615, 1100)),
        ]     
        url_name = image.generate_overlay_image_with_positions(file_master , text_positions)
        data = {
            'text_positions': text_positions,
            'url_name': url_name, 
            'mode' :  'Budget_Buddy_LD'    
        }
        session["data"] = data
        return render_template("Fincheck/Budget_Buddy_LD.html" , url_name=url_name) 
    
    @staticmethod
    def Budget_Buddy_LS():
        
        file_master = "static/media/analysis_images/Budget_Buddy_LS.jpg"
        financial_info = session.get("calculated_data", {})
        if financial_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        print("financial_info : " , financial_info)
        text_positions = [
                (f"{financial_info['age']}", (160, 1060)),
                (f"{financial_info['retirement_age']}", (380, 1060)),
                (f"{financial_info['monthly_expenses']}", (120, 1140)),
                (f"{financial_info['savings']}", (340, 1140)),
                (f"{financial_info['needed_retirement_fund']}", (630, 1015)),
                (f"{financial_info['will_have_fund']}", (730, 1060)),
                (f"{financial_info['missing_fund']}", (615, 1100)),
            ]     
        url_name = image.generate_overlay_image_with_positions(file_master , text_positions)
        data = {
            'text_positions': text_positions,
            'url_name': url_name, 
            'mode' :  'Budget_Buddy_LS'    
        }
        session["data"] = data
        return render_template("Fincheck/Budget_Buddy_LS.html" , url_name=url_name) 
    
    @staticmethod
    def Savings_Starter_D():
        file_master = "static/media/analysis_images/Savings_Starter_D.jpg"
        financial_info = session.get("calculated_data", {})
        if financial_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        print("financial_info : " , financial_info)
        text_positions = [
            (f"{financial_info['age']}", (160, 1060)),
            (f"{financial_info['retirement_age']}", (380, 1060)),
            (f"{financial_info['monthly_expenses']}", (120, 1140)),
            (f"{financial_info['savings']}", (340, 1140)),
            (f"{financial_info['needed_retirement_fund']}", (630, 1015)),
            (f"{financial_info['will_have_fund']}", (730, 1060)),
            (f"{financial_info['missing_fund']}", (615, 1100)),
        ]  
        url_name = image.generate_overlay_image_with_positions(file_master , text_positions)
        data = {
            'text_positions': text_positions,
            'url_name': url_name, 
            'mode' :  'Savings_Starter_D'    
        }
        session["data"] = data
        return render_template("Fincheck/Savings_Starter_D.html" , url_name=url_name) 
    
    @staticmethod
    def Savings_Starter_L():
        file_master = "static/media/analysis_images/Savings_Starter_L.jpg"
        financial_info = session.get("calculated_data", {})
        if financial_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        print("financial_info : " , financial_info)
        text_positions = [
                (f"{financial_info['age']}", (160, 1060)),
                (f"{financial_info['retirement_age']}", (380, 1060)),
                (f"{financial_info['monthly_expenses']}", (120, 1140)),
                (f"{financial_info['savings']}", (340, 1140)),
                (f"{financial_info['needed_retirement_fund']}", (630, 1015)),
                (f"{financial_info['will_have_fund']}", (730, 1060)),
                (f"{financial_info['missing_fund']}", (615, 1100)),
        ]   
        url_name = image.generate_overlay_image_with_positions(file_master , text_positions)
        data = {
            'text_positions': text_positions,
            'url_name': url_name, 
            'mode' :  'Savings_Starter_L'    
        }
        session["data"] = data
        return render_template("Fincheck/Savings_Starter_L.html" , url_name=url_name)

    @staticmethod
    def Savings_Starter():
        file_master = "static/media/analysis_images/Savings_Starter.jpg"
        financial_info = session.get("calculated_data", {})
        if financial_info == {}:
            return redirect(url_for("Fincheck.Personal_info"))
        print("financial_info : " , financial_info)
        text_positions = [
                (f"{financial_info['age']}", (160, 1060)),
                (f"{financial_info['retirement_age']}", (380, 1060)),
                (f"{financial_info['monthly_expenses']}", (120, 1140)),
                (f"{financial_info['savings']}", (340, 1140)),
                (f"{financial_info['needed_retirement_fund']}", (630, 1015)),
                (f"{financial_info['will_have_fund']}", (730, 1060)),
                (f"{financial_info['missing_fund']}", (615, 1100)),
        ]   
        url_name = image.generate_overlay_image_with_positions(file_master , text_positions)
        data = {
            'text_positions': text_positions,
            'url_name': url_name, 
            'mode' :  'Savings_Starter'    
        }
        session["data"] = data
        return render_template("Fincheck/Savings_Starter.html" , url_name=url_name)  