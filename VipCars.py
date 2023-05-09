from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.lang import Builder
from kivy.properties import StringProperty,ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.pickers.datepicker.datepicker import MDDatePicker,datetime
from kivy.core.window import Window
import os
from PIL import Image as img
from plyer import filechooser
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivymd.uix.snackbar import Snackbar
from kivy.clock import Clock
import time
from voiture import Voiture as vt
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.list import IconLeftWidget
from agence import Agence
from Reservation import Reservation
from client import Client
import re
import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError



class CardItem(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ContentNavigationDrawer(MDBoxLayout):
    pass

class Content(MDBoxLayout):
    '''Custom content.'''



class InfoCar(MDCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.elevation = 3

class Dialogue(BoxLayout):
    
    def clear(self,widget):
        widget.text=''
    
    def get_mtrcl(self):
        mtrcl=self.matricule
        return mtrcl
        
    
class DialogueDelete(BoxLayout):
    
    pass
class DialogueERRnotExist(BoxLayout):
    
    pass
class DialogueERRExist(BoxLayout):
    
    pass
class AdmineClient(BoxLayout):
    
    pass


class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()

class ClickableTextFieldRound2(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()



class VipCars(MDApp):
    
    dialog = None
    test=None
    add_modif=None
    id_client=None
    admine=None
    detete=None
    exist=None
    not_exist=None
    do=None
    selected_car=None
    resevation=None
    mtrcl_test=None
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.root = Builder.load_file('app.kv')
        self.select_carburant=vt.Afficher_v_carburant()
        self.select_marque=vt.Afficher_v_marque()
        self.select_transmission=vt.Afficher_v_transmission()
        self.select_place=vt.Afficher_v_place()
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": i[0],
                "height": dp(56),
                "on_release": lambda x="1 "+i[0]: self.menu_callback(x),
             } for i in self.select_marque
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )
        menu_items2 = [
            {
                "viewclass": "OneLineListItem",
                "text": i[0],
                "height": dp(56),
                "on_release": lambda x="2 "+i[0]: self.menu_callback(x),
             } for i in self.select_carburant
        ]
        self.menu2 = MDDropdownMenu(
            items=menu_items2,
            width_mult=4,
        )
        menu_items3 = [
            {
                "viewclass": "OneLineListItem",
                "text": i[0],
                "height": dp(56),
                "on_release": lambda x="3 "+i[0]: self.menu_callback(x),
             } for i in self.select_transmission
        ]
        self.menu3 = MDDropdownMenu(
            items=menu_items3,
            width_mult=4,
        )
        menu_items4 = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{i[0]}",
                "height": dp(56),
                "on_release": lambda x=f"4 {i[0]}": self.menu_callback(x),
             } for i in self.select_place
        ]
        self.menu4 = MDDropdownMenu(
            items=menu_items4,
            width_mult=4,
        )
        menu_items5 = [
            {
                "viewclass": "OneLineListItem",
                "text": "max = 5000",
                "height": dp(56),
                "on_release": lambda x="max": self.menu_callback(x),
             } ,
            {
                "viewclass": "OneLineListItem",
                "text": "min > 5000",
                "height": dp(56),
                "on_release": lambda x="min": self.menu_callback(x),
             }
        ]
        self.menu5 = MDDropdownMenu(
            items=menu_items5,
            width_mult=3,
        )
        
