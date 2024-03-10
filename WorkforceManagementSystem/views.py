import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import render, redirect

# Create your views here.
from geopy.distance import geodesic

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
            # return HttpResponse('''<script>alert("login successfully");window.location="/wForce/adminhome/"</script>''')
            return HttpResponse('''<script>window.location="/wForce/adminhome/"</script>''')
        elif a.Type=="employer":
            # return HttpResponse('''<script>alert("login successfully");window.location="/wForce/employerdash/"</script>''')
            return HttpResponse(
                '''<script>window.location="/wForce/employerdash/"</script>''')
        else:
            return HttpResponse('''<script>alert("User not found");window.location="/wForce/login/"</script>''')
    else:
        return HttpResponse('''<script>alert("Invalid username or password");window.location="/wForce/login/"</script>''')

























#
# /////////////////////////////    Admin    /////////////////////////////////////////////



def mainhome(request):
    return render(request, "mainhome1index.html")




def adminhome(request):
    return render(request,'admindashinbox.html')


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
    k =Employer.objects.filter(LOGIN__Type="pending").order_by('-id')
    # return render(request, "Approval_of_Registration.html",{'data':k})
    return render(request,'Approval_of_Registration.html',{'data':k})

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



def approvalofregistrationworker_more(request,id):
    k =Worker.objects.get(LOGIN=id)
    return render(request, "view_worker.html",{'data': k})


def approvalofregistrationworker_POST(request):
    name=request.POST['textfield']
    k =Worker.objects.filter(LOGIN__Type="pending",Username__icontains=name)
    return render(request, "approveworker.html", {'data': k})



def approvalofregistrationworker(request):
    k =Worker.objects.filter(LOGIN__Type="pending").order_by('-id')
    return render(request, "approveworker.html",{'data':k})


def approve_worker(request,lid):
    res=Login.objects.filter(id=lid).update(Type="worker")
    return HttpResponse('''<script>alert('Approve Successfull');window.location="/wForce/approvalofregistrationworker/"</script>''')

def reject_worker(request,lid):
    res=Login.objects.filter(id=lid).update(Type="rejected")
    return HttpResponse('''<script>alert('Reject Successfull');window.location="/wForce/approvalofregistrationworker/"</script>''')



#
# ////////// view employers /////////



def viewapprovedemployers(request):
    t=Employer.objects.filter(LOGIN__Type="employer").order_by('-id')
    return render(request, "viewapprovedemployers.html", {'data': t})

def viewrejectedemployers(request):

    t1=Employer.objects.filter(LOGIN__Type="rejected").order_by('-id')
    return render(request, "viewrejectedemployers.html", {'data': t1})

def viewpendingemployers(request):

    t=Employer.objects.filter(LOGIN__Type="pending").order_by('-id')
    return render(request, "viewpendingemployers.html", {'data': t})

def viewapprovedemployersmore(request,id):
    u=Employer.objects.get(LOGIN=id)
    return render(request, "viewapprovedemployersmore.html", {'data': u})

def viewarejectedemployersmore(request,id):

    w=Employer.objects.get(LOGIN=id)
    return render(request, "viewrejectedemployersmore.html", {'data': w})


def viewpendingemployersmore(request,id):

    y=Employer.objects.get(LOGIN=id)
    return render(request, "viewpendingemployersmore.html", {'data': y})



#
# //// view workers /////


def viewapprovedworkers(request):

    s=Worker.objects.filter(LOGIN__Type="worker").order_by('-id')
    return render(request, "viewapprovedworkers.html", {'data': s})

def viewrejectedworkers(request):

    s=Worker.objects.filter(LOGIN__Type="rejected").order_by('-id')
    return render(request, "viewrejectedworkers.html", {'data': s})

def viewpendingworkers(request):

    s=Worker.objects.filter(LOGIN__Type="pending").order_by('-id')
    return render(request, "viewpendingworkers.html", {'data': s})



def viewapprovedworkersmore(request,id):

    v=Worker.objects.get(LOGIN=id)
    return render(request, "viewapprovedworkersmore.html", {'data': v})


