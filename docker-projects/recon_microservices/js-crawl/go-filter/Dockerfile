# Use golang:alpine3.19 as base image
FROM golang:alpine3.19

# Install necessary packages
RUN apk add --no-cache curl jq

# Install required Go tools
RUN go install github.com/tomnomnom/unfurl@latest && \
    go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest

# Create a directory for storing outputs
RUN mkdir /golang-js-filter

# Set working directory
WORKDIR /golang-js-filter

# Copy the script file into the container
COPY script.sh .

# Make the script executable
RUN chmod +x script.sh

# Set the entry point to the script
ENTRYPOINT ["/bin/sh","/golang-js-filter/script.sh"]
