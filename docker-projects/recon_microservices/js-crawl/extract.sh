#!/bin/bash

# Define the directory to save the output
output_directory="scraped_content"

# Create the output directory if it doesn't exist
mkdir -p "$output_directory"

# Loop through each active URLs file
for active_urls_file in filtered_output/*_urls_active.txt; do
    # Extract the domain name from the active URLs file name
    domain_name=$(basename "$active_urls_file" | sed 's/_urls_active.txt$//')

    # Create a directory for the domain within the output directory
    domain_output_directory="$output_directory/$domain_name"
    mkdir -p "$domain_output_directory"

    # Define the output directory for modified files within the domain directory
    domain_output_directory_modified="$domain_output_directory/modified"
    mkdir -p "$domain_output_directory_modified"

    # Loop through each URL in the active URLs file
    while IFS= read -r url; do
        # Get the filename from the URL
        filename=$(basename "$url")

        # Perform curl -k on the URL and save the output to the output directory
        curl -k "$url" -o "$domain_output_directory/$filename"

        # Modify the file using jsluice
        jsluice format "$domain_output_directory/$filename" > "$domain_output_directory_modified/$filename"

        # Remove the original file
        rm "$domain_output_directory/$filename"

    done < "$active_urls_file"

    # Define the output text files within the domain directory
    output_file="$domain_output_directory/extracted-urls.txt"
    secret_file="$domain_output_directory/extracted-secrets.txt"

    # Loop through each file in the modified output directory within the domain directory
    for file in "$domain_output_directory_modified"/*; do
        # Execute jsluice on the file, pipe output through jq, and append to output text file
        jsluice urls "$file" -I -S | jq . >> "$output_file"
        jsluice secrets "$file" -I -S | jq . >> "$secret_file"
    done
done
