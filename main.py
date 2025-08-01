# 31 capstone flashcard project

from tkinter import *
import pandas
import random


# consts

BACKGROUND_COLOR = "#B1DDC6"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

word_data = []


def load_csv():
    data_file = pandas.read_csv("./data/english_words.csv")

    global word_data
    word_data = [{"english": value["English"], "czech": value["Czech"]} for key, value in data_file.iterrows()]


def get_random_word():
    random_word = random.choice(word_data)
    return random_word


def show_random_word():
    random_word = get_random_word()["english"]
    canvas.itemconfig(big_word, text=random_word)


def update_card():
    show_random_word()


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
big_word = canvas.create_text(SCREEN_WIDTH / 2, 250, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, relief="flat", borderwidth=0, activebackground=BACKGROUND_COLOR, command=update_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, relief="flat", borderwidth=0, activebackground=BACKGROUND_COLOR, command=update_card)
known_button.grid(column=1, row=1)

# load CSV data

load_csv()
show_random_word()


window.mainloop()
