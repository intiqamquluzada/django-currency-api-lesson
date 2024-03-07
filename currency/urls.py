from django.urls import path
from currency.views import index_view

urlpatterns = [
    path("home", index_view, name='index'),
]