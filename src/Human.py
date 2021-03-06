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
import threading
import msgpack
import sys

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
    #  @param human_name string : nom du Human
    #  @param room_id int : identifiant de la Room au sein de l'Application
    #  @param eye_tracker_port int : port de l'eye tracker du Human
    #
    #  @brief Constructeur de classe
    def __init__(self,human_id,human_name,room_id,eye_tracker_port):
        # Verification des types
        assert(type(human_id)==int)
        assert(type(human_name)==str)
        assert(type(room_id)==int)
        assert(type(eye_tracker_port)==int)
        # Creation des attributs
        self.id=human_id
        self.name=human_name
        self.room_id=room_id
        self.eye_tracker=EyeTracker(1,self.id,eye_tracker_port)
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
    #  @param port int : port d'écoute tcp du Trigger
    #  @param topic string : topic de publication du Trigger
    #  @param messageOn string : message etat actif
    #  @param messageOff string : message etat non actif
    #
    #  @brief Ajout d'un "Trigger" au dict "triggers"
    #  
    #  Création d'un objet Trigger et ajout au dict "triggers"
    def addTrigger(self,trigger_category,port,topic,messageOn,messageOff):
        # Verification des types
        assert(type(trigger_category)==str)
        # Verification trigger non deja existant
        assert(trigger_category not in [trigger.trigger_category for trigger in self.triggers.values()])
        # Recuperation de l'indice du trigger
        trigger_id=0
        if len(self.triggers)>0:
            trigger_id=max([trigger.id for trigger in self.triggers.values()])+1
        # Création et ajout du trigger au dict
        self.triggers[trigger_category]=Trigger(trigger_id,self.id,trigger_category,port,topic,messageOn,messageOff)
    
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
        # Suppression du trigger du dict
        del self.triggers[trigger_category]
     
    
    ##
    #
    #  @param self Le pointeur vers l'objet Human
    #  @param tags dict : dictionnaire des tags de la piece
    #
    #  @brief Met à jour les paramètres de positionnement du Human
    #
    #  Met à jour la position de la tête \n
    #  Met à jour l'orientation de la tête \n
    #  Met à jour l'orientation du regard \n
    #  Met à jour le rayon du regard \n
    def updateParams(self,tags):
        #print(len(self.eye_tracker.detected_tags)," tags detectes")
        
        # Initialisation des paramètres
        pos_head=Vector(0,0,0)
        rot_head=Matrix([[0,0,0],[0,0,0],[0,0,0]])
        
        nb_used_detected_tags=0
        # Parcours du dictionnaire des tags detectés
        for _,detected_tag in self.eye_tracker.detected_tags.items():
            #Tag correspondant dans la piece
            nom_tag=detected_tag.family[2:-1]+'_'+str(detected_tag.family_id)
            try:
                # Récupération de la configuration du tag dans le repère room
                room_tag=tags[nom_tag]
                T_room2tag=room_tag.pos
                R_room2tag=room_tag.rot
                # Récupération de la configuration de la caméra dans le repère tag
                T_tag2cam=-detected_tag.translation
                R_tag2cam=detected_tag.rotation.transpose()
                
                ## Pour pos_head
                # Cam -> Tag -> Room
                H_in_tag=R_tag2cam.dot(T_tag2cam)
                H_in_room=R_room2tag.dot(H_in_tag)+T_room2tag
                # Ajout de la positon pour le moyennage
                pos_head=pos_head+H_in_room
                
                ## Pour rot_head
                R_room2cam=R_room2tag.dot(R_tag2cam)
                rot_head=rot_head+R_room2cam
                
                #Incrémentation
                nb_used_detected_tags+=1
                
            except:
                print(nom_tag+" detecté mais non présent dans la pièce")
        
        # Division pour moyenne
        if nb_used_detected_tags>0:
            
            self.pos_head=pos_head/nb_used_detected_tags
            self.rot_head=rot_head/nb_used_detected_tags
            
            #self.pos_head.showVector()
            #self.rot_head.showMatrix()
        
        # Calcul du gaze (direction du regard)
        gaze_in_cam=self.eye_tracker.gaze_in_cam
        
        R_room2cam=self.rot_head
        H_in_room=self.pos_head
        
        point_on_gaze_ray_world=R_room2cam.dot(gaze_in_cam)+H_in_room
        
        gaze_direction=point_on_gaze_ray_world-H_in_room
        
        self.ray=Ray(H_in_room,Vector(gaze_direction[0,0],gaze_direction[1,0],gaze_direction[2,0]),self.id)
        #self.ray.showRay()
        
        
    
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
        print("Human name - ",self.name)
        print("Room id - ",self.room_id)
        print("EyeTracker - ",self.eye_tracker)
        print("Position head - ","Vector (x={},y={},z={})".format("%.4f" % self.pos_head.x(),"%.4f" % self.pos_head.y(),"%.4f" % self.pos_head.z()))
        print("Rotation head - ","Matrix :")
        print(self.rot_head)
        print("Rotation gaze - ","Matrix :")
        print(self.rot_gaze)
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
    #  @param port int : port d'écoute tcp du Trigger
    #  @param topic string : topic de publication du Trigger
    #  @param messageOn string : message etat actif
    #  @param messageOff string : message etat non actif
    #
    #  @brief Constructeur de classe
    def __init__(self,trigger_id,human_id,trigger_category,port,topic,messageOn,messageOff):
        # Verification des types
        assert(type(trigger_id)==int)
        assert(type(human_id)==int)
        assert(type(trigger_category)==str)
        assert(type(port)==int)
        assert(type(topic)==str)
        assert(type(messageOn)==str)
        assert(type(messageOff)==str)
        # Creation des attributs
        self.id=trigger_id
        self.human_id=human_id
        self.trigger_category=trigger_category
        self.state=False    
        self.__port=port
        self.__topic=topic
        self.__messageOn=messageOn
        self.__messageOff=messageOff
        # Connexion au port tcp
        self.__context = zmq.Context()
        self.__socket = self.__context.socket(zmq.SUB)
        self.__socket.connect("tcp://localhost:%s" % str(self.__port))
        self.__socket.setsockopt_string(zmq.SUBSCRIBE, self.__topic)
        print(self.trigger_category," connection OK")
        # Lancement de l'acquisition en continu
        self.__trigger_reader = threading.Thread(target=self.catchTrigger, args=(), daemon=True)
        self.__state_lock = threading.Lock()
        self.__trigger_reader.start()

    
    ##
    #
    #  @param self Le pointeur vers l'objet Trigger
    #
    #  @brief Verifie si le Trigger est activé par l'utilisateur
    #
    #  Fait le lien avec "l'objet" réel de déclenchement
    def catchTrigger(self):
        while True:
            string = self.__socket.recv()
            topic, messagedata = string.split()
            message=str(messagedata)[2:-1]
            # MàJ de l'etat
            if message==self.__messageOn:
                with self.__state_lock:
                    self.state=True
            elif message==self.__messageOff:
                with self.__state_lock:
                    self.state=False
            
    
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
    
    
    
    
    
    

