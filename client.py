
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
    def get_Nom(id_cl):
        sql="select nom from Client where id_cl=?"
        val=(id_cl,)
        cursor.execute(sql,val)
        result=cursor.fetchone()
        return result[0]
    
    # Prenom :
    def get_Prenom(id_cl):
        sql="select prenom from Client where id_cl=?"
        val=(id_cl,)
        cursor.execute(sql,val)
        result=cursor.fetchone()
        return result[0]
    def get_id(login,password):
        sql="select id_cl from Client where login=? and password=?"
        val=(login,password)
        cursor.execute(sql,val)
        result=cursor.fetchone()
        return result[0]
    # Tel :
    

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
        elif result[0]==674539:
            return 1           #c'est l'admin qui est connecte
        else:
            return 0           #c'est un client qui est connecte
            


    # Fonction d'inscription:
    def Inscription(nom,prenom,tel,email,login,password):
        sql="insert into Client(nom,prenom,tel,email,login,password) values(?,?,?,?,?,?)"
        val=(nom,prenom,tel,email,login,password)
        cursor.execute(sql,val)
        cnx.commit()


    # juste pour un test:

 