def viewrejectedworkersmore(request,id):

    x=Worker.objects.get(LOGIN=id)
    return render(request, "viewrejectedworkersmore.html", {'data': x})



def viewpendingworkersmore(request,id):

    z=Worker.objects.get(LOGIN=id)
    return render(request, "viewpendingworkersmore.html", {'data': z})


def newadmindash(request):
    return render(request,'newadminindex.html')

def demotable(request):
    return render(request,'demotable.html')












# //////////////////////////////      Employer      ///////////////////////////////////////


def employerdash(request):
    return render(request,'employerdashinbox.html')

def employerRegistration(request):
    da = str(datetime.date.today())
    return render(request,"registrationindex.html", {'dt':da})

def employersignup(request):
    date=datetime.datetime.now()
    return render(request, "employsignupindex.html",{"data":date})

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
    registration_date = datetime.datetime.now().date()
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
        g.registration_date=registration_date
        g.LOGIN=d
        g.save()

        return HttpResponse('''<script>alert("Success");window.location="/wForce/login/"</script>''')

    else:
        return HttpResponse('''<script>alert("Password mismatching");window.location="/wForce/employerprofile/"</script>''')



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





# def approvalofregistrationworker_more(request,id):
#     k =Worker.objects.get(LOGIN=id)
#     pay_info=Payment.objects.filter(LOGIN=id)










def employerdash(request):
    return render(request, "employerdashindex.html")
def employerhome(request):
    return render(request, "employerhomeindex.html")

#
# def workersignup(request):
#     return render(request, "employsignupindex.html")


# def reviewemployer(request):
#     r=Employer.objects.get(LOGIN=request.session['lid'])
#     return render(request,"",{'data':r})



def employerviewprofile(request):
    r=Employer.objects.get(LOGIN=request.session['lid'])
    return render(request,"EmployerViewProfile.html",{'data':r})


def editemployerviewprofile(request):
    dt = str(datetime.date.today())
    r=Employer.objects.get(LOGIN=request.session['lid'])
    return render(request,"editemployerprofile.html",{'data':r, 'dt':dt})


def editemployerviewprofile_POST(request):
    Companyname=request.POST['textfield']
    Phone=request.POST['textfield3']
    Email=request.POST['textfield2']
    Place = request.POST['textfield7']
    Post = request.POST['textfield9']
    District = request.POST['textfield10']
    State = request.POST['textfield15']
    Pincode = request.POST['textfield8']
    Date = request.POST['textfield5']
    # Status = request.POST['textfield2']
    # Category = request.POST['textfield2']
    Website =request.POST['textfield4']
    # Photo1 =request.POST['fileField3']
    # Photo2 = request.POST['fileField4']
    # Photo3 = request.POST['fileField5']
    Aboutcompany = request.POST['textarea']
    registration_date = datetime.datetime.now().date()


    g=Employer.objects.get(LOGIN_id=request.session['lid'])
    if 'coverphoto' in request.FILES:
        coverphoto = request.POST['coverphoto']

        e=FileSystemStorage()
        h='employer/photos/cover/'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S%f')+coverphoto.name
        e.save(h,coverphoto)
        g.Photo=e.url(h)
        g.save()
    elif 'photo1' in request.FILES:
        photo1 = request.POST['photo1']
        e=FileSystemStorage()
        j = 'employer/photos/photo1/' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S%f') + photo1.name
        e.save(j,photo1)
        g.Photo1=e.url(j)
        g.save()

    elif 'photo2' in request.FILES:
        photo2 = request.POST['photo2']
        e = FileSystemStorage()
        k = 'employer/photos/photo2/' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S%f') + photo2.name
        e.save(k, photo2)
        g.Photo2 = e.url(k)
        g.save()
    elif 'photo3' in request.FILES:
        photo3 = request.POST['photo3']
        e = FileSystemStorage()
        l = 'employer/photos/photo3/' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S%f') + photo3.name
        e.save(l, photo3)
        g.Photo3 = e.url(l)
        g.save()

    g.Companyname=Companyname
    g.Phone=Phone
    g.Email=Email
    g.Place =Place
    g.Post = Post
    g.District = District
    g.State =State
    g.Pincode = Pincode
    g.Date = Date
    g.Website =Website
    g.Aboutcompany =Aboutcompany
    g.registration_date=registration_date
    g.save()

    return HttpResponse('''<script>alert('Update Successfull');window.location="/wForce/editemployerviewprofile/"</script>''')





