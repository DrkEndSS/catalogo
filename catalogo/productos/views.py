from django.shortcuts import render, redirect
from .models import Categoria, Producto
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Vista principal para mostrar categorías y productos
def index(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request, 'index.html', {'categorias': categorias, 'productos': productos})

# Vista para agregar una nueva categoría
@csrf_exempt
def agregar_categoria(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        if nombre:
            categoria = Categoria.objects.create(nombre=nombre)
            return JsonResponse({"message": "Categoría agregada", "categoria_id": categoria.id, "nombre": categoria.nombre})
    return JsonResponse({"error": "Faltan datos"}, status=400)

# Vista para agregar un nuevo producto
@csrf_exempt
def agregar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        categoria_id = request.POST.get('categoria')
        stock = request.POST.get('stock')
        estado = request.POST.get('estado')

        categoria = Categoria.objects.get(id=categoria_id)
        producto = Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            categoria=categoria,
            stock=stock,
            estado=estado
        )
        return JsonResponse({"message": "Producto agregado", "producto_id": producto.id})
    return JsonResponse({"error": "Faltan datos"}, status=400)

# Vista para modificar un producto
@csrf_exempt
def modificar_producto(request, producto_id):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        estado = request.POST.get('estado')

        producto = Producto.objects.get(id=producto_id)
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.stock = stock
        producto.estado = estado
        producto.save()

        return JsonResponse({"message": "Producto modificado", "producto_id": producto.id})
    return JsonResponse({"error": "Faltan datos"}, status=400)

# Vista para eliminar un producto
@csrf_exempt
def eliminar_producto(request, producto_id):
    if request.method == "POST":
        producto = Producto.objects.get(id=producto_id)
        producto.delete()
        return JsonResponse({"message": "Producto eliminado"})
    return JsonResponse({"error": "Faltan datos"}, status=400)
