def send(text='default text', subject_text="Sent from Python"):
    """Sends email according to .env file."""
    import os
    from dotenv import load_dotenv

    load_dotenv()

    #print(os.getenv('MAILPW'))

    SMTPserver = 'posteo.de'
    sender =      os.getenv('MAILSENDER')
    destination = [os.getenv('MAILSENDER')]

    USERNAME = os.getenv('MAILUSER')
    PASSWORD = os.getenv('MAILPW')

    # typical values for text_subtype are plain, html, xml
    text_subtype = 'plain'

    content=text

    subject=subject_text

    import sys

    from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
    # from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

    # old version
    # from email.MIMEText import MIMEText
    from email.mime.text import MIMEText

    try:
        msg = MIMEText(content, text_subtype)
        msg['Subject']=       subject
        msg['From']   = sender # some SMTP servers will do this automatically, not all

        conn = SMTP(SMTPserver)
        conn.set_debuglevel(False)
        conn.login(USERNAME, PASSWORD)
        try:
            conn.sendmail(sender, destination, msg.as_string())
        finally:
            conn.quit()

    except:
        sys.exit( "mail failed; %s" % "CUSTOM_ERROR" ) # give an error message

def sendstatus(section="<3",subject="Python status update"):
    """Sends email with status text according to .env file."""
    send("I'm done ("+section+") ^^", subject)