# ////project/////


def addproject(request):
    return render(request,"addproject.html")

def addproject_POST(request):
    projecttitle= request.POST['textfield']
    projectdescription = request.POST['textarea']
    projectlocation = request.POST['textfield1']
    created_date= datetime.datetime.now().date()
    duration= request.POST['textfield2']
    no_of_workers=request.POST['textfield3']
    g = Projects()
    g.projecttitle = projecttitle
    g.projectdescription = projectdescription
    g.projectlocation = projectlocation
    g.created_date = created_date
    g.duration = duration
    g.no_of_workers = no_of_workers
    g.EMPLOYER=Employer.objects.get(LOGIN_id=request.session['lid'])
    g.save()
    return HttpResponse('''<script>alert('Added Successfully');window.location="/wForce/addproject/"</script>''')



def viewproject(request):
    g = Projects.objects.filter(EMPLOYER__LOGIN_id=request.session['lid'])
    # r=Jobvaccancy.objects.get(PROJECT=g)

    return render(request,"viewproject.html",{'data':g})


def viewproject_POST(request):
    projecttitle= request.POST['textfield']
    projectdescription = request.POST['textarea']
    projectlocation = request.POST['textfield1']
    created_date= datetime.datetime.now().date()
    duration = request.POST['textfield2']
    no_of_workers = request.POST['textfield3']
    search = request.POST['textfield']
    b = Projects.objects.filter(Type__icontains=search)

    return render(request, "viewproject.html", {'data': b})

def projectdelete(request,id):
    s=Projects.objects.get(id=id).delete()
    return HttpResponse('''<script>alert('Deleted Successfully');window.location="/wForce/viewproject/"</script>''')


def editproject(request,id):
    res=Projects.objects.get(id=id)
    return render(request,"editproject.html",{'data':res})


def editproject_POST(request):
    id=request.POST['id']
    projecttitle = request.POST['textfield']
    projectdescription = request.POST['textarea']
    projectlocation = request.POST['textfield1']
    created_date = datetime.datetime.now().date()
    duration = request.POST['textfield2']
    no_of_workers = request.POST['textfield3']
    g = Projects.objects.get(id=id)
    g.projecttitle = projecttitle
    g.projectdescription = projectdescription
    g.projectlocation = projectlocation
    g.created_date = created_date
    g.duration = duration
    g.no_of_workers = no_of_workers
    g.EMPLOYER = Employer.objects.get(LOGIN_id=request.session['lid'])
    g.save()
    return HttpResponse('''<script>alert('Updated Successfully');window.location="/wForce/viewproject/"</script>''')


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







def viewjobvacancy(request):
    res=Jobvaccancy.objects.filter(EMPLOYER__LOGIN_id=request.session['lid']).order_by('-id')
    l=[]
    p=Projects.objects.filter(EMPLOYER__LOGIN_id=request.session['lid'])
    for i in p:
        s=Jobvaccancy.objects.filter(EMPLOYER__LOGIN_id=request.session['lid'],PROJECT=i)
        ll=[]
        for m in s:
            ll.append(m)
        v={'project':i,'job':ll}
        l.append(v)

    return render(request,"viewjobvacancy.html",{'data':l})

def addjobvacancy(request):
    g=Projects.objects.filter(EMPLOYER__LOGIN_id=request.session['lid'])
    return render(request,"addjobvaccancy.html",{'data':g})


