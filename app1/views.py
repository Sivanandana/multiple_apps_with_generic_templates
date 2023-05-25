from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_string(request):
    return HttpResponse('This is app1_string Response')


def app1_htmlpage(request):
    return render(request,'app1_htmlpage.html')