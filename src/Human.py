##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief Human : module de description d'un utilisateur
#
#  Le module Human contient les classes : \n
#  -> Humain : représentation d'un être humain \n
#  -> Ray : représentation d'un rayon 3D \n
#  -> Trigger : représentation d'un déclencheur d'action \n
#  -> EyeTracker : représentation d'un eye-tracker Pupil-Labs \n
#  -> Detected : représentation d'un AprilTag détecté par l'eye-tracker

import Maths

##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief Human : classe de représentation d'un être humain
#
#  Un Human décrit un être humain : \n
#  -> Positionnement et orientation de sa tête dans la pièce \n
#  -> Direction de son regard \n
#  -> Rayon reptésentant le trajet du regard (voir classe Ray) \n
#  -> Un eye-tracker qui lui est propre (voir classe EyeTracker) \n
#  -> Un ensemble de déclencheurs d'action (voir classe Trigger)
class Human():
   
    ##
    #
    #  @param self Le pointeur vers l'objet Human
    #
    #  @brief Constructeur de classe
    def __init__(self):
        pass
   
    ##
    #
    #  @param self Le pointeur vers l'objet Human
    #
    #  @brief Ajout d'un "Trigger" au dict "triggers"
    #  
    #  Création d'un objet Trigger et ajout au dict "triggers"
    def addTrigger(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet Human
    #
    #  @brief Retrait d'un "Trigger" du dict "triggers"
    def removeTrigger(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet Human
    #
    #  @brief Vérifie les "Trigger" activés
    #
    #  Parcourt l'ensemble des "Trigger" du dict "triggers"
    #  et vérifie si ces derniers sont activés
    def checkTriggers(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet Human
    #
    #  @brief Envoie un rayon dans une pièce
    #
    #  Envoie le rayon du regard de l'utilisateur dans la pièce
    #  et vérifie si des "BoundingSphere" sont intersectées
    def traceRay(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet Human
    #
    #  @brief Met à jour les paramètres de positionnement du Human
    #
    #  Met à jour la position de la tête \n
    #  Met à jour l'orientation de la tête \n
    #  Met à jour l'orientation du regard \n
    #  Met à jour le rayon du regard \n
    def updateParams(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet Human
    #
    #  @brief Affichage de la configuration actuelle du Human
    #
    #  Affichage des informations de positionnement et de la liste des
    #  déclencheurs d'action
    def showHuman(self):
        pass






##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief Ray : classe de représentation d'un rayon (type rayon lumineux)
#
#  Un Ray décrit un rayon : \n
#  -> Origine et direction du rayon
class Ray():
   
    ##
    #
    #  @param self Le pointeur vers l'objet Ray
    #
    #  @brief Constructeur de classe
    def __init__(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet Ray
    #
    #  @brief Affichage de la configuration actuelle du Ray
    #
    #  Affichage de l'origine et de la direction du rayon
    def showRay(self):
        pass   
    
    
    
    
    
    
##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief Trigger : classe de représentation d'un déclencheur d'action
#
#  Un Trigger décrit un déclencheur : \n
#  -> Catégorie du déclencheur \n
#  -> Son état (activé/non activé)
class Trigger():
   
    ##
    #
    #  @param self Le pointeur vers l'objet Trigger
    #
    #  @brief Constructeur de classe
    def __init__(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet Trigger
    #
    #  @brief Verifie si le Trigger est activé par l'utilisateur
    #
    #  Fait le lien avec "l'objet" réel de déclenchement
    def catchTrigger(self):
        pass   
    
    ##
    #
    #  @param self Le pointeur vers l'objet Trigger
    #
    #  @brief Affichage de la configuration actuelle du Trigger
    #
    #  Affichage de la catégorie et du l'état
    def showTrigger(self):
        pass   
    
    
    
    
    
    
    
    
##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief EyeTracker : classe de représentation d'un eye-tracker Pupil
#
#  Un EyeTracker décrit un eye-tracker Pupil: \n
#  -> Son port \n
#  -> La liste des AprilTags qu'il détecte
class EyeTracker():
   
    ##
    #
    #  @param self Le pointeur vers l'objet EyeTracker
    #
    #  @brief Constructeur de classe
    def __init__(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet EyeTracker
    #
    #  @brief Verifie la connection avec l'eye-tracker
    def checkConnection(self):
        pass   
    
    ##
    #
    #  @param self Le pointeur vers l'objet EyeTracker
    #
    #  @brief Analyse l'image actuelle
    #
    #  Capture l'image frontale récente, détecte les tags présents et met
    #  à jour le dict "detected_tags"
    def updateFrame(self):
        pass   
    
    ##
    #
    #  @param self Le pointeur vers l'objet EyeTracker
    #
    #  @brief Affichage de la configuration actuelle de l'EyeTracker
    #
    #  Affichage du port et de la liste des AprilTags détectés
    def showEyeTracker(self):
        pass   
    
    
    
    
    
    
    
    

##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief DetectedTag : classe de représentation d'un AprilTag détecté
#
#  Un DetectedTag décrit un AprilTag détecté : \n
#  -> Famille de tags et identifiant \n
#  -> Vecteur translation Tag->Caméra \n
#  -> Matrice de rotation (Tag dans base Caméra)
class DetectedTag():
   
    ##
    #
    #  @param self Le pointeur vers l'objet DetectedTag
    #
    #  @brief Constructeur de classe
    def __init__(self):
        pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet DetectedTagay
    #
    #  @brief Affichage de la configuration actuelle du DetectedTag
    #
    #  Affichage de l'identité du tag et de ses informations de positionnement
    def showDetectedTag(self):
        pass   