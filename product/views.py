from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenida a Sendero de Café ☕🌱")
