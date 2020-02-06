##
#  @author BASSO-BERT Yanis
#  @author GOBERT Grégoire
#  @author ROUX Marie
#
#  @date 2020 
#
#  @brief Room : module de description statique de la salle
#
#  Le module Room contient les classes : \n
#  -> Room : représentation d'une pièce \n
#  -> Tag : représentation d'un AprilTag dans la pièce \n
#  -> ConnectedObject : représentation d'un objet connecté \n
#  -> BoundingSphere : représentation d'une sphère \n
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
    #  @param room id int : identifiant de la Room au sein de l'Application
    #
    #  @brief Constructeur de classe
    def __init__(self,room_id):
        # Verification des types
        assert(type(room_id)==int)
        # Creation des attributs
        self.id=room_id
        self.tags={}
        self.connected_objects={}
   
    ##
    #
    #  @param self Le pointeur vers l'objet Room
    #  @param family_name string : nom de la famille du tag
    #  @param family_id  int : identifiant du tag au sein de sa famille
    #  @param tag_name str : nom du tag
    #  @param size float : taille du tag (en mètres)
    #  @param position Vector : position du tag dans le repère de la pièce
    #  @param orientation Matrix : matrice de passage du repère lié à la pièce
    #  au repère lié au tag
    #
    #  @brief Ajout d'un "Tag" au dict "tags"
    #  
    #  Création d'un objet Tag et ajout au dict "tags"
    def addTag(self,family_name,family_id,tag_name,size,position,orientation):
        # Verification des types
        assert(type(family_name)==str)
        assert(type(family_id)==int)
        assert(type(tag_name)==str)
        assert(type(size)==float)
        assert(type(position)==Vector)
        assert(type(orientation)==Matrix)
        # Verification Tag non deja existant
        assert(tag_name not in [tag.name for tag in self.tags.values()])
        # Recuperation de l'indice du Tag
        tag_id=0
        if len(self.tags)>0:
            tag_id=max(self.tags.keys())+1
        # Création et ajout du Tag au dict
        self.tags[tag_id]=Tag(family_name,family_id,tag_id,tag_name,self.id,size,position,orientation)
   
    ##
    #
    #  @param self Le pointeur vers l'objet Room
    #  @param connectedObject_name str : nom du ConnectedObject
    #
    #  @brief Ajout d'un "ConnectedObject" au dict "connected_objects"
    #  
    #  Création d'un objet ConnectedObject et ajout au dict "connected_objects"
    def addConnectedObject(self,connectedObject_name):
         # Verification des types
        assert(type(connectedObject_name)==str)
        # Verification ConnectedObject non deja existant
        assert(connectedObject_name not in [CO.name for CO in self.connected_objects.values()])
        # Recuperation de l'indice du ConnectedObject
        CO_id=0
        if len(self.connected_objects)>0:
            CO_id=max(self.connected_objects.keys())+1
        # Création et ajout du ConnectedObject au dict
        self.connected_objects[CO_id]=ConnectedObject(CO_id,connectedObject_name,self.id)
    
    ##
    #
    #  @param self Le pointeur vers l'objet Room
    #  @param tag_name str : nom du tag
    #
    #  @brief Retrait d'un "Tag" du dict "tags"
    def removeTag(self,tag_name):
        # Verifications
        assert(type(tag_name)==str)
        assert(tag_name in [tag.name for tag in self.tags.values()])
        # Recuperation de l'id du Tag
        tag_id=0
        for tag in self.tags.values():
            if tag.name==tag_name:
                tag_id=tag.id
                break
        # Suppression du Tag du dict
        del self.tags[tag_id]
    
    ##
    #
    #  @param self Le pointeur vers l'objet Room
    #  @param connectedObject_name str : nom du ConnectedObject
    #
    #  @brief Retrait d'un "ConnectedObject" du dict "connected_objects"
    def removeConnectedObject(self,connectedObject_name):
        # Verifications
        assert(type(connectedObject_name)==str)
        assert(connectedObject_name in [CO.name for CO in self.connected_objects.values()])
        # Recuperation de l'id du ConnectedObject
        CO_id=0
        for CO in self.connected_objects.values():
            if CO.name==connectedObject_name:
                CO_id=CO.id
                break
        # Suppression du ConnectedObject du dict
        del self.connected_objects[CO_id]
    
    ##
    #
    #  @param self Le pointeur vers l'objet Room
    #
    #  @brief Affichage de la configuration actuelle de la Room
    #
    #  Affichage de la liste des Tag et de la liste des ConnectedObject
    def showRoom(self):
        print("")
        print("Room - ",self.id)
        print("Tags - ",self.tags)
        print("Connectd objects - ",self.connected_objects)
    
    



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
    #  @param family_name string : nom de la famille du tag
    #  @param family_id  int : identifiant du tag au sein de sa famille
    #  @param tag_id int : identifiant du tag
    #  @param tag_name str : nom du tag
    #  @param room_id int : identifiant de la Room contenant le tag
    #  @param size float : taille du tag (en mètres)
    #  @param position Vector : position du tag dans le repère de la pièce
    #  @param orientation Matrix : matrice de passage du repère lié à la pièce
    #  au repère lié au tag
    #
    #  @brief Constructeur de classe
    def __init__(self,family_name,family_id,tag_id,tag_name,room_id,size,position,orientation):
        # Verification des types
        assert(type(family_name)==str)
        assert(type(family_id)==int)
        assert(type(tag_id)==int)
        assert(type(tag_name)==str)
        assert(type(room_id)==int)
        assert(type(size)==float)
        assert(type(position)==Vector)
        assert(type(orientation)==Matrix)
        # Creation des attributs
        self.id=tag_id
        self.name=tag_name
        self.family=family_name
        self.family_id=family_id
        self.room_id=room_id
        self.size=size
        self.pos=position
        self.rot=orientation
   
    ##
    #
    #  @param self Le pointeur vers l'objet Tag
    #
    #  @brief Affichage de la configuration actuelle du Tag
    #
    #  Affichage de la taille, la position, l'orientation
    def showTag(self):
        print("")
        print("Tag - ",self.id)
        print("Tag name - ",self.name)
        print("Family - ",self.family)
        print("Family id - ",self.family_id)
        print("Room id - ",self.room_id)
        print("size - ",self.size)
        print("Position - ","Vector (x={},y={},z={})".format("%.4f" % self.pos.x(),"%.4f" % self.pos.y(),"%.4f" % self.pos.z()))
        print("Orientation - ","Matrix")
        print(self.rot)
    
    
    
    
    

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
    #  @param connectedObject_id int : identifiant du ConnectedObject au sein
    #  de la Room
    #  @param connectedObject_name str : nom du ConnectedObject
    #  @param room_id int : identifiant de la Room
    #
    #  @brief Constructeur de classe
    def __init__(self,connectedObject_id,connectedObject_name,room_id):
        # Verification des types
        assert(type(connectedObject_id)==int)
        assert(type(connectedObject_name)==str)
        assert(type(room_id)==int)
        # Creation des attributs
        self.id=connectedObject_id
        self.name=connectedObject_name
        self.room_id=room_id
        self.bounding_spheres={}
   
    ##
    #
    #  @param self Le pointeur vers l'objet ConnectedObject
    #  @param boundingSphere_name str : nom de la BoundingSphere
    #  @param center Vector  : centre de la sphere
    #  @param radius float : rayon de la sphere
    #
    #  @brief Ajout d'une "BoundingSphere" au dict "bounding_spheres"
    #  
    #  Création d'un objet BoundingSphere et ajout au dict "bounding_spheres"
    def addBoundingSphere(self,boundingSphere_name,center,radius):
        # Verification des types
        assert(type(center)==Vector)
        assert(type(radius)==float)
        # Verification BoundingSphere non deja existante
        assert((center,radius) not in [(BS.center,BS.radius)  for BS in self.bounding_spheres.values()])
        # Recuperation de l'indice de la BoundingSphere
        BS_id=0
        if len(self.bounding_spheres)>0:
            BS_id=max(self.bounding_spheres.keys())+1
        # Création et ajout de la BoundingSphere au dict
        self.bounding_spheres[BS_id]=BoundingSphere(BS_id,boundingSphere_name,self.id,center,radius)
    
    ##
    #
    #  @param self Le pointeur vers l'objet ConnectedObject
    #  @param boundingSphere_name str : nom de la BoundingSphere
    #
    #  @brief Retrait d'une "BoundingSphere" du dict "bounding_spheres"
    def removeBoundingSphere(self,boundingSphere_name):
        # Verifications
        assert(type(boundingSphere_name)==str)
        assert(boundingSphere_name in [BS.name for BS in self.bounding_spheres.values()])
        # Recuperation de l'id de la BoundingSphere
        BS_id=0
        for BS in self.bounding_spheres.values():
            if BS.name==boundingSphere_name:
                BS_id=BS.id
                break
        # Suppression de la BoundingSphere du dict
        del self.bounding_spheres[BS_id]
    
    ##
    #
    #  @param self Le pointeur vers l'objet ConnectedObject
    #
    #  @brief Affichage de la configuration actuelle du ConnectedObject
    #
    #  Affichage de la liste des BoundingSphere
    def showConnectedObject(self):
        print("")
        print("ConnectedObject - ",self.id)
        print("ConnectedObject Name - ",self.name)
        print("Room id - ",self.room_id)
        print("Bounding Spheres - ",self.bounding_spheres)
    
    
    
    
    
    


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
    #  @param boundingSphere_id int : identifiant de la BoundingSphere au sein
    #  du ConnectedObject
    #  @param boundingSphere_name str : nom de la BoundingSphere
    #  @param connected_object_id : identifiant du COnnectedObject possesseur
    #  de la BoundingSphere
    #  @param center Vector  : centre de la sphere
    #  @param radius float : rayon de la sphere
    #
    #  @brief Constructeur de classe
    def __init__(self,boundingSphere_id,boundingSphere_name,connected_object_id,center,radius):
        # Verification des types
        assert(type(boundingSphere_id)==int)
        assert(type(boundingSphere_name)==str)
        assert(type(connected_object_id)==int)
        assert(type(center)==Vector)
        assert(type(radius)==float)
        # Creation des attributs
        self.id=boundingSphere_id
        self.name=boundingSphere_name
        self.connected_object_id=connected_object_id
        self.center=center
        self.radius=radius
        self.actions={}
   
    ##
    #
    #  @param self Le pointeur vers l'objet BoundingSphere
    #
    #  @brief Ajout d'une "Action" au dict "actions"
    #  @param action_name string : nom de l'action
    #  @param trigger_category string: catégorie de Trigger
    #  @param output_message string : message à envoyer pour indiquer la 
    #  nécessité de réaliser l'action
    #  
    #  Création d'un objet Action et ajout au dict "actions"
    def addAction(self,action_name,trigger_category,output_message):
        # Verification des types
        assert(type(action_name)==str)
        assert(type(trigger_category)==str)
        assert(type(output_message)==str)
        # Verification action non deja existante
        assert(action_name not in [action.name for action in self.actions.values()])
        # Recuperation de l'indice de l'action
        action_id=0
        if len(self.actions)>0:
            action_id=max(self.actions.keys())+1
        # Création et ajout de l'action au dict
        self.actions[action_id]=Action(action_id,action_name,trigger_category,output_message)
    
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
    #  @param action_name string : nom de l'action à supprimer
    #
    #  @brief Retrait d'une "Action" du dict "actions"
    def removeAction(self,action_name):
        # Verifications
        assert(type(action_name)==str)
        assert(action_name in [action.name for action in self.actions.values()])
        # Recuperation de l'id de l'action
        action_id=0
        for action in self.actions.values():
            if action.name==action_name:
                action_id=action.id
                break
        # Suppression de l'action du dict
        del self.actions[action_id]
    
    ##
    #
    #  @param self Le pointeur vers l'objet BoundingSphere
    #
    #  @brief Affichage de la configuration actuelle du ConnectedObject
    #
    #  Affichage de la position, du rayon et de la liste des actions
    def showBoundingSphere(self):
        print("")
        print("BoundingSphere - ",self.id)
        print("Name - ",self.name)
        print("ConnectedObject id - ",self.connected_object_id)
        print("Center - ","Vector (x={},y={},z={})".format("%.4f" % self.center.x(),"%.4f" % self.center.y(),"%.4f" % self.center.z()))
        print("Radius - ",self.radius)
        print("Actions - ",self.actions)
    





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
    #  @param action_id int : identifiant de l'action au sein de la 
    #  BoundingSphere
    #  @param action_name string : nom de l'action
    #  @param trigger_category string: catégorie de Trigger
    #  @param output_message string : message à envoyer pour indiquer la 
    #  nécessité de réaliser l'action
    #
    #  @brief Constructeur de classe
    def __init__(self,action_id,action_name,trigger_category,output_message):
        # Verification des types
        assert(type(action_id)==int)
        assert(type(action_name)==str)
        assert(type(trigger_category)==str)
        assert(type(output_message)==str)
        # Creation des attributs
        self.id=action_id
        self.name=action_name
        self.trigger_category=trigger_category
        self.output_message=output_message
   
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
        print("")
        print("Action - ",self.id)
        print("Action name - ",self.name)
        print("Trigger category - ",self.trigger_category)
        print("Output message - ",self.output_message)
    