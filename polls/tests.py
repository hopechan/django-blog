import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Question

def create_question(question_text, days):
    date = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text = question_text, pub_date = date)

class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        #If there are no questions it should launch an error message, otherwise launch a status code
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No questions available.")
        self.assertQuerysetEqual(response.context['published_recently'], [])

    def test_past_question(self):
        #questions with old publication dates should be posted
        create_question(question_text="What did you do in April?", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['published_recently'], ['<Question: What did you do in April?>'])
    
    def test_future_question(self):
        #questions with recent publication dates should not be posted
        create_question(question_text="Did you go to see the September 15 parade?", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No questions available.")
        self.assertQuerysetEqual(response.context['published_recently'], [])

    def test_future_question_and_past_question(self):
        #if there are questions with previous date of publication and forward to the current date only show those that already passed
        create_question(question_text="How was your vacation?", days=-30)
        create_question(question_text="Have you seen this movie?", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['published_recently'], ['<Question: How was your vacation?>'])

    def test_two_past_questions(self):
        create_question(question_text="Where did you study?", days=-30)
        create_question(question_text="Are you hungry?", days=-5)
        response = self.client.get(reverse('polls:index')) 
        self.assertQuerysetEqual(response.context['published_recently'], ['<Question: Are you hungry?>', '<Question: Where did you study?>'])

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        future_question = timezone.now() + datetime.timedelta(days=30)
        question = Question(pub_date=future_question)
        self.assertIs(question.published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        #the current date is taken 1 day with 1 second
        past_date = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=past_date)
        self.assertIs(old_question.published_recently(), False)

    def test_was_published_recently(self):
        now = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=now)
        self.assertIs(recent_question.published_recently(), True)

class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        question = create_question(question_text="Is this a question?", days=5)
        url = reverse('polls:detail', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_pregunta_pasada(self):
        #si la fecha de publicacion ya ha pasado debe mostrar el texto de la pregunta
        question = create_question(question_text="Is this a question?", days=-8)
        url = reverse('polls:detail', args=(question.id,))
        response = self.client.get(url)
        self.assertContains(response, question.question_text)
