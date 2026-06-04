import tkinter as tk
import pandas as pd
from tkinter import messagebox

# --- Constants --- #
holder = {"fr_word": None}
BACKGROUND_COLOR = "#B1DDC6"
IMG_WI = 800
IMG_HI = 526
WIN_WI = IMG_WI + 50
WIN_HI = IMG_HI + 50


# --- Functions --- #
def pick_a_word():
    """Pick a random word from the words we haven't answered or answered wrong."""
    # Check if the word has been learnt
    filtered_df = df[df['learnt'] != 1]
    # Pick a random row
    word = filtered_df.sample(n=1).iloc[0]
    # Get the French and English word
    fr_word = word["French"]
    eng_word = word["English"]
    # Return the words
    return fr_word, eng_word


def flip(display_word):
    """Show the translation."""
    # Write the meaning and language of translation
    canvas.itemconfig(word_txt, text=display_word)
    canvas.itemconfig(lang_txt, text="English")


def display():
    """Display a new word, wait three seconds to flip and lock the buttons in the meantime."""
    global holder
    # Pick a random word
    fr_word, eng_word = pick_a_word()
    # Write the word and its language
    canvas.itemconfig(word_txt, text=fr_word)
    canvas.itemconfig(lang_txt, text="French")
    # Disable buttons for 3 seconds
    check_butt.config(state="disabled")
    window.after(3000, lambda: check_butt.config(state="normal"))
    cross_butt.config(state="disabled")
    window.after(3000, lambda: cross_butt.config(state="normal"))
    # Wait 3 seconds then flip the card
    window.after(3000, lambda: flip(eng_word))
    holder["fr_word"] = fr_word


def check_cmd():
    """Save the word as learnt and display the next card."""
    global holder, df
    df.loc[df["French"] == holder["fr_word"], "learnt"] = 1
    display()


def cross_cmd():
    """Display the next card."""
    display()


# --- Load the data --- #
df_path = r"E:\PycharmProjects\PythonProject\100DaysofCodePython\day-31\flash-card\data\french_words.csv"
df = pd.read_csv(df_path)

# --- Check if the status of the word is specified --- #
if "learnt" not in df.columns:
    df["learnt"] = 0

current_fr_word = None

# --- Create the window --- #
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# --- Create the flashcard as a canvas that fills the window --- #
# Create the canvas
canvas = tk.Canvas(width=IMG_WI, height=IMG_HI, bg="white", highlightthickness=0)
flashcard_img = tk.PhotoImage(file=r"E:\PycharmProjects\PythonProject\100DaysofCodePython\day-31\flash-card\images\card_front.png")
# Put the image on the canvas
card_img = canvas.create_image(IMG_WI, IMG_HI, image=flashcard_img)
# Display the image on both columns of the top row
canvas.grid(row=0, column=0, columnspan=2)

# Lock the window
window.resizable(False, False)

# --- Display the texts --- #
word_txt = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "italic"))
lang_txt = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))

# --- Create the correct answer button --- #
check_img = tk.PhotoImage(file=r"E:\PycharmProjects\PythonProject\100DaysofCodePython\day-31\flash-card\images\right.png")
check_butt = tk.Button(image=check_img, highlightthickness=0)
check_butt.grid(row=1, column=0)

# --- Create the wrong answer button --- #
cross_img = tk.PhotoImage(file=r"E:\PycharmProjects\PythonProject\100DaysofCodePython\day-31\flash-card\images\wrong.png")
cross_butt = tk.Button(image=cross_img, highlightthickness=0, command=cross_cmd)
cross_butt.config(padx=20)
cross_butt.grid(row=1, column=1)

# --- Start the flashcards --- #
display()
check_butt.config(command=lambda: check_cmd())

df.to_csv(df_path, index=False)
window.mainloop()
