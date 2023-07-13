from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import models




def cross_main(request):
    crossy = models.Mainpage1_cross.objects.all()
    return render(request, 'index.html', {'crossy': crossy})




def main2(request):
    crossy = models.main2.objects.all()
    return render(request, 'main2.html', {'crossy':crossy})


