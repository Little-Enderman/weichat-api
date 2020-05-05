# -*- coding: utf-8 -*-# 
# filename: handle.py
import hashlib
import reply
import receive
import web
import requests
import json
#tulingUrl = 'http://www.tuling123.com/openapi/api'
#msg = "你几岁了"
#data = {
#    'key': '7f05e31d381143d9948109e75484d9d0',
#    'info': msg
#}

#res = requests.post(tulingUrl, data=data).text
#tulingdata = json.loads(res)
#answer = tulingdata['text']

class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData
            #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "answer"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            return Argment
