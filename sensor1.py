##########################################
# PUBLISHER OF THE DIFFERENT SENSORS
# receives consumption, transforms it into amount of CO2 (kg)
# and publishes it on the corresponding channel
##############################################

#simulator device 1 for mqtt message publishing
import paho.mqtt.client as paho
import time
import random
import json

#hostname
broker="localhost"

#port
port=1884

def on_publish(client,userdata,result):
    print("Device 1 : Data published.")
    pass


# dict: {source: conversion_value, measurement, client, topic, range_start, range_end}
# using https://carbonfund.org/calculation-methods/ ans https://www.zaailingen.com/vliegtuig-op-vakantie-hoe-slecht-nou-eigenlijk/
# for conversion values
topics = {
    'electra': ['0.371', 'kWh', 'client_electra', '/household/electricity/co2', '0', '10'] ,
    'gas': ['1.8', 'liters', 'client_gas', '/household/gas/co2', '0', '2'] ,
    'water': ['0.0003', 'liters', 'client_water', '/household/water/co2', '20', '130'] ,

    'car': ['0.215', 'km', 'client_car', '/household/transport/car/co2', '30', '100'] ,
    'public': ['0.045', 'km', 'client_public', '/household/transport/bus/co2', '5', '10'] ,
    'air': ['0.270', 'km', 'client_air', '/household/transport/air/co2', '0', '200'] ,

    'waste': ['0.5', 'kg', 'client_waste', '/household/wastebin/co2', '0', '1'] ,
    'food': ['0.5', 'kg', 'client_food', '/household/food/co2', '0', '1'] ,
    # 'beef': ['27', 'kg','client_beef', '/food/beef', '0', '1'],
    # 'cheese': ['13.5', 'kg', 'client_cheese', '/food/cheese', '0', '1'],
    # 'chocolate': ['1', 'kg', 'client_chocolate', '/food/chocolate', '0', '1'],
    # 'coffee': ['0.28', 'pieces', 'client_coffee', '/food/coffee', '0', '1'],

    }

while True:

    d=random.randint(1,5)
    time.sleep(d)

    # randomly publish on one of the topics
    source = random.choice(list(topics))

    conversion_value = list(topics[source])[0]
    measurement = list(topics[source])[1]
    client = paho.Client(list(topics[source])[2])
    topic = list(topics[source])[3]
    range_start = list(topics[source])[4]
    range_end = list(topics[source])[5]

    value = random.randint(int(range_start), int(range_end))
    print(value)
    kgs = value * float(conversion_value)

    client.on_publish = on_publish
    client.connect(broker,port)

    #publish message
    ret= client.publish(topic,kgs)

print("Stopped...")