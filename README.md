# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 💡 Guiding Hints for Students

**"The hints are backwards"**
> Look at `check_guess`. When `guess > secret`, what message does it actually return?

**"I can never win even when I type the right number"**
> Add `print(type(secret), type(guess))` before the comparison. Are they the same type? Trace back to where `secret` gets passed in.

**"My attempts start at 1 before I even guess"**
> Find where `st.session_state.attempts` is first set. What's the value? What should it be?

**"After winning, New Game doesn't work"**
> What is `st.session_state.status` after you win? It needs to get reset to `"playing"`...

**"pytest fails right away"**
> Read the first failure message. `check_guess` returns a tuple — try `outcome, message = check_guess(...)` instead of `result = check_guess(...)`.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
