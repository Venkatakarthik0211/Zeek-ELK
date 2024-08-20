# Use the AWS Lambda Python 3.9 base image
FROM public.ecr.aws/lambda/python:3.9

# Setting S3 Environment Variables
ENV S3_BUCKET=nlpaccess2020
ENV S3_FILE=1342-0.txt

# Copy requirements.txt to the Lambda task root
COPY requirements.txt ${LAMBDA_TASK_ROOT}/

# Install the Python packages specified in requirements.txt
RUN pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt

# Pre-download NLTK data
RUN python -m nltk.downloader punkt -d /opt/nltk_data

# Copy the function code into the Lambda task root
COPY token_lambda.py ${LAMBDA_TASK_ROOT}/

# Set the CMD to the handler function in your Lambda code
CMD [ "token_lambda.handler" ]
