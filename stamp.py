import poplib
from email import parser
import pprint
import email
pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('enginecommerce.tester@gmail.com')
pop_conn.pass_('System76')
#Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
# Concat message pieces:
messages = [b"\n".join(mssg[1]) for mssg in messages]
#messages = ["\n".join(mssg[1]) for mssg in messages]
#Parse message intom an email object:
messages = [email.message_from_bytes(mssg) for mssg in messages]
#messages = [parser.Parser().parsestr(mssg) for mssg in messages]
pprint.pprint(messages)
for message in messages:
    print(message['subject'])
    print(message['body'])
pop_conn.quit()
