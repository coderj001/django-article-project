from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    # return HttpResponse('Here is some plain text.',content_type='text/plain')
    return render(req,'index.html',content_type='html')

def about(req):
    return render(req,'about.html')