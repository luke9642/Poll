class JSONDataRegistry {
    static get questionTypes() {
        return this._questionTypes;
    }

    static set questionTypes(value) {
        this._questionTypes = value;
    }

    static async getQuestionTypes() {
        if (JSONDataRegistry.questionTypes !== null)
            return JSONDataRegistry.questionTypes;

        return await $.ajax({
            url: questionTypesUrl,
            dataType: "json",
            success: result => {
                JSONDataRegistry.questionTypes = result;
            },
            error: result => {
                console.log(result);
            }
        });
    }

    static sendPoll(poll) {
        $.ajax({
            url: sendFormUrl,
            method: "POST",
            data: JSON.stringify(poll),
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            success: result => {
                window.location.href = result.redirect;
            },
            error: result => {
                console.log(result);
            }
        });
    }

    static removePoll(poll) {
        $.ajax({
            url: deletePollUrl,
            method: "DELETE",
            data: poll.id,
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            success: result => {
                poll.remove();
            },
            error: result => {
                console.log(result);
            }
        });
    }
}

JSONDataRegistry.questionTypes = null;

$.ajaxSetup({
    headers: {'X-CSRFToken': csrftoken}
});