############################################ RECHERCHER VOITURE ##########################################
    def callback(self, button):
        self.menu.caller = button
        self.menu.open()
    
    def callback2(self, button):
        self.menu2.caller = button
        self.menu2.open()
    def callback3(self, button):
        self.menu3.caller = button
        self.menu3.open()
    def callback4(self, button):
        self.menu4.caller = button
        self.menu4.open()
    def callback5(self, button):
        self.menu5.caller = button
        self.menu5.open()
    
    def menu_callback(self, text_item):
        self.menu.dismiss()
        self.menu2.dismiss()
        self.menu3.dismiss()
        self.menu4.dismiss()
        self.menu5.dismiss()
        index=text_item.split()
        if index[0]=="1":
            self.v_recherchee=vt.Rechercher_par_marque(index[1])
        if index[0]=="2":
            self.v_recherchee=vt.Rechercher_par_tcarb(index[1])
        if index[0]=="3":
            self.v_recherchee=vt.Rechercher_par_trans(index[1])
        if index[0]=="4":
            self.v_recherchee=vt.Rechercher_par_nbr_plc(index[1])
        if index[0]=="min":
            self.v_recherchee=vt.Rechercher_min_prix_loc_jrs()
        if index[0]=="max":
            self.v_recherchee=vt.Rechercher_max_prix_loc_jrs()
        self.root.ids.filter_cars.clear_widgets()
        for i in self.v_recherchee:
            
            
            self.root.ids.filter_cars.add_widget(CardItem(
                MDCard(

                    
                        Image(
                            source= i[1],
                            #id="image_car",
                            size_hint_x=None,
                            width= 340,
                                ),
                    
                    MDBoxLayout(
                        
                        
                        MDLabel(
                            text=i[6],
                            bold= True,
                            font_style="H5",
                            adaptive_height= True,
                            text_color=(105,228,255,1),
                            ),
                        MDLabel(
                            text=i[5],
                            bold= True,
                            font_style= "H5",
                            adaptive_height= True,
                            color=(105,228,255,1),
                            padding=(0,0,0,8) ,),
                           
                        MDLabel(
                            text=i[7],
                            font_size= "17",
                            adaptive_height= True,),
                            
                        MDLabel(
                            text=str(i[2])+" places",
                            font_size= "17",
                            adaptive_height= True,
                            padding=(0,0,0,8) ,),
                            
                            
                        
                        MDLabel(
                            text=str(i[3])+" dhs",
                            font_style= "H5",
                            color= "#FFFFFF",
                            bold=True,
                            adaptive_height= True,
                            padding=(0,0,0,20) ,),
                        
                        id= "card",
                        orientation= 'vertical',
                        padding=(50,0,0,0) ,
                    ),
                    id=i[0],
                    size_hint_x=1,
                    elevation=2,
                    shadow_offset=(0, -1),
                    shadow_softness= 4,
                    shadow_color= "#69e4ff",
                    ripple_behavior= True,
                    on_release=lambda x=id:self.go_to_info(text_item=x,y="filtre"),
                
                ),
                size_hint_y= None,
                height= (208),
                
            )
            
            )
##########################################################################################################        


    def navigation_draw(self):
        pass
    display_car=None    
    def on_start(self):
        self.v=vt.Afficher_v_dispo()
        n=0
        for i in self.v:
            
            
            self.root.ids.carditems.add_widget(CardItem(
                MDCard(

                    
                        Image(
                            source= i[1],
                            #id="image_car",
                            size_hint_x=None,
                            width= 340,
                                ),
                    
                    MDBoxLayout(
                        
                        
                        MDLabel(
                            text=i[6],
                            bold= True,
                            font_style="H5",
                            adaptive_height= True,
                            text_color=(105,228,255,1),
                            ),
                        MDLabel(
                            text=i[5],
                            bold= True,
                            font_style= "H5",
                            adaptive_height= True,
                            color=(105,228,255,1),
                            padding=(0,0,0,8) ,),
                           
                        MDLabel(
                            text=i[7],
                            font_size= "17",
                            adaptive_height= True,),
                            
                        MDLabel(
                            text=str(i[2])+" places",
                            font_size= "17",
                            adaptive_height= True,
                            padding=(0,0,0,8) ,),
                            
                            
                        
                        MDLabel(
                            text=str(i[3])+" dhs",
                            font_style= "H5",
                            color= "#FFFFFF",
                            bold=True,
                            adaptive_height= True,
                            padding=(0,0,0,20) ,),
                        
                        id= "card",
                        orientation= 'vertical',
                        padding=(50,0,0,0) ,
                    ),
                    id=i[0],
                    size_hint_x=1,
                    elevation=2,
                    shadow_offset=(0, -1),
                    shadow_softness= 4,
                    shadow_color= "#69e4ff",
                    ripple_behavior= True,
                    on_release=lambda x=id:self.go_to_info(text_item=x,y="main"),
                
                ),
                size_hint_y= None,
                height= (208),
                
            )
            
            )
            #self.root.ids.all_cars.ids.image_car=i[1]
            
        
        self.agence=Agence.Affichage()   
          
        for i in self.agence:
            #self.theme_cls.theme_style = "Dark"
            self.root.ids.box.add_widget(
                MDExpansionPanel(
                    
                    icon="home-city",
                    content=Content(
                            
                            OneLineIconListItem(
                                IconLeftWidget(
                                    icon= 'phone'),
                                text= i[3],
                                divider= None,
                                 ),
                                    
                            OneLineIconListItem(
                                IconLeftWidget(
                                    icon= 'map-marker-radius-outline',),
                                text= i[2],
                                divider= None,
                                ),
                            size_hint_y= None,
                            height= 140,
                            orientation= 'vertical',
                            md_bg_color= "#0F056B",
                            specific_text_color= "#FFFFFF",

                    ),
                    panel_cls=MDExpansionPanelThreeLine(
                        
                        text=i[1],
                        
                        
                        
                        
                    )
                )
            )  
    scrn=None
    def go_to_info(self,text_item,y):
        
        self.selected_car=vt.one_car(text_item.id)
        self.root.ids.car_select0.source=self.selected_car[1]
        self.root.ids.car_select1.source=self.selected_car[1]
        self.root.ids.car_select2.source=self.selected_car[1]
        self.root.ids.car_select3.source=self.selected_car[1]
        self.root.ids.car_select4.source=self.selected_car[1]
        self.root.ids.car_select5.source=self.selected_car[1]
        self.root.ids.car_select6.source=self.selected_car[1]
        self.root.ids.maq.text=self.selected_car[6]
        self.root.ids.mod.text=self.selected_car[5]
        self.root.ids.px.text=str(self.selected_car[3])+" dhs"
        self.root.ids.carb.text=self.selected_car[7]
        self.root.ids.trans.text=self.selected_car[4]
        self.root.ids.place.text=str(self.selected_car[2])
        
        self.scrn=y
        self.root.ids.manager.current = 'info_car'
    def go_back(self):
        if self.scrn=="main":
            self.root.ids.manager.current = 'menu'
        elif self.scrn=="filtre":
            self.root.ids.manager.current = 'cars'
    
    def go_to_res(self):
        self.root.ids.img_res.source=self.selected_car[1]
        self.root.ids.res_mod_marq.text=self.selected_car[6]+"\n"+self.selected_car[5]
        self.root.ids.manager.current = 'reservation'
    
    
    

