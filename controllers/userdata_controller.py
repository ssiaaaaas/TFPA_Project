from flask import Blueprint, request , render_template , redirect, session, url_for , jsonify
import os
from services.userdata_service import UserDataService

userdata = Blueprint('userdata', __name__)
userdata_service = UserDataService()

@userdata.route('/Goal_input1' , methods=["GET", "POST"])
def Goal_input1():
   return userdata_service.Goal_input1()

@userdata.route('/Goal_input2' , methods=["GET", "POST"])
def Goal_input2():
   return userdata_service.Goal_input2()

@userdata.route('/Pick_CFP' , methods=["GET", "POST"])
def Pick_CFP():
   return userdata_service.Pick_CFP()

@userdata.route('/User_Personal_info2' , methods=["GET", "POST"])
def User_Personal_info2():
   return userdata_service.User_Personal_info2()

@userdata.route('/Work_detail' , methods=["GET", "POST"])
def Work_detail():
   return userdata_service.Work_detail()

@userdata.route('/Asset' , methods=["GET", "POST"])
def Asset():
   return userdata_service.Asset()

@userdata.route('/Liabilities' , methods=["GET", "POST"])
def Liabilities():
   return userdata_service.Liabilities()

@userdata.route('/Income' , methods=["GET", "POST"])
def Income():
   return userdata_service.Income()

@userdata.route('/Expense' , methods=["GET", "POST"])
def Expense():
   return userdata_service.Expense()

@userdata.route('/Risk1' , methods=["GET", "POST"])
def Risk1():
   return userdata_service.Risk1()

@userdata.route('/Risk2' , methods=["GET", "POST"])
def Risk2():
   return userdata_service.Risk2()

@userdata.route('/Risk3' , methods=["GET", "POST"])
def Risk3():
   return userdata_service.Risk3()


@userdata.route('/Edit/User_Personal_info2' , methods=["GET", "POST"])
def Edit_User_Personal_info2():
   return userdata_service.Edit_User_Personal_info2()

@userdata.route('/Edit/Work_detail' , methods=["GET", "POST"])
def Edit_Work_detail():
   return userdata_service.Edit_Work_detail()

@userdata.route('/Edit/Asset' , methods=["GET", "POST"])
def Edit_Asset():
   return userdata_service.Edit_Asset()

@userdata.route('/Edit/Liabilities' , methods=["GET", "POST"])
def Edit_Liabilities():
   return userdata_service.Edit_Liabilities()

@userdata.route('/Edit/Income' , methods=["GET", "POST"])
def Edit_Income():
   return userdata_service.Edit_Income()

@userdata.route('/Edit/Expense' , methods=["GET", "POST"])
def Edit_Expense():
   return userdata_service.Edit_Expense()

@userdata.route('/Edit/Risk1' , methods=["GET", "POST"])
def Edit_Risk1():
   return userdata_service.Edit_Risk1()

@userdata.route('/Edit/Risk2' , methods=["GET", "POST"])
def Edit_Risk2():
   return userdata_service.Edit_Risk2()

@userdata.route('/Edit/Risk3' , methods=["GET", "POST"])
def Edit_Risk3():
   return userdata_service.Edit_Risk3()


