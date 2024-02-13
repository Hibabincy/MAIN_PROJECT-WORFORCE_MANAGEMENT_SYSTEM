import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from WorkforceManagementSystem.models import *


def login(request):
    return render(request,"loginnewindex.html")

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
        elif a.Type=="employer":
            return HttpResponse('''<script>alert("login successfully");window.location="/wForce/employerdash/"</script>''')
        else:
            return HttpResponse('''<script>alert("User not found");window.location="/wForce/login/"</script>''')
    else:
        return HttpResponse('''<script>alert("Invalid username or password");window.location="/wForce/login/"</script>''')

def employerdash(request):
    return render(request,'employerdashinbox.html')
def adminhome(request):
    return render(request,'admindashinbox.html')
def employerRegistration(request):
    return render(request,"registrationindex.html")


def employersignup(request):
    return render(request, "employsignupindex.html")

# def employerregistration(request):
    # return render(request,"Employer Profile.html")


def employerregistration_post(request):
    print(request.POST)
    coverphoto=request.FILES['fileField2']
    employername=request.POST['textfield']
    email=request.POST['textfield2']
    phonenumber=request.POST['textfield3']
    website=request.POST['textfield4']
    foundeddate=request.POST['textfield5']
    # companysize=request.POST['textfield6']
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
    Password = request.POST['textfield12']
    Conformpassword = request.POST['textfield13']

    if Password==Conformpassword:

        d=Login()
        d.Username=email
        d.Password=Conformpassword
        d.Type='pending'
        d.save()



        g=Employer()
        g.Companyname=employername

        e=FileSystemStorage()
        h='employer/photos/cover/'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S%f')+coverphoto.name
        e.save(h,coverphoto)
        g.Photo=e.url(h)

        g.Email=email
        g.Phone=phonenumber
        g.Website=website
        g.Date=foundeddate
        # g.Companysize=companysize
        g.Category=category
        g.Aboutcompany=aboutcompany

        j = 'employer/photos/photo1/' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S%f') + photo1.name
        e.save(j,photo1)
        g.Photo1=e.url(j)

        k = 'employer/photos/photo2/' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S%f') + photo2.name
        e.save(k, photo2)
        g.Photo2 = e.url(k)

        l = 'employer/photos/photo3/' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S%f') + photo3.name
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

    else:
        return HttpResponse('''<script>alert("Password mismatching");window.location="/wForce/employerprofile/"</script>''')


def addfee(request):
    return render(request, "Manage fee Add.html")

def addfee_post(request):
    type=request.POST['select']
    fee=request.POST['textfield']
    res=Fee.objects.filter(Type=type)
    if res.exists():
        return HttpResponse('''<script>alert("Already Added");window.location="/wForce/addfee/"</script>''')
    else:
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



def employer_aprrove_reject(request,lid):
    res=Login.objects.filter(id=lid).update(Type="employer")
    return HttpResponse('''<script>alert('Approve Successfull');window.location="/wForce/approvalofregistrationemployer/"</script>''')


def employer_reject(request,lid):
    res=Login.objects.filter(id=lid).update(Type="rejected")
    return HttpResponse('''<script>alert('Rejected Successfull');window.location="/wForce/approvalofregistrationemployer/"</script>''')



def approvalofregistrationemployer_more(request,id):
    k =Employer.objects.get(LOGIN=id)
    pay_info=Payment.objects.filter(LOGIN=id)
    if len(pay_info)>0:
        return render(request, "view_employer.html",{'data':k,"Feetype":pay_info[0].FEE.Type,"Fee":pay_info[0].FEE.Amount,"status":pay_info[0].Status,"Date":pay_info[0].Date,"check":"yes"})

    else:
        return render(request, "view_employer.html",
                      {'data': k, "check": "no"})


# def employer_aprrove_reject(request):
#     bt=request.POST["button"]
#     lid=request.POST["lid"]
#     if bt=="Approve":
#
#         m =Login.objects.filter(id=lid).update(Type="employer")
#         return HttpResponse('''<script>alert("Accepted successfuly");window.location="/wForce/approvalofregistrationemployer/"</script>''')
#     elif bt=="Reject":
#         m = Login.objects.filter(id=lid).update(Type="employer")
#         return HttpResponse(
#             '''<script>alert("Rejected successfuly");window.location="/wForce/approvalofregistrationemployer/"</script>''')

# def employerreject(request):
#     n =Employer.objects.get()
#     return render(request, "Approval_of_Registration.html",{'data':n})


