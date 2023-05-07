#from Client import *
#from Voiture import *
# Importer le module SQLite :
import sqlite3


# Se connecter à la base données :

cnx=sqlite3.connect('Location_voiture.db')
cursor=cnx.cursor()

# Fermeture de la connexion à la base de données :
#cnx.close()

class Reservation:

    def __init__(self) -> None:
        pass
    
    # Reserver :
    
    def Reserver(date_res,duree_res,mtrcl,id_cl):        
        cursor.execute("select prix_loc_j from Voiture where matricule=?",(mtrcl,))
        prix=cursor.fetchone()
        prix_res=duree_res*prix[0]
        sql="insert into Reservation (etat_res,prix_res,date_res,duree_res,matricule,id_cl) values(FALSE,?,?,?,?,?)" 
        val=(prix_res,date_res,duree_res,mtrcl,id_cl)
        cursor.execute(sql,val)
        cnx.commit()
        return True
    

    # Affichage des reservation :
    def Afficher(id_cl):
        cursor.execute("select * from Reservation r join Client c on r.id_cl=c.id_cl join Voiture v on v.matricule=r.matricule where c.id_cl=?",(id_cl,))
        res=cursor.fetchall()
        return res[-1]    
   

    # Confirmer reservation :      
    def Confirmation(code_res):
        cursor.execute("update Reservation set etat_res=TRUE where code_res=?",(code_res,))
        cnx.commit()
        return True
    
    # Annuler reservation :
    def Annuler(code_res):
        cursor.execute("delete from Reservation where code_res=?",(code_res,))
        cnx.commit()
        return True


    
    
    
    




r=Reservation()
print("")
print("---Reserver-----------------------------")
print("")

from datetime import datetime,date

time_str = input("enter time in this format yyyy-mm-dd")
date_res=datetime.strptime(time_str, "%Y-%m-%d")
date_res=date.strftime(date_res, "%Y-%m-%d")
duree_res=int(input("duree :"))
mtrcl=input("matricule :")

id_cl=int(input("id_client :"))
y=r.Reserver(date_res,duree_res,mtrcl,id_cl)
print(y)
print("")

print("---Afficher les reservations------------------------")
print("")
id_cl=int(input("id_cl:"))
a=r.Afficher(id_cl)
print(a)
print("")

print("---Confirmer reservation-----------------------------")
print("")
code_res=int(input("code_res :"))
e=r.Confirmation(code_res)
print(e)
print("")

print("---Annuler reservation ------------------------------")
code_res=int(input("code_res :"))
supp=r.Annuler(code_res)
print(supp)
