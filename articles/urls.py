from django.urls import path
from . import views
from django.conf.urls import url

app_name='articles'

urlpatterns = [
    path('',views.article_list,name='Article_List'),
    url(r'^create',views.article_create,name='create'),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail,name='Detail'),
]