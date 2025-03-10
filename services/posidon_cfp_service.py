from flask import jsonify , render_template


class PosidonCFPService:

    @staticmethod
    def home():
        return render_template("PosidonCFP/MainHomePage.html")