######################################## LOGIN & SIGN UP ####################################################        
    
    def log_in(self):
        login=self.root.ids.login_user.text
        password=self.root.ids.passwrd.ids.text_field.text
        if login=="":
            self.root.ids.login_user.error=True
        
        if password=="":
            self.root.ids.passwrd.ids.text_field.error=True
        
        if login!="" and password!="":
            if Client.Connexion(login,password)==1:
                self.id_client=Client.get_id(login,password)
                self.show_admine_client()
                self.root.ids.login_user.text = ""
                self.root.ids.passwrd.ids.text_field.text = ""
                self.root.ids.login_user.error=False
                self.root.ids.passwrd.ids.text_field.error=False
            elif Client.Connexion(login,password)==0:
                self.id_client=Client.get_id(login,password)
                self.root.ids.login_user.text = ""
                self.root.ids.passwrd.ids.text_field.text = ""
                self.root.ids.login_user.error=False
                self.root.ids.passwrd.ids.text_field.error=False
                self.root.ids.manager.current = "menu"
            elif Client.Connexion(login,password)==-1:
                self.root.ids.login_user.error=True
                self.root.ids.passwrd.ids.text_field.error=True    
    def log_in_to_sign(self):
        self.root.ids.login_user.text = ""
        self.root.ids.passwrd.ids.text_field.text = ""
        self.root.ids.manager.current='signup'
    def sign_up(self):
        nom=self.root.ids.fn.text
        prenom=self.root.ids.ln.text
        phone=self.root.ids.phone.text
        mail=self.root.ids.email.text
        login=self.root.ids.log.text
        pwd=self.root.ids.first_pswrd.ids.text_field.text
        conf_pwd=self.root.ids.confirm_pswrd.ids.text_field.text
        if nom=="":
            self.root.ids.fn.error=True
        if prenom=="":
            self.root.ids.ln.error=True
        if phone=="":
            self.root.ids.phone.error=True
        if mail=="":
            self.root.ids.email.error=True
        if login=="":
            self.root.ids.log.error=True
        if pwd=="":
            self.root.ids.first_pswrd.error=True
        if conf_pwd=="":
            self.root.ids.confirm_pswrd.error=True
        if nom!="" and prenom!="" and phone!="" and mail!="" and pwd!="" and conf_pwd!="":
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,15}$"
            match_re = re.compile(reg)
            res = re.search(match_re, pwd)
            if pwd==conf_pwd:
                print(pwd)
                if res:
                    print(login)
                    Client.Inscription(nom,prenom,phone,mail,login,pwd)
                    self.root.ids.manager.current='login'
                    self.root.ids.fn.text = ""
                    self.root.ids.ln.text = ""
                    self.root.ids.phone.text = ""
                    self.root.ids.email.text = ""
                    self.root.ids.log.text = ""
                    self.root.ids.first_pswrd.ids.text_field.text = ""
                    self.root.ids.confirm_pswrd.ids.text_field.text = ""
                else: self.root.ids.first_pswrd.error=True
            else: 
                self.root.ids.first_pswrd.error=True
                self.root.ids.confirm_pswrd.error=True

    def cancel_signup(self):
        self.root.ids.manager.current='login'
        self.root.ids.fn.text = ""
        self.root.ids.ln.text = ""
        self.root.ids.phone.text = ""
        self.root.ids.email.text = ""
        self.root.ids.log.text = ""
        self.root.ids.first_pswrd.ids.text_field.text = ""
        self.root.ids.confirm_pswrd.ids.text_field.text = ""            
