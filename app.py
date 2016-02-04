import flask
import random as rand
from flask import render_template


app = flask.Flask("Quiz")
number_of_questions = 4
quiz = tuple(
    (
        "question {}".format(i),
        "correct_answer",
        "incorrect answer",
        "incorrect answer",
        "incorrect answer"
    ) for i in range(number_of_questions)
)


@app.route("/")
def root():
    random_number = rand.randint(0, number_of_questions - 1)
    question, *answers = quiz[random_number]
    answers = list(answers)
    rand.shuffle(answers)

    return render_template(
        'index.html',
        question_number=random_number,
        question=question,
        answers=answers
    )


if __name__ == "__main__":
    app.run()
