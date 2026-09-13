from django.shortcuts import render


def inicio(request):
	eventos = [
		{'hora': '09:00', 'titulo': 'Revisión de objetivos', 'tipo': 'Trabajo'},
		{'hora': '12:30', 'titulo': 'Almuerzo con el equipo', 'tipo': 'Personal'},
		{'hora': '16:00', 'titulo': 'Bloque de estudio Django', 'tipo': 'Estudio'},
	]
	return render(request, 'agenda/inicio.html', {'eventos': eventos})


def semana(request):
	dias = [
		{'dia': 'Lunes', 'cantidad': 3, 'foco': 'Planificación'},
		{'dia': 'Martes', 'cantidad': 2, 'foco': 'Desarrollo'},
		{'dia': 'Miércoles', 'cantidad': 4, 'foco': 'Reuniones'},
		{'dia': 'Jueves', 'cantidad': 1, 'foco': 'Estudio'},
		{'dia': 'Viernes', 'cantidad': 2, 'foco': 'Cierre'},
	]
	return render(request, 'agenda/semana.html', {'dias': dias})
