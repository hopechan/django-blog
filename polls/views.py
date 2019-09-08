from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'preguntas_recientes'
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]

class DetalleView(generic.DetailView):
    #model representa la variable que se utiliza en el html
    model = Question
    template_name = 'polls/detalle.html'
    
    def get_queryset(self):
        #no incluye ningua pregunta que aun no ha sido publicada
        return Question.objects.filter(pub_date__lte=timezone.now())
    

class ResultadosView(generic.DetailView):
    model = Question
    template_name = 'polls/resultados.html'
    

def voto(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        opcion_elegida = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detalle.html', {'question' : question, 'mensaje_error' : 'No has elegido ninguna opcion'})
    else:
        opcion_elegida.votes += 1
        opcion_elegida.save()
        return HttpResponseRedirect(reverse('polls:resultados', args=(question.id,)))