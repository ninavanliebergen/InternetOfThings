FROM influxdb:2.0

# Expose port 8086 for InfluxDB API
EXPOSE 8086

# Copy over custom influxdb.conf file
COPY influxdb.conf /etc/influxdb/influxdb.conf
