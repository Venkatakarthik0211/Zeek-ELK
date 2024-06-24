#!/bin/bash

# Function to execute a script and display logs in case of failure
execute_script() {
    local script="$1"
    local script_name="$(basename "$script")"

    echo "Executing $script_name..."
    # Execute the script
    chmod +x "$script"
    ./"$script"

    # Check the exit status of the script
    if [ $? -ne 0 ]; then
        echo "Error: $script_name failed!"
        echo "Showing logs where the execution failed:"
        grep -nE "ERROR|Failed|Exception" "${script_name%.*}.log" || echo "No error logs found."
        exit 1
    fi
    echo "$script_name executed successfully."
}

# Main script
echo "Checking exec.sh..."
execute_script exec.sh

echo "Checking passive-subdomains.sh..."
execute_script passive-subdomains.sh

echo "Checking passive-filterating.sh..."
execute_script passive-filterating.sh

echo "Checking prepare-subdomain-wordlist.sh..."
execute_script prepare-subdomain-wordlist.sh

echo "All scripts executed successfully."
