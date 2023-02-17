import streamlit as st
import ast
from pages.helpers.image_generator import create_images

if st.session_state.story:

    with st.form("my_form"):
        story_sentences = st.text_input("Story: ", st.session_state.story_sentences)
        image_prompt_inputs= st.text_input("Image Prompts: ", st.session_state.image_prompt_inputs)
        story_sentences = ast.literal_eval(story_sentences)
        image_prompt_inputs = ast.literal_eval(image_prompt_inputs)
        submitted = st.form_submit_button("Submit")

    if submitted:
        with st.spinner(f'Generating Images using {st.session_state.model}'):
            file_paths_list = create_images(st.session_state.dalle_sess_token, image_prompt_inputs, st.session_state.prompt_style)
            caption = story_sentences
            idx = 0
            for _ in range(len(file_paths_list)-1): 
                cols = st.columns(2) 
                
                if idx < len(file_paths_list):
                    cols[0].image(file_paths_list[idx], width=300, caption=caption[idx])
                idx+=1 
                if idx < len(file_paths_list): 
                    cols[1].image(file_paths_list[idx], width=300, caption=caption[idx])
                    idx = idx + 1
                else:
                    break