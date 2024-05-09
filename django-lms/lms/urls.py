from django.urls import path

from lms.views import index

urlpatterns = [
    path('', index, name="home")
]