def approvalofregistrationworker(request):
    k =Worker.objects.filter(LOGIN__Type="pending")
    return render(request, "approveworker.html",{'data':k})


def approve_worker(request,lid):
    res=Login.objects.filter(id=lid).update(Type="worker")
    return HttpResponse('''<script>alert('Approve Successfull');window.location="/wForce/approvalofregistrationworker/"</script>''')

def reject_worker(request,lid):
    res=Login.objects.filter(id=lid).update(Type="rejected")
    return HttpResponse('''<script>alert('Reject Successfull');window.location="/wForce/approvalofregistrationworker/"</script>''')




def approvalofregistrationworker_POST(request):
    name=request.POST['textfield']
    k =Worker.objects.filter(LOGIN__Type="pending",Username__icontains=name)
    return render(request, "approveworker.html", {'data': k})

def approvalofregistrationworker_more(request,id):
    k =Worker.objects.get(LOGIN=id)
    pay_info=Payment.objects.filter(LOGIN=id)










def employerdash(request):
    return render(request, "employerdashindex.html")
def mainhome(request):
    return render(request, "mainhome1index.html")
def employerhome(request):
    return render(request, "employerhomeindex.html")

#
# def workersignup(request):
#     return render(request, "employsignupindex.html")



def workerregistration_post(request):

    Username=request.POST['name']
    # Address=request.POST['address']
    Photo=request.POST['photo']
    Photo2=request.POST['photo2']
    Photo3=request.POST['photo3']
    Photo4=request.POST['photo4']
    Phone=request.POST['phone']
    Email=request.POST['email']
    Adharnumber=request.POST['adharnumber']
    Jobtype=request.POST['jobtype']
    Salary=request.POST['salary']
    # Status=request.POST['status']
    Gender=request.POST['gender']
    State= request.POST['state']
    pincode=request.POST['pincode']
    Password = request.POST['password']
    Conformpassword = request.POST['conform password']
    dob = request.POST['dob']
    Nationality = request.POST['nationality']
    Qualification = request.POST['qualification']
    Location=request.POST['location']
    Experience=request.POST['experience']
    Skill=request.POST['skills']
    post=request.POST['post']
    district=request.POST['district']

    if Login.objects.filter(Username=Email).exists():
        return JsonResponse({'status': 'error', 'message': 'User with this email already exists.'}, status=400)

        # Check if the password matches the confirm password
    # if Password != Conformpassword:
    #     return JsonResponse({'status': 'error', 'message': 'Password and Confirm Password do not match.'}, status=400)

    from datetime import datetime
    date=datetime.now().strftime('%Y%m%d-%H%M%S')+'1.jpg'
    import base64
    a=base64.b64decode(Photo)
    fs= FileSystemStorage()
    # fn= fs.save(date,Photo)
    fh=open("C:\\Users\\hibab\\OneDrive\\Desktop\\MAIN_PROJECT-WORFORCE_MANAGEMENT_SYSTEM\\media\\worker\\"+date,'wb')
    path='/media/worker/'+date
    fh.write(a)
    fh.close()

    from datetime import datetime
    date2 = datetime.now().strftime('%Y%m%d-%H%M%S') + '2.jpg'
    import base64
    a = base64.b64decode(Photo2)
    fs = FileSystemStorage()
    # fn1 = fs.save(date2, Photo2)
    fh1 = open("C:\\Users\\hibab\\OneDrive\\Desktop\\MAIN_PROJECT-WORFORCE_MANAGEMENT_SYSTEM\\media\\worker\\" + date2,
              'wb')
    path1 = '/media/worker/' + date2
    fh1.write(a)
    fh1.close()

    from datetime import datetime
    date3 = datetime.now().strftime('%Y%m%d-%H%M%S') + '3.jpg'
    import base64
    a = base64.b64decode(Photo3)
    fs = FileSystemStorage()
    # fn2 = fs.save(date2, Photo3)
    fh2 = open("C:\\Users\\hibab\\OneDrive\\Desktop\\MAIN_PROJECT-WORFORCE_MANAGEMENT_SYSTEM\\media\\worker\\" + date3,
               'wb')
    path2 = '/media/worker/' + date3
    fh2.write(a)
    fh2.close()

    from datetime import datetime
    date4 = datetime.now().strftime('%Y%m%d-%H%M%S') + '4.jpg'
    import base64
    a = base64.b64decode(Photo4)
    fs = FileSystemStorage()
    # fn3 = fs.save(date4, Photo4)
    fh3 = open("C:\\Users\\hibab\\OneDrive\\Desktop\\MAIN_PROJECT-WORFORCE_MANAGEMENT_SYSTEM\\media\\worker\\" + date4,
               'wb')
    path3 = '/media/worker/' + date4
    fh3.write(a)
    fh3.close()

    # ress=Login.objects.get(username=Email,password=Conformpassword)
    # if ress.exists():
    #     return JsonResponse({"status":"none"})
    # else:
    d = Login()
    d.Username = Email
    d.Password = Conformpassword
    d.Type = 'pending'
    d.save()



    g = Worker()
    g.Username = Username
    # g.Address=Address
    g.Photo = path
    g.Photo1 = path1
    g.Photo2 = path2
    g.Photo3 = path3
    g.Phone = Phone
    g.Email = Email
    g.Adharnumber = Adharnumber
    g.Jobtype = Jobtype
    g.Salary = Salary
    g.Status = 'pending'
    g.Skills = Skill
    g.Gender = Gender
    g.dob = dob
    g.Nationality = Nationality
    g.Qualification = Qualification
    g.Location = Location
    g.Pincode = pincode
    g.Experience = Experience
    g.state = State
    g.post = post
    g.district = district
    g.LOGIN = d
    g.save()
    return JsonResponse({'status':'ok'})



