import json
import gspread

def lambda_handler(event, context):
    # Initialize Google Sheets client
    gc = gspread.service_account(filename='cred.json')
    gsheet = gc.open("Email Data").sheet1
    
    # Read data from Google Sheet
    data = read_data_from_google_sheet(gsheet)

    # Return data as JSON
    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }
    
def read_data_from_google_sheet(sheet):
    # Read all rows from the sheet
    rows = sheet.get_all_records()
    
    # Convert rows to a list of dictionaries
    data = [dict(row) for row in rows]

    return data
