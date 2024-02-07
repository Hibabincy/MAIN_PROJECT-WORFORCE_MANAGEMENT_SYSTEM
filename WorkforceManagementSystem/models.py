from django.db import models

# Create your models here.
class Login(models.Model):
    Username= models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)

class Employer(models.Model):
    Companyname= models.CharField(max_length=100)
    Phone= models.CharField(max_length=100)
    Email= models.CharField(max_length=100)
    Place= models.CharField(max_length=100)
    Post= models.CharField(max_length=100)
    District= models.CharField(max_length=100)
    State= models.CharField(max_length=100)
    Pincode= models.CharField(max_length=100)
    Photo= models.CharField(max_length=100)
    Date=models.CharField(max_length=100)
    Status=models.CharField(max_length=100,default='')
    Category=models.CharField(max_length=100)
    Website=models.CharField(max_length=100)
    Photo1=models.CharField(max_length=100)
    Photo2= models.CharField(max_length=100)
    Photo3= models.CharField(max_length=100)
    Aboutcompany=models.CharField(max_length=300)
    Companysize=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)


class Worker(models.Model):
    Username=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Photo=models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Adharnumber=models.CharField(max_length=100)
    Jobfield=models.CharField(max_length=100)
    Jobtype=models.CharField(max_length=100)
    Salary=models.CharField(max_length=100)
    Status=models.CharField(max_length=100)
    Skills=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    Age=models.CharField(max_length=100)
    Nationality=models.CharField(max_length=100)
    Qualification=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    Pincode=models.CharField(max_length=100)
    Experience=models.CharField(max_length=100)
    Cv=models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)

class Previousworks(models.Model):
    Photo1=models.CharField(max_length=100)
    Photo2=models.CharField(max_length=100)
    Photo3=models.CharField(max_length=100)
    WORKER=models.ForeignKey(Worker, on_delete=models.CASCADE)

class Fee(models.Model):
    Type = models.CharField(max_length=100)
    Amount = models.CharField(max_length=100)


class Payment(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    FEE = models.ForeignKey(Fee, on_delete=models.CASCADE)
    Date=models.CharField(max_length=100)
    Status=models.CharField(max_length=100)
