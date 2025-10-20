from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Producto
from .forms import ProductoForm


# Create your views here.
def index_productos(request):
	return render(request, 'productos/index.html', {
		'productos': Producto.objects.all()
	})


def add_producto(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'productos/add.html', {
				'form': ProductoForm(),
				'success': True
			})
	else:
		form = ProductoForm()
	return render(request, 'productos/add.html', {
		'form': form
	})


def edit_producto(request, id):
	producto = get_object_or_404(Producto, pk=id)
	if request.method == 'POST':
		form = ProductoForm(request.POST, instance=producto)
		if form.is_valid():
			form.save()
			return render(request, 'productos/edit.html', {
				'form': form,
				'producto': producto,
				'success': True
			})
	else:
		form = ProductoForm(instance=producto)
	return render(request, 'productos/edit.html', {
		'form': form,
		'producto': producto
	})


def delete_producto(request, id):
	producto = get_object_or_404(Producto, pk=id)
	if request.method == 'POST':
		producto.delete()
		return HttpResponseRedirect(reverse('index_productos'))
	return redirect('index_productos')


def view_producto(request, id):
	producto = get_object_or_404(Producto, pk=id)
	return render(request, 'productos/view_detail.html', {'producto': producto})