from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView, RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name="polls"), name='index'),
    path('user/register/', views.UserRegisterView.as_view(), name='register'),
    path('user/login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('user/logout/', LogoutView.as_view(next_page="login"), name='logout'),
    path('polls/', views.PollsView.as_view(), name='polls'),
    path('poll/new/', views.CreatePollView.as_view(), name='poll_create'),
    path('poll/<poll_hash>/answers/summary/', views.SummaryView.as_view(), name='summary'),
    path('poll/<poll_hash>/answers/page-<int:page>/', views.AnswersView.as_view(), name='answers'),
    path('poll/<poll_hash>/answers/', views.AnswersView.as_view(), name='answers'),
    path('poll/<poll_hash>/', views.PollView.as_view(), name='poll_view'),
    path('poll/<poll_hash>/', views.PollView.as_view(), name='poll_answer'),
    path('confirm/', TemplateView.as_view(template_name="questionnaire/confirm.html"), name='confirm'),
    path('question-types/', views.QuestionTypes.as_view(), name='question-types')
]
