from django.views.generic.base import TemplateView
from django.views.generic import  ListView
from django.views.generic import  DeleteView
from polls.models import Question, Choice

# Create your views here.

#--- TemplateView
class PollsModelView(TemplateView):
    template_name = 'polls/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Question', 'Choice']
        return context

    #---ListView
class QuestionList(ListView):
    model = Question

class ChoiceList(ListView):
    model = Choice

    #--- DetailView
class QuestionDetail(DeleteView):
    model = Question

class ChoiceDetail(DeleteView):
    model = Choice

