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

