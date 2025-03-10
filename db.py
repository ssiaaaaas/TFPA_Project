from dbconnection.dbconnector import DBConnector

# Connect to MySQL
con = DBConnector.connect()


cursor = con.cursor()

# Table creation queries
tables = {
    "personal_info": """
        CREATE TABLE IF NOT EXISTS personal_info (
            id SERIAL PRIMARY KEY,
            name_title_eng VARCHAR(50),
            name_title_thai VARCHAR(50),
            dob DATE,
            email VARCHAR(100) UNIQUE,
            english_name VARCHAR(100),
            gender VARCHAR(10),
            job VARCHAR(50),
            password VARCHAR(255),
            thai_name VARCHAR(100)
        )
    """,
     "user_info": """
        CREATE TABLE IF NOT EXISTS user_info (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            id_number VARCHAR(50),
            current_address VARCHAR(255),
            postal_code VARCHAR(10),
            province VARCHAR(100),
            district VARCHAR(100),
            subdistrict VARCHAR(100),
            street VARCHAR(255),
            village VARCHAR(255),
            education VARCHAR(50)
        )
    """,
     "user_info_backup": """
        CREATE TABLE IF NOT EXISTS user_info_backup (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            id_number VARCHAR(50),
            current_address VARCHAR(255),
            postal_code VARCHAR(10),
            province VARCHAR(100),
            district VARCHAR(100),
            subdistrict VARCHAR(100),
            street VARCHAR(255),
            village VARCHAR(255),
            education VARCHAR(50)
        )
    """,
    "financial_info": """
        CREATE TABLE IF NOT EXISTS financial_info (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            current_assets VARCHAR(120),
            debt_payments VARCHAR(120),
            life_expectancy VARCHAR(120),
            monthly_expenses VARCHAR(120),
            monthly_income VARCHAR(120),
            retirement_age VARCHAR(120),
            savings VARCHAR(120),
            total_assets VARCHAR(120),
            total_liabilities VARCHAR(120)
        )
    """,
    "financial_image": """
        CREATE TABLE IF NOT EXISTS financial_image (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            mode VARCHAR(50),
            url_name VARCHAR(255)
        )
    """,
    "Goal_input1": """
        CREATE TABLE IF NOT EXISTS goal_input1 (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            amount VARCHAR(120),
            duration VARCHAR(120),
            financial_goal VARCHAR(255),
            other_factors VARCHAR(255),
            payment_type VARCHAR(20),
            time_period VARCHAR(120)
        )
    """,
    "Goal_input2": """
        CREATE TABLE IF NOT EXISTS goal_input2 (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            name_goal VARCHAR(255),
            priority VARCHAR(255)
        )
    """,
    "Workdetail": """
        CREATE TABLE IF NOT EXISTS work_detail (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            job VARCHAR(255),
            work_place VARCHAR(255),
            department VARCHAR(255),
            job_title VARCHAR(255),
            salary VARCHAR(255),
            bonus VARCHAR(255),
            salary_growth VARCHAR(255),
            working_years VARCHAR(255),
            job_change_prop VARCHAR(255)
        )
    """,
    "Asset": """
        CREATE TABLE IF NOT EXISTS asset (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            number_bank VARCHAR(255),
            fixedDeposit VARCHAR(255)
        )
    """,
    "AssetDetail": """
        CREATE TABLE IF NOT EXISTS asset_detail (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            asset_type VARCHAR(255),
            asset_name VARCHAR(255),
            asset_value VARCHAR(255),
            asset_cost VARCHAR(255),
            dividend VARCHAR(255),
            growth_rate VARCHAR(255),
            purchase_date VARCHAR(255),
            maturity_date VARCHAR(255)
        )
    """,
    "Liabilities": """
        CREATE TABLE IF NOT EXISTS liabilities (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            liability_type VARCHAR(255),
            liability_name VARCHAR(255),
            amount_due VARCHAR(255),
            interest_rate VARCHAR(255)
        )
    """,
    "Income": """
        CREATE TABLE IF NOT EXISTS income (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            income_1 VARCHAR(255),
            income_2 VARCHAR(255),
            income_3 VARCHAR(255),
            income_4 VARCHAR(255),
            income_5 VARCHAR(255),
            income_6 VARCHAR(255),
            income_7 VARCHAR(255),
            income_8 VARCHAR(255)
        )
    """,
    "Expense": """
        CREATE TABLE IF NOT EXISTS expense (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            tax_income VARCHAR(255),
            tax_other VARCHAR(255)
        )
    """,
     "Expense_detail": """
        CREATE TABLE IF NOT EXISTS expense_detail (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            fix_cf_name VARCHAR(255),
            fix_cf_value VARCHAR(255),
            fix_cf_mode VARCHAR(255)
        )
    """,
     "Risk1": """
        CREATE TABLE IF NOT EXISTS risk1 (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            insurance_date VARCHAR(255),
            insurance_type VARCHAR(255),
            policyholder VARCHAR(255),
            policy_number VARCHAR(255),
            insurance_company VARCHAR(255),
            insurance_premium VARCHAR(255),
            insurance_fund VARCHAR(255),
            cash_value VARCHAR(255),
            policy_age VARCHAR(255)
        )
    """
    ,
     "Risk2": """
        CREATE TABLE IF NOT EXISTS risk2 (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            asset_insurance VARCHAR(255),
            insurance_type VARCHAR(255),
            policyholder VARCHAR(255),
            policy_number VARCHAR(255),
            insurance_company VARCHAR(255),
            insurance_premium VARCHAR(255),
            coverage_amount VARCHAR(255),
            coverage_period VARCHAR(255)
        )
    """,
     "Risk3": """
        CREATE TABLE IF NOT EXISTS risk3 (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            additional_welfare VARCHAR(255),
            medical_expense VARCHAR(255),
            group_insurance VARCHAR(255)
        )
    """,

    "personal_info_history": """
        CREATE TABLE IF NOT EXISTS personal_info_history (
            id SERIAL PRIMARY KEY,
            name_title_eng VARCHAR(50),
            name_title_thai VARCHAR(50),
            dob DATE,
            email VARCHAR(100) UNIQUE,
            english_name VARCHAR(100),
            gender VARCHAR(10),
            job VARCHAR(50),
            password VARCHAR(255),
            thai_name VARCHAR(100)
        )
    """,
    "financial_info_history": """
        CREATE TABLE IF NOT EXISTS financial_info_history (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            current_assets VARCHAR(120),
            debt_payments VARCHAR(120),
            life_expectancy VARCHAR(120),
            monthly_expenses VARCHAR(120),
            monthly_income VARCHAR(120),
            retirement_age VARCHAR(120),
            savings VARCHAR(120),
            total_assets VARCHAR(120),
            total_liabilities VARCHAR(120)
        )
    """,
    "financial_image_history": """
        CREATE TABLE IF NOT EXISTS financial_image_history (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            mode VARCHAR(50),
            url_name VARCHAR(255)
        )
    """,
    "Goal_input1_history": """
        CREATE TABLE IF NOT EXISTS goal_input1_history (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            amount VARCHAR(120),
            duration VARCHAR(120),
            financial_goal VARCHAR(255),
            other_factors VARCHAR(255),
            payment_type VARCHAR(20) CHECK (payment_type IN ('annual', 'monthly', 'weekly', 'daily')),
            time_period VARCHAR(120)
        )
    """,
    "Goal_input2_history": """
        CREATE TABLE IF NOT EXISTS goal_input2_backp (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            name_goal VARCHAR(255),
            priority VARCHAR(255)
        )
    """,
    "Workdetail_history": """
        CREATE TABLE IF NOT EXISTS work_detail_history (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            job VARCHAR(255),
            work_place VARCHAR(255),
            department VARCHAR(255),
            job_title VARCHAR(255),
            salary VARCHAR(255),
            bonus VARCHAR(255),
            salary_growth VARCHAR(255),
            working_years VARCHAR(255),
            job_change_prop VARCHAR(255)
        )
    """,
    "Asset_history": """
        CREATE TABLE IF NOT EXISTS asset_history (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            number_bank VARCHAR(255),
            fixedDeposit VARCHAR(255)
        )
    """,
    "AssetDetail_history": """
        CREATE TABLE IF NOT EXISTS asset_detail_history (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            asset_type VARCHAR(255),
            asset_name VARCHAR(255),
            asset_value VARCHAR(255),
            asset_cost VARCHAR(255),
            dividend VARCHAR(255),
            growth_rate VARCHAR(255),
            purchase_date VARCHAR(255),
            maturity_date VARCHAR(255)
        )
    """,
    "Liabilities_history": """
        CREATE TABLE IF NOT EXISTS liabilities_history (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            liability_type VARCHAR(255),
            liability_name VARCHAR(255),
            amount_due VARCHAR(255),
            interest_rate VARCHAR(255)
        )
    """,
    "Income_history": """
        CREATE TABLE IF NOT EXISTS income_history (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            income_1 VARCHAR(255),
            income_2 VARCHAR(255),
            income_3 VARCHAR(255),
            income_4 VARCHAR(255),
            income_5 VARCHAR(255),
            income_6 VARCHAR(255),
            income_7 VARCHAR(255),
            income_8 VARCHAR(255)
        )
    """,
    "Expense_history": """
        CREATE TABLE IF NOT EXISTS expense_history (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            tax_income VARCHAR(255),
            tax_other VARCHAR(255)
        )
    """,
     "Expense_detail_history": """
        CREATE TABLE IF NOT EXISTS expense_detail_history (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            fix_cf_name VARCHAR(255),
            fix_cf_value VARCHAR(255),
            fix_cf_mode VARCHAR(255)
        )
    """,
     "Risk1_history": """
        CREATE TABLE IF NOT EXISTS risk1_history (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            insurance_date VARCHAR(255),
            insurance_type VARCHAR(255),
            policyholder VARCHAR(255),
            policy_number VARCHAR(255),
            insurance_company VARCHAR(255),
            insurance_premium VARCHAR(255),
            insurance_fund VARCHAR(255),
            cash_value VARCHAR(255),
            policy_age VARCHAR(255)
        )
    """
    ,
     "Risk2_history": """
        CREATE TABLE IF NOT EXISTS risk2_history (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            asset_insurance VARCHAR(255),
            insurance_type VARCHAR(255),
            policyholder VARCHAR(255),
            policy_number VARCHAR(255),
            insurance_company VARCHAR(255),
            insurance_premium VARCHAR(255),
            coverage_amount VARCHAR(255),
            coverage_period VARCHAR(255)
        )
    """,
     "Risk3_history": """
        CREATE TABLE IF NOT EXISTS risk3_history (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            additional_welfare VARCHAR(255),
            medical_expense VARCHAR(255),
            group_insurance VARCHAR(255)
        )
    """,
     "CRP_Profile": """
        CREATE TABLE IF NOT EXISTS cfp_profile (
            id SERIAL PRIMARY KEY,
            personal_info_id INT REFERENCES personal_info(id) ON DELETE CASCADE,
            additional_welfare VARCHAR(255),
            medical_expense VARCHAR(255),
            group_insurance VARCHAR(255)
        )
    """
}

# Execute table creation
for table_name, query in tables.items():
    cursor.execute(query)
    print(f"Table '{table_name}' created successfully.")

con.commit()
cursor.close()
con.close()

print("All tables created successfully!")