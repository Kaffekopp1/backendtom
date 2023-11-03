from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("TestView", views.TestView, name="TestView"),
    path("TestViewPOST", views.TestViewPOST, name="TestViewPOST"),
]
