import json
import boto3
import os

sns_client = boto3.client('sns')

def lambda_handler(event, context):
    # Extract details from the event
    message = event.get('message', 'Hello from Lambda!')
    subject = event.get('subject', 'Lets shit start NLP')
    topic_arn = os.environ['SNS_TOPIC_ARN']
    
    # Publish the message to SNS
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject=subject
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to SNS topic!')
    }
