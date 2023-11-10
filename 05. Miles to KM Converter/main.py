from tkinter import *


def convert():
    user_entry = user_input.get()
    if not user_input.get().isdigit():
        response = 'Wrong Format'
    else:
        response = round(int(user_entry) * 1.6, 2)
    converted_response_label.config(text=response)


# Create a window
window = Tk()
window.title('Miles to Km Converter')
window.minsize(200, 150)
window.config(padx=20, pady=20)

# Labels
miles_label = Label()
miles_label.config(text='Miles', font=('Arial', 13), padx=30)
miles_label.grid(column=2, row=0)

is_equal_to_label = Label()
is_equal_to_label.config(text='is equal to', font=('Arial', 13), padx=30)
is_equal_to_label.grid(column=0, row=1)

converted_response_label = Label()
converted_response_label.config(text='0', font=('Arial', 13), pady=5)
converted_response_label.grid(column=1, row=1)

km_label = Label()
km_label.config(text='Km', font=('Arial', 13))
km_label.grid(column=2, row=1)

# Entry
user_input = Entry(width=15)
user_input.grid(column=1, row=0)

# Button
button = Button(text='Calculate', command=convert, font=('Arial', 11, 'bold'))
button.grid(column=1, row=2)

# Keep the window open
window.mainloop()