def addjobvacancy_POST(request):
    jobtitle= request.POST['textfield']
    jobfield = request.POST['select1s']

    projecttitle=request.POST['projecttitle']
    created_date= datetime.datetime.now().date()

    location=request.POST['textfield4']
    district=request.POST['select2']
    startdate=request.POST['textfield5']
    enddate=request.POST['textfield6']
    salary=request.POST['textfield13']
    eno_of_vaccancy =request.POST['textfield8']
    skills=request.POST['textfield7']
    created_date = datetime.datetime.now().date()

    g = Jobvaccancy()
    g.jobtitle = jobtitle
    g.jobfield  = jobfield
    g.PROJECT=Projects.objects.get(id=projecttitle)
    g.created_date = created_date

    g.location = location
    g.startdate =startdate
    g.enddate=enddate
    g.district=district
    g.eno_of_vaccancy =eno_of_vaccancy
    g.skills= skills
    g.salary= salary
    g.EMPLOYER=Employer.objects.get(LOGIN_id=request.session['lid'])
    g.save()
    return HttpResponse('''<script>alert('Added Successfully');window.location="/wForce/addjobvacancy/"</script>''')

def editjobvacancy(request,id):
    res=Jobvaccancy.objects.get(id=id)
    return render(request,"editjobvacancy.html",{'data':res})


def editjobvacancy_POST(request):
    id=request.POST['id']
    jobtitle = request.POST['textfield']
    jobfield = request.POST['select']

    created_date = datetime.datetime.now().date()

    location = request.POST['textfield4']
    district = request.POST['textfield12']
    startdate = request.POST['textfield5']
    enddate = request.POST['textfield6']
    skills = request.POST['textfield7']
    salary = request.POST['textfield13']
    eno_of_vaccancy = request.POST['textfield8']



    g = Jobvaccancy.objects.get(id=id)
    g.jobtitle = jobtitle
    g.jobfield = jobfield

    g.created_date = created_date

    g.location = location
    g.startdate = startdate
    g.enddate = enddate
    g.skills = skills
    g.district = district
    g.salary = salary
    g.eno_of_vaccancy = eno_of_vaccancy


    g.EMPLOYER = Employer.objects.get(LOGIN_id=request.session['lid'])
    g.save()
    return HttpResponse('''<script>alert('Updated Successfully');window.location="/wForce/viewjobvacancy/"</script>''')


def deletejobvacancy(request,id):
    obj=Jobvaccancy.objects.get(id=id)
    obj.delete()
    return HttpResponse('''<script>alert('Deleted Successfully');window.location="/wForce/viewjobvacancy/"</script>''')


#
# def viewjobvacancy(request):
#     return render(request,"viewjobvacancy.html")
#
#
#
# def viewjobvacancy_POST(request):
#     search= request.POST['textfield']
#
#     b = Projects.objects.filter(Type__icontains=search)
#     return render(request, "viewjobvacancy.html", {'data': b})


def viewsearchedworkers(request):
    return render(request, "viewsearchedworkers.html")

def viewsearchedworkers_post(request):
    search= request.POST['textfield']
    skill= request.POST['textfield2']
    from geopy.geocoders import Nominatim, Photon


    geolocator = Photon(user_agent="geoapiExercises")
    # geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(search)
    lat,lon= location.latitude, location.longitude

    b = Worker.objects.filter(Skills__icontains=skill,LOGIN__Type='worker')
    l=[]
    for i in b:
        distance = geodesic((lat, lon), (float(i.lattitude), float(i.longitude))).kilometers
        l.append({'id':i.id,'Username':i.Username,
        'Photo':i.Photo,
        'Location':i.Location,
        'post':i.post,
        'district':i.district,
        'state':i.state,
        'Pincode':i.Pincode,
        'Phone':i.Phone,
        'Email':i.Email,
        'latitude':i.lattitude,
        'longitude':i.longitude,
        'registration_date':i.registration_date,
        'distance':distance
        })


    for i in range(0,len(l)):
        for j in range(0,len(l)):

            if  float(l[i]['distance']) < float(l[j]['distance']):


                temp=l[i]
                l[i]=l[j]
                l[j]=temp




    return render(request, "viewsearchedworkers.html",{'data':l})


