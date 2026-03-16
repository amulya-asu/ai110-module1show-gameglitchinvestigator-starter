# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game had 3 levels, Easy (1-20), Medium(1-100) and Hard(1-50), It had Developer Debug Info to check actual number to expected output as well. Each level had different number of attempts. 
- List at least two concrete bugs you noticed at the start  
Bug1: Lucky number = 32, but when 31 was sent as input it asked for number lower , similarly for 35 it said to go higher.
Bug2: It takes any number as input although there is a specified range. Ex: It took 105 as input.
Bug 3: Expected number in difficulty Easy is 1-20 but secret number assigned is 42.
  

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude code and Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I pointed out bugs with enough examples for it to understand, like answered in first question.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Copilot simply inserted logic_utils.py to test_game_logic.py when they are in different directories.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Check in pytest, and check with some outputs in streamlit.
- Describe at least one test you ran (manual or using pytest)  and what it showed you about your code.
  One of the tests I ran was test_guess_too_high, which checks how the game responds when the player’s guess is higher than the secret number:
def test_guess_too_high():
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")
    - It correctly identifies that 60 is higher than 50, returning the status "Too High"
    - It produces the correct hint message, “Go LOWER!”, which had previously been reversed due to a logic bug.

- Did AI help you design or understand any tests? How?
I used AI understand where logic was going wrong and how to fix it. For example : updation of score for wrong guess.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
In the original version of the app, the code called random.randint(low, high) at the top of app.py every time the script ran. Because Streamlit reruns the entire script on every user interaction, the secret number was regenerated constantly. Even clicking a button or typing a guess caused a full rerun, so the secret number never stayed the same long enough for the player to win.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
A Streamlit rerun is like refreshing a webpage from the top every time you interact with it. All normal variables reset on each rerun. st.session_state works like a small notepad that survives these reruns. Anything stored there stays the same across interactions, which is why it’s the right place to keep the secret number.

- What change did you make that finally gave the game a stable secret number?
The solution was to wrap the secret number generation in a condition:
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)


This ensures the number is created only once, the first time the app loads. After that, Streamlit reruns skip this block because the key already exists, so the secret number stays consistent.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I believe testing before debugging, understanding structure of the code from root and how each function call is made to trace the errors. When in doubt and complexity of code we should ask AI to explain it in simple terms and try to understand developer's intent behind the code structure and logic.

- What is one thing you would do differently next time you work with AI on a coding task?
The next time I would take my time to clearly understand the flow of application, before anything I would first try to understand how a user will be interacting with the application, instead of simply asking ai to fix the code, I would ask few questions and plan, then try to debug a project. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I had a strong belief the there is an extent to which ai can help us code and once it's threshold is reached, it cannot provide better results. But right now I think, we need to well aware and equipped before we prompt the agent/chatbot, because when we cannot figure out if something is right or wrong just by copy pasting ai code, but validating it in real-time will help get us better. 
