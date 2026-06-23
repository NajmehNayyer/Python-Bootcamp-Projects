# Flashcard App

Interactive desktop application for learning French vocabulary using spaced repetition.

## Features

- **Interactive Flashcard GUI** - Built with Tkinter, displays French words and auto-flips to show English translation after 3 seconds
- **Progress Tracking** - Marks learned words and only shows unlearned vocabulary
- **Persistent Storage** - Saves learning progress to CSV file across sessions
- **Button Lock Mechanism** - Prevents accidental clicks during card flip delay

## CSV Format

```
French,English,learnt
bonjour,hello,0
merci,thank you,0
```

## Usage

1. Update file paths in `main.py`
2. Run: `python main.py`
3. Click ✓ for known words, ✗ to skip
4. Progress auto-saves to CSV

## Preview

https://github.com/user-attachments/assets/929c1b0a-f41d-4efd-9a13-ded89ce3ab79
