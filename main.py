from questions import questions
from leaderboard import save_score, show_leaderboard
from utils import get_random_questions

def run_quiz():
    name = input("Enter your name: ")
    score = 0

    selected_questions = get_random_questions(questions, 3)

    for q in selected_questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)

        ans = input("Your answer: ").upper()

        if ans == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}")

    print(f"\n{name}, your final score: {score}")

    save_score(name, score)
    show_leaderboard()

run_quiz()