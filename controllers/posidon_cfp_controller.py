from flask import Blueprint, request , render_template , redirect, session, url_for , jsonify
import os
from services.posidon_cfp_service import PosidonCFPService

PosidonCFPS = Blueprint('PosidonCFPS', __name__)
posidon_cfp_service = PosidonCFPService()

@PosidonCFPS.route('/')
def home():
   return posidon_cfp_service.home()