from pupil_apriltags import Detector
import zmq
from msgpack import unpackb, packb
import numpy as np

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
        self.gaze_in_cam=Vector(0.0,0.0,1.0)
        
        #Parametres de la caméra frontale du tracker
        # mtx : matrice intrinsèque
        # h : hauteur de l'image en nombre de pixels
        # w : largeur de l'image en nombre de pixels
        # dist : paramètres de distorsion de l'image
        self.__mtx = Matrix([[1.600e+03, 0.00000000e+00, 6.40e+02],
                               [0.00000000e+00, 1.600e+03, 3.60e+02],
                               [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
        #self.__mtx = Matrix([[829.3510515270362, 0.0, 659.9293047259697],[0.0, 799.5709408845464, 373.0776462356668],[0.0, 0.0, 1.0]])
        self.__h = 720
        self.__w = 1280
        self.__dist = np.array([[-0.43738542863224966,0.190570781428104,-0.00125233833830639,0.0018723428760170056,-0.039219091259637684]])
        
        # Communication avec le tracker
        self.__context= zmq.Context()
        self.__addr = '127.0.0.1'  # remote ip ou localhost
        self.__req = self.__context.socket(zmq.REQ)
        self.__req.connect("tcp://{}:{}".format(self.__addr, str(self.port)))
        self.__req.send_string('SUB_PORT') # Demande du port de requete
        self.__sub_port = self.__req.recv_string() # Stockage port de requete
        # Démarrer le frame publisher au format Noir et Blanc
        self.notify({'subject': 'start_plugin', 'name': 'Frame_Publisher', 'args': {'format': 'gray'}})
        
        # Ouvert d'un port de souscription(sub) pour ecouter le tracker (frames)
        self.__sub_frame = self.__context.socket(zmq.SUB)
        self.__sub_frame.connect("tcp://{}:{}".format(self.__addr, self.__sub_port))
        # Recevoir uniquement les notifications concernant les frames
        self.__sub_frame.setsockopt_string(zmq.SUBSCRIBE, 'frame.world')
        
        # Ouvert d'un port de souscription(sub) pour ecouter le tracker (gaze)
        self.__sub_gaze = self.__context.socket(zmq.SUB)
        self.__sub_gaze.connect("tcp://{}:{}".format(self.__addr, self.__sub_port))
        # Recevoir uniquement les notifications concernant les frames
        self.__sub_gaze.setsockopt_string(zmq.SUBSCRIBE, 'gaze.2d.0')
        
        # Thread lecteur de frames en continu
        self.__frames_reader = threading.Thread(target=self.always_recv_frame, args=(), daemon=True)
        self.__frames_lock = threading.Lock()
        self.__available_frame=False
        self.__frames_reader.start()
        
        # Thread lecteur de gaze en continu
        self.__gaze_reader = threading.Thread(target=self.always_recv_gaze, args=(), daemon=True)
        self.__gaze_lock = threading.Lock()
        self.__available_gaze=False
        self.__gaze_reader.start()
        
        # Détecteur de tags
        self.__at_detector = Detector(families='tag36h11',
                       nthreads=1,
                       quad_decimate=1.0,
                       quad_sigma=0.0,
                       refine_edges=1,
                       decode_sharpening=0.25,
                       debug=0)
        
    
    ##
    #
    #  @param self Le pointeur vers l'objet EyeTracker
    #
    #  @brief Lit la dernièere frame reçue par le 'sub' et la stocke
    def always_recv_frame(self):
        # Vide le cache : on lit 10 frames sans les traiter
        # Nombre a adapter aux performances de l'ordinateur
        print("start reader")
        while(True):
            try:
                topic = self.__sub_frame.recv_string()
                payload = unpackb(self.__sub_frame.recv(), raw=False)
                extra_frames = []
                while self.__sub_frame.get(zmq.RCVMORE):
                    extra_frames.append(self.__sub_frame.recv())
                if extra_frames:
                    payload['_raw_data_'] = extra_frames
                    with self.__frames_lock:
                        self.__payload = payload
                        self.__available_frame=True
            except:
                pass
    
    ##
    #
    #  @param self Le pointeur vers l'objet EyeTracker
    #
    #  @brief Lit le dernier message regard reçu par le 'sub' et le stocke
    def always_recv_gaze(self):
        # Vide le cache : on lit 10 frames sans les traiter
        # Nombre a adapter aux performances de l'ordinateur
        print("start reader")
        while(True):
            try:
                topic, payload = self.__sub_gaze.recv_multipart()
                message = msgpack.loads(payload)
                with self.__gaze_lock:
                    self.__normalized_pos=[message[b'norm_pos'][0],message[b'norm_pos'][1]]
                    self.__available_gaze=True
            except:
                pass
   
        
    ##
    #
    #  @param self Le pointeur vers l'objet EyeTracker
    #  @param notification dict : Le message à envoyer
    #
    #  @brief Envoie un message à l'API de l'Eye Tracker    
    def notify(self,notification):
        topic = 'notify.' + notification['subject']
        payload = packb(notification, use_bin_type=True)
        self.__req.send_string(topic, flags=zmq.SNDMORE)
        self.__req.send(payload)
        return self.__req.recv_string()
    
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
    #  @param size_tag float : taille réelle d'un tag (en mètre)
    #
    #  @brief Analyse l'image actuelle
    #
    #  Capture l'image frontale récente, détecte les tags présents et met
    #  à jour le dict "detected_tags"
    def updateFrame(self,size_tag):
        # Récupération de la frame
        with self.__frames_lock:
            if(self.__available_frame==True):
                msg = self.__payload
            else:
                return
        with self.__gaze_lock:
            if(self.__available_gaze==True):
                norm_pos = self.__normalized_pos
            else:
                return
        
        # Position regard dans caméra
        fx=self.__mtx[0,0]
        fy=self.__mtx[1,1]
        cx=self.__mtx[0,2]
        cy=self.__mtx[1,2]
        self.gaze_in_cam=Vector(norm_pos[0]*self.__w/fx-cx/fx,
                                (1-norm_pos[1])*self.__h/fy-cy/fy,
                                1.0)
            
        #Image caméra frontale en noir et blanc
        recent_world = np.frombuffer(msg['_raw_data_'][0], dtype=np.uint8,count=msg['height']*msg['width']).reshape(msg['height'], msg['width'])
        tags = self.__at_detector.detect(recent_world, estimate_tag_pose=True, camera_params=[self.__mtx[0,0],self.__mtx[1,1],self.__mtx[0,2],self.__mtx[1,2]], tag_size=size_tag)
        
        # Remplissage du dictionnaire de tags
        self.detected_tags={}
        id_in_dict=0
        for tag in tags :
            # Caractéristiques du tag détecté
            tag_family=str(tag.tag_family)
            tag_family_id=tag.tag_id
            translation=tag.pose_t
            rotation=tag.pose_R
            # Ajout du tag dans le dictionnaire
            self.detected_tags[id_in_dict]=DetectedTag(tag_family,
                                        tag_family_id,
                                        id_in_dict,
                                        Vector(translation[0,0],translation[1,0],translation[2,0]),
                                        Matrix(rotation.tolist()))
            # Incrémentation de l'indice
            id_in_dict+=1
                
        

            
    
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
        