from django.shortcuts import render, redirect
from .models import Widgets
from .forms import WidgetForm
from django.db.models import Sum

def home(request):
    widgets = Widgets.objects.all()
    widgets_form = WidgetForm()
    total = Widgets.objects.aggregate(sum=Sum('quantity'))['sum']
    return render(request, 'index.html', {'widgets': widgets, 'widgets_form':widgets_form, 'total': total}) 

def add_widget(request):
  form = WidgetForm(request.POST)
  if form.is_valid():
    new_widget = form.save(commit=False)
    new_widget.save()
  return redirect('/')

def widgets_delete(request, id):
    widgets = Widgets.objects.get(id=id)
    widgets.delete()
    return redirect('/')