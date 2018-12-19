import datetime
import user

#----------------------------------------------------------
# NODE STORAGE
#----------------------------------------------------------
class Node:
    def __init__(self):
        self.sender = None
        self.subject = None
        self.body = None
        self.year = None
        self.month = None
        self.day = None
        self.hour = None
        self.minute = None
        self.clock = None
        self.next = None # contains the reference to the next node

#----------------------------------------------------------
# LINKED LIST STORAGE
#----------------------------------------------------------
class linked_list:
    def __init__(self):
        self.size = 0
        self.width = 75
        self.cur_node = None

    def add_node(self,
            sender,
            subject,
            body,
            year,
            month,
            day,
            hour=None,
            minute=None,
            clock=None):
        new_node = Node() # create a new node
        new_node.sender = sender
        new_node.subject = subject
        new_node.body = body
        new_node.year = year
        new_node.month = month
        new_node.day = day
        new_node.hour = hour
        new_node.minute = minute
        new_node.clock = clock
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.
        self.size = self.size + 1

    def search_node(self, upc):
        node = self.cur_node
        while node:
            if str(upc) in str(node.filename) or str(node.filename) in str(upc) or str(upc) == str(node.filename):
                return node
            node = node.next

    def get_size(self):
        return self.size

    def list_print(self):
        node = self.cur_node
        while node:
            if isinstance(node.body, str):
                lines = []
                line=''
                num = 0
                for i in range(len(str(node.body))):
                    line+=node.body[i]
                    if int(i / self.width) > num:
                        print(i/self.width)
                        num += 1
                        lines.append(line)
                        line=''

            inter_sender='%'+str(25)+'s'
            inter_subject='%'+str(25)+'s'
            inter_date='%'+str(25)+'s'
            inter_body='%'+str(25)+'s'

            print("#####################################################################################################")
            print(str(inter_sender)%"SENDER: "+str(node.sender))
            print(str(inter_subject)%"SUBJECT: "+str(node.subject))
            print(str(inter_date)%"DATE: "+str(node.year)+"/"+str(node.month)+"/"+str(node.day)+" "+str(node.hour)+":"+str(node.minute))

            if isinstance(node.body, str):
                num=0
                for line in lines:
                    num+=1
                    if num == 1:
                        print(str(inter_body)%"BODY: "+str(line))
                    else:
                        print(str(inter_body)%"|"+str(line))
            else:
                print(str(inter_body)%"BODY: None")

            node = node.next
