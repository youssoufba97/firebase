
import pyrebase
from flask import *

ap = Flask(__name__)

Config = {

  "apiKey": "AIzaSyAZPZLD5Oo8_WRA9ziDLJq_vUVvqT6M0Vk",
  "authDomain": "cpanel5427.firebaseapp.com",
  "databaseURL": "https://cpanel5427.firebaseio.com",
  "projectId": "cpanel5427",
  "storageBucket": "cpanel5427.appspot.com",
  "messagingSenderId": "228227778190",
  "appId": "1:228227778190:web:92c2f36cb913eab7"
}

#initialisation
firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()


#email = input("Entrez votre adresse email: \n") #réccupérer la saisie de l'email
#password = input ("Entrez votre mot de passe: \n") # réccupérer la saisie du password

#user = auth.create_user_with_email_and_password(email,password) #permet de créer un utilisateur avec identifiant l'email et le password

#user = auth.sign_in_with_email_and_password(email,password) #permet l'authentification par l'emaail et le password

#auth.send_email_verification(user['idToken']) #vérifie l'email de l'utilisateur
#auth.send_password_reset_email(email) #réinitiliser le password

#print (auth.get_account_info(user['idToken'])) # reccupère et affiche les données du compte

@ap.route('/', methods=['GET', 'POST'])

def basic():
	
	unsuccessful = 'Please check your credentials!'
	successful = 'Login Successfully completed!' 

	if request.method == 'POST':
		email = request.form['name']
		password = request.form['pass']
		try:
			auth.sign_in_with_email_and_password(email, password)
			return'login successfully completed'
		
		except :
			return render_template('new.html', us=unsuccessful) 
			
		return 'Login successful'

	return render_template('new.html')		

if __name__ =='__main__':
	
	ap.run()
