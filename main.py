# 31 capstone flashcard project

from tkinter import *

# consts

BACKGROUND_COLOR = "#B1DDC6"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# code

window = Tk()
window.title("Capstone Flashcard")
window.minsize(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas

canvas = Canvas(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, image=card_front_img)
canvas.create_text(SCREEN_WIDTH / 2, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(SCREEN_WIDTH / 2, 250, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, relief="flat", borderwidth=0, activebackground=BACKGROUND_COLOR)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, relief="flat", borderwidth=0, activebackground=BACKGROUND_COLOR)
known_button.grid(column=1, row=1)


window.mainloop()
