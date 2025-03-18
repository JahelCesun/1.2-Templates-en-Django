from django.shortcuts import render

def inicio(request):
    contexto = {
        'usuario': 'Juan',
        'productos': ['Laptop', 'Teléfono', 'Tablet']
    }
    return render(request, 'templateapp/index.html', contexto)