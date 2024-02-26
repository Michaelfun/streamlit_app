#!/bin/env python3
import streamlit as st
import asyncio
import random

from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
from telethon.sessions import StringSession
import configparser
import os, sys
import csv
import random
import time

st.title("Send sms 💭")

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

class main():

    def send_sms():
        try:
            cpass = configparser.RawConfigParser()
            cpass.read('config.data')
            api_id = cpass['cred']['id']
            api_hash = cpass['cred']['hash']
            phone = cpass['cred']['phone']
            string = cpass['cred']['string']
            client = TelegramClient(StringSession(string), api_id, api_hash)
            client.start()

            if not client.is_user_authorized():
                client.send_code_request(phone)
                code = st.text_input('Enter the code: ')
                if st.button("submite"):
                    client.sign_in(phone,code)
            else:
                st.subheader("This number" +' '+ phone + ":" + " Is logged In 😉")

        except KeyError:
            st.write("Setup your telegram info in setup page first !!")

        users = []
        with open('members.csv', encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['username'] = row[0]
                user['id'] = int(row[1])
                user['access_hash'] = int(row[2])
                user['name'] = row[3]
                users.append(user)

        st.write("Enter your message below.👇👇👇")
        message = st.text_input("Enter Your Message : ")
        if st.button("send"):
            for user in users:
                if user['username'] == "":
                    continue
                receiver = client.get_input_entity(user['username'])
                try:
                    st.write("Sending Message to:", user['name'])
                    with st.spinner("Sending Message"):
                        client.send_message(receiver, message.format(user['name']))
                    def timess_s():
                        time_s = random.randrange(120,300)
                        return time_s
                        
                    SLEEP_TIME = timess_s()
                    st.write("Waiting {} seconds".format(SLEEP_TIME))
                    time.sleep(SLEEP_TIME)
                except PeerFloodError:
                    st.write("Getting Flood Error from telegram. Script is stopping now.")
                    st.write("Please try again after some time.")
                    client.disconnect()
                    sys.exit()
                except Exception as e:
                    st.write("Error:", e)
                    st.write("Trying to continue...")
                    continue
            client.disconnect()
            st.write("Done. Message sent to all users.")

main.send_sms()

