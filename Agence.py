
class Agence:

    # Constructeur de classe agence :
    
    def __init__(self,c=None,v=None,t=None,a=None) :
        self.code_ag=c
        self.ville=v
        self.tel=t
        self.adresse=a


    # Creation d'une liste vide des agences :

    def __init__(self):
        self.Agence=[]





    # Affichage des informations :

    def Affichage(self):
        print("Code :" ,self.code,
               "\nVille :" ,self.ville,
               "\nTel :" ,self.tel,
               "\nAdresse :" ,self.adresse)

    # Getters :-----------------------------------------------------------------------------------------

    # Code :
    def get_Code(self):
        return self.code
    
    # Ville :
    def get_Ville(self):
        return self.ville
    
    # Tel :
    def get_Tel(self):
        return self.tel
    
    # Adresse :
    def get_Adresse(self):
        return self.adresse
    

    # Setters: ---------------------------------------------------------------------------------------

    # Code :
    def set_Code(self,c):
        self.code=c
    
    # Ville :
    def set_Ville(self,v):
        self.ville=v
    
    # Tel :
    def set_Tel(self,t):
        self.tel=t
    
    # Adresse :
    def set_Adresse(self,a):
        self.adresse=a

    

