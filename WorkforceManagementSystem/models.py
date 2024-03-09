from django.db import models

# Create your models here.
class Login(models.Model):
    Username= models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)


#
# ///////////////////////////////// employer //////////////////////////////////////////



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
    registration_date = models.CharField(max_length=100, default="")
    # Companysize=models.CharField(max_length=100)

    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)




class Projects(models.Model):

    EMPLOYER = models.ForeignKey(Employer,on_delete=models.CASCADE)

    projecttitle= models.CharField(max_length=100)

    projectdescription = models.CharField(max_length=100)
    projectlocation = models.CharField(max_length=100)
    created_date= models.CharField(max_length=100)
    duration= models.CharField(max_length=100)
    status= models.CharField(max_length=100)
    no_of_workers=models.CharField(max_length=100,default="")


class Jobvaccancy(models.Model):
    EMPLOYER = models.ForeignKey(Employer, on_delete=models.CASCADE,default="")
    PROJECT = models.ForeignKey(Projects, on_delete=models.CASCADE,default="")
    jobtitle = models.CharField(max_length=100)
    jobfield = models.CharField(max_length=100)
    created_date = models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    startdate= models.CharField(max_length=100)
    enddate= models.CharField(max_length=100)
    eno_of_vaccancy= models.CharField(max_length=100)
    skills= models.CharField(max_length=100)
    salary= models.CharField(max_length=100,default="")
    district= models.CharField(max_length=100,default="")


#
# /////////////////////// worker //////////////////////////



class Worker(models.Model):
    Username=models.CharField(max_length=100)
    # Address=models.CharField(max_length=100)
    Photo=models.CharField(max_length=100)
    Photo1 = models.CharField(max_length=100)
    Photo2 = models.CharField(max_length=100)
    Photo3 = models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Adharnumber=models.CharField(max_length=100)
    Jobtype=models.CharField(max_length=100)
    Salary=models.CharField(max_length=100)
    Status=models.CharField(max_length=100)
    Skills=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    Nationality=models.CharField(max_length=100)
    Qualification=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    Pincode=models.CharField(max_length=100)
    Experience=models.CharField(max_length=100)
    post=models.CharField(max_length=100,default=0)
    district=models.CharField(max_length=100,default=0)
    state=models.CharField(max_length=100,default=0)
    registration_date=models.CharField(max_length=100,default="")
    lattitude=models.CharField(max_length=100,default=0)
    longitude=models.CharField(max_length=100,default=0)



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

class Jobrequest(models.Model):
    JOBVACANCY = models.ForeignKey(Jobvaccancy, on_delete=models.CASCADE)
    WORKER = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Workerrequest(models.Model):
    PROJECT = models.ForeignKey(Projects, on_delete=models.CASCADE)
    WORKER = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
