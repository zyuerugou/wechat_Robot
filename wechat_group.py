# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:01:06 2020

@author: 14001
"""

import itchat
from itchat.content import *
import os
import time
import xlrd
import xlwt

# 文件临时存储页
rec_tmp_dir = os.path.join(os.getcwd(), 'tmp/')

# 存储数据的字典
rec_msg_dict = {}

# 特定的群聊id
from_group = ''

# 保存数据
def saveData(msg_id, msg_from_user, msg_content, msg_create_time):
    print('save data')

# 解析消息
def decodeMsg(msg_id, msg_from_user, msg_content, msg_create_time):
    print('decode msg')

# 群聊信息监听
@itchat.msg_register([TEXT], isGroupChat=True)
def information(msg):
    # print(msg['ToUserName'])
    if msg['ToUserName'] == from_group:
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
        decodeMsg(msg_id, msg_from_user, msg_content, msg_create_time)
        print("群聊信息: ",msg_id, msg_from_user, msg_content, msg_create_time,msg_type)


if __name__ == '__main__':
    if not os.path.exists(rec_tmp_dir):
        os.mkdir(rec_tmp_dir)
    itchat.auto_login(hotReload = True)
    group = itchat.get_chatrooms(update = True)
    for g in group:
        if g['NickName'] == '喵喵喵':
            from_group = g['UserName']
            break   
    print(from_group)
    itchat.run()
