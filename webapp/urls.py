from django.urls import path
from . import views


urlpatterns = [
    path("", views.AboutTemplateView.as_view(), name='index'),
    path("home/", views.HomeListView.as_view(), name='home'),
    path("search/", views.HomeListView.search, name='search'),
    path("test/", views.TesteTemplateView.as_view(), name='test')
]
