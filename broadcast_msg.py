# 导入项目中所需要的包
#coding:utf-8

import pandas as pd
import numpy as np
import itchat

# 调用login()函数以登录网页微信
itchat.login()

#不选择自己的账号信息
dataset = itchat.get_friends(update=True)[1:]

# dataset选择部分列,
data = [{'NickName':item['NickName'], 'RemarkName':item['RemarkName'], 'UserName':item['UserName']} for item in dataset]

#转换为dataframe
df_all = pd.DataFrame()
for i in range(len(data)):
    df = pd.DataFrame([data[i]],index=[data[i]['NickName']])
    df_all =df_all.append(df)
    
#群发消息
while True:
    usernames=[]
    while len(usernames)==0:
        remarknmae_pre = input('请输入群发成员前缀：')
        df = df_all[df_all["RemarkName"].str.find(remarknmae_pre, start=0, end=None)>=0]
        usernames = df['UserName'].tolist()
    print('群发人数共{}人：'.format(len(usernames)),df['RemarkName'].values.tolist(),'\n')
    message = input('请输入群发内容：')
    print('\n')
    confirm =input('是否确认发送(y/n):')

    if confirm != 'y':
        print('\n','再来一次','\n')
        continue
    else: 
        for username in usernames: 
            itchat.send(message,toUserName = username)
        print('\n','发送成功!')
  