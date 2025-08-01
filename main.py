# 31 capstone flashcard project

from tkinter import *
import pandas
import random


# consts

BACKGROUND_COLOR = "#B1DDC6"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

lang = None
trans_lang = None
to_learn = []
active_row = {}
timer = None

card_front_img = None
card_back_img = None


def load_csv():
    data_file = pandas.read_csv("./data/english_words.csv")

    global lang, trans_lang, to_learn
    lang = data_file.columns[0]
    trans_lang = data_file.columns[1]

    # ruční způsob
    # word_data = [{"english": value["English"], "czech": value["Czech"]} for key, value in data_file.iterrows()]

    # pandas způsob
    to_learn = pandas.DataFrame.to_dict(data_file, orient="records")


def get_random_word():
    random_word = random.choice(to_learn)
    return random_word


def show_random_word():
    global active_row
    active_row = get_random_word()

    random_word = active_row[lang]
    canvas.itemconfig(big_word, text=random_word, fill="black")
    canvas.itemconfig(small_word, text=lang, fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)

    global timer
    if timer:
        window.after_cancel(timer)
    timer = window.after(3000, func=flip_card)


def flip_card():
    trans_word = active_row[trans_lang]
    canvas.itemconfig(big_word, text=trans_word, fill="white")
    canvas.itemconfig(small_word, text=trans_lang, fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)

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
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, image=card_front_img)
small_word = canvas.create_text(SCREEN_WIDTH / 2, 150, text="Title", font=("Arial", 30, "italic"))
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
