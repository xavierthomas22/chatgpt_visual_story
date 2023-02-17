from revChatGPT.V1 import Chatbot
import streamlit as st

def return_story(access_token, story_input, num_sentences):

    chatbot = Chatbot(config={
        "access_token": access_token
    })

    full_story_input = f"Write a {num_sentences} sentences very short story about a {story_input}. After each sentence, write a prompt sentence in brackets to generate a DALL-E image. The sentences inside the brackets must not include names, but includes ethnicity, nationality and context from previous sentences."

    print("Chatbot: ")
    chatgpt_output = ""
    prev_text = ""
    for data in chatbot.ask(
        full_story_input,
    ):
        message = data["message"][len(prev_text) :]
        print(message, end="", flush=True)
        prev_text = data["message"]
        chatgpt_output += message
    print()
    
    return chatgpt_output
