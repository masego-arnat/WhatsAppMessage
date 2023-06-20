import pywhatkit as kit
import datetime
import pyautogui
import time
import random

# Set the messages
messages = [  
    "Good morning! Wishing you a day full of sunshine and happiness.",
    "Rise and shine! It's a new day full of opportunities.",
    "Good morning! May your day be filled with love and laughter.",
    "A beautiful day starts with a beautiful mindset. Good morning!",
    "Good morning! Let's make today amazing.",
    "Good morning! Today is a new beginning.",
    "Good morning! May your day be as wonderful as you are.",
    "Good morning! Let's make the most of this beautiful day.",
    "Good morning! May your day be filled with joy and blessings.",
    "Good morning! Here's to a great day ahead.",
    'Good morning, angel. I hope you dreamed the sweetest dreams.',
'Hope your morning is as bright and beautiful as you are.',
'You were the first person I thought of when I woke up, and it made me smile.',
'Dang, girl—they don’t call it “beauty sleep” for nothing! You just wake up this gorgeous?',
'Everyone should get to experience a sunrise with you.',
'Ah, you’re finally awake, my sleeping beauty!',
'For me, the sun only rises when you smile in the morning and sets when you close your eyes at night.'
    ]

# Send the message
for i in range(24):
 
    message = random.choice(messages)



    kit.sendwhatmsg("+264817500205", message, 10, 59,  tab_close=True)

    # kit.sendwhatmsg("+264812413654", message, 7, 31,  tab_close=True)
    # time.sleep(10)

    
    # kit.sendwhatmsg("+264816326442", message, 7, 32,  tab_close=True)
    # kit.sendwhatmsg("+264817700626", message, 7, 33,  tab_close=True)
    # Close the tab +
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(3600)

# Wait for 10 seconds after sending the message
# time.sleep(10)


