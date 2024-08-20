#!/bin/bash
set -e
# Install Jupyter Notebook if not already installed
sudo -u ec2-user -i <<\'EOF\'
if ! command -v jupyter &> /dev/null
then
  pip install notebook
fi
EOF
# Download the notebook from S3
aws s3 cp s3://${S3Bucket}/${S3NotebookKey} /home/ec2-user/SageMaker/your-notebook-file.ipynb