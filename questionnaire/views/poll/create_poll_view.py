import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse
from django.views.generic import TemplateView

from questionnaire.controllers.poll_controller import PollController


class CreatePollView(LoginRequiredMixin, TemplateView):
    template_name = "questionnaire/form.html"

    def post(self, request):
        try:
            data = json.loads(request.body)
            PollController.create_poll(data["title"], request.user, data["poll"])
        except Exception as e:
            print(e)
            return JsonResponse({"status": "Could not add new poll"}, status=400)

        return JsonResponse({
            "redirect": reverse("polls"),
            "status": "Successfully added new poll"
        })
