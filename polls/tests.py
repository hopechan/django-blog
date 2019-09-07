import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

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