# 🃏 Flash Card App

A Python desktop application for learning French vocabulary using interactive flashcards. Cards automatically flip to reveal the English translation, and the app tracks your progress by removing words you've already learned.

---

## Features

- Displays a random French word on a flashcard
- Automatically flips the card after 5 seconds to show the English translation
- Mark words as **known** to remove them from future sessions
- Progress is saved between sessions — only unseen words are shown on next launch
- Clean, minimal GUI built with Tkinter

## Screenshots

<img width="893" height="750" alt="Screenshot 2026-06-15 at 14 14 03" src="https://github.com/user-attachments/assets/6c7b290b-f8b8-4c53-98ba-95d54476ae62" />

<img width="900" height="749" alt="Screenshot 2026-06-15 at 14 12 00" src="https://github.com/user-attachments/assets/0c7f53ba-7df3-40e6-8ddb-ef0c0a5cb5bc" />

## Requirements

- Python 3.x
- pandas

Install dependencies:

```bash
pip install pandas
```

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/abatima/flash-card-app.git
cd flash-card-app
```

2. Run the app:

```bash
python main.py
```

On first launch, the app loads from `data/french_words.csv`. As you mark words as known, a `data/words_to_learn.csv` file is created and used for all future sessions.

## How to Use

- When a card appears, try to recall the English translation.
- After 5 seconds, the card flips to reveal the answer.
- Click ✅ if you knew the word — it will be removed from your deck.
- Click ❌ if you didn't — it stays in the deck for next time.

## Project Structure

```
flash-card-app/
├── data/
│   ├── french_words.csv       # Full word list
│   └── words_to_learn.csv     # Auto-generated: words not yet learned
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
├── main.py
└── README.md
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
