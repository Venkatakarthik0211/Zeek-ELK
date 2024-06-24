# Use golang:alpine3.19 as base image
FROM golang:alpine3.19

# Install necessary packages
RUN apk add --no-cache curl jq

# Install required Go tools
RUN go install github.com/tomnomnom/waybackurls@latest \
    && go install github.com/jaeles-project/gospider@latest \ 
    && go install github.com/hakluke/hakrawler@latest

# Create a directory for storing outputs
RUN mkdir /golang-js-crawl

# Set working directory
WORKDIR /golang-js-crawl

# Copy the script file into the container
COPY script.sh .

# Make the script executable
RUN chmod +x script.sh

# Set the entry point to the script
ENTRYPOINT ["./script.sh"]
