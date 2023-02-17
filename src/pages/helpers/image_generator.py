import os
from dalle2 import Dalle2
from diffusers import StableDiffusionPipeline
import torch
import streamlit as st

def create_images(dalle_sess_token, image_prompt_inputs, prompt_style):

    if st.session_state.model == "DALL-E":

        dalle = Dalle2(dalle_sess_token) # your bearer key

        file_paths_list = []
        for idx, prompt in enumerate(image_prompt_inputs):
            print(f"Scene_{idx}")
            prompt = prompt.replace(".","") + f", {prompt_style}"
            folder_path = f"gen_imgs/scene_{idx}"
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            print(prompt)
            file_paths = dalle.generate_and_download(prompt, image_dir=folder_path)
            file_paths_list.append(file_paths[0])

    elif st.session_state.model == "Openjourney-v2":

        file_paths_list = []
        model_id = "prompthero/openjourney-v2"
        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
        pipe = pipe.to("cuda")

        for idx, prompt in enumerate(image_prompt_inputs):
            print(f"Scene_{idx}")
            prompt = prompt.replace(".","") + f", {prompt_style}"
            folder_path = f"gen_imgs/scene_{idx}"
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            print(prompt)
            image = pipe(prompt).images[0]
            image.save(folder_path + f"/{idx}.jpg")
            file_paths_list.append([folder_path + f"/{idx}.jpg"])

    return file_paths_list