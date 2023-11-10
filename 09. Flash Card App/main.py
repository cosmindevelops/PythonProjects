from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ('Ariel', 30, 'italic')
FONT_WORD = ('Ariel', 50, 'bold')

# --------------------------- DATA SETUP ------------------------------ #
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    if data.empty:
        raise pandas.errors.EmptyDataError
except (FileNotFoundError, pandas.errors.EmptyDataError):
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# --------------------------- CARD LOGIC ------------------------------ #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    try:
        current_card = random.choice(to_learn)
    except IndexError:
        canvas.itemconfig(card_title, text='You\'ve learned all the words!', fill='black')
        canvas.itemconfig(card_word, text='', fill='black')
        canvas.itemconfig(card_background, image=front_card_img)
        unknown_button.config(state='disabled')
        known_button.config(state='disabled')
        reset_button.grid(column=0, row=2, columnspan=2)  # Afișează butonul de reset
    else:
        canvas.itemconfig(card_title, text='French', fill='black')
        canvas.itemconfig(card_word, text=current_card['French'], fill='black')
        canvas.itemconfig(card_background, image=front_card_img)
        flip_timer = window.after(3000, func=flip_card)


def is_known():
    try:
        to_learn.remove(current_card)
        data = pandas.DataFrame(to_learn)
        data.to_csv('data/words_to_learn.csv', index=False)
    except ValueError:
        canvas.itemconfig(card_title, text='You\'ve learned all the words!', fill='black')
        canvas.itemconfig(card_word, text='', fill='black')
        canvas.itemconfig(card_background, image=front_card_img)
        unknown_button.config(state='disabled')
        known_button.config(state='disabled')
        reset_button.grid(column=0, row=2, columnspan=2)
    else:
        next_card()


def reset_list():
    global to_learn, original_data
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
    reset_button.grid_forget()
    unknown_button.config(state='active')
    known_button.config(state='active')
    next_card()


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=back_card_img)


# ---------------------------- UI SETUP ------------------------------- #

# Window Setup
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas Setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file='images/card_front.png')
back_card_img = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=front_card_img)
card_title = canvas.create_text(400, 150, text='Title', font=FONT_TITLE)
card_word = canvas.create_text(400, 263, text='word', font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

# Buton Setup
cross_img = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_img = PhotoImage(file='images/right.png')
known_button = Button(image=check_img, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

reset_button = Button(text='Reset List', command=reset_list)
reset_button.grid(column=0, row=2, columnspan=2)
reset_button.grid_forget()

next_card()

window.mainloop()
