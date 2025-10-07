# Use an official MongoDB image as a base
FROM mongo:7.0

# Add any custom configurations or scripts
COPY ./mongod.conf /etc/mongod.conf
COPY ./init-mongo.sh /docker-entrypoint-initdb.d/

# Expose the default MongoDB port
EXPOSE 27017

# Start MongoDB with the custom configuration
CMD ["mongod", "--config", "/etc/mongod.conf"]
