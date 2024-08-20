import imaplib
import email
import yaml 
import csv 

# Load credentials from YAML file
with open("credentials.yml") as f:
    content = f.read()
my_credentials = yaml.load(content, Loader=yaml.FullLoader)
user, password = my_credentials["user"], my_credentials["password"]

# IMAP connection URL
imap_url = 'imap.gmail.com'

# Connect to Gmail using SSL
my_mail = imaplib.IMAP4_SSL(imap_url)

# Log in with credentials
my_mail.login(user, password)

# select inbox, spam 

# # Select the Inbox to fetch messages
# my_mail.select('Inbox')

# # Define search criteria
# key = 'FROM'
# value = 'kdraksharam@yahoo.com'
# status, data = my_mail.search(None, key, value)

# # List of email IDs to fetch
# mail_id_list = data[0].split()

# # Initialize list to hold messages
# msgs = []

# # Fetch emails
# for num in mail_id_list:
#     typ, data = my_mail.fetch(num, '(RFC822)')
#     msgs.append(data)

# # Process and print emails
# for msg in msgs[::-1]:
#     for response_part in msg:
#         if isinstance(response_part, tuple):
#             my_msg = email.message_from_bytes(response_part[1])
#             print("_________________________________________")
#             print("Subject:", my_msg['subject'])
#             print("From:", my_msg['from'])
#             print("Body:")
#             for part in my_msg.walk():
#                 if part.get_content_type() == 'text/plain':
#                     print(part.get_payload(decode=True).decode())

# Split the subject, from and body of the email and write to a CSV file
# with open("email_data.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Subject", "From", "Body"])
#     for msg in msgs[::-1]:
#         for response_part in msg:
#             if isinstance(response_part, tuple):
#                 my_msg = email.message_from_bytes(response_part[1])
#                 subject = my_msg['subject']
#                 sender = my_msg['from']
#                 body = ""
#                 for part in my_msg.walk():
#                     if part.get_content_type() == 'text/plain':
#                         body = part.get_payload(decode=True).decode()
#                 writer.writerow([subject, sender, body])

# # fetch the data from email_Data.csv file and print only subject and from
# with open("email_data.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row[0], row[1])