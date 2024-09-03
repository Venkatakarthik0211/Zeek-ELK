import pandas as pd
import re
import gspread
import dns.resolver
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