import pprint

def prompt(feed,options=False,notice=False,custom=False,custom_space=False, type_of=False):
    if options:
        inter='%'+str(45)+'s'
        for key in feed.keys():
            print(str(inter)%str(key)+" "+str(feed[key]))
    elif custom:
        inter='%'+str(int(custom_space))+'s'
        print(str(inter)%str(feed))
    elif type_of:
        if 'dict' in str(type(feed)):
            pprint.pprint(feed)
        else:
            print(str(type(feed))+"<-type | value->"+str(feed))
    elif notice:
        print('\n\n<ERROR>')
        inter='%'+str(int(50))+'s'
        print(str(inter)%str(feed))
        print('</ERROR>\n\n')
    else:
        inter='%'+str(30)+'s'
        print(str(inter)%str(feed))
