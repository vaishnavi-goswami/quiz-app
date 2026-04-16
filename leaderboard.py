import json

FILE = "scores.json"

def load_scores():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_score(name, score):
    scores = load_scores()
    scores.append({"name": name, "score": score})

    scores = sorted(scores, key=lambda x: x["score"], reverse=True)

    with open(FILE, "w") as f:
        json.dump(scores, f, indent=4)

def show_leaderboard():
    scores = load_scores()
    print("\nLeaderboard")
    print("-" * 20)

    for i, s in enumerate(scores[:5], 1):
        print(f"{i}. {s['name']} - {s['score']}")