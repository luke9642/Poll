'use strict';

class Question {
    constructor(name, type, choice, required=false) {
        this.name = name;
        this.type = type;
        this.choice = choice;
        this.required = required;
        this.questionNumber = Question.numberOfQuestions;
        Question.numberOfQuestions++;
    }

    static get numberOfQuestions() {
        return this._numberOfQuestions;
    }

    static set numberOfQuestions(value) {
        this._numberOfQuestions = value;
    }


    get html() {
        return this._html;
    }

    set html(value) {
        if (!this._html)
            this._html = this.getHTML(value);
    }

    getHTML(questionTypesOptions) {
        this.type = questionTypesOptions[0];

        this.content = $("<div>", {
            "class": "content mb-3"
        });

        return $("<div>", {
            "id": this.questionNumber,
            "class": "question form-group"
        }).append(this.getHeaderGroup(questionTypesOptions)).append(this.content).append(this.getFooterGroup());
    };

    changeQuestionType(type) {
        this.html.find("#header select").val(type).trigger("change")
    }

    getHeaderGroup(questionTypesOptions) {
        this.headerQuestionName = $("<input>", {
            "class": "header form-control form-control-lg",
            "type": "text",
            "placeholder": "Question text",
            "required": "required",
            "css": {
                "flex": "2"
            }
        });

        this.questionTypes = $("<select>", {
            "class": "custom-select custom-select-lg"
        }).on("change", event => {
            this.type = $(event.currentTarget).val();
            // const block = $(event.currentTarget).closest(".question").find(".content").first();
            // const currentFields = questionTypesOptions.filter(option => option.name === this.type)[0].fields;
            this.choice = new (ChoicesMapper.mapChoiceToClass(this.type))(this.content);
        });

        $.each(questionTypesOptions, (index, option) => {
            this.questionTypes.append($("<option>", {
                "value": option,
                "text": option
            }));
        });

        return $("<div>", {
            "id": "header",
            "class": "input-group input-group-lg mb-3"
        }).append(this.headerQuestionName).append(this.questionTypes);
    }

    getFooterGroup() {
        this.requiredCheckbox = $("<input>", {
            "id": "defaultCheck" + this.questionNumber,
            "class": "custom-control-input",
            "type": "checkbox"
        });

        const required = $("<div>", {
            "class": "required custom-control custom-checkbox"
        }).append(this.requiredCheckbox).append($("<label>", {
            "class": "custom-control-label",
            "for": "defaultCheck" + this.questionNumber,
            "text": "required"
        }));

        this.removeButton = $("<div>", {
            "class": "remove-question btn btn-outline-danger",
            "html": "<i class='fas fa-trash-alt'></i>"
        });

        const groupPrepend = $("<div>", {
            "class": "input-group-prepend"
        });

        const groupAppend = $("<div>", {
            "class": "input-group-append"
        });

        const requiredGroup = groupPrepend.append($("<div>", {
            "class": "input-group-text"
        }).append(required));

        const removeGroup = groupAppend.append(this.removeButton);

        return $("<div>", {
            "class": "input-group justify-content-end"
        }).append(requiredGroup).append(removeGroup);
    }

    getValues() {
        return {
            "question_name": this.headerQuestionName.val(),
            "question_type": this.questionTypes.val(),
            "question_required": this.requiredCheckbox[0].checked,
            "question_choice": this.choice.getValues()
        }
    }

    addEvents(poll) {
        this.removeButton.on("click", () => poll.removeQuestion(this.questionNumber));
    }
}

Question.numberOfQuestions = 0;