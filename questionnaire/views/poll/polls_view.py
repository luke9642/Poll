from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import ListView

from questionnaire.controllers.poll_controller import PollController


class PollsView(LoginRequiredMixin, ListView):
    template_name = "questionnaire/polls.html"
    context_object_name = "polls"

    def get_queryset(self):
        return PollController.get_author_polls(author=self.request.user)

    def delete(self, request):
        try:
            poll_controller = PollController(poll_hash=request.body.decode("utf-8"))
            poll_controller.delete_poll()
        except Exception as e:
            print(e)
            return JsonResponse({
                "status": "Could not delete poll"
            }, status=400)

        return JsonResponse({"status": "Successfully removed poll"})
