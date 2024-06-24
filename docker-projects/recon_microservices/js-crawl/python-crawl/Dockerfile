# Use the official Python image as the base image
FROM python:slim      

# Install required system dependencies
RUN apt-get update && \
    apt-get install -y \
    libxml2-dev \
    libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

# Install required Python packages
RUN pip install waymore xnLinkFinder

# Set the working directory in the container
WORKDIR /output

# Copy the current directory contents into the container at /output
COPY . .

# Copy the config file to the ~/.config/waymore
RUN mkdir -p ~/.config/waymore && cp config.yml ~/.config/waymore

# Copy the entry point script into the container
COPY script.sh /output/script.sh

# Add execute permission to the entry point script
RUN chmod +x /output/script.sh

# Set the entry point to the script and pass arguments
ENTRYPOINT ["/output/script.sh"]
