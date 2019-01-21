from django.shortcuts import render
from django.views.generic import DetailView

from questionnaire.controllers.poll_controller import PollController
from questionnaire.models import Poll


class PollView(DetailView):
    template_name = "questionnaire/poll.html"
    context_object_name = "poll"

    def get_object(self, **kwargs):
        return Poll.objects.get_hash(self.kwargs["poll_hash"])

    def post(self, request, poll_hash):
        try:
            poll_controller = PollController(poll_hash)
            poll_controller.add_answer(request.POST)
            return render(request, "questionnaire/confirm.html", context={"poll_name": poll_controller.poll.name})
        except Exception as e:
            print(e)
