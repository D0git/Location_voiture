
    # Importer le module SQLite :
import sqlite3

    # Se connecter à la base données :
cnx=sqlite3.connect('Location_voiture.db')

    # Fermeture de la connexion à la base de données :
#cnx.close()

cursor=cnx.cursor()

    # Creation d'une liste vide des agences :"""




class Voiture():
   
    # Constructeur d'initiation :
    
    def __init__(self,m=None,i=None,mar=None,mod=None,tr=None,type=None,np=None,plj=None,dispo=None):
        self.matricule=m 
        self.image=i
        self.marque=mar
        self.modele=mod
        self.transmission=tr
        self.type_car=type
        self.nbr_plc=np
        self.prix_loc_j=plj
        self.disponibilite=dispo
  
    # Creation d'une' liste vide des voitures :
    def Voiture(self):
        self.Voiture=[]

    # Affichage de la liste des voitures :-------------------------------------------------------------------------------------
    def Afficher_v_dispo(self):
        self.Voiture=[]
        cursor.execute("select * from Voiture")
        result=cursor.fetchall()
        return result
    
# Fonctions de recherche :

    # Recherche par marque :
    def Rechercher_par_marque(self):
        cursor.execute("select * from Voiture group by marque")
        result=cursor.fetchall()
        return result
  
    # Recherche par type de carburant :
    def Rechercher_par_tcarb(self):
        cursor.execute("select * from Voiture group by type_car")
        result=cursor.fetchall()
        return result
    
    # Rechercher par transmission :
    def Rechercher_par_trans(self):
        cursor.execute("select * from Voiture group by trans")
        result=cursor.fetchall()
        return result  
      
    # Recherche par nombre de places :
    def Rechercher_par_nbr_plc(self):
        cursor.execute("select * from Voiture group by nbr_plc")
        result=cursor.fetchall()
        return result     

    
        
    # Rechercher par prix de location par jours :
    def Rechercher_par_prix_loc_jrs(self):
        cursor.execute("select * from Voiture group by prix_loc_j")
        result=cursor.fetchall()
        return result
    

    def Ajouter(self,matricule,image,nbr_plc,prix_loc_j,transmission,modele,marque,type_car):
        
        
        sql="insert into Voiture (matricule,image,nbr_plc,prix_loc_j,trans,modele,marque,type_car,disponibilite) values(?,?,?,?,?,?,?,?,FALSE)"
        val=(matricule,image,nbr_plc,prix_loc_j,transmission,modele,marque,type_car)
        cursor.execute(sql,val)
        cnx.commit()
        return True
""""
    # Fonction d'ajout d'une voiture :
    def Ajouter(self,matricule,image,nbr_plc,prix_loc_j,transmission,modele,marque,type_car):
        sql="insert into Voiture (matricule,image,nbr_plc,prix_loc_j,trans,modele,marque,type_car,disponibilite) values(%s,%s,%d,%f,%s,%s,%s,%s,FALSE)"
        val=(matricule,image,nbr_plc,prix_loc_j,transmission,modele,marque,type_car)
        cursor.execute(sql,val)
        cnx.commit()
        return True
"""
   










"""
    
    # Fonction de modification d'une voiture :
    def Modifier(self):
        
    
 # Fonction de suppression d'une voiture :
    def Supprimer(self):
        """
    



v=Voiture()
print("---Affichage des voiture disponibles-----------------------------------------------------------------------------")
print("")
y=v.Afficher_v_dispo()
print(y)
print("")
print("---Recherche_par_marque-----------------------------------------------------------------------------------------")
print("")
mrq=v.Rechercher_par_marque()
print(mrq)
print("")
print("---Rechercher_par_tcarb-----------------------------------------------------------------------------------------")
print("")
tc=v.Rechercher_par_tcarb()
print(tc)
print("")
print("---Rechercher_par_trans-----------------------------------------------------------------------------------------")
print("")
tr=v.Rechercher_par_trans()
print(tr)
print("")
print("---Rechercher_par_nbr_plc-----------------------------------------------------------------------------------------")
print("")
nbr=v.Rechercher_par_nbr_plc()
print(nbr)
print("")
print("---Rechercher_par_prix_loc_jrs-----------------------------------------------------------------------------------------")
print("")
prix=v.Rechercher_par_prix_loc_jrs()
print(nbr)


print("")
print("---Ajouter voiture-----------------------------------------------")
matricule=input("matricule: ")
image=input("image: ")
nbr_plc=int(input("nbr_plc: "))
prix_loc_j=float(input("prix_loc_j: "))
transmission=input("transmission: ")
modele=input("modele: ")
marque=input("marque: ")
type_car=input("type_car: ")

ajout=v.Ajouter(matricule,image,nbr_plc,prix_loc_j,transmission,modele,marque,type_car)
print(ajout)
"""
print("")
print("---Modifier voiture-----------------------------------------------")
supp=v.Supprimer()
print(supp)"""
print("---Affichage des voiture disponibles-----------------------------------------------------------------------------")
print("")
y=v.Afficher_v_dispo()
print(y)
