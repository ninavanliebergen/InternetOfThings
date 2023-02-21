# Use the latest Alpine image as the base image
FROM eclipse-mosquitto:latest

# Install Mosquitto
RUN apk update && \
    apk add mosquitto && \
    apk add nano

# Configure Mosquitto
RUN sed -i 's/#listener 1883/listener 1883/g' /etc/mosquitto/mosquitto.conf && \
    echo "allow_anonymous true" >> /etc/mosquitto/mosquitto.conf

# Expose the MQTT port
EXPOSE 1883

# Start Mosquitto when the container launches
CMD ["/usr/sbin/mosquitto", "-c", "/etc/mosquitto/mosquitto.conf"]
