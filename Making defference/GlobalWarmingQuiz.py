quiz = [
    {
        "question": "Which of the following gases is a major contributor to global warming?",
        "answers": [
            "Carbon dioxide (CO2)",
            "Oxygen (O2)",
            "Nitrogen (N2)",
            "Helium (He)\n"
        ],
        "correct_answer": 0
    },
    {
        "question": "What is the primary source of carbon dioxide emissions?",
        "answers": [
            "Fossil fuels",
            "Volcanoes",
            "Forest fires",
            "Decomposition of organic matter\n"
        ],
        "correct_answer": 0
    },
    {
        "question": "What is the main impact of global warming on the environment?",
        "answers": [
            "Rising sea levels",
            "Decreased rainfall",
            "Increased snowfall",
            "More frequent hurricanes\n"
        ],
        "correct_answer": 0
    },
    {
        "question": "Which of the following is a possible solution to reduce greenhouse gas emissions?",
        "answers": [
            "Renewable energy",
            "Banning air travel",
            "Planting more trees",
            "All of the above\n"
        ],
        "correct_answer": 3
    },
    {
        "question": "What is the current scientific consensus on the cause of global warming?",
        "answers": [
            "It is primarily caused by human activity",
            "It is primarily caused by natural factors",
            "There is no consensus",
            "It is not happening\n"
        ],
        "correct_answer": 0
    }
]


def administer_quiz():
    score = 0
    for question in quiz:
        print(question["question"])
        for i, answer in enumerate(question["answers"]):
            print(f"{i + 1}. {answer}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    if score == 5:
        print("Excellent")
    elif score == 4:
        print("Very good")
    else:
        print("Time to brush up on your knowledge of global warming.")
        print("Some useful websites to learn more:")
        print("- https://climate.nasa.gov/")
        print("- https://www.epa.gov/ghgemissions/sources-greenhouse-gas-emissions")
        print("- https://www.ipcc.ch/")


# Call the function to administer the quiz
administer_quiz()
