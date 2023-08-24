from tkinter import *
import time
import tkinter as tk
from paras import para

tim = time.time()


def start_test():
    canvas = Canvas(width=660, height=200)
    canvas.config(highlightthickness=0, bg="grey")
    canvas.grid(row=0, column=0, columnspan=2)
    x, y =325, 100
    canvas.create_text(x, y, text=para[0], font=("Arial", 15), fill="white")
    typing_entry.delete(1.0, tk.END)
    typing_entry.focus()
    tim = time.time()


def checking_words():
    global para
    parag = para[0].replace("\n", "")

    par = parag.split(" ")
    for word in par:
        if "\n" in word:
            word.replace("\n", "")
            print(word)

    data = typing_entry.get(1.0, tk.END)
    data = data.split(" ")
    data = [dat for dat in data if dat != " "]
    wrong_words = {
        "Wrong Words": "Right Words",
    }
    if len(data) <= len(par):
        for wd in range(len(data)):
            if data[wd] != par[wd]:
                wrong_words[data[wd]] = par[wd]


    no_of_words = len(data)
    correct_characters = sum(1 for c1, c2 in zip(data, par) if c1 == c2)
    accuracy = (correct_characters / no_of_words) * 100

    wrong_canvas = Canvas(width=80, height=300, )
    right_canvas = Canvas(width=80, height=300, bg="CadetBlue")
    wrong_canvas.grid(row=4, column=0, pady=20)
    right_canvas.grid(row=4, column=1, pady=20)
    x, y = 40, 20
    for wrong, right in wrong_words.items():
        wrong_canvas.create_text(x, y, text="-" + wrong, font=("Arial", 10), fill="red")
        right_canvas.create_text(x, y, text="-" + right, font=("Arial", 10), fill="white")
        y += 20

    global tim
    total_time = round(time.time() - tim, 2)
    typing_speed = (no_of_words / total_time) * 60
    result = f"Speed: {typing_speed:.2f} WPM, Accuracy: {accuracy:.2f}%"
    speed_show_label = Label(text=result, foreground="DimGray", font=("Arial", 12))
    speed_show_label.grid(row=3, column=0)


if __name__ == '__main__':
    window = Tk()
    window.config(pady=50, padx=50, bg="Pink")
    typing_entry = Text(width=70, height=10,)
    typing_entry.grid(row=1, column=0, pady=10, columnspan=2)
    typing_entry.bind("<Return>", lambda event: checking_words())

    start_btn = Button(text="Start the Test", command=start_test)
    start_btn.grid(row=2, column=1, pady=5)

    window.mainloop()



