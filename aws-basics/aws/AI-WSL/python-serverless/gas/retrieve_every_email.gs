// Initial Script if Analysis Never Started

function saveEmailsInBatches() {
  const sheet = SpreadsheetApp.create("Email Data").getActiveSheet();
  sheet.appendRow(["Subject", "Sender", "Date", "Recipients", "CC", "BCC", "Message ID", "Body"]); // Add header row

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

        sheet.appendRow([subject, sender, date, recipients, cc, bcc, messageId, body]);
      });
    });
    start += batchSize; // Move to the next batch
  } while (threads.length > 0);

  Logger.log("Emails saved to Google Sheets in batches.");
}
