"""
Receive world camera data from Pupil using ZMQ.
Make sure the frame publisher plugin is loaded and confugured to gray or rgb
"""
import zmq
from msgpack import unpackb, packb
import numpy as np
import cv2
from pupil_apriltags import Detector

context = zmq.Context()
# open a req port to talk to pupil
addr = '127.0.0.1'  # remote ip or localhost
req_port = "50020"  # same as in the pupil remote gui
req = context.socket(zmq.REQ)
req.connect("tcp://{}:{}".format(addr, req_port))
# ask for the sub port
req.send_string('SUB_PORT')
sub_port = req.recv_string()


# send notification:
def notify(notification):
    """Sends ``notification`` to Pupil Remote"""
    topic = 'notify.' + notification['subject']
    payload = packb(notification, use_bin_type=True)
    req.send_string(topic, flags=zmq.SNDMORE)
    req.send(payload)
    return req.recv_string()


# Start frame publisher with format BGR
notify({'subject': 'start_plugin', 'name': 'Frame_Publisher', 'args': {'format': 'gray'}})

# open a sub port to listen to pupil
sub = context.socket(zmq.SUB)
sub.connect("tcp://{}:{}".format(addr, sub_port))

# set subscriptions to topics
# recv just pupil/gaze/notifications
sub.setsockopt_string(zmq.SUBSCRIBE, 'frame.')



# main poll loop
# We route topic updates from frontend to backend, and
# we handle subscriptions by sending whatever we cached,
# if anything:
poller = zmq.Poller()
poller.register(sub, zmq.POLLIN)

def recv_from_sub():
    '''Recv a message with topic, payload.
    Topic is a utf-8 encoded string. Returned as unicode object.
    Payload is a msgpack serialized dict. Returned as a python dict.
    Any addional message frames will be added as a list
    in the payload dict with key: '__raw_data__' .
    '''
    
    #Vide le cache
    try:
        events = dict(poller.poll(10000))
    except KeyboardInterrupt:
        print("interrupted")
    
    if sub in events:
        #Recoit des messages pour vider le cache
        msg = sub.recv_multipart()
        print(msg)
        
    topic = sub.recv_string()
    payload = unpackb(sub.recv(), raw=False)
    extra_frames = []
    while sub.get(zmq.RCVMORE):
        extra_frames.append(sub.recv())
    if extra_frames:
        payload['__raw_data__'] = extra_frames
    return topic, payload

at_detector = Detector(families='tag36h11',nthreads=1,quad_decimate=1.0,quad_sigma=0.2,
                       refine_edges=1,
                       decode_sharpening=0.25,
                       debug=0)

recent_world = None
recent_eye0 = None
recent_eye1 = None

i=0
indice=0

try:
    while True:
        topic, msg = recv_from_sub()
        if topic == 'frame.world':
            recent_world = np.frombuffer(msg['__raw_data__'][0], dtype=np.uint8,count=msg['height']*msg['width']).reshape(msg['height'], msg['width'])
        elif topic == 'frame.eye.0':
            pass
            #recent_eye0 = np.frombuffer(msg['__raw_data__'][0], dtype=np.uint8).reshape(msg['height'], msg['width'])
        elif topic == 'frame.eye.1':
            pass
            #recent_eye1 = np.frombuffer(msg['__raw_data__'][0], dtype=np.uint8).reshape(msg['height'], msg['width'])

        if recent_world is not None:
            
            if i%50==0 :
                tags = at_detector.detect(recent_world, estimate_tag_pose=True, camera_params=[542.098,542.128,311.448,217.969], tag_size=0.0305)
                print(len(tags))
            i+=1
            
            
            
            cv2.imshow("world", recent_world)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            pass  # here you can do calculation on the 3 most recent world, eye0 and eye1 images
            
            if cv2.waitKey(1) & 0xFF == ord('p'):
                print("Photo prise")
                cv2.imwrite( "C:/Users/gobgr/Desktop/photos_calbration_4/calib_img_"+str(indice)+".jpg", recent_world)
                indice+=1
            
except KeyboardInterrupt:
    pass
finally:
    cv2.destroyAllWindows()