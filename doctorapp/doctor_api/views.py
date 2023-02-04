from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Doctor, OfficeHour, Patient, Appointments
from .serializers import DoctorSerializer, OfficeHourSerializer, PatientSerializer, AppointmentsSerializer

class DoctorListDoctorsApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.data.get('first_name'), 
            'last_name': request.data.get('last_name'), 
            'specialty': request.data.get('specialty')
        }
        serializer = DoctorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

