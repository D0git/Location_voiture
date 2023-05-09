
    # Importer le module SQLite :
import sqlite3

    # Se connecter à la base données :
cnx=sqlite3.connect('Location_voiture.db')

    # Fermeture de la connexion à la base de données :
#cnx.close()

cursor=cnx.cursor()





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
    def Afficher_v_dispo():
        #self.Voiture=[]
        cursor.execute("SELECT * FROM Voiture where disponibilite=TRUE")
        result=cursor.fetchall()
        return result
    def Afficher_v_marque():
        #self.Voiture=[]
        cursor.execute("SELECT DISTINCT marque FROM Voiture where disponibilite=TRUE")
        result=cursor.fetchall()
        return result
    
    def Afficher_v_carburant():
        #self.Voiture=[]
        cursor.execute("SELECT DISTINCT type_car FROM Voiture where disponibilite=TRUE")
        result=cursor.fetchall()
        return result
    def Afficher_v_transmission():
        #self.Voiture=[]
        cursor.execute("SELECT DISTINCT transmission FROM Voiture where disponibilite=TRUE")
        result=cursor.fetchall()
        return result
    def Afficher_v_place():
        #self.Voiture=[]
        cursor.execute("SELECT DISTINCT nbr_plc FROM Voiture where disponibilite=TRUE")
        result=cursor.fetchall()
        return result
    

# Fonctions de recherche :

    # Recherche par marque :
    def Rechercher_par_marque(marque):
        sql="select * from Voiture where marque=? and disponibilite=TRUE"
        val=(marque,)
        cursor.execute(sql,val)
        result=cursor.fetchall()
        return result

    # Recherche par type de carburant :
    def Rechercher_par_tcarb(type_car):
        sql="select * from Voiture where type_car=? and disponibilite=TRUE"
        val=(type_car,)
        cursor.execute(sql,val)
        result=cursor.fetchall()
        return result
    
    # Rechercher par transmission :
    def Rechercher_par_trans(transmission):
        sql="select * from Voiture where transmission=? and disponibilite=TRUE"
        val=(transmission,)
        cursor.execute(sql,val)
        result=cursor.fetchall()
        return result  
      
    # Recherche par nombre de places :
    def Rechercher_par_nbr_plc(nbr_plc):
        sql="select * from Voiture where nbr_plc=? and disponibilite=TRUE"
        val=(nbr_plc,)
        cursor.execute(sql,val)
        result=cursor.fetchall()
        return result     
        
    # Rechercher par prix de location par jours :
    def Rechercher_max_prix_loc_jrs():
        cursor.execute("select * from Voiture where prix_loc_j<=5000 and disponibilite=TRUE")
        result=cursor.fetchall()
        return result
    
    def Rechercher_min_prix_loc_jrs():
        cursor.execute("select * from Voiture where prix_loc_j>5000 and disponibilite=TRUE")
        result=cursor.fetchall()
        return result


    #Fonction d'ajout d'une voiture :
    def Ajouter(matricule,image,nbr_plc,prix_loc_j,transmission,modele,marque,type_car,code_ag):    
        cursor.execute("select * from Agence where code_ag=?", (code_ag,))
        ag=cursor.fetchone()
        if ag==None:
            return False
        else:
            sql="insert into Voiture (matricule,image,nbr_plc,prix_loc_j,transmission,modele,marque,type_car,code_ag,disponibilite) values(?,?,?,?,?,?,?,?,?,TRUE)"
            val=(matricule,image,nbr_plc,prix_loc_j,transmission,modele,marque,type_car,code_ag)
            cursor.execute(sql,val)
        cnx.commit()
        return True
            

         
    # Fonction de modification de l'image d'une voiture :
    def Modifier_image(image,matricule):
        sql="update Voiture set image=? where matricule=?"
        val=(image,matricule)
        cursor.execute(sql,val)
        cnx.commit()
    
    # Fonction de modification du prix de location d'une voiture :
    def Modifier_Prix(prix_loc_j,matricule):
        sql="update Voiture set prix_loc_j=? where matricule=?"
        val=(prix_loc_j,matricule)
        cursor.execute(sql,val)
        cnx.commit()
    
    # Fonction de modification de la disponibilite d'une voiture :
    def Modifier_Dispo(disponibilite,matricule):
        if disponibilite=="TRUE":
            sql="update Voiture set disponibilite=TRUE where matricule=?"
        if disponibilite=="FALSE":
            sql="update Voiture set disponibilite=FALSE where matricule=?"
        
        val=(matricule,)
        cursor.execute(sql,val)
        cnx.commit()

  
 # Fonction de suppression d'une voiture :
    def Supprimer(matricule):
        sql="delete from Voiture where matricule=?"
        val=(matricule,)
        cursor.execute(sql,val)
        cnx.commit()
    
# Fonction teste sur l'existance du matricule dans la base de donnees :
    def one_car(matricule):
        sql="select * from Voiture where matricule =? "
        val=(matricule,)
        cursor.execute(sql,val)
        result=cursor.fetchone()
        return result
    
    def Test_matricule(matricule):
        sql="select matricule from Voiture where matricule =? "
        val=(matricule,)
        cursor.execute(sql,val)
        result=cursor.fetchone()
        if result is None:
            return False
        else:
            return True