def viewworkerrequests(request,id):
    res=Jobrequest.objects.filter(JOBVACANCY_id=id,status='pending').order_by('-id')
    return render(request, "viewworkerrequests.html",{"data":res})

def viewworkerrequests_POST(request):
    return render(request, "viewworkerrequests.html")

def searchproject(request):
    q=Projects.objects.filter(EMPLOYER__LOGIN_id=request.session['lid'])
    return render(request, "searchproject.html",{"data":q})


def searchproject_post(request):
    wid=request.session['wid']
    pid=request.POST['pid']
    if Workerrequest.objects.filter(PROJECT_id=pid,WORKER_id=wid).exists():
     return HttpResponse('''<script>alert('Project already exist to this person ');history.back()</script>''')



    a = Workerrequest()

    a.PROJECT_id = pid
    a.WORKER_id = wid
    a.date = datetime.datetime.now().strftime('%d-%m-%Y')
    a.status = 'Pending'
    a.save()

    return HttpResponse('''<script>alert('Requested ');window.location="/wForce/viewsearchedworkers/"</script>''')


def employerrequesttoworker(request,id):
    request.session['wid']=id
    q=Projects.objects.filter(EMPLOYER__LOGIN_id=request.session['lid'])
    return render(request, "searchproject.html",{"data":q})

def employerrejectworkerrequest(request,id):

    return HttpResponse('''<script>alert('Rejected ');window.location="/wForce/viewsearchedworkers/"</script>''')







def approveworkerjobrequest(request,id):
    res=Jobrequest.objects.filter(id=id).update(status="Accepted")
    return HttpResponse('''<script>alert('Approve Successfull');window.location="/wForce/viewjobvacancy/"</script>''')

def rejectworkerjobrequest(request,id):
    res=Jobrequest.objects.filter(id=id).update(status="rejected")
    return HttpResponse('''<script>alert('Reject Successfull');window.location="/wForce/viewjobvacancy/"</script>''')

def viewsearchedworkerprofile(request,id):

    v=Worker.objects.get(id=id)

    return render(request, "viewsearchedworkerprofile.html", {'data': v})



def viewapprovedjobrequests(request,id):
    res=Jobrequest.objects.filter(JOBVACANCY_id=id,status='Accepted').order_by('-id')
    return render(request, "viewapprovedjobrequests.html",{"data":res})

def viewapprovedjobrequests_POST(request):
    return render(request, "viewapprovedjobrequests.html")



def chat1(request, id):
    if request.session['lid']!='':
        request.session["workerid"] = id
        cid = str(request.session["workerid"])
        request.session["new"] = cid
        qry = Worker.objects.get(LOGIN=cid)

        return render(request, "Chats.html", {'photo': qry.photo, 'name': qry.name, 'toid': cid})
    else:
        return HttpResponse('''<script>alert('You are not Logined');window.location='/wForce/login/'</script>''')


def chat_view(request):
    if request.session['lid']!='':
        fromid = request.session["lid"]
        toid = request.session["workerid"]
        qry = Worker.objects.get(LOGIN=request.session["workerid"])
        from django.db.models import Q

        res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid))
        l = []

        for i in res:
            l.append({"id": i.id, "message": i.message, "to": i.TOID_id, "date": i.date, "from": i.FROMID_id})

        return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.name, 'toid': request.session["workerid"]})
    else:
        return HttpResponse('''<script>alert('You are not Logined');window.location='/wForce/login/'</script>''')


def chat_send(request, msg):
    if request.session['lid']!='':
        lid = request.session["lid"]
        toid = request.session["workerid"]
        message = msg

        import datetime
        d = datetime.datetime.now().date()
        chat = Chat()
        chat.message = message
        chat.TOID_id = toid
        chat.FROMID_id = lid
        chat.date = d
        chat.save()
    else:
        return HttpResponse('''<script>alert('You are not Logined');window.location='/wForce/login/'</script>''')
    return JsonResponse({"status": "ok"})















