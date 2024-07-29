#!/bin/bash -xe

# For Debugging purposes, use the following command to view the logs: cat /var/log/cloud-init-output.log
# Debug ApACHE: sudo tail -f /var/log/apache2/error.log
# Update package lists 
sudo apt-get update -y

# Install necessary packages
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    python3-venv \
    python3-pip \
    git \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    libmysqlclient-dev \
    awscli \
    mysql-client \
    apache2 \
    nfs-common \
    libapache2-mod-wsgi-py3 \
    mysql-server

# Enable and start MySQL service
sudo systemctl enable mysql
sudo systemctl start mysql
sudo systemctl status mysql

# Clone the repository
cd ~
git clone https://github.com/Venkatakarthik0211/testrepo.git

# Export the current directory into s bash variable
export CURRENT_DIR=$(pwd)

# Change directory to the project folder
cd $CURRENT_DIR/testrepo/three-tier/python/test

# Install requirements for WSIG and Flask
pip3 install -r requirements.txt


# Fetch parameters from AWS SSM Parameter Store
export DBPassword=$(aws ssm get-parameters --region us-east-1 --names /P4L/Python/DBPassword --with-decryption --query 'Parameters[0].Value' --output text)
export DBRootPassword=$(aws ssm get-parameters --region us-east-1 --names /P4L/Python/DBRootPassword --with-decryption --query 'Parameters[0].Value' --output text)
export DBUser=$(aws ssm get-parameters --region us-east-1 --names /P4L/Python/DBUser --query 'Parameters[0].Value' --output text)
export DBName=$(aws ssm get-parameters --region us-east-1 --names /P4L/Python/DBName --query 'Parameters[0].Value' --output text)
export DBEndpoint=$(aws ssm get-parameters --region us-east-1 --names /P4L/Python/DBEndpoint --query 'Parameters[0].Value' --output text)
export EFS_ID=$(aws ssm get-parameters --region us-east-1 --names /P4L/Python/EFS_ID --query 'Parameters[0].Value' --output text)
export EFS_DNS=$(aws ssm get-parameters --region us-east-1 --names /P4L/Python/EFS_DNS --query 'Parameters[0].Value' --output text)
export ALB_DNS=$(aws ssm get-parameters --region us-east-1 --names /P4L/Python/ALB_DNS --query 'Parameters[0].Value' --output text)

# Get the public IP of the server
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
SERVER_IP=$(curl http://169.254.169.254/latest/meta-data/public-ipv4 -H "X-aws-ec2-metadata-token: $TOKEN")

# Create the database and table
echo "GRANT ALL PRIVILEGES ON $DBName.* TO '$DBUser'@'%';" | mysql -h $DBEndpoint -u $DBUser --password=$DBPassword
echo "FLUSH PRIVILEGES;" | mysql -h $DBEndpoint -u $DBUser --password=$DBPassword
echo "USE $DBName; CREATE TABLE IF NOT EXISTS planet (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL UNIQUE, distance INT NOT NULL, radius INT NOT NULL, mass INT NOT NULL);" | mysql -h $DBEndpoint -u $DBUser --password=$DBPassword
echo "USE $DBName; INSERT INTO planet (name, distance, radius, mass) SELECT * FROM (SELECT 'Earth', 149600000, 6371, 5972) AS tmp WHERE NOT EXISTS (SELECT name FROM planet WHERE name = 'Earth') LIMIT 1;" | mysql -h $DBEndpoint -u $DBUser --password=$DBPassword

# Setup Python virtual environment and install requirements
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Enable and start Apache service
sudo systemctl enable apache2
sudo systemctl start apache2
sudo systemctl status apache2

# Enable WSGI module
sudo a2enmod wsgi

sudo tee /etc/apache2/sites-available/flaskapp.conf > /dev/null <<EOF
<VirtualHost *:80>
    ServerName $ALB_DNS
    ServerAdmin youremail@example.com
    WSGIScriptAlias / $CURRENT_DIR/testrepo/three-tier/python/test/flaskapp.wsgi
    <Directory $CURRENT_DIR/testrepo/three-tier/python/test/>
        Require all granted
    </Directory>
    Alias /static $CURRENT_DIR/testrepo/three-tier/python/test/static
    <Directory $CURRENT_DIR/testrepo/three-tier/python/test/static/>
        Require all granted
    </Directory>
    ErrorLog \${APACHE_LOG_DIR}/error.log
    LogLevel warn
    CustomLog \${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
EOF

# Write the WSGI file
sudo tee $CURRENT_DIR/testrepo/three-tier/python/test/flaskapp.wsgi > /dev/null <<EOF
import sys
import logging
import os 

# Add the variables to the wsgi environment
os.environ['DBPassword'] = '$DBPassword'
os.environ['DBUser'] = '$DBUser'
os.environ['DBName'] = '$DBName'
os.environ['DBEndpoint'] = '$DBEndpoint'
os.environ['ALB_DNS'] = '$ALB_DNS'

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "$CURRENT_DIR/testrepo/three-tier/python/test")
from app import app as application
EOF

# Set directory permissions
sudo chmod +x $CURRENT_DIR
sudo chmod +x $CURRENT_DIR/testrepo
sudo chmod +x $CURRENT_DIR/testrepo/three-tier
sudo chmod +x $CURRENT_DIR/testrepo/three-tier/python
sudo chmod +x $CURRENT_DIR/testrepo/three-tier/python/test

# Enable the new site and restart Apache
sudo a2ensite flaskapp.conf
sudo systemctl restart apache2

# Backup the database
mysqldump -h $DBEndpoint -u $DBUser --password=$DBPassword $DBName > $CURRENT_DIR/$DBName.sql
sudo systemctl stop mysql

# Log script completion
echo "Setup script completed" | sudo tee /var/log/user-data.log

# Move static content temporarily
sudo mv $CURRENT_DIR/testrepo/three-tier/python/test/static /tmp
cd $CURRENT_DIR/testrepo/three-tier/python/test && mkdir -p static
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport $EFS_DNS:/ /$CURRENT_DIR/testrepo/three-tier/python/test/static
sudo cp -r /tmp/static/* $CURRENT_DIR/testrepo/three-tier/python/test/static
sudo chown -R $USER:$USER $CURRENT_DIR/testrepo/three-tier/python/test/static