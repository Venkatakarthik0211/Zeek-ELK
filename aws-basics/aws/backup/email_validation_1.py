# Validating a Email Actually Exist

from validate_email import validate_email
import dns.resolver
import re

# Optimized function to check if an email is gibberish
def is_gibberish(email):
    local_part = email.split('@')[0]

    # Gibberish detection pattern with a combination of repetitive characters and random sequences
    gibberish_pattern = re.compile(
        r'^(?=.*[a-z])(?=.*[0-9])?(?!.*(.)\1{3,})[a-z0-9._%+-]{8,}$'
    )

    # Check if the local part is unusually long, which is common in gibberish emails
    if len(local_part) > 20:
        return True

    # Match against the pattern
    return not gibberish_pattern.match(local_part)

# Function to check DNS MX records directly
def has_mx_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        return True if answers else False
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return False

# Main function to validate email using validate_email
def validate_email_address(email):
    is_valid = validate_email(
        email_address=email,
        check_format=True,
        check_blacklist=False,
        check_dns=True,
        dns_timeout=10,
        check_smtp=True,
        smtp_timeout=10
    )

    if not is_valid:
        return f"Invalid email: {email}"

    domain = email.split('@')[1]
    # Check if the domain has MX records
    if not has_mx_record(domain):
        return f"Invalid email: No MX record found for domain {domain}"

    # Check if the email is gibberish
    if is_gibberish(email):
        return f"Email is likely gibberish: {email}"

    return f"Email is valid: {email}"

# Example usage
emails = [
    "valid.email@facebook.com",
    "shlediwbfvu199391@gmail.com",
    "euwiejfiwlekfogo@gmail.com",
    "invalid_email@nonexistentdomain.xyz",
    "sacredspirits47@gmail.in",
    "sacredspirits7@tempmail.com",
    "fjwifjwofnhtbbwwkckowlslakc@tempmail.com",
    "ActiveKBMass1@gmail.com",
    "1939194719abfmwofj_qufkqk@hotmail.com",
    "kqmail56@gmail.com",
    "kqmail56@gmail.in"
]

for email in emails:
    print(validate_email_address(email))