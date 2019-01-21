class Questionaire {
    constructor() {
        const removeButton = $("<button>", {
            "class": "btn btn-secondary btn-sm",
            "html": "<i class='fas fa-trash-alt'></i>"
        }).on("click", () => {
            option.remove();

            this.options = this.options.filter(option => option !== optionInput);
        });
    }
}