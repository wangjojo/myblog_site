"""blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from DjangoUeditor import urls as DjangoUeditor_urls
from blog import views as blog_views
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/favicon.ico')),
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/',include(DjangoUeditor_urls)),
    #blog_urls
    url(r'^$',blog_views.index,name = 'index'),
    url(r'^category/$',blog_views.category_detail_all,name = 'category_all'),
    url(r'^category/(?P<category_slug>[^/]+)/$',blog_views.category_detail,name = 'category'),
    url(r'^blog/(?P<pk>\d+)/(?P<blog_slug>[^/]+)/$',blog_views.blog_detail,name = 'blog'),

]

from django.conf import settings
 
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)