##########################################
# HOUSEHOLD - GAS PUBLISHER
# every few hours, the gas usage is pushed (IN Liters)
# normally, an average household uses 3,39 litres gas per person per day
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

client= paho.Client("gas")
client.on_publish = on_publish
client.connect(broker,port)

for i in range(20):
    d=random.randint(1,5)
    
 #telemetry to send 
    # message="Device 1 : Data " + str(i)
    message = random.randint(0,2)
    time.sleep(d)
    
 #publish message
    ret= client.publish("/household/gas",message)

print("Stopped...")