from django.shortcuts import render


def inicio(request):
	productos_destacados = [
		{'nombre': 'Cuaderno ejecutivo', 'categoria': 'Papelería', 'precio': '$8.990'},
		{'nombre': 'Mochila urbana', 'categoria': 'Accesorios', 'precio': '$29.990'},
		{'nombre': 'Set de marcadores', 'categoria': 'Escritorio', 'precio': '$6.490'},
	]
	return render(request, 'catalogo/inicio.html', {'productos': productos_destacados})


def productos(request):
	inventario = [
		{'nombre': 'Lámpara de escritorio', 'stock': 12, 'estado': 'Disponible'},
		{'nombre': 'Agenda semanal 2026', 'stock': 4, 'estado': 'Últimas unidades'},
		{'nombre': 'Organizador modular', 'stock': 0, 'estado': 'Agotado'},
	]
	return render(request, 'catalogo/productos.html', {'inventario': inventario})
