# Get insight in your carbon emission footprint
#mosquitto, node-red, influxdb and grafana were run as orchestration containers on docker.
#mosquitto is running on port 1883, change the setting to suit your configuration.
#edit the server configuration for mosquitto and influxdb to suit your configuration

Motivation
The need to address the urgent issue of climate change is becoming increasingly critical. While governments worldwide are debating and implementing policies and agreements to tackle this challenge, it is essential to recognize the role of individuals in contributing towards this goal. However, people often find it difficult to understand how their daily activities impact the environment and what they can do to reduce their carbon footprint. In response to this challenge, we propose an innovative IoT solution that helps individuals monitor their carbon emissions and take action towards creating a more sustainable world.

The Project
This code provides a technical framework for an application that continuously measures the user's carbon footprint through the use of various sensors. In this project, the sensors are simulated, but one can connect its own sensors. The folling techniques are used:

- MQTT
- PAHO
- NODERED
- INFLUXDB
- GRAFANA
- PYTHON

How to start this project?
1. Clone the code
2. run: docker-compose up
3. open nodered: http://localhost:1880 
4. import the json flow to nodered
