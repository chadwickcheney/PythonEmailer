from email import parser
import inbox
import poplib
poplib._MAXLINE=20480
import pprint
import email


class Carrier:
    #def __init__(self, username='enginecommerce.tester@gmail.com', password='System76'):
    def __init__(self, username='chdwckchny@gmail.com', password='Lieutenantw3ck'):
        self.username = username
        self.password = password
        self.ll = inbox.linked_list()

    def fetch(self):
        pop_conn = poplib.POP3_SSL('pop.gmail.com')
        pop_conn.user(self.username)
        pop_conn.pass_(self.password)

        #Get messages from server:
        messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
        # Concat message pieces:

        messages = [b"\n".join(mssg[1]) for mssg in messages]
        #Parse message intom an email object:
        messages = [email.message_from_bytes(mssg) for mssg in messages]

        for message in messages:
            '''print("\n\n########################################")
            print('From')
            print(type(message['From']))
            print(message['From'])
            print('Delivered-To')
            print(type(message['Delivered-To']))
            print(message['Delivered-To'])
            print('sender')
            print(type(message['sender']))
            print(message['sender'])
            print('Date')
            print(type(message['Date']))
            print(message['Date'])
            print('Subject')
            print(type(message['Subject']))
            print(message['Subject'])
            print('Body')
            print(type(message['Body']))
            print(message['Body'])'''

            date_array = message['Date'].split(" ")
            index = None
            for date in date_array:
                if ":" in str(date):
                    index = date_array.index(date)
                else:
                    index=-1
            if index and not index == -1:
                time_array = date_array[index].split(":")
                print(date_array)
                print(time_array)
                self.ll.add_node(
                        sender=message['From'],
                        subject=message['Subject'],
                        body=message['Body'],
                        year=date_array[3],
                        month=date_array[2],
                        day=date_array[1],
                        hour=time_array[0],
                        minute=time_array[1]
                    )

            else:
                print(date_array)
                self.ll.add_node(
                        sender=message['From'],
                        subject=message['Subject'],
                        body=message['Body'],
                        year=date_array[3],
                        month=date_array[2],
                        day=date_array[1],
                        clock=message['Date']
                    )

        pop_conn.quit()

    def print_all(self):
        self.ll.list_print()

c = Carrier()
c.fetch()
c.print_all()
