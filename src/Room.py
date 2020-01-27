##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief Room : module de description statique de la salle
#
#  Le module Room contient les classes :
#  -> Room : représentation d'une pièce
#  -> Tag : représentation d'un AprilTag dans la pièce
#  -> ConnectedObject : représentation d'un objet connecté
#  -> BoundingSphere : représentation d'une sphère
#  -> Action : représentation d'une action à déclencher pour interaction

import Maths

##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief Room : classe de représentation d'une pièce
#
#  Une Room décrit une pièce physique : \n
#  -> Ensemble des AprilTags présents (voir classe Tag) \n
#  -> Ensemble des objets connectés présents (voir classe ConnectedObject)
class Room():
   
    ##
    #
    #  @param self Le pointeur vers l'objet Room
    #
    #  @brief Constructeur de classe
    def __init__(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet Room
    #
    #  @brief Ajout d'un "Tag" au dict "tags"
    #  
    #  Création d'un objet Tag et ajout au dict "tags"
    def addTag(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet Room
    #
    #  @brief Ajout d'un "ConnectedObject" au dict "connected_objects"
    #  
    #  Création d'un objet ConnectedObject et ajout au dict "connected_objects"
    def addConnectedObject(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet Room
    #
    #  @brief Retrait d'un "Tag" du dict "tags"
    def removeTag(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet Room
    #
    #  @brief Retrait d'un "ConnectedObject" du dict "connected_objects"
    def removeConnectedObject(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet Room
    #
    #  @brief Affichage de la configuration actuelle de la Room
    #
    #  Affichage de la liste des Tag et de la liste des ConnectedObject
    def showRoom(self):
        pass
    
    



##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief tag : classe de représentation d'un AprilTag
#
#  Un Tag décrit un AprilTag dans une pièce : \n
#  -> Famille et id de famille \n
#  -> Pièce qu'il sert à décrire \n
#  -> Taille réelle du tag imprimé \n
#  -> Position du tag dans la pièce \n
#  -> Orientation du tag dans la pièce
class Tag():
   
    ##
    #
    #  @param self Le pointeur vers l'objet Tag
    #
    #  @brief Constructeur de classe
    def __init__(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet Tag
    #
    #  @brief Affichage de la configuration actuelle du Tag
    #
    #  Affichage de la taille, la position, l'orientation
    def showTag(self):
        pass
    
    
    
    
    

##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief ConnectedObject : classe de représentation d'un objet connecté
#
#  Un ConnectedObject décrit un objet connecté : \n
#  -> Ensemble des sphères le représentant (voir classe BoundingSphere)
class ConnectedObject():
   
    ##
    #
    #  @param self Le pointeur vers l'objet ConnectedObject
    #
    #  @brief Constructeur de classe
    def __init__(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet ConnectedObject
    #
    #  @brief Ajout d'une "BoundingSphere" au dict "bounding_spheres"
    #  
    #  Création d'un objet BoundingSphere et ajout au dict "bounding_spheres"
    def addBoundingSphere(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet ConnectedObject
    #
    #  @brief Retrait d'une "BoundingSphere" du dict "bounding_spheres"
    def removeBoundingSphere(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet ConnectedObject
    #
    #  @brief Affichage de la configuration actuelle du ConnectedObject
    #
    #  Affichage de la liste des BoundingSphere
    def showConnectedObject(self):
        pass
    
    
    
    
    
    


##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief BoundingSphere : classe de représentation d'une sphère englobante
#
#  Une BoundingSphere décrit une sphère englobante : \n
#  -> Position et rayon \n
#  -> Ensemble d'actions associées à la sphère (voir classe Action)
class BoundingSphere():
   
    ##
    #
    #  @param self Le pointeur vers l'objet BoundingSphere
    #
    #  @brief Constructeur de classe
    def __init__(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet BoundingSphere
    #
    #  @brief Ajout d'une "Action" au dict "actions"
    #  
    #  Création d'un objet Action et ajout au dict "actions"
    def addAction(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet BoundingSphere
    #
    #  @brief Calcule si il y a intersection entre un rayon donné et la sphère
    def intersection(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet BoundingSphere
    #
    #  @brief Vérifie s'il y a une action à éxécuter
    #  
    #  Parcourt la liste des actions et vérifie si leur trigger est activé.
    #  Dans ce cas, effectue l'action (affichage d'un message prédéfini)
    def checkActions(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet BoundingSphere
    #
    #  @brief Retrait d'une "Action" du dict "actions"
    def removeAction(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet BoundingSphere
    #
    #  @brief Affichage de la configuration actuelle du ConnectedObject
    #
    #  Affichage de la position, du rayon et de la liste des actions
    def showBoundingSphere(self):
        pass    
    





##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief Action : classe de représentation d'une action
#
#  Une Action décrit un couple (déclencheur,message) :\n
#  -> Déclencheeur de l'action (voir classe Trigger)\n
#  -> Message prédéfini à afficher
class Action():
   
    ##
    #
    #  @param self Le pointeur vers l'objet Action
    #
    #  @brief Constructeur de classe
    def __init__(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet Action
    #
    #  @brief Affichage du message prédéfini
    def sendMessage(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet Action
    #
    #  @brief Affichage de la configuration actuelle de l'Action
    #
    #  Affichage du trigger et du message
    def showAction(self):
        pass    