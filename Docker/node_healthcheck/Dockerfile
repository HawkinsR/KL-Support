FROM node:alpine

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000


# The HEALTHCHECK instruction in a Dockerfile is used to specify a test that will be run periodically to determine if the container is healthy. If the test is successful, the container will be considered healthy. If the test fails, the container will be considered unhealthy.
# Health checks are useful for ensuring that your containers are always running and available. They can also be used to detect problems with your containers early on, before they cause any major issues.
# There are a few different types of health checks that you can perform in a Dockerfile. The most common type of health check is a simple command that is run periodically. For example, you could use a health check to check the status of a process in the container or to check if a file exists.
# Another type of health check is a readiness probe. A readiness probe is similar to a health check, but it is used to determine if the container is ready to receive traffic. For example, you could use a readiness probe to check if a database is ready to accept connections.
# Finally, you can also use a liveness probe. A liveness probe is used to determine if the container is still alive. For example, you could use a liveness probe to check if the container is responding to ping requests.

# HEALTHCHECK NONE
# HEALTHCHECK CMD curl --fail http://localhost:3000/kill || exit 1
# HEALTHCHECK --interval=30s --timeout=15s --start-period=45s --retries=3 CMD node healthcheck.js

# Interval - specifies the time between the health check for the application container. it waits for the specified time from one check to another.
# Timeout - specifies the time that the health check waits for a response to consider the status of the container. For example, if we define 30 seconds and our server doesn’t respond within 30 seconds, then it’s considered as failed.
# Start-period - specifies the number of seconds the container needs to start; health check will wait for that time to start.
# Retries - specifies the number of consecutive health check failures required to declare the container status as unhealthy. Health check will only try up to the specified retry number. If the server fails consecutively up to the specified times, it is then considered unhealthy.


CMD ["node","app.js"]
