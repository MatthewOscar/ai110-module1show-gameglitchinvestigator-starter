from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High" with a LOWER hint
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low" with a HIGHER hint
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_check_guess_requires_int_secret():
    # Secret should always be an int — string comparison would break this
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low"  # "9" > "50" is True in string compare, so this catches the bug
