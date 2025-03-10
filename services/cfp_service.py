from flask import jsonify , render_template , redirect , request , request , url_for , session
from repositories.userdata_repositories import UserDataRepositories
from repositories.fincheck_repositories import FinCheckRepositories

userdata_repo = UserDataRepositories()
fincheck_repo = FinCheckRepositories() 

class CFPService:

    @staticmethod
    def Home():

        if request.method == "POST":
            data = request.form.to_dict()
            print("data : " , data)
            
            return redirect(url_for("cfp.Dashboard"))
        
        return render_template("CFPSignupLogin/Login_CFP.html")
    
    @staticmethod
    def Dashboard():
        print("Dashboard : ")

        user = fincheck_repo.GetPersonalInfoAll()
        print("user :" , user )
        # return ""
        return render_template("CFPSignupLogin/CFP_CRM.html" , user=user) 