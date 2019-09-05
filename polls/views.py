from django.http import HttpResponse

def index(reques):
    return HttpResponse("Hola mundo desde la vista polls")
