#!/bin/env python3
# code by : youtube.com/theunknon

"""

you can re run setup.py 
if you have added some wrong value

"""
import streamlit as st
import asyncio

import os, sys
import time

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

st.title("Save telegram-API Id and Key ⚙️")

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

def config_setup():
	import configparser
	cpass = configparser.RawConfigParser()
	cpass.add_section('cred')
	xid = st.text_input("enter api ID : ")
	xhash = st.text_input("enter hash ID : ")
	xphone = st.text_input("enter phone number : ")
	
	if st.button("submite"):
		cpass.set('cred', 'id', xid)
		cpass.set('cred', 'hash', xhash)
		cpass.set('cred', 'phone', xphone)
		

		setup = open('config.data', 'w')
		cpass.write(setup)
		setup.close()

config_setup()

def merge_csv():
	import pandas as pd
	import sys
	banner()
	file1 = pd.read_csv(sys.argv[2])
	file2 = pd.read_csv(sys.argv[3])
	print(gr+'['+cy+'+'+gr+']'+cy+' merging '+sys.argv[2]+' & '+sys.argv[3]+' ...')
	print(gr+'['+cy+'+'+gr+']'+cy+' big files can take some time ... ')
	merge = file1.merge(file2, on='username')
	merge.to_csv("output.csv", index=False)
	print(gr+'['+cy+'+'+gr+']'+cy+' saved file as "output.csv"\n')


