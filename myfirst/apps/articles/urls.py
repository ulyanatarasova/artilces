from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

app_name='articles'
urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:article_id>/", views.detail, name = "detail"),
    path("<int:article_id>/leave_comment/", views.leave_comment, name = "leave_comment"),
    path("article_create/", views.article_create, name = "article_create"),
              ]
