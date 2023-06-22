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


number = "+264811234567"  # Phone number to send the message to

# Send the message
for i in range(24):
    message = random.choice(messages)  # Select a random message from the list of messages

    # Send the message using the 'sendwhatmsg' function from the 'pywhatkit' library
    # Parameters: number (phone number), message (text message), hour, minute, tab_close (optional, closes the browser tab)
    kit.sendwhatmsg(number, message, 11, 25, tab_close=True)

    # Close the tab using the 'hotkey' function from the 'pyautogui' library
    pyautogui.hotkey('ctrl', 'w')

    # Wait for 24 hours (3600 seconds per hour) before running the script again
    time.sleep(3600)

