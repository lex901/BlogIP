from django.conf.urls import include, url

from django.contrib import admin

admin.autodiscover()


    # Examples:
    # url(r'^$', 'dichblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^basicview/', include('article.urls')),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^', include('article.urls')),
]
