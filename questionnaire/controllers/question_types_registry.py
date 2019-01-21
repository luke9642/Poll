from questionnaire.models import TextChoice, TextareaChoice, RangeChoice, SingleChoice, \
    TextAnswer, TextareaAnswer, RangeAnswer, SingleAnswer


class Registry:
    __choices = {
        "Short Answer": {
            "choice": TextChoice,
            "answer": TextAnswer
        },
        "Long Answer": {
            "choice": TextareaChoice,
            "answer": TextareaAnswer
        },
        "Linear Scale": {
            "choice": RangeChoice,
            "answer": RangeAnswer
        },
        "Single Choice": {
            "choice": SingleChoice,
            "answer": SingleAnswer
        }
    }

    @classmethod
    def get_fields(cls):
        return cls.__choices.keys()

    @classmethod
    def choice_cls(cls, choice_type):
        return cls.__choices[choice_type]["choice"]

    @classmethod
    def answer_cls(cls, answer_type):
        return cls.__choices[answer_type]["answer"]
