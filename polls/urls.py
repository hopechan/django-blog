from django.urls import path
from . import views

#nombre de la app
app_name = 'polls'
urlpatterns = [
    path('', views.index, name="index"),
    path('detalle/<int:question_id>/', views.detalle, name='detalle'),
    path('<int:question_id>/resultados', views.resultados, name='resultados'),
    path('<int:question_id/voto>', views.voto, name="voto")
]