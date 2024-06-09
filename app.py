from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    skills = models.CharField(max_length=100)
    experience = models.TextField()
    education = models.CharField(max_length=100)
    projects = models.TextField()
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    linkedin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    website = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'


from django.shortcuts import render, redirect
from .forms import PortfolioForm

def portfolio_create_view(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio_success')
    else:
        form = PortfolioForm()
    return render(request, 'portfolio_form.html', {'form': form})

def portfolio_success_view(request):
    return render(request, 'portfolio_success.html')


from django.urls import path
from .views import portfolio_create_view, portfolio_success_view

urlpatterns = [
    path('portfolio/new/', portfolio_create_view, name='portfolio_create'),
    path('portfolio/success/', portfolio_success_view, name='portfolio_success'),
]
