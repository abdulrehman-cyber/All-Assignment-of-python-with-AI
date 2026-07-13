
questions = (
    "How many elements are in periodic table?",
    "Which animal lays largest eggs?",
    "Who is the founder of pakistan?",
    "How many bones are there in the human body?",
    "Who invented bulb?"
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Allama Iqbal", "B. Indra Gandhi", "C. Muhammad Ali Jinnah", "D. Lord Mountbatten"),
    ("A. 206", "B. 207", "C. 208", "D. 210"),
    ("A. Nikola Tesla", "B. Thomas Edison", "C. Rutherford", "D. Galileo")
)

answers = ("C", "D", "C", "A", "B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Choose the correct option: ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")

    question_num += 1

# Results
print("--------------------------------")
print("             RESULTS            ")
print("--------------------------------")

print("answers:", " ".join(answers))
print("guesses:", " ".join(guesses))

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")