from django.db import models



class Doctor(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    specialty = models.CharField(max_length = 50)

    def __str__(self):
        return self.first_name


class OfficeHour(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, blank = True, null = True)
    begin = models.TimeField(auto_now = False, blank = True)
    end = models.TimeField(auto_now = False, blank = True)
    day_of_week = models.IntegerField()
    slot_length_minutes = models.IntegerField()

    def __str__(self):
        return self.begin


class Patient(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)

    def __str__(self):
        return self.first_name


class Appointments(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, blank = True, null = True)
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE, blank = True, null = True)
    appointment_date = models.DateTimeField(auto_now = False, blank = True)
    appointment_time = models.TimeField(auto_now = False, blank = True)

    def __str__(self):
        return self.appointment_date 



    