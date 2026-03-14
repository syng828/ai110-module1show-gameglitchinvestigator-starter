# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game UI displayed input and hints, but the behavior was broken. The secret number changed unexpectedly and hints were often opposite. The game still looked like a basic number guesser, but it was not playable.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
- The secret number changed after each submit even without winning. The hints were backward (it said go higher when the secret was lower). The history only showed the previous guess, not the current one. The attempts-left count and final state were off by one, and the score could go negative. The new game button did not fully reset the game state.


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Copilot and Claude while working on bug fixes and testing. They helped suggest code edits and tests for logic functions.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI correctly pointed out scoring bugs where too-high feedback added points and that score could go negative. I verified this by running tests and checking score updates for too high and too low outcomes.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
An AI suggestion was misleading when it assumed Streamlit was running in the right environment without activating the venv. I verified by running the terminal manually with `.
venv\Scripts\python.exe -m streamlit run app.py` and then it worked.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 
  I reviewed the code logic and ran unit tests. I also tested the Streamlit app manually in the browser. When the output matched expected values for attempts, score, and hints, I considered the bug fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran pytest and created tests for `check_guess` to verify correct hints and for `update_score` to prevent negative scores. The tests passed and confirmed the core logic behaved correctly.
- Did AI help you design or understand any tests? How?
Yes, AI helped by quickly generating test cases and guiding where to add assertions for bug fixes. It made test creation faster and helped verify fixes systematically.
---

## 4. What did you learn about Streamlit and state?

<<<<<<< HEAD
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? 
  Streamlit reruns the whole script on each user action, like pressing a button or changing input. Session state stores values between reruns so the game can remember state such as the secret number and score. This prevents the app from resetting on every click and makes interactive behavior stable.

- What change did you make that finally gave the game a stable secret number?
  I stored the secret number in `st.session_state` and only initialized it once when the key was missing. That ensured future reruns kept the same secret until the user clicked New Game, which then explicitly reset session state.
=======
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
>>>>>>> 65c93e357d6e1a97f6329182b0ef76461058bb6b


## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? 
  I want to keep writing tests for the bug scenarios and confirm they pass before moving on. I also want to keep using small incremental fixes and verify each change.
- What is one thing you would do differently next time you work with AI on a coding task? 
  I would start by explicitly asking for simplified explanations and focused test examples earlier. That helps avoid confusion and makes the process smoother.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project showed me AI code can save time, but it still needs careful review and tests. I now trust AI for suggestions, but I always verify output with logic and unit tests.
