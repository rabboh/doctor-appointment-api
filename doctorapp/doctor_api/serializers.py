from rest_framework import serializers
from .models import Doctor, OfficeHour, Patient, Appointments


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["first_name", "last_name", "specialty"]


class OfficeHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeHour
        fields = ["doctor", "begin", "end", "day_of_week", "slot_length_minutes"]


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["first_name", "last_name", "email"]


class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ["doctor", "patient", "appointment_date", "appointment_time"]


