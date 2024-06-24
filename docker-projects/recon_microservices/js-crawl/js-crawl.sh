#!/bin/bash

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Check if domains.txt exists
if [ ! -f "domains.txt" ]; then
    echo -e "${RED}Error:${NC} domains.txt file not found."
    exit 1
fi

# Read domains from domains.txt file into an array
mapfile -t domains < "domains.txt"

# Function to ensure Docker images are available locally
ensure_images_exist() {
    for image in "$@"; do
        if docker inspect "$image" &>/dev/null; then
            echo -e "Image ${GREEN}$image${NC} is already present locally."
        else
            echo -e "Image ${RED}$image${NC} is not present locally. Pulling..."
            docker pull "$image"
            [ $? -eq 0 ] && echo -e "Image ${GREEN}$image${NC} pulled successfully." || { echo -e "${RED}Error:${NC} Failed to pull image $image. Please check and try again."; exit 1; }
        fi
    done
    echo "All required images are present locally."
}

# Function to run Docker containers in parallel and save output
run_containers_and_save_output() {
    local output_dir="$1"
    shift
    for container in "$@"; do
        IFS=' ' read -r -a parts <<< "$container"
        image_name="${parts[0]}"
        arguments="${parts[@]:1}"
        for domain in "${domains[@]}"; do
            timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
            mkdir -p "$output_dir"
            docker run "$image_name" $arguments $domain > "${output_dir}/${image_name//\//-}_${domain}_${timestamp}.txt" 2>&1 &
        done
    done
    wait
    echo "All Docker containers have finished running."
}

# Define the list of Docker images
images=(
    "golang:alpine3.19"
    "python:alpine3.19"
    "sxcurity/gau:latest"
    "projectdiscovery/katana"
    "kqmail56/wayback-machine:latest"
)

# Define the list of Docker containers to run
containers=(
    "projectdiscovery/katana -no-color -system-chrome -depth 10 -headers 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36' -js-crawl -concurrency 80 -crawl-duration 50 -u"
    "sxcurity/gau:latest --subs"
    "kqmail56/wayback-machine:latest"
    "go-crawl:latest"
)

# Ensure Docker images are available locally
echo -e "${GREEN}Ensuring Docker images are available locally...${NC}"
ensure_images_exist "${images[@]}"

echo -e "${GREEN}Required images have been available locally. Starting the building process if there are any in respective directories...${NC}"
chmod +x build.sh
./build.sh .

# Run Docker containers in parallel and save output
output_dir="output_$(date +"%Y-%m-%d_%H-%M-%S")"
echo -e "${GREEN}Running Docker containers in parallel and saving output to ${output_dir}...${NC}"
run_containers_and_save_output "$output_dir" "${containers[@]}"

# Waymore + xnLinkFinder
echo -e "${GREEN}Running waymore + xnLinkFinder...${NC}"
chmod +x python-crawl-support.sh && ./python-crawl-support.sh
mv wm_xn/ "$output_dir"

echo -e "${GREEN}Let's find out active urls.............${NC}"
chmod +x active-urls.sh && ./active-urls.sh "$output_dir"
echo -e "${GREEN}Gotch!!!!!a Let's scrape everything.............${NC}"

echo -e "${GREEN}Scraping is in process.............${NC}"
docker run -it --name js-finder -v "$(pwd)/filtered_output:/app/filtered_output" js-finder:latest && docker wait js-finder && docker cp js-finder:/app/scraped_content "$(pwd)/scraped_content"
echo -e "${GREEN}Shell execution is done successfully.............${NC}"

echo -e "${GREEN}Performing cleanup......${NC}"
chmod +x exit.sh && ./exit.sh
