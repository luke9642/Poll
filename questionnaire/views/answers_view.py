from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from questionnaire.controllers.poll_controller import PollController


class AnswersView(LoginRequiredMixin, ListView):
    template_name = "questionnaire/answers.html"
    context_object_name = "answers"
    paginate_by = 1

    def get_queryset(self):
        return PollController(self.kwargs["poll_hash"]).get_all_answers()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["poll"] = PollController(poll_hash=self.kwargs["poll_hash"]).poll
        return context
