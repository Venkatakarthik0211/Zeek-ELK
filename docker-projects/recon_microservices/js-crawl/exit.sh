#!/bin/bash

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Emojis
CHECK_MARK="✅"
CROSS_MARK="❌"

# Function to prompt for user input
prompt_yes_no() {
    while true; do
        echo -e "${1} ${GREEN}(y/n)${NC}: \c"
        read -r yn
        case $yn in
            [Yy]* ) return 0;;  # Yes
            [Nn]* ) return 1;;  # No
            * ) echo "Please answer ${GREEN}yes${NC} or ${RED}no${NC}.";;
        esac
    done
}

# Check if there are any containers
container_count=$(docker ps -q | wc -l)
if [ "$container_count" -eq 0 ]; then
    echo -e "${CROSS_MARK} No containers are currently running."
    containers_removed=true
else
    # Prompt user to remove all containers
    if prompt_yes_no "Do you want to ${RED}remove all containers${NC}?"; then
        docker rm -f $(docker ps -aq)  # Remove all containers
        containers_removed=true
    else
        echo -e "${CHECK_MARK} Containers will ${GREEN}not${NC} be removed."
        containers_removed=false
    fi
fi

# Check if there are any images
image_count=$(docker images -q | wc -l)
if [ "$image_count" -eq 0 ]; then
    echo -e "${CROSS_MARK} No images are currently available."
    images_removed=true
else
    # Prompt user to remove all images
    if prompt_yes_no "Do you want to ${RED}remove all images${NC}?"; then
        docker rmi -f $(docker images -q)  # Remove all images
        images_removed=true
    else
        echo -e "${CHECK_MARK} Images will ${GREEN}not${NC} be removed."
        images_removed=false
    fi
fi

# If both containers and images are removed, prune system
if [ "$containers_removed" = true ] && [ "$images_removed" = true ]; then
    if prompt_yes_no "Do you want to ${RED}prune the system${NC} (remove all unused data)?"; then
        docker system prune -a  # Prune system
    else
        echo -e "${CHECK_MARK} System will ${GREEN}not${NC} be pruned."
    fi
fi
