from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente

def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def ver_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'ver_cliente.html', {'cliente': cliente})

def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        email = request.POST['email']
        sandwich_favorito = request.POST['sandwich_favorito']
        Cliente.objects.create(
            nombre=nombre,
            telefono=telefono,
            email=email,
            sandwich_favorito=sandwich_favorito
        )
        return redirect('inicio')
    return render(request, 'agregar_cliente.html')

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.telefono = request.POST['telefono']
        cliente.email = request.POST['email']
        cliente.sandwich_favorito = request.POST['sandwich_favorito']
        cliente.save()
        return redirect('inicio')
    return render(request, 'editar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('inicio')
    return render(request, 'borrar_cliente.html', {'cliente': cliente})