# from django.http import JsonResponse
# from django.contrib.auth.models import User
# from .models import Worker, Login
#
# def workerregistration_post(request):
#     # Extract data from the request
#     Username = request.POST.get('name')
#     Photo = request.POST.get('photo')
#     Photo2 = request.POST.get('photo2')
#     Photo3 = request.POST.get('photo3')
#     Photo4 = request.POST.get('photo4')
#     Phone = request.POST.get('phone')
#     Email = request.POST.get('email')
#     Adharnumber = request.POST.get('adharnumber')
#     Jobtype = request.POST.get('jobtype')
#     Salary = request.POST.get('salary')
#     Gender = request.POST.get('gender')
#     State = request.POST.get('state')
#     pincode = request.POST.get('pincode')
#     Password = request.POST.get('password')
#     Conformpassword = request.POST.get('conform password')
#     dob = request.POST.get('dob')
#     Nationality = request.POST.get('nationality')
#     Qualification = request.POST.get('qualification')
#     Location = request.POST.get('location')
#     Experience = request.POST.get('experience')
#     Skill = request.POST.get('skills')
#     post = request.POST.get('post')
#     district = request.POST.get('district')
#
#     # Check if the user already exists with the same email
#     if User.objects.filter(email=Email).exists():
#         return JsonResponse({'status': 'error', 'message': 'User with this email already exists.'}, status=400)
#
#     # Check if the password matches the confirm password
#     if Password != Conformpassword:
#         return JsonResponse({'status': 'error', 'message': 'Password and Confirm Password do not match.'}, status=400)
#
#     # Proceed with registration
#     from datetime import datetime
#     date = datetime.now().strftime('%Y%m%d-%H%M%S') + '1.jpg'
#     import base64
#     a = base64.b64decode(Photo)
#     fs = FileSystemStorage()
#     fh = open("C:\\Users\\hibab\\OneDrive\\Desktop\\MAIN_PROJECT-WORFORCE_MANAGEMENT_SYSTEM\\media\\worker\\" + date, 'wb')
#     path = '/media/worker/' + date
#     fh.write(a)
#     fh.close()
#
#     # Saving other photos and other details similar to the above
#
#     # Save the login information
#     d = Login()
#     d.Username = Email
#     d.Password = Conformpassword
#     d.Type = 'pending'
#     d.save()
#
#     # Save the worker information
#     g = Worker()
#     g.Username = Username
#     g.Photo = path
#         g.Username = Username
#         # g.Address=Address
#         g.Photo = path
#         g.Photo1 = path1
#         g.Photo2 = path2
#         g.Photo3 = path3
#         g.Phone = Phone
#         g.Email = Email
#         g.Adharnumber = Adharnumber
#         g.Jobtype = Jobtype
#         g.Salary = Salary
#         g.Status = 'pending'
#         g.Skills = Skill
#         g.Gender = Gender
#         g.dob = dob
#         g.Nationality = Nationality
#         g.Qualification = Qualification
#         g.Location = Location
#         g.Pincode = pincode
#         g.Experience = Experience
#         g.state = State
#         g.post = post
#         g.district = district
#         g.LOGIN = d
#         g.save()
#         return JsonResponse({'status': 'ok'})
#
#
#     # Saving other details similar to the above
#
