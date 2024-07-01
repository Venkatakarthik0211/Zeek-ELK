import boto3
import json

FROM_EMAIL_ADDRESS = 'sender_Email'

ses = boto3.client('ses')

def lambda_handler(event, context):
    try:
        payload = event.get('Payload')
        if not payload:
            raise KeyError("Payload key not found in event.")
        
        input_data = payload.get('Input')
        if not input_data:
            raise KeyError("Input key not found in Payload.")
        
        email = input_data.get('email')
        message = input_data.get('message')
        if not email or not message:
            raise KeyError("The event dictionary does not contain the required keys 'email' and 'message'.")
        
        # Send email using Amazon SES
        ses.send_email(
            Source=FROM_EMAIL_ADDRESS,
            Destination={'ToAddresses': [email]},
            Message={
                'Subject': {'Data': 'Whiskers Commands You to attend!'},
                'Body': {'Text': {'Data': message}}
            }
        )
        return 'Success!'
    except KeyError as e:
        print(f"KeyError: {str(e)}")
        raise e
    except Exception as e:
        print(f"Unhandled exception: {str(e)}")
        raise e
