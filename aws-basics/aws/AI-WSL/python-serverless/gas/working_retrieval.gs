function saveEmailsFromDate() {
  const spreadsheetId = '13JYwb7nktTbt3kkSdsPeOBmY97Y2Otg22Pt9HxJTZAg';
  const spreadsheet = SpreadsheetApp.openById(spreadsheetId);
  const sheet = spreadsheet.getSheetByName("Sheet1") || spreadsheet.insertSheet("Sheet1");

  // Check if header row is already present
  const headers = sheet.getRange(1, 1, 1, 8).getValues()[0];
  if (headers[0] !== "Subject") {
    sheet.appendRow(["Subject", "Sender", "Date", "Recipients", "CC", "BCC", "Message ID", "Body"]);
  }

  // Get the last processed date from the sheet or use the default date
  const lastProcessedCell = sheet.getRange("I1");
  let lastProcessedDate = new Date(lastProcessedCell.getValue());
  if (isNaN(lastProcessedDate.getTime())) {
    // Default to "20 Aug 2024 12:00 AM" if no valid date is found
    lastProcessedDate = new Date("August 20, 2024 00:00:00");
  }

  const batchSize = 100; // Adjust the batch size according to your needs
  let start = 0;
  let threads;
  const cutoffDate = lastProcessedDate;

  // Track existing message IDs in a Set
  const existingMessageIds = new Set();
  if (sheet.getLastRow() > 1) {
    const existingMessages = sheet.getRange(2, 7, sheet.getLastRow() - 1, 1).getValues();
    existingMessages.forEach(row => existingMessageIds.add(row[0]));
  }

  const newRows = []; // Array to store new rows for batch appending

  // Retrieve new emails in a paginated manner
  do {
    threads = GmailApp.search(`after:${Math.floor(cutoffDate.getTime() / 1000)}`, start, batchSize);
    if (threads.length === 0) break; // Exit loop if no more threads

    // Process threads and messages
    threads.forEach(thread => {
      const messages = thread.getMessages();
      messages.forEach(message => {
        const date = message.getDate();
        if (date > cutoffDate) {
          const subject = message.getSubject();
          const sender = message.getFrom();
          const recipients = message.getTo();
          const cc = message.getCc();
          const bcc = message.getBcc();
          const messageId = message.getId();
          const body = message.getPlainBody();

          // Append only new messages
          if (!existingMessageIds.has(messageId)) {
            newRows.push([subject, sender, date, recipients, cc, bcc, messageId, body]);
            existingMessageIds.add(messageId);
          }
        }
      });
    });
    start += batchSize; // Move to the next batch
  } while (threads.length > 0);

  // Batch write new rows if there are any
  if (newRows.length > 0) {
    const range = sheet.getRange(sheet.getLastRow() + 1, 1, newRows.length, 8);
    range.setValues(newRows);
  }

  // Update the last processed date
  if (threads.length > 0) {
    lastProcessedDate = new Date();
    lastProcessedCell.setValue(lastProcessedDate.toISOString());
  }

  Logger.log("Emails saved to Google Sheets from the specified date.");
}

// Function to create a time-based trigger
function createTrigger() {
  ScriptApp.newTrigger('saveEmailsFromDate')
    .timeBased()
    .everyMinutes(1) // Adjust as needed
    .create();
}
