from revChatGPT.V1 import Chatbot
from dalle2 import Dalle2
import os

# chatbot = Chatbot(config={
#     "access_token": ""
# })

# story_input = "Indian Boy in a Forest"
# num_sentences = 4
# full_story_input = f"Write a {num_sentences} sentences very short story about a {story_input}. After each sentence, write a short prompt sentence in round brackets to generate a DALL-E image. The sentences inside the round brackets must not include names, but includes ethnicity, nationality and context from previous sentences."

# print("Chatbot: ")
# prev_text = ""
# for data in chatbot.ask(
#     full_story_input,
# ):
#     message = data["message"][len(prev_text) :]
#     print(message, end="", flush=True)
#     prev_text = data["message"]
# print()
# exit()


response = "The Indian boy walked deep into the forest, following a path he had never taken before. (Create an image of a dense forest with a faint path leading into it, with an Indian boy walking towards it.) He was in search of a rare herb that only grew in that part of the forest. (Create an image of the Indian boy searching for the herb, with various plants around him.) As the sun began to set, the boy realized he was lost and started to panic. (Create an image of the Indian boy looking worried and lost, with the sun setting in the background.) Just then, he saw a flicker of light in the distance and started running towards it. (Create an image of the boy running towards the light, with a hint of hope on his face.)"
response_split = response.split(") ")

story_sentences = []
image_prompt_inputs = []
for t in response_split:
    t_split = t.split(". (")
    story_sentences.append(t_split[0])
    image_prompt_inputs.append(t_split[1].strip(')'))
print(image_prompt_inputs)


prompt_style = " photorealistic, midjourney like image"

# dalle = Dalle2("") # your bearer key

# file_paths_list = []
# for idx, prompt in enumerate(image_prompt_inputs):
#     prompt = prompt + prompt_style
#     folder_path = f"gen_imgs/scene_{idx}"
#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)
#     print(prompt)
#     file_paths = dalle.generate_and_download(prompt, image_dir=folder_path)
#     file_paths_list.append(file_paths[0])
#     print(file_paths_list)
#     exit()

file_paths_list = ['gen_imgs/scene_0/generation-tiJIcwcOTvTmOsrjkxgvPJrX.webp']

final_list = [[x, y, z] for x, y, z in zip(story_sentences, image_prompt_inputs, file_paths_list)]
print(final_list)

# print(file_paths)