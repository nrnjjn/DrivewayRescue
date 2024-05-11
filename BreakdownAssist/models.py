from django.db import models

# Create your models here.
class Login(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Type = models.CharField(max_length=20)

class Mechanic(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    mechanic_name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    district = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()
    status = models.CharField(max_length=100)
    availability = models.CharField(max_length=100,default="")

class Service_center(models.Model):
    center_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()

class Petrol_pump(models.Model):
    pump_name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()

class User(models.Model):
    user_name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)



class Feedback(models.Model):
    date = models.DateField()
    feedback = models.CharField(max_length=100)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)

class Request(models.Model):
    date = models.DateField()
    status = models.CharField(max_length=100)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    MECHANIC = models.ForeignKey(Mechanic, on_delete=models.CASCADE)

class Tow_service(models.Model):
    tow_name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()


class Chat(models.Model):
    date = models.DateField()
    message = models.CharField(max_length=100)
    FROM = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='From')
    TO = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='To')

class Rating(models.Model):
    MECHANIC = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    rating = models.CharField(max_length=100)

