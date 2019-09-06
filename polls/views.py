from django.http import HttpResponse
from .models import Question

def index(request):
    #con [:5] toma las primeras 5 preguntas y en orden descendiente segun su fecha de publicacion
    preguntas_recientes = Question.objects.order_by('-pub_date')[:5]
    salida = ', '.join([q.question_text for q in preguntas_recientes])
    return HttpResponse(salida)

def detalle(request, question_id):
    return HttpResponse("Estas viendo la pregunta %s. " % question_id)

def resultados(request, question_id):
    response = "Estas viendo los resultados de la pregunta %s. "
    return HttpResponse(response % question_id)

def voto(request, question_id):
    return HttpResponse("Estas votando en la pregunta %s. " % question_id)