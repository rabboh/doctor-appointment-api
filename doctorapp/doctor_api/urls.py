#from django.conf.urls import url
from django.urls import path, include
from .views import (
    DoctorListDoctorsApiView,
)

urlpatterns = [
    path('api', DoctorListDoctorsApiView.as_view()),
]