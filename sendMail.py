#!/usr/bin/env python3

"""Send the contents of a directory as a MIME message."""

import os
import sys
import smtplib
# For guessing MIME type based on file name extension
import mimetypes

from argparse import ArgumentParser

from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

COMMASPACE = ', '
def main(mailoptions):
    args = {}
    outer = MIMEMultipart()
    outer['Subject'] = mailoptions['subject']
    outer['To'] = COMMASPACE.join(mailoptions['recipients'])
    outer['From'] = mailoptions['sender']
    outer.preamble = mailoptions['message']

    ctype, encoding = mimetypes.guess_type(mailoptions['path'])
    if ctype is None or encoding is not None:
        # No guess could be made, or the file is encoded (compressed), so
        # use a generic bag-of-bits type.
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    if maintype == 'text':
        with open(mailoptions['path']) as fp:
            print(fp.read())
            # msg = MIMEText(fp.read(), _subtype=subtype)
    elif maintype == 'image':
        with open(mailoptions['path'], 'rb') as fp:
            msg = MIMEImage(fp.read(), _subtype=subtype)
    else:
        with open(mailoptions['path'], 'rb') as fp:
            msg = MIMEBase(maintype, subtype)
            msg.set_payload(fp.read())
        # Encode the payload using Base64
        encoders.encode_base64(msg)
    # Set the filename parameter
    msg.add_header('Content-Disposition', 'attachment', filename=mailoptions.filename)
    outer.attach(msg)
    # Now send or store the message
    composed = outer.as_string()

    with smtplib.SMTP(mailoptions['host'], mailoptions['port']) as s:
        s.login(mailoptions['from_addr'], mailoptions['password'])
        s.sendmail(mailoptions['sender'], mailoptions['recipients'], composed)

if __name__ == '__main__':
    mailoptions = {
        'subject': 'subject2',
        'recipients': 'heyonghan@163.com',
        'sender': 'heyonghan@163.com',
        'path':'/Users/jiangyantao/PycharmProjects/stockAnalysisGit/test_python.py',
        'filename':'filename',
        'message':'hello smtp',
        'host':'smtp.163.com',
        'port':'994',
        'from_addr':'heyonghan',
        'password':'163zaq12wsx'
    }
    main(mailoptions)