import streamlit as st
from pages.helpers.story_generator import return_story
from streamlit_extras.stateful_button import button
import re


with st.form("my_form"):

    story_input = st.text_input("What should the story be about?", "Indian boy")
    num_sentences = st.text_input("Number of sentences", "4")
    prompt_style = st.text_input("What should the style of the generated images be? (For examples see DALL-E prompts)", "photorealistic, digital art")
    access_token = st.text_input("Enter OpenAI Chatgpt access token")
    model =  st.selectbox( "Which model to generate the images (Openjourney-v2, DALL-E)", ("Openjourney-v2", "DALL-E"))
    dalle_sess_token = st.text_input("Enter DALL-E sess token (Leave blank if not using DALL-E)")
    submitted = st.form_submit_button("Submit")


if submitted:

    with st.spinner('Generating Story from ChatGPT'):
        response = return_story(access_token, story_input, num_sentences)

    story = re.sub(r'\([^)]*\)', '', response)
    story_sentences = story.split('. ')
    image_prompt_inputs = re.findall(r'\((.*?)\)', response)
    st.write('Story: ', story)
    st.write('Image Prompts: ', image_prompt_inputs)

    st.session_state.update({
        "story": story,
        "story_sentences": story_sentences,
        "image_prompt_inputs": image_prompt_inputs,
        "dalle_sess_token": dalle_sess_token,
        "prompt_style": prompt_style,
        "model": model

    })

    st.write("**:blue[Go to]** **:red[create visuals]** **:blue[to edit story/prompt and to generate the images!]**")
