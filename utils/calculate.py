
def must_have_fund_on_retirment(retirement_age , life_expectancy , fund_on_retirement , result):
    retirement_age = int(retirement_age)
    life_expectency = int(life_expectancy)
    pmt_list = []
    print("result: ", result)
    print("1+result :" , 1+result)
    print("fund_on_retirement: ", fund_on_retirement)
    for i in range(life_expectency - retirement_age):
        pv = int(fund_on_retirement) / ((1+result) ** (i+1) )
        pmt_list.append(pv)
    must_have_fund_on_retirment = sum(pmt_list)
    print(must_have_fund_on_retirment)
    return must_have_fund_on_retirment


def will_have_fund_on_retirment(sum_asset , sumall, retirement_age, age ):
    current_saving = sum_asset
    print("sumall: ", sumall)
    total_cashflow = int(sumall)
    fv_pmt_list = []
    THOR = 2
    for j in range(int(retirement_age) - int(age)):
        fv = total_cashflow * ((1+(THOR/100))**(j))
        fv_pmt_list.append(fv)
        
    will_have_fund_on_retirment = sum(fv_pmt_list) + (current_saving*((1+(THOR/100))**(int(retirement_age) - int(age))))
    print(will_have_fund_on_retirment) #เงินที่จะมีตอนเก
    return will_have_fund_on_retirment

def sum_have_fund_on_retirment(will_have_fund_on_retirment, must_have_fund_on_retirment , retirement_age , age , sumall):
    print(" --- sum_have_fund_on_retirment 1 ---")
    missing_fund = int(will_have_fund_on_retirment) - int(must_have_fund_on_retirment)
    THOR = 2
    total_cashflow = int(sumall)
    print(" --- sum_have_fund_on_retirment 2 ---")
    missing_PMT = ((missing_fund*THOR/100)/(((1+THOR/100)**(int(retirement_age)-int(age)))-1))
    message = ""
    print(" --- sum_have_fund_on_retirment ---")
    if missing_fund > 0:
        print("เงินเพียงพอสำหรับการเกษียณ")#ขาดไป
        message = "เงินเพียงพอสำหรับการเกษียณ"
    else:

        message = "{:,.2f}".format(missing_fund)
    
    print(missing_PMT)#ต้องออมเพิ่มขึ้นเดือนละ
    return missing_PMT , message