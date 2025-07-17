import json
import random
from typing import List, Dict


def load_questions(filename: str) -> List[Dict]:
    """Load questions from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    return questions


def run_quiz(questions: List[Dict]) -> None:
    """Run the quiz interactively in the terminal."""
    random.shuffle(questions)
    score = 0
    for idx, q in enumerate(questions, start=1):
        print(f"\nQuestion {idx} ({q['category']}): {q['question']}")
        for i, option in enumerate(q['options']):
            print(f"  {i + 1}. {option}")
        while True:
            try:
                choice = int(input("Your answer (number): ")) - 1
                if 0 <= choice < len(q['options']):
                    break
                else:
                    print("Please enter a valid option number.")
            except ValueError:
                print("Please enter a number.")
        if choice == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            correct_option = q['options'][q['answer']]
            print(f"Incorrect. The correct answer was: {correct_option}\n")
    print(f"Quiz finished! You scored {score}/{len(questions)}.")


def main() -> None:
    questions = load_questions('questions.json')
    run_quiz(questions)


if __name__ == '__main__':
    main()
