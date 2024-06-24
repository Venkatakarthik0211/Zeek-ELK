#!/bin/bash

# Redirect stdout and stderr to /dev/null
exec > /dev/null 2>&1

# Function to build Dockerfile in a directory
build_dockerfile() {
    local directory="$1"
    local image_name=$(basename "$directory" | tr '[:upper:]' '[:lower:]') # Convert directory name to lowercase
    echo "Building Dockerfile in directory: $directory"
    docker build -t "$image_name" "$directory"
}

# Function to recursively search for Dockerfile and build
search_and_build() {
    local search_dir="$1"
    # Recursively search for Dockerfile
    while IFS= read -r -d '' file; do
        directory=$(dirname "$file")
        build_dockerfile "$directory" &
    done < <(find "$search_dir" -type f -name 'Dockerfile' -print0)
    wait
}

# Main function
main() {
    # Check if argument provided
    if [ $# -ne 1 ]; then
        echo "Usage: $0 <directory>"
        exit 1
    fi
    # Check if directory exists
    if [ ! -d "$1" ]; then
        echo "Error: Directory not found"
        exit 1
    fi
    # Search and build Dockerfiles
    search_and_build "$1"
    echo -e "\e[32mBuild completed successfully ✔️\e[0m"
    echo -e "\e[36mCrawling in progress... 🚀\e[0m"

}

# Run main function with provided directory
main "$@"

