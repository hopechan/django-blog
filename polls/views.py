from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Question

def index(request):
    #con [:5] toma las primeras 5 preguntas y en orden descendiente segun su fecha de publicacion
    preguntas_recientes = Question.objects.order_by('-pub_date')[:5]
    #el preguntas recientes dentro de las comillas simples es la variable que se usa en el html
    context = {
        'preguntas_recientes' : preguntas_recientes
    }
    return render(request, 'polls/index.html', context)

def detalle(request, question_id):
    try:
        pregunta = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("La pregunta no existe :c")
    return render(request, 'polls/detalle.html', {'pregunta' : pregunta})

def resultados(request, question_id):
    response = "Estas viendo los resultados de la pregunta %s. "
    return HttpResponse(response % question_id)

def voto(request, question_id):
    return HttpResponse("Estas votando en la pregunta %s. " % question_id)