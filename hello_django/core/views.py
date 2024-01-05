from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos</h1>')

def soma(request, numero1, numero2):
    somar = numero1 + numero2
    return HttpResponse(f'<h1>Soma de {numero1} + {numero2} = {somar}.</h1>')

def multi(request, numero1, numero2):
    mul = numero1 + numero2
    return HttpResponse(f'<h1>Multiplicação de {numero1} * {numero2} = {mul}.</h1>')

def divi(request, numero1, numero2):
    dividir = numero1 + numero2
    return HttpResponse(f'<h1>Divisão de {numero1} / {numero2} = {dividir}.</h1>')