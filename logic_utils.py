import random

#FIX: Refactored logic into logic_utils.py with Copilot
def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    if raw is None or raw == "":
        return False, None, "Enter a guess."
    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."
    return True, value, None


def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"
    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        #FIX: Used Claude to fix the hint logic. 
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"

#FIX: The min score is 0 points and cannot go lower fixed with Copilot 
def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        current_score += points
    elif outcome == "Too High":
        current_score -= 5 # FIX: With Copilot added score penalty for wrong guesses
    elif outcome == "Too Low":
        current_score -= 5
    if current_score < 0:
        current_score = 0
    return current_score

#FIX: Added attempts_left with Copilot to calculate remaining attempts 
def attempts_left(attempts: int, attempt_limit: int):
    return max(0, attempt_limit - attempts)


def append_guess(history: list, guess):
    history.append(guess)
    return history


def reset_game_state(difficulty: str):
    low, high = get_range_for_difficulty(difficulty)
    return {
        "secret": random.randint(low, high),
        "attempts": 0,
        "score": 0,
        "status": "playing",
        "history": [],
    }

