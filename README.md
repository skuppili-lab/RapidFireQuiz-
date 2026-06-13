Python Timed Quiz Game ⏱️🧠
<br>
A fun, interactive, command-line quiz game built in Python. Test your knowledge of India with randomized multiple-choice questions and a strict time limit!
<br>
Features ✨
<br>
Randomized Questions: Questions are selected completely at random and are never repeated during a single playthrough.
Shuffled Options: The multiple-choice options (1-4) are randomized every time using Python's random.sample(), so you can't just memorize the option numbers!
Per-Question Timer: You have exactly 15 seconds to answer each question (tracked using time.perf_counter()). Take too long, and the game ends!
Live Scoring & Total Time: The game tracks your current score and, at the end of the game, displays your final score along with the total time you spent playing.
Immediate Feedback: Instantly tells you if your answer was correct or incorrect. If you get it wrong, it kindly reveals the correct answer.
Prerequisites 🛠️
<br>
Python 3.x installed on your system.
No external libraries required! This project uses only built-in Python modules (random and time).
How to Play 🕹️
Open your terminal or command prompt.
Navigate to the folder containing the script.
Run the script using Python:
bash
<br>
python Quiz_game_with_timer.py
Read the question and the 4 options provided.
Type the number (1, 2, 3, or 4) corresponding to your answer and press Enter.
Be quick! You only have 15 seconds per question.
Game Rules 📜
<br>
Answer correctly to increase your score and proceed to the next question.
If you answer incorrectly, the game ends immediately and reveals the right answer.
If you take longer than 15 seconds on a single question, you will "Time out" and the game ends.
Answer all questions correctly to win the game!
<br>
Code Structure 💻
questions_set: A dictionary mapping the question string to a tuple of 4 possible options.
answer_set: A dictionary mapping the question string to the exact correct answer string.
unasked_questions: A list that tracks which questions haven't been asked yet to prevent repetition.
