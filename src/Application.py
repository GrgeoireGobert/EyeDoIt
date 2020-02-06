##
#  @mainpage EyeDoIt - Utilisation
#
#  @section matos_sec Matériel nécessaire
#
#  Matériel 1 \n
#  Matériel 2 \n
#  Matériel 3 \n
#
#  @section install_sec Installation
#
#  Informations d'installation
#
#  @subsection step1 Etape 1 : Allumer l'ordinateur
#
#  etc...




##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief Application : module de définition de l'application
#
#  Le module Application contient les classes : \n
#  -> Application : chef d'orchestre du projet complet

from Maths import *
from Room import *
from Human import *

##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief Application : classe chef.
#
#  La classe Application contient l'ensemble des variables
#  et orchestre les échanges entre celles-ci.
class Application:
   
    ##
    #
    #  @param self Le pointeur vers l'objet.
    #
    #  @brief Constructeur de classe
    def __init__(self):
        self.rooms={}
        self.humans={}
   
    ##
    #
    #  @param self Le pointeur vers l'objet Application
    #  @param human_name string : nom du Human
    #  @param room_id int : identifiant de la Room au sein de l'Application
    #  @param eye_tracker_port int : port de l'eye tracker du Human
    #
    #  @brief Ajout d'un "Human" au dict "humans"
    #  
    #  Création d'un objet Human et ajout au dict "humans"
    def addHuman(self,human_name,room_id,eye_tracker_port):
        # Verification des types
        assert(type(human_name)==str)
        assert(type(room_id)==int)
        assert(type(eye_tracker_port)==int)
         # Verification Human non deja existant
        assert(human_name not in [human.name for human in self.humans.values()])
        # Recuperation de l'indice du Human
        human_id=0
        if len(self.humans)>0:
            human_id=max([human.id for human in self.humans.values()])+1
        # Création et ajout du Human au dict
        self.humans[human_name]=Human(human_id,human_name,room_id,eye_tracker_port)
   
    ##
    #
    #  @param self Le pointeur vers l'objet Application
    #  @param room_name string : nom de la Room
    #
    #  @brief Ajout d'un "Room" au dict "rooms"
    #  
    #  Création d'un objet Room et ajout au dict "rooms"
    def addRoom(self,room_name):
        # Verification des types
        assert(type(room_name)==str)
         # Verification Room non deja existante
        assert(room_name not in [room.name for room in self.rooms.values()])
        # Recuperation de l'indice de la Room
        room_id=0
        if len(self.rooms)>0:
            room_id=max([room.id for room in self.rooms.values()])+1
        # Création et ajout de la Room au dict
        self.rooms[room_name]=Room(room_id,room_name)
   
    ##
    #
    #  @param self Le pointeur vers l'objet Application
    #  @param human_name string : nom du Human
    #
    #  @brief Retrait d'un "Human" du dict "humans"
    def removeHuman(self,human_name):
        # Verifications
        assert(type(human_name)==str)
        assert(human_name in [human.name for human in self.humans.values()])
        # Suppression du Human du dict
        del self.humans[human_name]
   
    ##
    #
    #  @param self Le pointeur vers l'objet Application
    #  @param room_name string : nom de la Room
    #
    #  @brief Retrait d'un "Room" du dict "rooms"
    def removeRoom(self,room_name):
        # Verifications
        assert(type(room_name)==str)
        assert(room_name in [room.name for room in self.rooms.values()])
        # Suppression du Human du dict
        del self.rooms[room_name]
   
    ##
    #
    #  @param self Le pointeur vers l'objet Application
    #
    #  @brief Affichage de la configuration actuelle de l'Application
    #
    #  Affichage de la liste des Human et de la liste des Room
    def showConfiguration(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet Application
    #
    #  @brief Chargement d'une configuration enregistrée
    #
    #  Lit un fichier décrivant une configuration de l'application
    #  puis modifie les paramètres de l'objet pour le configurer.
    def loadConfiguration(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet Application
    #
    #  @brief Sauvegarde de la configuration actuelle
    #
    #  Sérialise l'objet Application et l'écrit dans un fichier texte
    def saveConfiguration(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet Application.
    #
    #  @brief Lancement de l'application
    #
    #  Lance une boucle infinie de traitement
    def run(self):
        pass
    
    
    

if __name__ == "__main__":
    # instanciation de l'application :
    App=Application()
    
    ####### PIECE #######
    # Création d'une piece
    App.addRoom("Bedroom")
    Bedroom=App.rooms["Bedroom"]
    # Paramétristaion des tags de la piece
    Bedroom.addTag("Tag36h11",0,"Tag36h11_0",0.216,Vector(2.21,0.87,0.76),Matrix([[1,0,0],
                                                                                [0,1,0],
                                                                                [0,0,1]]))
    Bedroom.addTag("Tag36h11",1,"Tag36h11_1",0.216,Vector(2.76,0.87,0.62),Matrix([[1,0,0],
                                                                                [0,1,0],
                                                                                [0,0,1]]))
    Bedroom.addTag("Tag36h11",2,"Tag36h11_2",0.216,Vector(1.341,0.29,1.82),Matrix([[1,0,0],
                                                                                 [0,1,0],
                                                                                 [0,0,1]]))
    # Création d'un objet connecte dans la piece
    Bedroom.addConnectedObject("TV")
    TV=Bedroom.connected_objects["TV"]
    # Ajout de BS à l'objet
    TV.addBoundingSphere("Left_Side",Vector(2.03,5.07,1.03),0.75)
    TV.addBoundingSphere("Right_Side",Vector(2.03,6.73,1.03),0.75)
    TV_Left_BS=TV.bounding_spheres["Left_Side"]
    TV_Right_BS=TV.bounding_spheres["Right_Side"]
    # Ajout d'actions à chaque BS
    TV_Left_BS.addAction("Turn_on","Click","TV-01-001")
    TV_Right_BS.addAction("Turn_off","Click","TV-01-002")
    
    ####### HUMAIN #######
    # Creation d'un Human
    App.addHuman("John",Bedroom.id,5252)
    John=App.humans["John"]
    # Ajout de Triggers
    John.addTrigger("Click")
    John.addTrigger("Voice")
    John.addTrigger("Gesture")
    
    ####### LANCEMENT DE L'APLLICATION #######
    App.run()
    