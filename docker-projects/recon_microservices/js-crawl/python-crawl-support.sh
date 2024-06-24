#!/bin/bash
# Redirect stdout and stderr to /dev/null
#exec > /dev/null 2>&1

# Read domains from domains.txt file into an array
mapfile -t domains < "domains.txt"

# Define the main output directory
main_output_dir="wm_xn"

# Iterate over each domain and start a container for each one
for domain in "${domains[@]}"; do
    # Create a separate directory for each domain within the main output directory
    output_dir="$main_output_dir/$domain"
    mkdir -p "$output_dir"
    # Construct the command to be executed within the Docker container
    command_to_execute="./script.sh $domain"
    # Run the Docker container, execute the command, and copy the output directory
    docker run -it --name python-crawl-"$domain" --entrypoint /bin/sh python-crawl:latest -c "$command_to_execute" && docker cp python-crawl-"$domain":/output "$(pwd)/$output_dir" && docker rm python-crawl-"$domain"
done

# Wait for all containers to finish
wait

