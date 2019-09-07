from django.urls import path
from . import views

#nombre de la app
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetalleView.as_view(), name='detalle'),
    path('<int:pk>/resultados/', views.ResultadosView.as_view(), name='resultados'),
    path('<int:question_id>/voto/', views.voto, name='voto'),
]