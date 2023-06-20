import pywhatkit as kit
import datetime
import pyautogui
import time
import random

# Set the messages
messages = [  
    "Good morning to everyone except the person who stole my coffee mug.",
    "Good morning sunshine! Just kidding, it's raining cats and dogs.",
    "Good morning world! I'm ready to face the day with a smile and a positive attitude. And a lot of caffeine.",
    "Good morning! I hope you slept well. Because I didn't. Thanks for snoring all night.",

    "Good morning! Today is a great day to be alive. Unless you have a hangover. Then it's a terrible day.",
    ]

#enter your numner here
number = ("+264811234567")

# Send the message
for i in range(24):
 
    message = random.choice(messages)



    kit.sendwhatmsg(number, message, 11, 25,  tab_close=True)

 
    # Close the tab +
    pyautogui.hotkey('ctrl', 'w')
    # wait 24 hours before running the script again 
    time.sleep(3600)


