#! /usr/bin/python3
from skpy import Skype, SkypeChats
import base64
import os
import sys
from flask import Flask, request, abort
import time
from datetime import datetime
import logging

timeStamp = time.time()
date = datetime.fromtimestamp(timeStamp).strftime("%Y-%m-%d %H:%M:%S")
username = os.environ.get('Skype_Username')
password = os.environ.get('Skype_Password')
host = os.environ.get('flask_host')
port = os.environ.get('flask_port')
sk = Skype(username, password)


app = Flask(__name__)
@app.route('/group/<group>/<message>', methods=['POST'])
def webhook(message,group):
    if request.method == 'POST':
        ch = sk.chats.chat(group)
        ch.sendMsg(message)
        return 'success', 200
        app.logger.info('Info level log')
    else:
        abort(400)

@app.route('/user/<user>/<message>', methods=['POST'] )
def webhook2(message,user):
    if request.method == 'POST':
        ch = sk.contacts[user].chat
        ch.sendMsg(message)
        app.logger.info('Info level log')
        return 'success', 200
    else:
        abort(400)

timeStamp = time.time()
date = datetime.fromtimestamp(timeStamp).strftime("%Y-%m-%d %H:%M:%S")
logging.basicConfig(filename='/root/skype/record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s : %(message)s')

if __name__ == '__main__':
    app.run(host, port)
