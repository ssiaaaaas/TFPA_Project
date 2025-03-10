from flask import Blueprint, request , render_template , redirect, session, url_for , jsonify
import os
from services.crm_service import CRMService

crm = Blueprint('crm', __name__)
crm_service = CRMService()

@crm.route('/', methods=["GET", "POST"])
def Home():
   return crm_service.Home()

@crm.route('/logout')
def logout():
    session.pop('username', None)
    return redirect("/CRM")

@crm.route('/Dashboard')
def Dashboard():
   return crm_service.Dashboard()

@crm.route('/Dashboard/dashboard1')
def Dashboard1():
   return crm_service.Dashboard1()

@crm.route('/Dashboard/dashboard2')
def Dashboard2():
   return crm_service.Dashboard2()

@crm.route('/Dashboard/dashboard3')
def Dashboard3():
   return crm_service.Dashboard3()

@crm.route('/Dashboard/DownloadCashFlows')
def DownloadCashFlows():
   return crm_service.DownloadCashFlows()

@crm.route('/Dashboard/DownloadFinStatement')
def DownloadFinStatement():
   return crm_service.DownloadFinStatement()
