# Medical Quiz Application

This repository provides a simple command-line quiz application for
medical students or professionals. Questions are stored in a JSON file so
new questions can easily be added without modifying the source code.

## Requirements

- Python 3.7+

## Usage

1. Install Python if not already available.
2. Run the quiz:

```bash
python quiz.py
```

Answer each question by typing the number of the chosen option.
A summary of your score will appear at the end of the quiz.

## Adding Questions

Questions are stored in `questions.json`. Each question has a category,
its text, an array of possible options, and the index of the correct
answer. Example entry:

```json
{
  "category": "Cardiology",
  "question": "Which organ pumps blood throughout the body?",
  "options": ["Heart", "Liver", "Lung", "Kidney"],
  "answer": 0
}
```

Add more entries to the JSON array to extend the quiz.

## Future Improvements

This basic application can be expanded with features such as:

- Question difficulty levels.
- A timer for each question.
- Review of correct answers after completing the quiz.

Feel free to experiment and enhance the application to suit your needs.
