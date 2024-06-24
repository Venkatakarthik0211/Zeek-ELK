#!/bin/bash

# Check if the directory argument is provided
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <directory> <pattern>"
    exit 1
fi

directory="$1"
pattern="$2"

# Create a directory to store the merged output files
merged_output_dir="filtered_output"
mkdir -p "$merged_output_dir"

# Loop through each file in the specified directory
for filename in "$directory"/*; do
    if [ -f "$filename" ]; then
        # Extract domain name from the filename
        domain_name=$(basename "$filename" | sed -n 's/^extracted_urls_\(.*\)\.txt$/\1/p')

        # Perform the desired operation using the extracted domain name
        httpx -mc 200,300,301 -l "$filename" > "${domain_name}_urls_active.txt" && rm "$filename"

        # Move the *_urls_active.txt files to the merged output directory
        mv "${domain_name}_urls_active.txt" "${merged_output_dir}/${domain_name}_urls_active.txt"
    fi
done
