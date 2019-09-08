import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Question

def crear_pregunta(question_text, days):
    fecha = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text = question_text, pub_date = fecha)

class QuestionIndexViewTest(TestCase):
    def test_sin_preguntas(self):
        #Si no existen preguntas debe lanzar un mensaje de error, sino lanza un codigo de estado
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hay preguntas disponibles.")
        self.assertQuerysetEqual(response.context['preguntas_recientes'], [])

    def test_preguntas_antiguas(self):
        #se deben mostrar preguntas con fechas de publicacion antiguas
        crear_pregunta(question_text="¿Qué hiciste en abril?", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['preguntas_recientes'], ['<Question: ¿Qué hiciste en abril?>'])
    
    def test_preguntas_futuras(self):
        #Preguntas que su fecha de publicacion esta adelantada a la fecha actual no se muestran
        crear_pregunta(question_text="¿Fuiste a ver el desfile del 15 de septiembre?", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No hay preguntas disponibles.")
        self.assertQuerysetEqual(response.context['preguntas_recientes'], [])

    def test_preguntas_pasadas_y_futuras(self):
        #si hay preguntas con fecha de publicacion pasada y adelantas a la fecha actual 
        #solo se muestran la que ya pasaron
        crear_pregunta(question_text="¿Como estuvieron las vacaciones?", days=-30)
        crear_pregunta(question_text="¿Ya viste la pelicula de Joker?", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['preguntas_recientes'], ['<Question: ¿Como estuvieron las vacaciones?>'])

    def test_dos_preguntas_antiguas(self):
        #la pagina principal debe mostrar varias preguntas
        crear_pregunta(question_text="¿Donde estudiastes?", days=-30)
        crear_pregunta(question_text="¿Tienes hambre?", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['preguntas_recientes'], ['<Question: ¿Tienes hambre?>', '<Question: ¿Donde estudiastes?>'])
class QuestionModelTest(TestCase):
    def test_se_publico_con_fecha_en_el_futuro(self):
        #se coloca una fecha adelantada 30 dias a la actual
        fecha_adelantada = timezone.now() + datetime.timedelta(days=30)
        #se le asigna la fecha adelantada a la propiedad pub_date de un objeto Question
        pregunta = Question(pub_date=fecha_adelantada)
        self.assertIs(pregunta.publicada_recientemente(), False)

    def test_se_publico_en_el_pasado(self):
        #a la fecha actual se le resta 1 dia con 1 segundo
        fecha_atrasada = timezone.now() - datetime.timedelta(days=1, seconds=1)
        pregunta_antigua = Question(pub_date=fecha_atrasada)
        self.assertIs(pregunta_antigua.publicada_recientemente(), False)

    def test_se_publico_recientemente(self):
        fecha_reciente = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        pregunta_reciente = Question(pub_date=fecha_reciente)
        self.assertIs(pregunta_reciente.publicada_recientemente(), True)