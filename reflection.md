# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The hints were backwards! Guessing too high told me to go higher, which made the game unwinnable. On even-numbered attempts the secret was silently cast to a string, so comparisons broke in subtle ways that were hard to spot without reading the code carefully.

---

## 2. How did you use AI as a teammate?

Used Copilot with `#file:app.py` and `#file:logic_utils.py` for context. It correctly identified the swapped hint messages. For the string coercion bug it suggested adding more type-checking inside `check_guess`, which I rejected — the right fix was removing the `str()` cast at the call site, not patching around it.

---

## 3. Debugging and testing your fixes

Ran `pytest` after each fix and manually played the game to confirm the hints were correct. The `test_check_guess_requires_int_secret` test was the most useful since it caught the string comparison bug by checking that `check_guess(9, 50)` returns `"Too Low"` rather than `"Too High"` as string compare would give.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the whole script on every interaction, so any variable not stored in `st.session_state` resets on each click. The secret was already guarded correctly, so the real state bugs were in `New Game` not resetting `status`, `score`, and `history`.

---

## 5. Looking ahead: your developer habits

Writing a targeted test right after a fix is a habit worth keeping because it takes a minute and makes regression obvious later. AI suggestions that add complexity rather than remove the root cause are usually a sign to push back and ask "why does this exist at all?"
