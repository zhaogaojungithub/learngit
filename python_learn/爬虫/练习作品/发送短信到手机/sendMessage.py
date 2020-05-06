#! /usr/bin/python3
import time
from twilio.rest import Client
def sendMessage(msg,phone):
    print('开始发送短信...........');
    # Your Account SID from twilio.com/console
    account_sid = "ACdd131c4fcadf20fde812156448f05cda";
    # Your Auth Token from twilio.com/console
    auth_token  = "c4a74f4fc60ebab9d4c4933f0297c3d8";
    client = Client(account_sid, auth_token);

    message = client.messages.create(
        to="+86"+phone, 
        from_="+12568264269",
        body=msg);
    print(message.sid);
    print('短信发送成功..............');
