from pynput.mouse import Listener
import zmq
import time

port = "59140"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)


def on_click(x, y, button, pressed):
    if pressed :
        topic = "MOUSE"
        messagedata = "LC-0001"
        print ("%s %s" % (topic, messagedata))
        socket.send_string("%s %s" % (topic, messagedata))
    else:
        topic = "MOUSE"
        messagedata = "LC-0000"
        print ("%s %s" % (topic, messagedata))
        socket.send_string("%s %s" % (topic, messagedata))
        
# Collect events until released
with Listener(on_click=on_click) as listener:
    listener.join()