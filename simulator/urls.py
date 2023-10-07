from . import views
from django.urls import path
from .views import UserFormView

urlpatterns = [
    path("", views.index, name="index"),
    path("user-form/", UserFormView.as_view(), name="user-form"),
]

