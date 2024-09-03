import pandas as pd
import re
import gspread
import dns.resolver
from google.colab import drive
drive.mount('/content/drive')
from validate_email import validate_email
from multiprocessing import Pool

def read_data_from_google_sheet(sheet):
    """Fetch all data from the Google Sheet and return as DataFrame."""
    data = sheet.get_all_records()
    return pd.DataFrame(data)

def extract_email(email_str):
    """Extract the email address from a string that may contain a name."""
    email_regex = r'<([^<>]+)>|([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
    match = re.search(email_regex, email_str)
    if match:
        return match.group(1) or match.group(2)
    return None

def process_emails(df):
    """Process the DataFrame to extract email addresses from the 'Sender' column."""
    df['Sender'] = df['Sender'].apply(extract_email)
    return df

def check_email_format(email):
    """Check if the email format is valid."""
    return validate_email(email_address=email, check_format=True, check_blacklist=True, check_dns=True, check_smtp=True)

def check_email_domain(email):
    """Check if the domain part of the email is valid."""
    domain = email.split('@')[1]
    return re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', domain)

def has_dns_records(domain):
    """Check if DNS records exist for the domain."""
    try:
        dns.resolver.resolve(domain, 'A')
        return True
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        return False

def has_mx_record(domain):
    """Check if the domain has MX records."""
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        return bool(answers)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        return False

def is_gibberish(email):
    """Check if the email is gibberish."""
    if not email:
        return False
    local_part = email.split('@')[0]
    gibberish_pattern = re.compile(r'^[a-zA-Z0-9._%+-]{8,}$')  # Simplified pattern
    return len(local_part) > 20 or not gibberish_pattern.match(local_part)

def is_spam(email):
    """Check if the email is likely spam based on specific patterns."""
    if not email:
        return False
    local_part = email.split('@')[0]
    spam_patterns = re.compile(r'(do-not-reply|notify|alert|no-reply|noreply)', re.IGNORECASE)
    return bool(spam_patterns.search(local_part))

def validate_email_address(email):
    """Validate the email address step by step and categorize."""
    if not email:
        return "Invalid Email - No Address Provided"

    if not check_email_format(email) or not check_email_domain(email):
        return "Basic Validations Failed"

    domain = email.split('@')[1]

    if not has_dns_records(domain) or not has_mx_record(domain):
        return "Basic Validations Failed"

    if is_spam(email):
        return "Valid Domains - Likely Notification Email"

    if is_gibberish(email):
        return "Valid Domains - Likely Gibberish"

    return "Valid Email - Possibly Personal or Corporate Email"

def process_email_validation(email):
    """Wrapper function for multiprocessing."""
    return email, validate_email_address(email)

# Initialize Google Sheets client
gc = gspread.service_account(filename='cred.json')
gsheet = gc.open("Email Data").get_worksheet(1)

# Read data from Google Sheet
df = read_data_from_google_sheet(gsheet)

# Process the DataFrame to extract email addresses
df = process_emails(df)

# Get unique email addresses
unique_emails = df['Sender'].dropna().unique()

# Use multiprocessing to speed up validation
with Pool() as pool:
    validation_results = dict(pool.map(process_email_validation, unique_emails))

# Map the validation results back to the DataFrame
df['Sender_Validation'] = df['Sender'].map(validation_results)


# Writing a function to validate any url present in the cells of Body column, if no url is present then skip the cell 
# and if url is present then validate the url using the regular expression and return the result as Valid or Invalid
# Using Refex: (https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?\/[a-zA-Z0-9]{2,}|((https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?)|(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})?

# def extract_and_validate_urls(text):
#     """Extract and validate URLs from a block of text using a regular expression."""
    
#     # Updated URL pattern
#     url_pattern = re.compile(
#         r'(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?\/[a-zA-Z0-9]{2,}|((https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?)|(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})?'
#     )
    
#     # Find all matches using finditer which returns an iterator over match objects
#     matches = url_pattern.finditer(text)
    