# #####################    worker   ##############################




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
    print(dob)
    Nationality = request.POST['nationality']
    Qualification = request.POST['qualification']
    Location=request.POST['location']
    Experience=request.POST['experience']
    Skill=request.POST['skills']
    post=request.POST['post']
    district=request.POST['district']
    latitude=request.POST['latitude']
    longitude=request.POST['longitude']
    from datetime import datetime
    registration_date = datetime.now().date().today()
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
    g.lattitude=latitude
    g.longitude=longitude
    g.registration_date=registration_date
    g.LOGIN = d
    g.save()
    return JsonResponse({'status':'ok'})







def flutterlogin(request):
    username=request.POST['name']
    password=request.POST['password']
    print(username)
    print(password)
    a = Login.objects.filter(Username=username, Password=password)
    if a.exists():
        a = Login.objects.get(Username=username, Password=password)


        if a.Type == 'worker':
            return JsonResponse({'status': 'ok',"lid":a.id})
        else:
            return JsonResponse({'status': 'no'})
    else:
        return JsonResponse({'status': 'no'})



def workerprofile(request):
    lid=request.POST['lid']
    f=Worker.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok',
                         'name':f.Username,
                         'Photo':f.Photo,
                         'Photo1':f.Photo1,
                         'Photo2':f.Photo2,
                         'Photo3':f.Photo3,
                         'Phone':f.Phone,
                         'Email':f.Email,
                         'Adharnumber':f.Adharnumber,
                         'Jobtype':f.Jobtype,
                         'Salary':f.Salary,
                         'Status':f.Status,
                         'Skills':f.Skills,
                         'Gender':f.Gender,
                         'Date of birth':f.dob,
                         'Nationality':f.Nationality,
                         'Qualification':f.Qualification,
                         'location':f.Location,
                         'Pincode':f.Pincode,
                         'Experience':f.Experience,
                         'Post': f.post,
                         'District': f.district,
                         'State':f.state,
                         })

