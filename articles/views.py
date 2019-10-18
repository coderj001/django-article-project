from django.http import HttpResponse
from django.shortcuts import render,redirect
from articles.models import Article
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def article_list(req):
    article=Article.objects.all().order_by('date')
    return render(req,'articles/article_list.html',{'article':article})

def article_detail(req,slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(req,'articles/article_detail.html',{'article':article})

@login_required(login_url='/account/login/')
def article_create(req):
    if req.method == 'POST':
        form=forms.CreateArticle(req.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            if 'thumb' in req.FILES:
                instance.thumb=req.FILES['thumb']
            instance.author=req.user
            instance.save()
        return redirect('articles:Article_List')
    form=forms.CreateArticle()
    return render(req,'articles/create.html',{'forms':form})