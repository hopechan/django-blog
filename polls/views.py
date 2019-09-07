from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'preguntas_recientes'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetalleView(generic.DetailView):
    model = Question
    template_name = 'polls/detalle.html'

class ResultadosView(generic.DetailView):
    model = Question
    template_name = 'polls/resultados.html'

def voto(request, question_id):
    pregunta = get_object_or_404(Question, pk=question_id)
    try:
        opcion_elegida = pregunta.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detalle.html', {'pregunta' : pregunta, 'mensaje_error' : 'No has elegido ninguna opcion'})
    else:
        opcion_elegida.votes += 1
        opcion_elegida.save()
        return HttpResponseRedirect(reverse('polls:resultados', args=(pregunta.id,)))