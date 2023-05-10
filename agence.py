
# Importer le module SQLite :
import sqlite3

# Se connecter à la base données :

cnx=sqlite3.connect('Location_voiture.db')

# Fermeture de la connexion à la base de données :
#cnx.close()

cursor=cnx.cursor()

    # Creation d'une liste vide des agences :"""

class Agence:
    
    def __init__(self,c=None,v=None,a=None,t=None):
        self.code_ag=c
        self.ville=v
        self.adresse=a
        self.tel=t

    def Affichage():
        cursor.execute("select * from Agence")
        result=cursor.fetchall()
        return result
    def Affichage_villes():
        cursor.execute("select ville from Agence")
        result=cursor.fetchall()
        return result
    def select_ville(code_ag):
        cursor.execute("select ville from Agence where code_ag=?",(code_ag,))
        
        result=cursor.fetchone()
        return result[0]

    

