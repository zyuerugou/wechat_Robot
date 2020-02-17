# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:01:06 2020

@author: 14001
"""

import itchat
from itchat.content import *
import os
import time

# 文件临时存储页
rec_tmp_dir = os.path.join(os.getcwd(), 'tmp/')

# 存储数据的字典
rec_msg_dict = {}

# 群聊信息监听
@itchat.msg_register([TEXT], isGroupChat=True)
def information(msg):
    rooms = itchat.search_chatrooms(name = '喵喵喵')
    if len(rooms) ！= 0:
        msg_id = msg['MsgId']
        msg_from_user = msg['ActualNickName']
        msg_content = ''
        # 收到信息的时间
        msg_time_rec = time.strftime("%Y-%m-%d %H:%M%S", time.localtime())
        msg_create_time = msg['CreateTime']
        msg_type = msg['Type']
        
        msg_content = msg['Content']
        
        rec_msg_dict.update({
            msg_id: {
                'msg_from_user': msg_from_user,
                'msg_time_rec': msg_time_rec,
                'msg_create_time': msg_create_time,
                'msg_type': msg_type,
                'msg_content': msg_content
            }
        })
        print("群聊信息: ",msg_id, msg_from_user, msg_content, msg_create_time,msg_type)


if __name__ == '__main__':
    if not os.path.exists(rec_tmp_dir):
        os.mkdir(rec_tmp_dir)
    itchat.auto_login(hotReload = True)
    itchat.run()
