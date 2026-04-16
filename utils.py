import random

def get_random_questions(questions, limit=3):
    return random.sample(questions, min(limit, len(questions)))