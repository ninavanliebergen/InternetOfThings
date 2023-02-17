##########################################
# HOUSEHOLD - ELECTRICITY PUBLISHER
# every few hours, the electricity usage is pushed (IN kWh)
# normally, an average household uses 29 KWh per day
##############################################

#simulator device 1 for mqtt message publishing
import paho.mqtt.client as paho
import time
import random
import json 

#hostname
broker="localhost"

#port
port=1883

def on_publish(client,userdata,result):
    print("Device 1 : Data published.")
    pass

client= paho.Client("electra")
client.on_publish = on_publish
client.connect(broker,port)

for i in range(20):
    d=random.randint(1,5)
    
 #telemetry to send 
    # message="Device 1 : Data " + str(i)
    message = random.randint(1,10)
    #message = '{"_msgid":"c0c60d0174d527e2","value":5.866002153323057}'
    time.sleep(d)
    
 #publish message
    ret= client.publish("/household/electricity",message)

print("Stopped...")