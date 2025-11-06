import imaplib
import email
import os
from email.header import decode_header

# IMAP server settings
username = "kapricon733@gmail.com"
password = "Kajal@4321"
mail_server = "imap.gmail.com"

# Connect to Gmail IMAP server
mail = imaplib.IMAP4_SSL(mail_server)
mail.login(username, password)
mail.select("inbox")

# Search for all emails in the inbox
status, messages = mail.search(None, "ALL")
messages = messages[0].split()

for mail_id in messages:
    _, msg_parts = mail.fetch(mail_id, "(RFC822)")
    msg = email.message_from_bytes(msg_parts[0][1])

    # If the email contains attachments
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            # Get the filename and decode it if needed
            filename = part.get_filename()
            decoded_filename = decode_header(filename)[0][0]
            if isinstance(decoded_filename, bytes):
                filename = decoded_filename.decode()

            # Download the attachment
            if filename:
                attachment_path = os.path.join("downloaded_attachments", filename)
                if not os.path.isfile(attachment_path):
                    with open(attachment_path, 'wb') as f:
                        f.write(part.get_payload(decode=True))

# Logout and close the connection
mail.close()
mail.logout()