#     # Use a set to avoid duplicates
#     valid_urls = {match.group() for match in matches}
    
#     # Convert set to list for final output
#     return list(valid_urls)

# # For each body n the DataFrame, extract and validate URLs
# df['Valid_URLs'] = df['Body'].apply(extract_and_validate_urls)


# Save the csv file to drive
# df.to_csv('/content/drive/My Drive/email_validation_results.csv', index=False)

def extract_and_validate_urls(text):
    """Extract and validate URLs from a block of text using a regular expression."""
    
    # Updated URL pattern
    url_pattern = re.compile(
        r'(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9\-\.]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?\/[a-zA-Z0-9\-\.\/?&=]*|((https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9\-\.]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?)|(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9\-\.]{2,}\.[a-zA-Z0-9\-\.]{2,}(\.[a-zA-Z0-9\-\.]{2,})?'
    )
    
    # Find all matches using finditer which returns an iterator over match objects
    matches = url_pattern.finditer(text)
    
    # Use a set to avoid duplicates
    valid_urls = {match.group() for match in matches}
    
    # Call the function to check the file extensions
    validate_url_file_extensions = check_file_extensions(valid_urls)

    return validate_url_file_extensions

def check_file_extensions(valid_urls):
    """Check if the URLs contain any file extensions."""

    # Regular expression to match file extensions
    file_extension_pattern = re.compile(r'\.(exe|bat|cmd|msi|scr|com|pif|js|vbs|ps1|sh|php|pl|py|docx?|xlsx?|pptx?|rtf|pdf|zip|rar|7z|tar|gz|jpe?g|png|gif|mp3|mp4|html?|xml|css|json|lnk|iso|dll|ocx|reg|hta|wsf|jar)$')

    # Initialize empty dictionaries to store the results
    possibly_dangerous = {}
    possible_macro_virus = {}
    potentially_malicious = {}

    # Iterate over each URL
    for url in valid_urls:
        # Check if the URL contains a file extension
        match = file_extension_pattern.search(url)
        if match:
            # Get the file extension
            extension = match.group(1).lower()

            # Check the file extension category
            if extension in ['exe', 'bat', 'cmd', 'msi', 'scr', 'com', 'pif', 'js', 'vbs', 'ps1', 'sh']:
                possibly_dangerous[url] = extension
            elif extension in ['docx', 'doc', 'xlsx', 'xls', 'pptx', 'ppt', 'rtf', 'pdf', 'zip', 'rar', '7z', 'tar', 'gz', 'jpeg', 'jpg', 'png', 'gif', 'mp3', 'mp4']:
                possible_macro_virus[url] = extension
            else:
                potentially_malicious[url] = extension

    return {
        'possibly_dangerous': possibly_dangerous,
        'possible_macro_virus': possible_macro_virus,
        'potentially_malicious': potentially_malicious
    }

# For each body in the DataFrame, extract and validate URLs
df['Valid_URLs'] = df['Body'].apply(extract_and_validate_urls)
    
# print the first 5 rows of the column Valid_URLs
print(df['Valid_URLs'].head(5))

# Write a function, Which categorizes if it is spam or not based on Sender_Validation column
# If the email is Basic Validations Failed then it is spam
# If the email is Valid Domains - Likely Gibberish then it is Possible Spam
# If the email is Possibly Personal or Corporate Email then it is not spam - Contine to URK validation(Use Valid URLS for nested test condition)
# If email domain is Basic Validations Failed or url is possibly_dangerous then it is potentially phishing
# If email domain Possibly Personal or Corporate Email or Valid Domains - Likely Gibberish and url is possible macro virus then it is Possible Manipulation
# If email domain Possibly Personal or Corporate Email or Valid Domains - Likely Gibberish is possibly malicious then it is Possibly Malicious
# If email domain is Possibly Personal or Corporate Email and no url is present it is safe
# Mark the values: Safe - 1, Spam - -1/2, phising - -1, manipulation/malicious - 0





