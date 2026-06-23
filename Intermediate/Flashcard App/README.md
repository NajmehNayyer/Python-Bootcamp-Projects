# Flashcard App

Interactive desktop application for learning French vocabulary using spaced repetition.

## Features

- **Interactive Flashcard GUI** - Built with Tkinter, displays French words and auto-flips to show English translation after 3 seconds
- **Progress Tracking** - Marks learned words and only shows unlearned vocabulary
- **Persistent Storage** - Saves learning progress to CSV file across sessions
- **Button Lock Mechanism** - Prevents accidental clicks during card flip delay

## Python Concepts Used

**Object-Oriented Principles**
- Modular function design with single responsibilities
- State encapsulation using dictionary (`holder`) for current word tracking

**Data Handling**
- Pandas DataFrame for efficient CSV operations
- Boolean indexing to filter unlearned words: `df[df['learnt'] != 1]`
- DataFrame updates and persistence

**GUI Development**
- Tkinter Canvas for visual flashcard
- Image integration (PhotoImage)
- Widget state management (enabling/disabling buttons)
- Event binding with lambda functions

**Functional Programming**
- Pure functions for specific tasks
- Higher-order functions with `lambda`
- Timed execution using `window.after()`

## Project Structure

```
Flashcard App/
├── main.py
├── data/
│   └── french_words.csv
└── images/
    ├── card_front.png
    ├── right.png
    └── wrong.png
```

## Requirements

```bash
pip install pandas
```

## Usage

1. Update file paths in `main.py`
2. Run: `python main.py`
3. Click ✓ for known words, ✗ to skip
4. Progress auto-saves to CSV

## CSV Format

```
French,English,learnt
bonjour,hello,0
merci,thank you,0
```
