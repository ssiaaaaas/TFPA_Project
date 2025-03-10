from flask import Blueprint, request , render_template , redirect, session, url_for , jsonify
import os
from services.cfp_service import CFPService

cfp = Blueprint('cfp', __name__)
cfp_service = CFPService()

@cfp.route('/' , methods=["GET", "POST"])
def Home():
   return cfp_service.Home()

@cfp.route('/Dashboard')
def Dashboard():
   return cfp_service.Dashboard()

