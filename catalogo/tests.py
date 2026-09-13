from django.test import TestCase
from django.urls import reverse


class CatalogoViewsTests(TestCase):
	def test_inicio_muestra_productos_destacados(self):
		response = self.client.get(reverse('catalogo:inicio'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Cuaderno ejecutivo')

	def test_productos_muestra_inventario(self):
		response = self.client.get(reverse('catalogo:productos'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Lámpara de escritorio')
from django.test import TestCase

# Create your tests here.
