##########################################
# HOUSEHOLD - WATER PUBLISHER
# every few hours, the water usage is pushed (IN liter)
# normally, an average household uses 130 litres water per person per day
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

client= paho.Client("water")
client.on_publish = on_publish
client.connect(broker,port)

for i in range(20):
    d=random.randint(1,5)
    
 #telemetry to send 
    # message="Device 1 : Data " + str(i)
    message = random.randint(10,100)
    time.sleep(d)
    
 #publish message
    ret= client.publish("/household/water",message)

print("Stopped...")