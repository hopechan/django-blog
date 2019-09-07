from django.urls import path
from . import views

#nombre de la app
app_name = 'polls'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.detalle, name='detalle'),
    path('<int:question_id>/resultados', views.resultados, name='resultados'),
    path('<int:question_id>/vote/', views.voto, name='voto'),
]