from logic_utils import (
    append_guess,
    attempts_left,
    check_guess,
    reset_game_state,
    update_score,
)

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_hint_too_high_says_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_hint_too_low_says_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_attempts_left_stops_at_zero():
    assert attempts_left(0, 8) == 8
    assert attempts_left(7, 8) == 1
    assert attempts_left(8, 8) == 0
    assert attempts_left(10, 8) == 0


def test_score_cannot_go_negative():
    assert update_score(0, "Too Low", 1) == 0
    assert update_score(5, "Too Low", 1) == 0


def test_new_game_resets_state():
    state = reset_game_state("Normal")
    assert state["attempts"] == 0
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []
    assert 1 <= state["secret"] <= 100


def test_history_append_has_all_values():
    history = []
    append_guess(history, 5)
    append_guess(history, 12)
    append_guess(history, 9)
    assert history == [5, 12, 9]