#############################################################################################################        
    def send_email(self,subject, body, recipients):
        SCOPES = [
        "https://www.googleapis.com/auth/gmail.send"
        ]
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        service = build('gmail', 'v1', credentials=creds)
        message = MIMEText(body)
        message['to'] = recipients
        message['subject'] = subject
        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

        try:
            message = (service.users().messages().send(userId="me", body=create_message).execute())
            print(F'sent message to {message} Message Id: {message["id"]}')
        except HTTPError as error:
            print(F'An error occurred: {error}')
            message = None    
        
        
        
    
    def annuler_res2(self):
        self.root.ids.manager.current="menu"
    
    def contacter(self):
        nom=Client.get_Nom(self.id_client)
        prenom=Client.get_Prenom(self.id_client)
        subject = "M. "+prenom+" "+nom+" :Email From VipCars Client"
        body = self.root.ids.contactez_nous.text
       
        recipients = "fatimazahra.zaha1504@gmail.com"
        

        self.send_email(subject, body, recipients)
        
        
        
        self.root.ids.contactez_nous.text = "" 
        self.root.ids.manager.current = "menu" 
    
    date_res=None
    duree_res=None
    def on_save(self, instance, value, date_range):
        i=0 
        self.date_res=value
        for d in date_range:
            i=i+1
            f=d
        self.duree_res=i
        self.root.ids.date_debut.text=value.strftime('%d-%m-%Y')
        self.root.ids.date_fin.text=f.strftime('%d-%m-%Y')
        self.root.ids.duree.text=str(i)+" jours"
        
        
    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
    def show_date_picker(self):
        date_dialog = MDDatePicker(
            min_date=datetime.date.today(),
            mode="range",
            min_year=datetime.date.today().year, max_year=datetime.date.today().year+5,
            helper_text="",
            selector_color="#69e4ff",
            primary_color="#1A237E",
            text_toolbar_color="#ffffff",
            text_button_color="#69e4ff",
            
           
        )
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def reserver_btn(self):
        t_debut=self.root.ids.date_debut.text
        t_fin=self.root.ids.date_fin.text
        t_duree=self.root.ids.duree.text
        if t_debut!="" and t_fin!="" and t_duree!="":
            Reservation.Reserver(self.date_res,self.duree_res,self.selected_car[0],self.id_client)
            self.resevation=Reservation.Afficher(self.id_client)
            self.root.ids.name_cl.text="Mr/Mme "+self.resevation[8]+" "+self.resevation[9]
            self.root.ids.ft_marq.text="Marque:  "+self.resevation[20]
            self.root.ids.ft_mod.text="Modèle:  "+self.resevation[19]
            self.root.ids.ft_px.text="Prix de location:  "+str(self.resevation[17])+" dhs"
            self.root.ids.ft_date_debut.text="Date de reservation:  "+t_debut
            self.root.ids.ft_duree.text="Duree:  "+str(self.resevation[3])+" jours"
            self.root.ids.ft_montant.text="Montant à payer:  "+str(self.resevation[1])+" dhs"
            self.root.ids.ft_date_fin.text="Veuillez déposer la voiture le  "+t_fin
            self.root.ids.date_debut.text=""
            self.root.ids.date_fin.text=""
            self.root.ids.duree.text=""
            self.root.ids.manager.current="facture"
            #self.change_theme(fltr=1)
    def annuler_res(self):
        Reservation.Annuler(self.resevation[0])
        self.root.ids.manager.current="menu"



    def open_file(self):
        filechooser.open_file(on_selection=self.selected)
    def selected(self, selection):
        file=selection[0]
        file=file.split('\\')
        path=file[-1].split('.')
        if self.add_modif==0:
            
            if path[-1]=='png' or path[-1]=='jpg':
                self.root.ids.img_add.text = file[-1]
            elif path[-1]!='png' and path[-1]!='jpg':
                self.root.ids.img_add.text = "file selected is NOT IMAGE!!!(*.png/*.jpg)"
        
        elif self.add_modif==1:
            if path[-1]=='png' or path[-1]=='jpg':
                self.root.ids.img_modif.text = file[-1]
            else:
                self.root.ids.img_modif.text = "file selected is NOT IMAGE!!!(*.png/*.jpg)"
    def update(self):
        return time.asctime()
    def widget_save(self, inst):
        
        date=self.update()
        d=date.split(":")
        date=d[0]+"h"+d[1]+"m"+d[2]
        inst.export_to_png(f"reservation({date}).jpg")
        file=f"reservation({date}).jpg"
        image=img.open(file)
        image_converted=image.convert('RGB')
        image_converted.save('{0}.pdf'.format(file.split('.')[-2]))
        os.remove(file)
        Reservation.Confirmation(self.resevation[0],self.selected_car[0])
        self.root.ids.manager.current="menu"
        #self.change_theme(fltr=0)
        
