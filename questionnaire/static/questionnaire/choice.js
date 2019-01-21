class Choice {
    constructor(parentBlock) {
        this.parentBlock = parentBlock;
        this.parentBlock.empty();

    }

    getValues() {
        return {}
    };
}


class ShortAnswerChoice extends Choice {
    constructor(parentBlock) {
        super(parentBlock);

        this.content = $("<input>", {
            "class": "form-control",
            "type": "text",
            "placeholder": "short answer text",
            "readonly": "readonly"
        });

        this.parentBlock.append(this.content);
    }
}


class LongAnswerChoice extends Choice {
    constructor(parentBlock) {
        super(parentBlock);

        this.content = $("<textarea>", {
            "class": "form-control",
            "placeholder": "long answer text",
            "rows": "3",
            "readonly": "readonly"
        });

        this.parentBlock.append(this.content);
    }
}


class LinearScaleChoice extends Choice {
    constructor(parentBlock) {
        super(parentBlock);
        this.values = [];

        const wrapper = $("<div>", {
            "class": "input-group"
        });

        $.each([1, 5], (index, elem) => {
            const content = $("<input>", {
                "class": "form-control",
                "type": "number",
                "value": elem
            });
            this.parentBlock.append(wrapper.append(content));
            this.values.push(content);
        });
    }

    getValues() {
        return {
            "value_min": this.values[0].val(),
            "value_max": this.values[1].val()
        }
    };
}


class SingleChoice extends Choice {
    constructor(parentBlock) {
        super(parentBlock);

        this.options = [];

        this.addOptionButton();
        this.addOption();
    }

    addOption() {
        const optionInput = $("<input>", {
            "class": "form-control form-control-sm",
            "type": "text",
            "placeholder": "Option " + (this.options.length + 1)
        });

        const circle = $("<i>", {
            "class": "far fa-circle mr-2",
            "css": {
                "font-size": "24px",
                "line-height": "31px"
            }
        });

        const option = $("<div>", {
            "class": "form-group d-flex"
        });

        const removeButton = $("<button>", {
            "class": "btn btn-secondary btn-sm",
            "html": "<i class='fas fa-trash-alt'></i>"
        }).on("click", () => {
            option.remove();

            this.options = this.options.filter(option => option !== optionInput);
        });

        const inputGroupAppend = $("<div>", {
            "class": "input-group-append"
        }).append(removeButton);

        const inputGroup = $("<div>", {
            "class": "input-group w-auto"
        });

        option.append(circle).append(inputGroup.append(optionInput).append(inputGroupAppend));

        this.options.push(optionInput);
        this.addOptionButton.before(option);
    }

    addOptionButton() {
        this.addOptionButton = $("<div>", {
            "class": "text-muted",
            "css": {
                "font-size": "24px",
                "cursor": "pointer"
            }
        });

        this.addOptionButton
            .on("mouseenter", () => {this.addOptionButton.removeClass("text-muted")})
            .on("mouseleave", () => {this.addOptionButton.addClass("text-muted")});

        this.addOptionButton.append($("<i>", {
            "class": "fas fa-plus-circle mr-3"
        }));

        this.addOptionButton.append($("<span>", {
            "text": "add option"
        }));


        this.addOptionButton.on("click", () => this.addOption());

        this.parentBlock.append(this.addOptionButton);
    }

    getValues() {
        return this.options.map(option => option.val())
    };
}