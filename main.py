from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
data = pandas.read_csv("data/french_words.csv")
words_dictionary = data.to_dict(orient="records")

def get_new_card():
    random_card = random.choice(words_dictionary)
    foreign_language_name = list(random_card.keys())[0]
    canvas.itemconfig(foreign_language_name_text, text=foreign_language_name.lower())
    foreign_word = random_card[foreign_language_name]
    canvas.itemconfig(foreign_word_canvas_text, text=foreign_word)

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image= card_front)

foreign_language_name_text = canvas.create_text(400, 143, text="title", font=(FONT_NAME, 40, "italic"))
foreign_word_canvas_text = canvas.create_text(400, 303, text="word", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=1,row=0,columnspan=2)


wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, command=get_new_card, highlightthickness=0)
wrong_button.grid(column=1,row=1)
right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, command=get_new_card, highlightthickness=0)
right_button.grid(column=2,row=1)

get_new_card()

window.mainloop()