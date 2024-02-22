import streamlit as st
import asyncio

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import os, sys
import configparser
import csv
import time

st.title("Get users from a selected group 🧘")

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

cpass = configparser.RawConfigParser()
cpass.read('config.data')

class scraper():

    def scrape_user():
        try:
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
                        client.sign_in(phone,code )
        except KeyError:
            st.write("Setup your telegram info in setup page first !!")

        
        os.system('cls')
        chats = []
        last_date = None
        chunk_size = 200
        groups=[]
        
        result = client(GetDialogsRequest(
                    offset_date=last_date,
                    offset_id=0,
                    offset_peer=InputPeerEmpty(),
                    limit=chunk_size,
                    hash = 0
                ))
        chats.extend(result.chats)
        
        for chat in chats:
            try:
                if chat.megagroup== True:
                    groups.append(chat)
            except:
                continue
        
        st.write('Choose a group to scrape members :')
        i=0
        for g in groups:
            st.write(str(i)+'.'+' '+ g.title)
            i+=1

        g_index = st.text_input("Enter group Number : ")
        if st.button("submite"):
            target_group=groups[int(g_index)]
            with st.spinner("Fetching Members..."):
                all_participants = []
                all_participants = client.get_participants(target_group, aggressive=True)

            time.sleep(5)

            with st.spinner('Saving In file...'):
                with open("members.csv","w",encoding='UTF-8') as f:
                    writer = csv.writer(f,delimiter=",",lineterminator="\n")
                    writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
                    for user in all_participants:
                        if user.username:
                            username= user.username
                        else:
                            username= ""
                        if user.first_name:
                            first_name= user.first_name
                        else:
                            first_name= ""
                        if user.last_name:
                            last_name= user.last_name
                        else:
                            last_name= ""
                        name= (first_name + ' ' + last_name).strip()
                        writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])
                time.sleep(5)      
                st.write('Members scraped successfully.')
            client.disconnect()

scraper.scrape_user()
