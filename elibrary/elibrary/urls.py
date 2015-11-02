"""elibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/', include('books.urls')),
    url(r'^accounts/login/$','elibrary.views.login'),
    url(r'^accounts/auth/$','elibrary.views.auth_view'),
    url(r'^accounts/logout/$','elibrary.views.logout'),
    url(r'^accounts/loggedin/$','elibrary.views.loggedin'),
    url(r'^accounts/invalid/$','elibrary.views.invalid_login'),
    url(r'^hello/$','elibrary.views.hello'),
    url(r'^accounts/register/$','elibrary.views.register'),
    url(r'^accounts/register_user/$','elibrary.views.register_user'),
    url(r'^accounts/register_success/','elibrary.views.register_success'),
    url(r'^home/$','elibrary.views.home'),
    #url(r'^upload/$', include('books.urls')),
    url(r'^bookview/','elibrary.views.book_view'),
    url(r'^videoview/','elibrary.views.video_view'),
    url(r'^compview/','elibrary.views.comp_view'),
    url(r'^editbook/(?P<book_id>\d+)/$','elibrary.views.edit_book'),
    url(r'^mechview/','elibrary.views.mech_view'),
    url(r'^etcview/','elibrary.views.etc_view'),
    url(r'^itview/','elibrary.views.it_view'),
    url(r'^civilview/','elibrary.views.civil_view'),
    url(r'^electricalview/','elibrary.views.electrical_view'),
    url(r'^json_view/','elibrary.views.json_view'),
    url(r'^angular_test/','elibrary.views.angular_test'),


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



