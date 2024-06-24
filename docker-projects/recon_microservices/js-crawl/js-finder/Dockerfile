# Use the go:alpine3.19 image as base
FROM golang:alpine3.19

# Install necessary packages
RUN apk update && apk add --no-cache curl jq git gcc musl-dev

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the current directory into the container
COPY . .

# Install jsluice
RUN go install github.com/BishopFox/jsluice/cmd/jsluice@latest

# Define entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
