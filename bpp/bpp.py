import pyrebase
from flask import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

bp = Flask(__name__)

cred = credentials.Certificate("cpanel5427-firebase-adminsdk-cqc0e-fc4d18e0a9.json")
config = {

  "apiKey": "AIzaSyAZPZLD5Oo8_WRA9ziDLJq_vUVvqT6M0Vk",
  "authDomain": "cpanel5427.firebaseapp.com",
  "databaseURL": "https://cpanel5427.firebaseio.com",
  "projectId": "cpanel5427",
  "storageBucket": "cpanel5427.appspot.com",
  "messagingSenderId": "228227778190",
  "appId": "1:228227778190:web:92c2f36cb913eab7"
  "cred"
}






firebase = pyrebase.initialize_app(config)
db = firebase.database()

#db.child("names").push({"name":"Karim Aboubakar"})
#db.child("names").update({"name": "Dion Aymard"}) #ajoute à la base de données "names" un champ "name" de valeur "Karim Aboubakar"
#users = db.child("names").child("name").get() #Récupère les valeurs du champ "name"
#print(users.val()) #Affiche les valeurs du champ "name"
#print(users.key()) # Affiche les valeurs du champ "name" et le nom du champ le contenant 
#db.child("names").child("name").remove() #supprime le champ "name" contenu dans la base "names"
#db.child("names").remove() #supprime la base "names"

@bp.route('/', methods=['GET', 'POST'])
def basic():
	if request.method == 'POST':
		if request.form['submit'] == 'add':
		
			name = request.form['name']
			db.child("todo").push(name)
			todo = db.child("todo").get()
			to = todo.val()
			return render_template('index.html', t=to.values())
		
		elif request.form['submit'] == 'delete':
			db.child("todo").remove()
			return render_template('index.html')
	return render_template('index.html')
if __name__ == '__main__':
	bp.run(debug=True)
	

"""
@bp.route('/', methods=['GET', 'POST'])
def basic():

	if request.method == 'POST':

		if request.form['submit'] == 'add':
			name = request.form['name']
			db.child("todo").push(name)
			todo = db.child("todo").get()
			to = todo.val()
			return render_template ('index.html', t=to.values())

		elif request.form['submit'] == 'delete':
			db.child("todo").remove()
		return render_template ('index.html')

	return render_template ('index.html')

if __name__ == '__main__':

	bp.run(debug=True)
	"""