#!/bin/bash

# Check if the output directory is provided as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <output_directory>"
    exit 1
fi

output_dir="$1"

# Check if the output directory exists
if [ ! -d "$output_dir" ]; then
    echo "Error: Output directory '$output_dir' not found!"
    exit 1
fi

# Check if domains.txt file exists
if [ ! -f "domains.txt" ]; then
    echo "Error: domains.txt file not found!"
    exit 1
fi

# Check if domain_files directory already exists
if [ ! -d "domain_files" ]; then
    mkdir -p domain_files
    echo "Created: domain_files directory"
fi

# Read each domain from domains.txt
while IFS= read -r domain; do
    # Use grep to extract URLs ending with .js from the output directory
    grep -hoE "https?://[^ ]+\.js" "$output_dir"/*.txt | sort -u  > "domain_files/extracted_urls_$domain.txt"
    echo "Extracted URLs from $output_dir for domain $domain"
done < domains.txt

# Check if the go-filter container is already running
if docker ps -a --format '{{.Names}}' | grep -q "go-filter"; then
    echo "Error: The go-filter container is already running!"
    exit 1
fi

# Run the go-filter container
docker run --name go-filter -v $(pwd)/domain_files:/mounted_dir go-filter:latest "/mounted_dir" "\.js$" && docker cp go-filter:/golang-js-filter/filtered_output "$(pwd)"
