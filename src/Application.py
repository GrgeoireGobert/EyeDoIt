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
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet Application
    #
    #  @brief Ajout d'un "Human" au dict "humans"
    #  
    #  Création d'un objet Human et ajout au dict "humans"
    def addHuman(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet Application
    #
    #  @brief Ajout d'un "Room" au dict "rooms"
    #  
    #  Création d'un objet Room et ajout au dict "rooms"
    def addRoom(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet Application
    #
    #  @brief Retrait d'un "Human" du dict "humans"
    def removeHuman(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet Application
    #
    #  @brief Retrait d'un "Room" du dict "rooms"
    def removeRoom(self):
        pass
   
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