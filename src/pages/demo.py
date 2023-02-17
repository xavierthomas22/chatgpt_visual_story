import streamlit as st
import re

st.write("""A story about an "Indian boy" """)

# ChatGPT Generated story about an Indian Boy.
response = "The Indian boy walked along the dusty road with a small smile on his face. (Generate an image of a dusty road with a smiling Indian boy walking on it.) He was on his way to school, eager to learn and make new friends. (Generate an image of a school building with the Indian boy standing in front of it.) As he approached the school gates, he saw a group of children playing cricket and felt a pang of longing. (Generate an image of a group of children playing cricket in a field near the school.) But he knew that he would have plenty of time to play after class, and continued walking towards the classroom with a skip in his step. (Generate an image of the Indian boy skipping towards a school building with a backpack on his back.)"
story = re.sub(r'\([^)]*\)', '', response)
story_sentences = story.split('. ')
image_prompt_inputs = re.findall(r'\((.*?)\)', response)

file_paths_list = ['gen_imgs/demo/1.webp', 'gen_imgs/demo/2.webp', 'gen_imgs/demo/3.webp', 'gen_imgs/demo/4.webp']

final_list = [[x, y, z] for x, y, z in zip(story_sentences, image_prompt_inputs, file_paths_list)]

for l in final_list:
    sent, prompt, img_path = l[0], l[1], l[2]
    st.markdown("***")
    st.write(f"""Story Sentence: **:blue[{sent}]**""")
    st.write(f"""Image Prompt from Sentence: **:red[{prompt}]**""")
    st.image(img_path, width=300)
