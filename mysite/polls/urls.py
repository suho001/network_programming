from django.urls import path
from . import views

from django.urls import path
from .views import PollsModelView, QuestionList, ChoiceList, QuestionDetail, ChoiceDetail

app_name = 'polls'
urlpatterns = [
    path('', PollsModelView.as_view(), name='index'),
    path('questions/', QuestionList.as_view(), name='question_list'),
    path('choices/', ChoiceList.as_view(), name='choice_list'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='question_detail'),
    path('choices/<int:pk>/', ChoiceDetail.as_view(), name='choice_detail'),
]