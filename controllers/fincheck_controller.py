from flask import Blueprint, request , render_template , redirect, session, url_for , jsonify
import os
from services.fincheck_service import FinCheckService

Fincheck = Blueprint('Fincheck', __name__)
fincheck_service = FinCheckService()

@Fincheck.route('/')
def home():
   return fincheck_service.Home()

@Fincheck.route('/Personal_info' , methods=["GET", "POST"])
def Personal_info():
   return fincheck_service.Personal_info()

@Fincheck.route('/Financial_info' , methods=["GET", "POST"])
def Financial_info():
   return fincheck_service.Financial_info()

@Fincheck.route('/Future_Millionaire' , methods=["GET", "POST"])
def Future_Millionaire():
   return fincheck_service.Future_Millionaire()

@Fincheck.route('/Savings_Starter_S' , methods=["GET", "POST"])
def Savings_Starter_S():
   return fincheck_service.Savings_Starter_S()

@Fincheck.route('/Budget_Buddy_DS' , methods=["GET", "POST"])
def Budget_Buddy_DS():
   return fincheck_service.Budget_Buddy_DS()

@Fincheck.route('/Budget_Buddy_LD' , methods=["GET", "POST"])
def Budget_Buddy_LD():
   return fincheck_service.Budget_Buddy_LD()

@Fincheck.route('/Budget_Buddy_LS' , methods=["GET", "POST"])
def Budget_Buddy_LS():
   return fincheck_service.Budget_Buddy_LS()

@Fincheck.route('/Savings_Starter_D' , methods=["GET", "POST"])
def Savings_Starter_D():
   return fincheck_service.Savings_Starter_D()

@Fincheck.route('/Savings_Starter_L' , methods=["GET", "POST"])
def Savings_Starter_L():
   return fincheck_service.Savings_Starter_L()

@Fincheck.route('/Savings_Starter' , methods=["GET", "POST"])
def Savings_Starter():
   return fincheck_service.Savings_Starter()


