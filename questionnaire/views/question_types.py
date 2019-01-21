from django.http import JsonResponse
from django.views import View

from questionnaire.controllers.question_types_registry import Registry


class QuestionTypes(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"question_types": list(Registry.get_fields())})
