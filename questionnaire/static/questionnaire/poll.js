'use strict';

class Poll {
    constructor() {
        this._questions = [];
        this.form = $("#poll");
        this.title = $("#poll-title");
    }

    get questions() {
        return this._questions;
    }

    async addQuestion() {
        const newQuestion = new Question();
        this.questions.push(newQuestion);

        const questionTypesOptions = await JSONDataRegistry.getQuestionTypes();
        newQuestion.html = questionTypesOptions["question_types"];
        newQuestion.addEvents(this);
        $("#poll ul").append($("<li>", {
            "class": "list-group-item py-4"
        }).append(newQuestion.html));

        newQuestion.changeQuestionType(questionTypesOptions["question_types"][0]);
    }

    removeQuestion(questionId) {
        const index = this.getQuestionIndex(questionId);
        if (index !== -1) {
            this.form.find("#" + questionId).first().parent().remove();
            this.questions.splice(index, 1);
        }
    }

    getQuestionIndex(questionId) {
        return this.questions.findIndex(question => question.questionNumber === Number(questionId));
    }

    save(event) {
        event.preventDefault();

        const questionsValues = this.questions
            .map(question => question.getValues());

        const anyQuestionsRequired = questionsValues
            .map(question => question.question_required)
            .reduce((a, b) => a + b, 0);

        const questionsNamesSet = new Set(questionsValues
            .map(question_value => question_value.question_name));

        if (questionsNamesSet.size !== questionsValues.length) {

            $(".container").prepend($("<div>", {
                "class": "alert alert-danger sticky-top",
                "html": "Questions names cannot duplicate" +
                    "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">\n" +
                    "    <span aria-hidden=\"true\">&times;</span>\n" +
                    "  </button>"
            }));

        }
        else if (anyQuestionsRequired === 0) {
            $(".container").prepend($("<div>", {
                "class": "alert alert-danger sticky-top",
                "html": "At least one question must be required" +
                    "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">\n" +
                    "    <span aria-hidden=\"true\">&times;</span>\n" +
                    "  </button>"
            }));
        }
        else {
            JSONDataRegistry.sendPoll({
                "poll": questionsValues,
                "title": this.title.val()
            });
        }
    }

    addEvents() {
        this.form.on("submit", event => this.save(event));
        $("#add-question").on("click", () => this.addQuestion());
    }
}