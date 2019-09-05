from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola mundo desde la vista polls")

def detalle(request, question_id):
    return HttpResponse("Estas viendo la pregunta %s. " % question_id)

def resultados(request, question_id):
    response = "Estas viendo los resultados de la pregunta %s. "
    return HttpResponse(response % question_id)

def voto(request, question_id):
    return HttpResponse("Estas votando en la pregunta %s. " % question_id)