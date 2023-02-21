FROM nodered/node-red:2.0

# Install additional Node-RED nodes
RUN npm install node-red-contrib-influxdb

# Copy over custom settings.js file
COPY settings.js /data/settings.js
