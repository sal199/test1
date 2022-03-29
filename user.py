
"""un programme qui permetre de cree une compte et de se 
connecter a ce compte 
"""
class user:
    def __init__(self):
        self.nom=str
        self.prenom=str 
        self.adress_email=str
        self.password=str
        self.sexe=str
        self.nationalite=str
        self.data=dict()
    def create(self):
        print(" bienvenue dans la programation orient objet\n")
        self.nom=input(" entrer votre nom s'il vous plait\n")
        self.prenom=input("entrer votre prenom s'il vous plait\n")
        self.sexe=input("donner votre sexe\n")
        self.nationalite=input("donner votre nationalite\n")
        self.adress_email=input("entre votre adress email\n")
        self.password=input("entrer votre mot de passe\n")
        while len(self.password) < 8:
            print ("votre mot de passe est inferieur a 8\n")
            self.password=("entrer votre mot de passe\n")
        password_comfirme=input("veuillez confirmer votre mot de passe\n")
        while password_comfirme !=self.password:
            print('votre mot de passe est incorrect\n')
            password_comfirme=input("entrez votre mot de passe\n")
        self.data[self.adress_email]=[self,self.nom,self.prenom,self.password,self.sexe,self.nationalite]
    def login (self):
        email= input("entre votre mot de passe\n")
        while email!=self.data.keys:
            print("votre emaile est bien normail\n")
        password_login=input('entre votre password')
        while password_login!=self.data[email].values():
            print('donner a nouveau votre mot de passe')
            
#programmme principal
user=user()
demander=('voulez vous ce connecter ou bien cree un compte\n')
if demander=="connecter":
    user.login()
else:
    user.create()
        
        