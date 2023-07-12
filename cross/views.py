from django.contrib.auth import authenticate, login
from django.forms import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import models, forms




def cross_main(request):
    crossy = models.Mainpage1_cross.objects.all()
    return render(request, 'index.html', {'crossy': crossy})

def about(request):
    about = models.About_us.objects.all()
    return render(request, 'about.html', {'about': about})

def contact(request):
    contact = models.Contact.objects.all()
    return render(request, 'contact.html', {'contact': contact})

def product(request):
    products = models.Products.objects.all()
    return render(request, 'products.html', {'products': products})

def sneakers_view(request):
    sneakers = models.Sneakers.objects.all()
    return render(request, 'sneakersorder.html', {'sneakers': sneakers})
def more_inf1(request):
    m_inf1 = models.More_inform1.objects.all()
    return render(request, '1_moreinf.html',{'m_inf1':m_inf1})
def more_inf2(request):
    m_inf2 = models.More_inform2.objects.all()
    return render(request, '2_moreinf.html',{'m_inf2':m_inf2})
def more_inf3(request):
    m_inf3 = models.More_inform3.objects.all()
    return render(request, '3_moreinf.html',{'m_inf3':m_inf3})
def more_inf4(request):
    m_inf4 = models.More_inform4.objects.all()
    return render(request, '4_moreinf.html',{'m_inf4':m_inf4})
def more_inf5(request):
    m_inf5 = models.More_inform5.objects.all()
    return render(request, '5_moreinf.html',{'m_inf5':m_inf5})
def more_inf6(request):
    m_inf6 = models.More_inform6.objects.all()
    return render(request, '6_moreinf.html',{'m_inf6':m_inf6})
def reg(request):
    return render(request,'actions_reg.html')

#add Sneakers

def add_sneakers_view(request):
    method = request.method
    if method == 'POST':
        form = forms.SneakersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<center><b>Ваш заказ принят!<b><center>')
    else:
        form = forms.SneakersForm()

    return render(request, 'add_sneakers.html', {'form': form})



