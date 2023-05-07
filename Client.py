
# Importer le module SQLite :
import sqlite3

# Se connecter à la base données :

cnx=sqlite3.connect('Location_voiture.db')
 # Fermeture de la connexion à la base de données :
#cnx.close()

cursor=cnx.cursor()



class Client:

    # Constructeur de client :

    def __init__(self,id=None,n=None,pr=None,t=None,e=None,log=None,pwd=None):
        self.id_cl=id   
        self.nom=n
        self.prenom=pr
        self.tel=t
        self.email=e
        self.login=log
        self.password=pwd


    # Getters :------------------------------------------------------------------------------

    # Nom :
    def get_Nom(self):
        return self.nom
    
    # Prenom :
    def get_Prenom(self):
        return self.prenom
    
    # Tel :
    def get_Tel(self):
        return self.tel 
    
    # Email :
    def get_Emeil(self):
        return self.email
    
    # Login :
    def get_Login(self):
        return self.login
    
    # Password :
    def get_Password(self):
        return self.password

# Setters : ---------------------------------------------------------------------------------------------------------------------------

    # Nom :
    # Prenom :
    # Tel :


    
#-------------------------------------------------------------------------------------




    # Fonction connexion :
    def Connexion(login,password):
        sql="select id_cl from Client where login=? and password=?"
        val=(login,password)
        cursor.execute(sql,val)
        result=cursor.fetchone()
        if result is None:
            return -1          #client introuvable
        elif result==674539:
            return 1           #c'est l'admin qui est connecte
        else:
            return 0           #c'est un client qui est connecte
            


    # Fonction d'inscription:
    def Inscription(nom,prenom,tel,email,login,password):
        sql="insert into Client(nom,prenom,tel,email,login,password) values(?,?,?,?,?,?)"
        val=(nom,prenom,tel,email,login,password)
        cursor.execute(sql,val)
        cnx.commit()
        return True


    # juste pour un test:

    def supp(id_cl):
        sql="delete from Client where id_cl=?"
        val=(id_cl,)
        cursor.execute(sql,val)
        cnx.commit()
        return True






c=Client()
print("---Inscription-------------------------")
print("")
nom=input("Nom : ")
prenom=input("Prenom : ")
tel=input("Tel : ")
email=input("Email : ")
login=input("Login : ")
password=input("Password :")
i=c.Inscription(nom,prenom,tel,email,login,password)
print(i)
print("")
print("---suppression-----------------------")
print("")
id=input("Id :")
supp=c.supp(id)
print(supp)
