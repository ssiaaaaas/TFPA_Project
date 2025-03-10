import psycopg2
import os
from repositories.fincheck_repositories import FinCheckRepositories

fincheck_repo = FinCheckRepositories()

conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )

jsonData = {
    'personal_info': {
        'Name_title_eng': 'miss', 'Name_title_thai': 'miss', 'dob': '2013-06-27', 'email': 'admin@admin.com', 'english_name': 'fdsfdsfsdfsf', 'gender': 'male', 'job': 'student', 'password': '1', 'thai_name': 'dfdsfs'
        }, 
    'financial_info': {
        'current_assets': '1', 'debt_payments': '1', 'life_expectancy': '1', 'monthly_expenses': '1', 'monthly_income': '1', 'personal_info_id': '', 'retirement_age': '1', 'savings': '1', 'total_assets': '1', 'total_liabilities': '1'
    }, 
    'data': {
        'mode': 'Budget_Buddy_LS', 
        'text_positions': [('11', (160, 1060)), ('1', (380, 1060)), ('1', (120, 1140)), ('1', (340, 1140)), ('1653542033102', (630, 1015)), ('-118', (730, 1060)), ('1653542033220', (615, 1100))], 
        'url_name': 'static/media/cover/overlayed_budget_ld_precise.png'
        }, 
    'Goal_input1': [
        {'amount': '1', 'duration': '1', 'financial_goal': '1', 'other_factors': '1', 'payment_type': 'annual', 'time_period': '1'
            }
    ], 'Goal_input2': {
        'goal1': '1'
        }
    }

# status_personal , personal_info_id = fincheck_repo.SavePersonalInfo(jsonData['personal_info'])
# print("personal_info_id:" , personal_info_id)
# print("status_personal:" , status_personal)

for iten in jsonData['Goal_input1']:
    print(iten)

for key, sub_dict in jsonData['Goal_input2'].items():
    print(f"Key: {key}, Value: {sub_dict}")