def editworkerprofile(request):
    name=request.POST['name']
    Photo=request.POST['Photo']
    Photo1=request.POST['Photo1']
    Photo2=request.POST['Photo2']
    Photo3=request.POST['Photo3']
    Phone=request.POST['Phone']
    Email=request.POST['Email']
    Adharnumber=request.POST['Adharnumber']
    Jobtype=request.POST['Jobtype']
    Salary=request.POST['Salary']
    # Status=request.POST['Status']
    Skills=request.POST['Skills']
    Gender=request.POST['Gender']
    dob=request.POST['dob']
    Nationality=request.POST['Nationality']
    Qualification=request.POST['Qualification']
    location=request.POST['location']
    Pincode=request.POST['Pincode']
    Experience=request.POST['Experience']
    Post=request.POST['Post']
    District=request.POST['District']
    State=request.POST['State']
    lid=request.POST['lid']

    if len(Photo)>5:
        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + '1.jpg'
        import base64
        a = base64.b64decode(Photo)
        fs = FileSystemStorage()
        # fn= fs.save(date,Photo)
        fh = open(
            "C:\\Users\\hibab\\OneDrive\\Desktop\\MAIN_PROJECT-WORFORCE_MANAGEMENT_SYSTEM\\media\\worker\\" + date,
            'wb')
        path = '/media/worker/' + date
        fh.write(a)
        fh.close()
        y = Worker.objects.get(LOGIN_id=lid)
        y.Photo = path
        y.save()


    if len(Photo1)>5:
        from datetime import datetime
        date2 = datetime.now().strftime('%Y%m%d-%H%M%S') + '2.jpg'
        import base64
        a = base64.b64decode(Photo1)
        fs = FileSystemStorage()
        # fn1 = fs.save(date2, Photo2)
        fh1 = open(
            "C:\\Users\\hibab\\OneDrive\\Desktop\\MAIN_PROJECT-WORFORCE_MANAGEMENT_SYSTEM\\media\\worker\\" + date2,
            'wb')
        path1 = '/media/worker/' + date2
        fh1.write(a)
        fh1.close()
        y = Worker.objects.get(LOGIN_id=lid)
        y.Photo1 = path1
        y.save()

    if len(Photo2)>5:
        from datetime import datetime
        date3 = datetime.now().strftime('%Y%m%d-%H%M%S') + '3.jpg'
        import base64
        a = base64.b64decode(Photo2)
        fs = FileSystemStorage()
        # fn2 = fs.save(date2, Photo3)
        fh2 = open(
            "C:\\Users\\hibab\\OneDrive\\Desktop\\MAIN_PROJECT-WORFORCE_MANAGEMENT_SYSTEM\\media\\worker\\" + date3,
            'wb')
        path2 = '/media/worker/' + date3
        fh2.write(a)
        fh2.close()
        y = Worker.objects.get(LOGIN_id=lid)
        y.Photo2 = path2
        y.save()

    if len(Photo3)>5:
        from datetime import datetime
        date4 = datetime.now().strftime('%Y%m%d-%H%M%S') + '4.jpg'
        import base64
        a = base64.b64decode(Photo3)
        fs = FileSystemStorage()
        # fn3 = fs.save(date4, Photo4)
        fh3 = open(
            "C:\\Users\\hibab\\OneDrive\\Desktop\\MAIN_PROJECT-WORFORCE_MANAGEMENT_SYSTEM\\media\\worker\\" + date4,
            'wb')
        path3 = '/media/worker/' + date4
        fh3.write(a)
        fh3.close()
        y = Worker.objects.get(LOGIN_id=lid)
        y.Photo3=path3
        y.save()

    y=Worker.objects.get(LOGIN_id=lid)
    y.Username=name
    # y.Photo=Photo
    # y.Photo1=Photo1
    # y.Photo2=Photo2
    # y.Photo3=Photo3
    y.Phone=Phone
    y.Email=Email
    y.Adharnumber=Adharnumber
    y.Jobtype=Jobtype
    y.Salary=Salary
    y.Skills=Skills
    y.Gender=Gender
    y.dob=dob

    y.Nationality=Nationality
    y.Qualification=Qualification
    y.Location=location
    y.Pincode=Pincode
    y.Experience=Experience
    y.post=Post
    y.district=District
    y.state=State
    y.save()

    return JsonResponse({'status':'ok'})

def viewjobvacancyworker(request):
    location=request.POST["value"]
    jobtitle=request.POST["value"]
    district=request.POST["value"]
    lid=request.POST['lid']
    p=Jobvaccancy.objects.filter(location__icontains=location)|Jobvaccancy.objects.filter(jobtitle__icontains=jobtitle)|Jobvaccancy.objects.filter(district__icontains=district)
    l=[]
    for i in p:
        s='yes'
        if Jobrequest.objects.filter(JOBVACANCY=i.id,WORKER=Worker.objects.get(LOGIN_id=lid)).exists():
            s='no'
        l.append({'id':i.id,
                  'Company':i.EMPLOYER.Companyname,
                  'email':i.EMPLOYER.Email,
                  'Phone':i.EMPLOYER.Phone,
                  'Title':i.jobtitle,
                  'Jobfield':i.jobfield,
                  'Location':i.location,
                  'Start_date':i.startdate,
                  'End_date':i.enddate,
                  'Skills':i.skills,
                  'No_of_vacancy':i.eno_of_vaccancy,
                  's':s})
    return JsonResponse({'status': 'ok',"data":l})

