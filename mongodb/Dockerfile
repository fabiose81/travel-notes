# Use an official MongoDB image as a base
FROM mongo:7.0

# Set environment variables
ARG DATABASE
ENV MONGO_INITDB_DATABASE=$DATABASE

# Expose MongoDB port
EXPOSE 27017

# Optional: define default command (MongoDB image already has one)
CMD ["mongod"]
