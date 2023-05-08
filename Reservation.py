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
    

    # Affichage des reservation :
    def Afficher(id_cl):
        cursor.execute("select * from Reservation r join Client c on r.id_cl=c.id_cl join Voiture v on v.matricule=r.matricule where c.id_cl=?",(id_cl,))
        res=cursor.fetchall()
        res=tuple(res[-1])
        return res   
   

    # Confirmer reservation :      
    def Confirmation(code_res,mtrcl):
        cursor.execute("update Reservation set etat_res=TRUE where code_res=?;",(code_res,))
        cnx.commit()
        cursor.execute("update Voiture set disponibilite=FALSE where matricule=?",(mtrcl,))
        cnx.commit()
    
    # Annuler reservation :
    def Annuler(code_res):
        cursor.execute("delete from Reservation where code_res=?",(code_res,))
        cnx.commit()


    
    
    
    




