import streamlit as st

def home():
    st.set_page_config(page_title="Telegram-dm-bot", page_icon="🤖")
    st.header("Telegram Automation sms 🤖")
    st.subheader('✍️.Start by setup page to setup your telegram credentials...')
    st.subheader('✍️.Then use scraper page to scrape member from group of your choices...')
    st.subheader('✍️.Go to sms page to send message...')

    st.sidebar.success("Select page above")

home()