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

from Maths import *

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
    #  @param human_id int : identifiant du Human au sein de l'Application
    #  @param room_id int : identifiant de la Room au sein de l'Application
    #  @param eye_tracker EyeTracker : eye tracker du Human
    #
    #  @brief Constructeur de classe
    def __init__(self,human_id,room_id,eye_tracker):
        # Verification des types
        assert(type(human_id)==int)
        assert(type(room_id)==int)
        assert(type(eye_tracker)==EyeTracker)
        assert(eye_tracker.human_id==human_id)
        # Creation des attributs
        self.id=human_id
        self.room_id=room_id
        self.eye_tracker=eye_tracker
        # Initialisation des attributs de positionnement
        self.pos_head=Vector(0,0,0)
        self.rot_head=Matrix([[1,0,0],[0,1,0],[0,0,1]])
        self.rot_gaze=Matrix([[1,0,0],[0,1,0],[0,0,1]])
        self.ray=Ray(self.pos_head,Vector(1,0,0),self.id)
        self.triggers={}
   
    ##
    #
    #  @param self Le pointeur vers l'objet Human
    #  @param trigger_category string : catégorie de Trigger
    #
    #  @brief Ajout d'un "Trigger" au dict "triggers"
    #  
    #  Création d'un objet Trigger et ajout au dict "triggers"
    def addTrigger(self,trigger_category):
        # Verification des types
        assert(type(trigger_category)==str)
        # Verification trigger non deja existant
        assert(trigger_category not in [trigger.trigger_category for trigger in self.triggers.values()])
        # Recuperation de l'indice du trigger
        trigger_id=0
        if len(self.triggers)>0:
            trigger_id=max(self.triggers.keys())+1
        # Création et ajout du trigger au dict
        self.triggers[trigger_id]=Trigger(trigger_id,self.id,trigger_category)
    
    ##
    #
    #  @param self Le pointeur vers l'objet Human
    #  @param trigger_category string : catégorie de Trigger
    #
    #  @brief Retrait d'un "Trigger" du dict "triggers"
    def removeTrigger(self,trigger_category):
        # Verifications
        assert(type(trigger_category)==str)
        assert(trigger_category in [trigger.trigger_category for trigger in self.triggers.values()])
        # Recuperation de l'id du trigger
        trigger_id=0
        for trigger in self.triggers.values():
            if trigger.trigger_category==trigger_category:
                trigger_id=trigger.id
                break
        # Suppression du trigger du dict
        del self.triggers[trigger_id]
        
    
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
        print("")
        print("Human - ",self.id)
        print("Room id - ",self.room_id)
        print("EyeTracker - ",self.eye_tracker)
        print("Position head - ","Vector (x={},y={},z={})".format("%.4f" % self.pos_head.x(),"%.4f" % self.pos_head.y(),"%.4f" % self.pos_head.z()))
        print("Rotation head - ","Matrix :")
        print(self.rot_head)
        print("Rotation gaze - ","Matrix :")
        print("Triggers - ",self.triggers)
        print(self.rot_gaze)
        self.ray.showRay()
        






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
    #  @param origin Vector : Position de l'origine du rayon
    #  @param direction Vector : Direction du rayon
    #  @param human_id int : identifiant du Human porteur du rayon
    #
    #  @brief Constructeur de classe
    def __init__(self,origin,direction,human_id):
        # Verification des types
        assert(type(origin)==Vector)
        assert(type(direction)==Vector)
        assert(type(human_id)==int)
        # Creation des attributs
        self.origin=origin
        direction.normalize()
        self.direction=direction
        self.human_id=human_id
    
    ##
    #
    #  @param self Le pointeur vers l'objet Ray
    #
    #  @brief Affichage de la configuration actuelle du Ray
    #
    #  Affichage de l'origine et de la direction du rayon
    def showRay(self):
        print("")
        print("Ray")
        print("Human id - ",self.human_id)
        print("Origin - ","Vector (x={},y={},z={})".format("%.4f" % self.origin.x(),"%.4f" % self.origin.y(),"%.4f" % self.origin.z()))
        print("Direction - ","Vector (x={},y={},z={})".format("%.4f" % self.direction.x(),"%.4f" % self.direction.y(),"%.4f" % self.direction.z()))   
    
    
    
    
    
    
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
    #  @param trigger_id int : identifiant du Trigger au sein du Human
    #  @param human_id int : identifiant du Human porteur du Trigger
    #  @param trigger_category string : catégorie de Trigger
    #
    #  @brief Constructeur de classe
    def __init__(self,trigger_id,human_id,trigger_category):
        # Verification des types
        assert(type(trigger_id)==int)
        assert(type(human_id)==int)
        assert(type(trigger_category)==str)
        # Creation des attributs
        self.id=trigger_id
        self.human_id=human_id
        self.trigger_category=trigger_category
        self.state=False
    
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
        print("")
        print("Trigger - ",self.id)
        print("Human id - ",self.human_id)
        print("Category - ",self.trigger_category)
        print("State - ",self.state)
    
    
    
    
    
    
    
    
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
    #  @param tracker_id int : identifiant du tracker au sein du Human
    #  @param human_id int : identifiant du Human porteur du tracker
    #  @param port int : numéro du port de communication du tracker
    #
    #  @brief Constructeur de classe
    def __init__(self,tracker_id,human_id,port):
        # Verification des types
        assert(type(tracker_id)==int)
        assert(type(human_id)==int)
        assert(type(port)==int)
        # Creation des attributs
        self.id=tracker_id
        self.human_id=human_id
        self.port=port
        self.detected_tags={}
    
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
        print("")
        print("Eye Tracker - ",self.id)
        print("Human id - ",self.human_id)
        print("Port - ",self.port)
        print("Detected Tags - ",self.detected_tags)
    
    
    
    
    
    
    
    

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
    #  @param family_name string : nom de la famille de tags
    #  @param family_id int : identifiant du tag au sein de sa famille 
    #  @param id_int int : identifiant du tag au sein de l'EyeTracker
    #  @param translation Vector : vecteur translation repère tag -> repère
    #  caméra
    #  @param rotation Matrix : matrice de passage repère tag -> repère caméra
    #
    #  @brief Constructeur de classe
    def __init__(self,family_name,family_id,tag_id,translation,rotation):
        # Verification des types
        assert(type(family_name)==str)
        assert(type(family_id)==int)
        assert(type(tag_id)==int)
        assert(type(translation)==Vector)
        assert(type(rotation)==Matrix)
        # Creation des attributs
        self.family=family_name
        self.family_id=family_id
        self.id=tag_id
        self.translation=translation
        self.rotation=rotation
    
    ##
    #
    #  @param self Le pointeur vers l'objet DetectedTagay
    #
    #  @brief Affichage de la configuration actuelle du DetectedTag
    #
    #  Affichage de l'identité du tag et de ses informations de positionnement
    def showDetectedTag(self):
        print("")
        print("Detected tag - ",self.id)
        print("Tag family - ",self.family)
        print("Family id - ",self.family_id)
        print("Tag translation - ","Vector (x={},y={},z={})".format("%.4f" % self.translation.x(),"%.4f" % self.translation.y(),"%.4f" % self.translation.z()))
        print("Tag orientation - ", "Matrix :")
        print(self.rotation)
        pass
