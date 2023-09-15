import random
import pandas as pd

from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


# Get Word List

try:
    df = pd.read_csv("./data/words_to_learn")
    
except FileNotFoundError:
    df = pd.read_csv("./data/Spanish Word List.csv")
    df["Spanish"] = df["Spanish"].str.capitalize()
    df["English"] = df["English"].str.title()
    word_list = df.to_dict(orient = "records")
    
else:
    df["Spanish"] = df["Spanish"].str.capitalize()
    df["English"] = df["English"].str.title()
    word_list = df.to_dict(orient = "records")
    
#Get Word and Translation
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_list)
    spanish_word = current_card["Spanish"]
    canvas.itemconfig(
        title_text, 
        text = "Spanish", 
        fill = "black"
        )
    canvas.itemconfig(
        word_text, 
        text = spanish_word,
        fill = "black"
        )
    canvas.itemconfig(card_background, image = front_image)
    
    flip_timer = window.after(3000, func = flip_card)
    
# Flip Card
def flip_card():
    english_word = current_card["English"]
    canvas.itemconfig(
        title_text, 
        text = "English", 
        fill = "white"
        )
    canvas.itemconfig(
        word_text, 
        text = english_word, 
        fill = "white"
        )
    canvas.itemconfig(card_background, image = back_image)
    
def is_known():
    word_list.remove(current_card)
    save_data = pd.DataFrame(word_list)
    save_data.to_csv("./data/words_to_learn", index = False)
    
    
# Build UI
window = Tk()
window.title("Flashy Flash Cards")
window.config(
    padx = 50,
    pady = 50,
    bg = BACKGROUND_COLOR
    )

flip_timer = window.after(3000, func = flip_card)

canvas = Canvas(
    width = 800,
    height = 526
    )

card_front = "./images/card_front.png"
front_image = PhotoImage(file = card_front)

card_back = "./images/card_back.png"
back_image = PhotoImage(file = card_back)

card_background = canvas.create_image(
    400,
    263,
    image = front_image
    )

# Canvas Text
title_text = canvas.create_text(
    400, 
    150,
    text = "Spanish",
    font = ("Ariel", 40, "italic")
    )

word_text = canvas.create_text(
    400,
    263,
    text = "Word",
    font = ("Ariel", 60, "bold")
    )

canvas.config(
    bg = BACKGROUND_COLOR, 
    highlightthickness = 0
    )
canvas.grid(
    column = 0, 
    row = 0, 
    columnspan = 2
    )

# Buttons
cross_image_file = "./images/wrong.png"
cross_image = PhotoImage(file = cross_image_file)
cross_button = Button(
    image = cross_image, 
    highlightthickness = 0,
    command = next_card
    )

cross_button.grid(
    row = 1,
    column = 0,
    )

check_mark_file = "./images/right.png"
check_mark_image = PhotoImage(file = check_mark_file)
check_mark_button = Button(
    image = check_mark_image,
    highlightthickness = 0,
    command = next_card
    )

check_mark_button.grid(
    row = 1,
    column = 1
    )

next_card()

window.mainloop()