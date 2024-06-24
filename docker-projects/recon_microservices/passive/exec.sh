#!/bin/bash

# Check if Docker is installed
if ! command -v docker &> /dev/null
then
    echo "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null
then
    echo "Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "Both Docker and Docker Compose are installed."

# Check if user has permission to run docker ps
if docker ps &>/dev/null; then
    echo "User has permission to run docker commands."
else
    # Try to create docker group and add current user to docker group
    echo "User does not have permission to run docker commands. Trying to rectify..."

    # Check if docker group already exists
    if grep -q "^docker:" /etc/group; then
        echo "Docker group already exists."
    else
        # Create docker group if it doesn't exist
        sudo groupadd docker
        echo "Docker group created."
    fi

    # Add current user to docker group
    sudo usermod -aG docker $USER

    echo "User added to docker group."
    echo "Please log out and log back in for changes to take effect."
    exit 1
fi


