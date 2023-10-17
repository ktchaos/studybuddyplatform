from .Authentication import Authentication
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyA7MEHCEYler-Di8IA2iIG0Yl-X_x5VN7g",
    'authDomain': "studybuddy-b2751.firebaseapp.com",
    'databaseURL': "https://studybuddy-b2751-default-rtdb.firebaseio.com",
    'projectId': "studybuddy-b2751",
    'storageBucket': "studybuddy-b2751.appspot.com",
    'messagingSenderId': "196421480481",
    'appId': "1:196421480481:web:2151c7d581bb6e52b93360",
    'measurementId': "G-5419DLQYWK"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Autenticação via Firebase
class FirebaseAuthentication(Authentication):
    def login(self, username, password):
        try:
            userAuthenticated = auth.sign_in_with_email_and_password(username, password)
            print(userAuthenticated.json())
        except:
            print("Credenciais incorretas.")

    def logout(self):
        pass