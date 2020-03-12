import zmq
import sys
import serial as sr

ser=sr.Serial("COM3",9600)

port = "59144"
    
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting data frome EyeDoIt")
socket.connect ("tcp://localhost:%s" % port)

#Choix du topi
topicfilter = "EDI"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

object_state=False

while True:
    string = socket.recv()
    topic, messagedata = string.split()
    print(topic,messagedata)
    message=str(messagedata)[2:-1]
    if message=="TV-CLICK":
        if object_state==False:
            #print('\a')
            ser.write("H".encode('ascii'))
            object_state=True
        
        else :
            ser.write("L".encode('ascii'))
            object_state=False
            