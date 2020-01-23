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
    #  @brief Ajout d'un "Human" à la liste "humans"
    #  
    #  Création d'un objet Human et ajout à la liste "humans"
    def addHuman(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet Application
    #
    #  @brief Ajout d'un "Room" à la liste "rooms"
    #  
    #  Création d'un objet Room et ajout à la liste "rooms"
    def addRoom(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet Application
    #
    #  @brief Retrait d'un "Human" de la liste "humans"
    def removeHuman(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet Application
    #
    #  @brief Retrait d'un "Room" de la liste "rooms"
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