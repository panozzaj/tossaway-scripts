# Get starred GMail items and print them in a form for importing into my personal log files.
# Original source from a random stackoverflow topic, but modified for my needs
# AJP20100103
import email, getpass, imaplib, os, time, datetime, dateutil.parser

user = "panozzaj"
pwd = getpass.getpass("Enter your password: ")

# connecting to the gmail imap server
m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user, pwd)
m.select("[Gmail]/Starred") # here you a can choose a mail box like INBOX instead
# use m.list() to get all the mailboxes

resp, items = m.search(None, "ALL") # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
items = items[0].split() # getting the mails id

for emailid in items:
    resp, data = m.fetch(emailid, "(RFC822)") # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
    email_body = data[0][1] # getting the mail content
    mail = email.message_from_string(email_body) # parsing the mail content to get a mail object

    # dates in format: Sat, 15 Aug 2009 16:05:39 -0400 
    # however, I want dates in format YYYYMMDD - HHMM
    print
    print dateutil.parser.parse(mail["Date"]).strftime("%Y%m%d - %H%M")
    print
    print "["+mail["From"]+"] - " + mail["Subject"]

    for part in mail.walk():
        maintype = part.get_content_maintype()
        if maintype == 'text' and part.get_content_subtype() == 'plain':
            print
            print part.get_payload()
