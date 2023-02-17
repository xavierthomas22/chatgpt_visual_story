import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to StoryGEN! 👋")
st.info("You would need to configure your OpenAI Chatgpt credentials to generate the story. Please follow the instructions here: https://github.com/acheong08/ChatGPT")
st.info("To use DALL-E, the app would need your dalle sess token. Please follow the instructions here: https://github.com/ezzcodeezzlife/dalle2-in-python")

st.markdown(
    """
    **👈 Once you're ready, go to **:red[create story]** in the sidebar**
"""
)
