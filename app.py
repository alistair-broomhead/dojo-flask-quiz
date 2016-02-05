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
        "incorrect answer",
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


@app.route("/", methods=["POST"])
def answer():
    form = flask.request.form
    answers = list(form.items())
    # We assume that there is only one answer for now
    question_number, given_answer = answers[0]
    question_number = int(question_number)

    question, correct_answer, *incorrect_answers = quiz[question_number]

    return render_template(
        'result.html',
        question_number=question_number,
        question=question,
        correct_answer=correct_answer,
        given_answer=given_answer,
    )


if __name__ == "__main__":
    app.run(debug=True)