def viewjobvacancyworkermore(request):
    jid=request.POST['jid']
    lid=request.POST['lid']
    i=Jobvaccancy.objects.get(id=jid)
    s = 'yes'
    if Jobrequest.objects.filter(JOBVACANCY=i.id, WORKER=Worker.objects.get(LOGIN_id=lid)).exists():
        s = 'no'
    return JsonResponse({'status': 'ok','id':i.id,
                  'companyname':i.EMPLOYER.Companyname,
                  'email':i.EMPLOYER.Email,
                  'phone':i.EMPLOYER.Phone,
                  'photo':i.EMPLOYER.Photo,
                  'district':i.district,
                  'salary':i.salary,
                  'jobtitle':i.jobtitle,
                  'jobfield':i.jobfield,
                  'location':i.location,
                  'startdate':i.startdate,
                  'enddate':i.enddate,
                  'skills':i.skills,
                  'vacancynumber':i.eno_of_vaccancy,
                  's':s})

def applyforjob(request):
    lid=request.POST['lid']
    jid=request.POST['jid']
    jobj=Jobrequest()
    jobj.JOBVACANCY_id=jid
    jobj.WORKER=Worker.objects.get(LOGIN_id=lid)
    jobj.date=datetime.datetime.now().strftime("%d-%m-%Y")
    jobj.status="pending"
    jobj.save()

    return JsonResponse({'status': 'ok'})


def viewandsearchemployer(request):
    Place=request.POST["value"]
    Companyname=request.POST["value"]
    lid=request.POST['lid']
    p=Employer.objects.filter(Companyname__icontains=Companyname,LOGIN__Type="employer").order_by('-id')|Employer.objects.filter(Place__icontains=Place,LOGIN__Type="employer").order_by('-id')
    l=[]
    for i in p:
        l.append({'id':i.id,
                  'Company':i.Companyname,
                  'Photo':i.Photo,
                  'email':i.Email,
                  'Phone':i.Phone,
                  'Date':i.Date,
                  'Location':i.Place,
                  })
    return JsonResponse({'status': 'ok',"data":l})

def viewemployerprofilemore(request):

        lid =request.POST['lid']
        eid =request.POST['eid']
        # i = Employer.objects.get(id=lid)
        i = Employer.objects.get(id=eid)
        # if Jobrequest.objects.filter(EMPLOYER=i.id, WORKER=Worker.objects.get(LOGIN_id=lid)).exists():
        #     s = 'no'
        return JsonResponse({'status': 'ok', 'id': i.id,
                             'Companyname': i.Companyname,
                             'Email': i.Email,
                             'Phone': i.Phone,
                             'Photo': i.Photo,
                             'District': i.District,
                             'Place': i.Place,
                             'Post': i.Post,
                             'State': i.State,
                             'Pincode': i.Pincode,
                             'Category': i.Category,
                             'Website': i.Website,
                             'Photo1': i.Photo1,
                             'Photo2': i.Photo2,
                             'Photo3': i.Photo3,
                             'Aboutcompany':i.Aboutcompany,
                           })

def Viewemployerrequestsworker(request):
    lid=request.POST['lid']
    p=Workerrequest.objects.filter(WORKER__LOGIN_id=lid).order_by('-id')
    l=[]
    for i in p:
        l.append({'id':i.id,

                  'Company':i.PROJECT.EMPLOYER.Companyname,
                  'Photo':i.PROJECT.EMPLOYER.Photo,
                  'email':i.PROJECT.EMPLOYER.Email,
                  'projecttitle':i.PROJECT.projecttitle,
                  'date':i.date,
                  'Location':i.PROJECT.EMPLOYER.Place,
                  })
    return JsonResponse({'status': 'ok',"data":l})


def workersendchat(request):
    frm_id=request.POST['from_id']
    to_id = request.POST['to_id']
    message=request.POST['message']
    obj=Chat()
    obj.FROMID_id=frm_id
    obj.TOID_id=to_id
    obj.message=message
    obj.date=datetime.now()
    obj.save()
    return JsonResponse({'status': 'ok'})

def workerviewchat(request):
    fromid = request.POST["from_id"]
    toid = request.POST["to_id"]
    # lmid = request.POST["lastmsgid"]
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid))
    l = []

    for i in res:
        l.append({"id": i.id, "msg": i.message, "from": i.FROMID_id, "date": i.date, "to": i.TOID_id})

    return JsonResponse({"status":"ok",'data':l})
