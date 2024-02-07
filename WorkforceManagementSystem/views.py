import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from WorkforceManagementSystem.models import *


def login(request):
    return render(request,"loginindex.html")

def logout(request):
    return render(request,"loginindex.html")
def login_post(request):
    username=request.POST['textfield']
    Password=request.POST['textfield2']
    a=Login.objects.filter(Username=username,Password=Password)
    if a.exists():
        a=Login.objects.get(Username=username,Password=Password)
        request.session['lid']=a.id
        if a.Type == 'admin':
            return HttpResponse('''<script>alert("login successfully");window.location="/wForce/adminhome/"</script>''')
        # elif a.Type=="worker":
        #     return
        else:
            return HttpResponse('''<script>alert("User not found");window.location="/wForce/login/"</script>''')
    else:
        return HttpResponse('''<script>alert("Invalid username or password");window.location="/wForce/login/"</script>''')


def adminhome(request):
    return render(request,'adminindex.html')
def employerRegistration(request):
    return render(request,"registrationindex.html")

def employerRegistration_post(request):
    email=request.POST['textfield']
    password=request.POST['textfield2']
    confirmpassword=request.POST['textfield3']
    if password !=confirmpassword:
        return HttpResponse(
            '''<script>alert("Passwords do not match");history.back()</script>''')
    request.session['tempmail']=email
    request.session['temppass'] =password
    return redirect("/wForce/employerprofile/")
def employerprofile(request):
    return render(request, "Employer Profile.html")

def employerprofile_post(request):
    coverphoto=request.FILES['fileField2']
    employername=request.POST['textfield']
    email=request.POST['textfield2']
    phonenumber=request.POST['textfield3']
    website=request.POST['textfield4']
    foundeddate=request.POST['textfield5']
    companysize=request.POST['textfield6']
    category=request.POST['select']
    aboutcompany=request.POST['textarea']
    photo1=request.FILES['fileField3']
    photo2=request.FILES['fileField4']
    photo3=request.FILES['fileField5']
    location=request.POST['textfield7']
    Post=request.POST['textfield9']
    State= request.POST['textfield10']
    District= request.POST['textfield11']
    pincode=request.POST['textfield8']

    d=Login()
    d.Username=request.session['tempmail']
    d.Password=request.session['temppass']
    d.Type='pending'
    d.save()
    g=Employer()
    g.Companyname=employername
    e=FileSystemStorage()
    h='employer/photos/cover/'+datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')+coverphoto.name
    e.save(h,coverphoto)
    g.Photo=e.url(h)

    g.Email=email
    g.Phone=phonenumber
    g.Website=website
    g.Date=foundeddate
    g.Companysize=companysize
    g.Category=category
    g.Aboutcompany=aboutcompany

    j = 'employer/photos/photo1/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + photo1.name
    e.save(j,photo1)
    g.Photo1=e.url(j)

    k = 'employer/photos/photo2/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + photo2.name
    e.save(k, photo2)
    g.Photo2 = e.url(k)

    l = 'employer/photos/photo3/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + photo3.name
    e.save(l, photo3)
    g.Photo3 = e.url(l)

    g.Place=location
    g.Post=Post
    g.State=State
    g.District=District
    g.Pincode=pincode
    g.LOGIN=d
    g.save()

    return HttpResponse('''<script>alert("Success");window.location="/wForce/login/"</script>''')


def addfee(request):
    return render(request, "Manage fee Add.html")

def addfee_post(request):
    type=request.POST['select']
    fee=request.POST['textfield']
    f=Fee()
    f.Type=type
    f.Amount=fee
    f.save()
    return HttpResponse('''<script>alert("added fees successfuly");window.location="/wForce/addfee/"</script>''')


def viewfee(request):
    b=Fee.objects.all()
    return render(request, "Managefee_view.html",{'data':b})

def viewfee_post(request):
    search=request.POST['textfield']
    b=Fee.objects.filter(Type__icontains=search)

    return render(request, "Managefee_view.html",{'data':b})

def editfee(request,id):
    b=Fee.objects.get(id=id)

    return render(request, "editfee.html",{'data':b})

def editfee_post(request):
    type=request.POST['select']
    fee=request.POST['textfield']
    id=request.POST['id']
    f = Fee.objects.get(id=id)
    f.Type = type
    f.Amount = fee
    f.save()
    return HttpResponse('''<script>alert("Updated fees successfuly");window.location="/wForce/viewfee/"</script>''')

def deletefee(request,id):
    b=Fee.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert("deleted successfuly");window.location="/wForce/viewfee/"</script>''')

def approvalofregistrationemployer(request):
    k =Employer.objects.filter(LOGIN__Type="pending")
    return render(request, "Approval_of_Registration.html",{'data':k})

def approvalofregistrationemployer_POST(request):
    name=request.POST['textfield']
    k = Employer.objects.filter(LOGIN__Type="pending",Companyname__icontains=name)
    return render(request, "Approval_of_Registration.html", {'data': k})

def approvalofregistrationemployer_more(request,id):
    k =Employer.objects.get(LOGIN=id)
    pay_info=Payment.objects.filter(LOGIN=id)
    if len(pay_info)>0:
        return render(request, "view_employer.html",{'data':k,"Feetype":pay_info[0].FEE.Type,"Fee":pay_info[0].FEE.Amount,"status":pay_info[0].Status,"Date":pay_info[0].Date,"check":"yes"})

    else:
        return render(request, "view_employer.html",
                      {'data': k, "check": "no"})

def employer_aprrove_reject(request):
    bt=request.POST["button"]
    lid=request.POST["lid"]
    if bt=="Approve":

        m =Login.objects.filter(id=lid).update(Type="employer")
        return HttpResponse('''<script>alert("Accepted successfuly");window.location="/wForce/approvalofregistrationemployer/"</script>''')
    elif bt=="Reject":
        m = Login.objects.filter(id=lid).update(Type="employer")
        return HttpResponse(
            '''<script>alert("Rejected successfuly");window.location="/wForce/approvalofregistrationemployer/"</script>''')

# def employerreject(request):
#     n =Employer.objects.get()
#     return render(request, "Approval_of_Registration.html",{'data':n})

def employerdash(request):
    return render(request, "employerindex.html")