################################## ADMINE ##############################################################################        
    def add_car(self):
        
        test=0
        matricule=self.root.ids.add_matricule.text
        marque=self.root.ids.add_marque.text
        model=self.root.ids.add_modele.text
        trans=self.root.ids.add_trans.text
        img1=self.root.ids.img_add.text
        carb=self.root.ids.add_carb.text
        place=self.root.ids.add_place.text
        prix=self.root.ids.add_prix.text
        cd_ag=self.root.ids.add_agence.text
        if matricule=="":
            self.root.ids.add_matricule.error=True 
            test=0
        else: test=1  
        if model=="" :
            self.root.ids.add_modele.error=True 
            test=0
        else: test=1
        if marque=="":
            self.root.ids.add_marque.error=True
            test=0
        else: test=1
        if trans=="" :
            self.root.ids.add_trans.error=True
            test=0
        else: test=1
        if img1=="" or img1=="file selected is NOT IMAGE!!!(*.png/*.jpg)":
            self.root.ids.img_add.error=True
            test=0
        else: test=1
        if carb=="":
            self.root.ids.add_carb.error=True
            test=0
        else: test=1
        if place=="":
            self.root.ids.add_place.error=True
            test=0
        else: test=1
        if prix=="":
            self.root.ids.add_prix.error=True
            test=0
        else: test=1
        if cd_ag=="":
            self.root.ids.add_agence.error=True
            test=0
        else: test=1
        try:
            place=int(place)
        except:
            self.root.ids.add_place.error=True
            test=0    
        try:
            prix=int(prix)
        except:
            self.root.ids.add_prix.error=True
            test=0    
        try:
            cd_ag=int(cd_ag)
        except:
            self.root.ids.add_agence.error=True
            test=0

        if test==1:
            self.root.ids.add_modele.error=False
            self.root.ids.add_matricule.error=False 
            self.root.ids.add_marque.error=False
            self.root.ids.add_trans.error=False
            self.root.ids.img_add.error=False
            self.root.ids.add_carb.error=False
            self.root.ids.add_place.error=False
            self.root.ids.add_prix.error=False
            self.root.ids.add_agence.error=False
            img1="vip_cars\\"+img1
            verifie_ag=vt.Ajouter(matricule,img1,int(place),float(prix),trans,model,marque,carb,cd_ag)
            if verifie_ag==True:
                self.root.ids.add_modele.text=''
                self.root.ids.add_matricule.text='' 
                self.root.ids.add_marque.text=''
                self.root.ids.add_trans.text=''
                self.root.ids.img_add.text=''
                self.root.ids.add_carb.text=''
                self.root.ids.add_place.text=''
                self.root.ids.add_prix.text=''
                self.root.ids.add_agence.text=''
                self.root.ids.manager.current = "admin"
            else: self.root.ids.add_agence.error=True
                    
    def modif_car(self):
        
        test=0
        img=self.root.ids.img_modif.text
        prix=self.root.ids.modif_prix.text
        dispo=self.root.ids.modif_dispo.text
        
        if img=="file selected is NOT IMAGE!!!(*.png/*.jpg)":
            self.root.ids.img_add.error=True
            test=0
        elif img!="":
            test=1
            vt.Modifier_image(img,self.mtrcl_test)
        else: test=1
        
        
        if prix!="":
            try:
                prix=int(prix)
                vt.Modifier_Prix(prix,self.mtrcl_test)
                test=1
            except:
                test=0
                self.root.ids.modif_prix.error=True
        else: test=1    
        
        if dispo.upper()=="TRUE" or dispo.upper()=="FALSE":
            vt.Modifier_Dispo(dispo.upper(),self.mtrcl_test)
            test=1
        elif dispo!="" and dispo.upper()!="TRUE" and dispo.upper()!="FALSE":
            self.root.ids.add_agence.error=True
        else: test=1

        if test==1:
            self.root.ids.img_modif.text=""
            self.root.ids.modif_prix.text=""
            self.root.ids.modif_dispo.text=""
            self.root.ids.manager.current = "admin"
                  
    def delete_car(self,obj):
        vt.Supprimer(self.mtrcl_test)
        self.detete.dismiss()

    def show_confirmation_dialog(self):
        
        if not self.dialog:
            self.dialog = MDDialog(
                title="Matricule:",
                type="custom",
                content_cls=Dialogue(),
                
            )
        self.dialog.open() 

    def show_confirmation_delete(self):
        
        if not self.detete:
            self.detete = MDDialog(
                title="Delete Car:",
                type="custom",
                content_cls=DialogueDelete(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialogDelete,
                            
                    ),
                    MDFlatButton(
                        text="Confirm",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release= self.delete_car,
                    ),
                ],
            )
        self.detete.open()
    def show_err_existe(self):
        
        if not self.exist:
            self.exist = MDDialog(
                title="ERROR:",
                type="custom",
                content_cls=DialogueERRExist(),
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialogExist,
                            
                    ),
                    
                ],
            )
        self.exist.open()
    def show_err_not_existe(self):
        
        if not self.not_exist:
            self.not_exist = MDDialog(
                title="ERROR:",
                type="custom",
                content_cls=DialogueERRnotExist(),
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialogNotExist,
                            
                    )
                ],
            )
        self.not_exist.open()
    def close_dialogExist(self,obj):
        self.exist.dismiss()
    def close_dialogNotExist(self,obj):
        self.not_exist.dismiss()
    def show_admine_client(self):
        
        if not self.admine:
            self.admine = MDDialog(
                title="Welcome ",
                type="custom",
                content_cls=AdmineClient(),
                buttons=[
                    MDFlatButton(
                        text="Admin",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.go_to_Admin,
                            
                    ),
                    MDFlatButton(
                        text="Client",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release= self.go_to_Client,
                    ),
                ],
            )
        self.admine.open()
    def go_to_Admin(self,obj):
        self.admine.dismiss()
        self.root.ids.manager.current='admin'
    def go_to_Client(self,obj):
        self.admine.dismiss()
        self.root.ids.manager.current='menu'
    
    def go_to_sreen(self):
        self.dialog.dismiss()
        print(self.mtrcl_test)
        on_matricule=vt.Test_matricule(self.mtrcl_test)
        
        if self.test==1:
            if on_matricule==False:
                self.root.ids.manager.current='add'
            else: self.show_err_existe() 
        elif self.test==2:
            if on_matricule==True:
                self.root.ids.manager.current='modify'
            else:self.show_err_not_existe() 
        elif self.test==3:
            if on_matricule==True:
                self.show_confirmation_delete()
            else: self.show_err_not_existe() 
    
    
    def close_dialog(self,obj):
        self.dialog.dismiss()
    def close_dialogDelete(self,obj):
        self.detete.dismiss()
    ############################################################################
            
            
            







if __name__ == "__main__":    
    VipCars().run()
