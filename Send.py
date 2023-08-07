import pywhatkit as kit
import datetime
import pyautogui
import time
import random
import requests
import transformers
import numpy as np



# r = requests.post(
#     "https://api.deepai.org/api/text-generator",
#     data={
#         'text': 'good morning text',
#     },
#     headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
# )
# print(r.json())

 
# import transformers

# model = transformers.GPT2LMHeadModel.from_pretrained('gpt2')
# tokenizer = transformers.GPT2Tokenizer.from_pretrained('gpt2')

# prompt = "Good morning! I hope you slept well."

# input_ids = tokenizer.encode(prompt)

# attention_mask = tokenizer.encode(prompt, add_special_tokens=False)
# pad_token_id = tokenizer.eos_token_id

# output = model.generate(
#     input_ids=input_ids,
#     max_length=100,
#     temperature=0.7,
#     repetition_penalty=1.0,
#     prompt_token_id=model.config.decoder_start_token_id,
#     attention_mask=attention_mask,
#     pad_token_id=pad_token_id,
#     return_dict=True,
# )

# generated_text = output['generated_text']

# print(generated_text)


 

model = transformers.GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = transformers.GPT2Tokenizer.from_pretrained('gpt2')

prompt = "Good morning! I hope you slept well."

input_ids = tokenizer.encode(prompt, return_tensors="pt")

output = model.generate(
    input_ids=input_ids,
    max_length=100,
    temperature=0.7,
    repetition_penalty=1.0,
    pad_token_id=tokenizer.eos_token_id,
)

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)

 


# def print_output(r):
#   """Prints the output of the request object."""
#   if r.status_code == 200:
#     print(r.json()['output'])
#   else:
#     print(r.status_code)

# if __name__ == "__main__":
#   r = requests.post(
#     "https://api.deepai.org/api/text-generator",
#     data={
#         'text': 'good morning text',
#     },
#     headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
#   )

#   print_output(r)









# def convert_r_to_string(r):
#   """Converts r to a string."""
#   if not isinstance(r, (bytes, bytearray)):
#     return r
#   return r.decode("utf-8")

# if __name__ == "__main__":
 
#   print(convert_r_to_string(r))


# Set the messages
messages = [  
    "Good morning to everyone except the person who stole my coffee mug.",
    "Good morning sunshine! Just kidding, it's raining cats and dogs.",
    "Good morning world! I'm ready to face the day with a smile and a positive attitude. And a lot of caffeine.",
    "Good morning! I hope you slept well. Because I didn't. Thanks for snoring all night.",

    "Good morning! Today is a great day to be alive. Unless you have a hangover. Then it's a terrible day.",
    ]


number = "+264811234567"  # Phone number to send the message to

# # # Send the message
# for i in range(24):









#     # message = random.choice(r)  # Select a random message from the list of messages

#     # Send the message using the 'sendwhatmsg' function from the 'pywhatkit' library
#     # Parameters: number (phone number), message (text message), hour, minute, tab_close (optional, closes the browser tab)
#  kit.sendwhatmsg(number, r, 12, 59, tab_close=True)

#     # Close the tab using the 'hotkey' function from the 'pyautogui' library
#     # pyautogui.hotkey('ctrl', 'w')

#     # Wait for 24 hours (3600 seconds per hour) before running the script again
#  time.sleep(3600)

