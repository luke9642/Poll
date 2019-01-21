class ChoicesMapper {
    static mapChoiceToClass(choice) {
        switch (choice) {
            case "Short Answer":
                return ShortAnswerChoice;
            case "Linear Scale":
                return LinearScaleChoice;
            case "Long Answer":
                return LongAnswerChoice;
            case "Single Choice":
                return SingleChoice;
        }
    }
}