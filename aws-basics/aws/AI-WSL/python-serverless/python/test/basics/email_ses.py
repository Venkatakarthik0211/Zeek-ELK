import boto3, os, json

from_email = os.getenv('FROM_EMAIL')
to_email = os.getenv('TO_EMAIL')

client = boto3.client('ses')

def lambda_handler(event,context): 

    print("Received event: " + json.dumps(event))
    ses.send_email(
        source=from_email, 
        Destination={'ToAddresses': [to_email]}, 
        Message={'Subject': {'Data': 'AI is Generating Prompt....'}, 
                 'Body': {'Text': {'Data': 'This is a test email'} }})
    return {
        'statusCode': 200,
        'body': json.dumps('Email sent!')
    }