import itchat
import time
import requests
import hashlib

# robot
def get_response(msg, FromUserName):
    api_url = 'http://www.tuling123.com/openapi/api'
    apikey = '033aca27e13942db8d44bcb38a140a6a'
    hash = hashlib.md5()
    userid = hash.update(FromUserName.encode('utf-8'))
    data = {'key': apikey,
            'info': msg,
            'userid': userid
            }
    try:
        req = requests.post(api_url, data=data).json()
        return req.get('text')
    except:
        return

itchat.auto_login(hotReload=True)
## personal chat
#@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
#def Tuling_robot(msg):
#    respones = get_response(msg['Content'], msg['FromUserName'])
#    itchat.send(respones, msg['FromUserName'])
#
## return pic, record, attachment
#@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
#def download_files(msg):
#    fileDir = '%s%s'%(msg['Type'], int(time.time()))
#    msg['Text'](fileDir)
#    itchat.send('%s received'%msg['Type'], msg['FromUserName'])
#    itchat.send('@%s@%s'%('img' if msg['Type'] == 'Picture' else 'fil', fileDir), msg['FromUserName'])
#
## add stranger
#@itchat.msg_register('Friends')
#def add_friend(msg):
#    itchat.add_friend(**msg['Text'])
#    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

# get sina content
def group_id(name):
    df = itchat.search_chatrooms(name=name)
    return df[0]['UserName']

Message = 'this is a test msg'
#GroupsContainer = set()

@itchat.msg_register('Text', isGroupChat = True) #isGroupChat = True: autoreply
def broadcast(msg):
    response = get_response(msg['Content'], msg['FromUserName'])
    itchat.send(response, msg['FromUserName'])
    grn = group_id('test')
    #groups_json_list = itchat.get_chatrooms()
    #groupsName = [nm.get('UserName') for nm in groups_json_list]
    #groupsName = set(groupsName)
    #for grpn in groupsName:
        #GroupsContainer.add(grpn)
    while True:
        t=5
        print "Start: %s" % time.ctime()
        time.sleep(t)
            #current_time = time.localtime(time.time())
            #if current_time.tm_sec == 0:
                #for grn in GroupsContainer:
        itchat.send(Message, grn)
        print "End: %s" % time.ctime()

itchat.run()
