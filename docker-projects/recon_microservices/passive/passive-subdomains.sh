#!/bin/bash

# Check if domains.txt exists
if [ ! -f "domains.txt" ]; then
    echo "domains.txt file not found."
    exit 1
fi

# Read domains from domains.txt file into an array
mapfile -t domains < "domains.txt"

# Function to ensure Docker images are available locally
ensure_images_exist() {
    for image in "$@"; do
        if docker inspect "$image" &>/dev/null; then
            echo "Image $image is already present locally."
        else
            echo "Image $image is not present locally. Pulling..."
            docker pull "$image"
            [ $? -eq 0 ] && echo "Image $image pulled successfully." || { echo "Failed to pull image $image. Please check and try again."; exit 1; }
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
    "edu4rdshl/findomain:latest"
    "kqmail56/assetfinder:gov1"
    "projectdiscovery/subfinder:latest"
    "kqmail56/subdomain-fetcher:latest"
)

# Define the list of Docker containers to run
containers=(
    "edu4rdshl/findomain:latest -t"
    "kqmail56/assetfinder:gov1 --subs-only"
    "projectdiscovery/subfinder:latest -d"
    "kqmail56/subdomain-fetcher "
)

# Ensure Docker images are available locally
ensure_images_exist "${images[@]}"

# Run Docker containers in parallel and save output
output_dir="output_$(date +"%Y-%m-%d_%H-%M-%S")"
run_containers_and_save_output "$output_dir" "${containers[@]}"

# filteration
find $output_dir -type f -exec cat {} + | sort -n | uniq | tee output-passive.txt
# cat output.txt | grep '\.upwork\.com$' > output-passive.txt && rm output.txt

