import time
from itertools import chain
import imaplib
import email

imap_ssl_host = 'imap.gmail.com'  # imap.mail.yahoo.com
imap_ssl_port = 993
username = 'enginecommerce.tester@gmail.com'
password = 'System76'

# Restrict mail search. Be very specific.
# Machine should be very selective to receive messages.
'''criteria = {
        'FROM':    'chadwick@enginecommerce.com',
        'SUBJECT': 'this is a subject',
        'BODY':    'this is a test',
    }'''


criteria = {
        'FROM':    'chadwick@enginecommerce.com',
        'SUBJECT': 't',
        'BODY':    't',
    }

uid_max = 0


def search_string(uid_max, criteria):
    c = list(map(lambda t: (t[0], '"'+str(t[1])+'"'), criteria.items())) + [('UID', '%d:*' % (uid_max+1))]
    return '(%s)' % ' '.join(chain(*c))
    # Produce search string in IMAP format:
    #   e.g. (FROM "me@gmail.com" SUBJECT "abcde" BODY "123456789" UID 9999:*)


def get_first_text_block(msg):
    type = msg.get_content_maintype()

    if type == 'multipart':
        for part in msg.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif type == 'text':
        return msg.get_payload()


server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
server.login(username, password)
server.select('INBOX')

result, data = server.uid('search', None, search_string(uid_max, criteria))

uids = [int(s) for s in data[0].split()]
if uids:
    uid_max = max(uids)
    # Initialize `uid_max`. Any UID less than or equal to `uid_max` will be ignored subsequently.

server.logout()


# Keep checking messages ...
# I don't like using IDLE because Yahoo does not support it.
attempt=0
while 1:
    attempt+=1
    # Have to login/logout each time because that's the only way to get fresh results.
    print("Attempt: "+str(attempt))
    server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
    server.login(username, password)
    server.select('INBOX')

    result, data = server.uid('search', None, search_string(uid_max, criteria))
    print("Result:::::::::::::::::::::::::::::::\n+"+str(type(result))+"\n")
    print("Data:::::::::::::::::::::::::::::::::\n+"+str(type(data))+"\n")
    uids = [int(s) for s in data[0].split()]
    for uid in uids:
        print("    "+str(uid))
        # Have to check again because Gmail sometimes does not obey UID criterion.
        if uid > uid_max:
            result, data = server.uid('fetch', uid, '(RFC822)')  # fetch entire message
            uid_max = uid

            msg = email.message_from_string(data[0][1])

            fp = StringIO()
            g = Generator(fp, mangle_from_=True, maxheadlen=60)
            g.flatten(msg)

            text = fp.getvalue()

            print('New message :::::::::::::::::::::')
            print(text)

    server.logout()
    time.sleep(1)
