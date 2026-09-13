from django.test import TestCase
from django.urls import reverse


class AgendaViewsTests(TestCase):
	def test_inicio_muestra_eventos(self):
		response = self.client.get(reverse('agenda:inicio'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Revisión de objetivos')

	def test_semana_muestra_dias(self):
		response = self.client.get(reverse('agenda:semana'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Planificación')
from django.test import TestCase

# Create your tests here.
