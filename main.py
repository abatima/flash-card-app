from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image= card_front)
canvas.create_text(400, 143, text="French", font=(FONT_NAME, 40, "italic"))
canvas.create_text(400, 303, text="Trouve", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=1,row=0,columnspan=2)

# learning_language_label = Label(text = "French", font=(FONT_NAME, 40, "italic"))
# learning_language_label.grid(column=1,row=0)
#
# data_language_word_label = Label(text = "Timer", font=(FONT_NAME, 60, "bold"))
# data_language_word_label.grid(column=1,row=0)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0)
wrong_button.grid(column=1,row=1)

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0)
right_button.grid(column=2,row=1)

window.mainloop()