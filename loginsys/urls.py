from django.conf.urls import url
from loginsys import views

urlpatterns = [
                       # Examples:
                       # url(r'^$', 'dichblog.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^login/$', views.login),
                       url(r'^logout/$', views.logout),
                       url(r'^register/$', views.register),

                       ]
