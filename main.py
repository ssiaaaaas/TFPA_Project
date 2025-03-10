from flask import Flask 
from flask_cors import CORS
from controllers.posidon_cfp_controller import PosidonCFPS
from controllers.fincheck_controller import Fincheck
from controllers.cfp_controller import cfp
from controllers.userdata_controller import userdata
from controllers.crm_controller import crm
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  
cors = CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})

app.register_blueprint(PosidonCFPS)
app.register_blueprint(Fincheck , url_prefix="/fincheck")
app.register_blueprint(cfp , url_prefix="/CFP")
app.register_blueprint(userdata , url_prefix="/UserDataCollection")
app.register_blueprint(crm , url_prefix="/CRM")




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0" , port=3000)
