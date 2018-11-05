from django.urls import path, include
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("articles/", include('articles.urls')),
    path("about/", views.about),
]

urlpatterns += staticfiles_urlpatterns()
