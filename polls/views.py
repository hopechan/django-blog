from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'published_recently'
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]

class DetalleView(generic.DetailView):
    #model represents the variable used in html
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        #doesn't include any questions that have not yet been posted
        return Question.objects.filter(pub_date__lte=timezone.now())
    

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        option_chosen = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question' : question, 'error_message' : "You didn't choose any option."})
    else:
        option_chosen.votes += 1
        option_chosen.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))