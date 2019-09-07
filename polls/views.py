from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question
from django.urls import reverse

def index(request):
    #con [:5] toma las primeras 5 preguntas y en orden descendiente segun su fecha de publicacion
    preguntas_recientes = Question.objects.order_by('-pub_date')[:5]
    #el preguntas recientes dentro de las comillas simples es la variable que se usa en el html
    context = {
        'preguntas_recientes' : preguntas_recientes
    }
    return render(request, 'polls/index.html', context)

def detalle(request, question_id):
    pregunta = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detalle.html', { 'pregunta' : pregunta })

def resultados(request, question_id):
    pregunta = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/resultados.html', {'pregunta' : pregunta})

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