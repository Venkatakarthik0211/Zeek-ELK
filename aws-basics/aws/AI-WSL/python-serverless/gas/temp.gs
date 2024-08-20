function checkAndProcessEmails() {
  const spreadsheetId = '13JYwb7nktTbt3kkSdsPeOBmY97Y2Otg22Pt9HxJTZAg'; // Corrected ID
  const spreadsheet = SpreadsheetApp.openById(spreadsheetId);
  const sheet = spreadsheet.getSheetByName("Sheet1");
  
  // Check if the sheet is empty
  const data = sheet.getDataRange().getValues();
  const isEmpty = data.length <= 1; // Only the header row exists
  
  if (isEmpty) {
    Logger.log("Sheet is empty. Initializing email data...");
    initializeEmailData(); // Retrieve all emails if the sheet is empty
  } else {
    Logger.log("Sheet is not empty. Appending new emails...");
    appendNewEmails(); // Append new emails if the sheet is not empty
  }
}

function initializeEmailData() {
  const spreadsheetId = '13JYwb7nktTbt3kkSdsPeOBmY97Y2Otg22Pt9HxJTZAg'; // Corrected ID
  const spreadsheet = SpreadsheetApp.openById(spreadsheetId);
  const sheet = spreadsheet.getSheetByName("Sheet1");
  
  // Add header row if not already present
  const data = sheet.getDataRange().getValues();
  if (data.length === 0) {
    sheet.appendRow(["Subject", "Sender", "Date", "Recipients", "CC", "BCC", "Message ID", "Body"]); 
  }

  const batchSize = 100; // Adjust the batch size according to your needs
  let start = 0;
  let threads;

  do {
    threads = GmailApp.search("label:all", start, batchSize); // Process emails in batches
    threads.forEach(thread => {
      const messages = thread.getMessages();
      messages.forEach(message => {
        const subject = message.getSubject();
        const sender = message.getFrom();
        const date = message.getDate();
        const recipients = message.getTo();
        const cc = message.getCc();
        const bcc = message.getBcc();
        const messageId = message.getId();
        const body = message.getPlainBody();

        // Append email details to the sheet
        sheet.appendRow([subject, sender, date, recipients, cc, bcc, messageId, body]);
      });
    });
    start += batchSize; // Move to the next batch
  } while (threads.length > 0);

  Logger.log("All emails saved to Google Sheets in batches.");
}

function appendNewEmails() {
  const spreadsheetId = '13JYwb7nktTbt3kkSdsPeOBmY97Y2Otg22Pt9HxJTZAg'; // Corrected ID
  const spreadsheet = SpreadsheetApp.openById(spreadsheetId);
  const sheet = spreadsheet.getSheetByName("Sheet1");
  const lastRow = sheet.getLastRow();
  const lastProcessedTime = lastRow > 1 ? new Date(sheet.getRange(lastRow, 3).getValue()) : new Date(0); // Get the last processed time from the date column

  const batchSize = 100; // Adjust the batch size according to your needs
  const threads = GmailApp.search("label:all after:" + Math.floor(lastProcessedTime.getTime() / 1000)); // Search for emails received after the last processed time

  if (threads.length === 0) {
    Logger.log("No new emails found.");
    return;
  }

  threads.forEach(thread => {
    const messages = thread.getMessages();
    messages.forEach(message => {
      const subject = message.getSubject();
      const sender = message.getFrom();
      const date = message.getDate();
      const recipients = message.getTo();
      const cc = message.getCc();
      const bcc = message.getBcc();
      const messageId = message.getId();
      const body = message.getPlainBody();

      // Append email details to the sheet
      sheet.appendRow([subject, sender, date, recipients, cc, bcc, messageId, body]);
    });
  });

  Logger.log("New emails appended to Google Sheets.");
}

// Call this function to set up initial and periodic triggers
function setupTriggers() {
  // Remove existing triggers
  const existingTriggers = ScriptApp.getProjectTriggers();
  existingTriggers.forEach(trigger => {
    if (trigger.getHandlerFunction() === 'checkAndProcessEmails') {
      ScriptApp.deleteTrigger(trigger);
    }
  });

  // Create a new daily trigger
  ScriptApp.newTrigger('checkAndProcessEmails')
    .timeBased()
    .everyDays(1) // Adjust frequency as needed
    .create();
}
