from django.conf.urls import include, url
from . import views
urlpatterns = [

                       url(r'^articles/all/$',  views.articles),
                       url(r'^articles/get/(?P<article_id>\d+)/$',  views.article),
                       url(r'^articles/addlike/(?P<article_id>\d+)/$',  views.addlike),
                       url(r'^articles/addcomment/(?P<article_id>\d+)/$',  views.addcomment),
                       url(r'^page/(\d+)/$',  views.articles),
                       url(r'^',  views.articles),

]
