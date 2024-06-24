# Use Alpine Linux as base image
FROM alpine:latest

# Install required packages
RUN apk --no-cache add jq curl wget git grep

# Copy the script.sh file into the container
COPY script.sh /usr/local/bin/script.sh

# Give execute permissions to the script.sh file
RUN chmod +x /usr/local/bin/script.sh

# Set the script.sh file as the entrypoint
ENTRYPOINT ["/usr/local/bin/script.sh"]
