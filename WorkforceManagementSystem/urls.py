"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""





# ////////////////////////////   admin ///////////////////////////////



from django.contrib import admin
from django.urls import path

from WorkforceManagementSystem import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('login_post/', views.login_post),

    # path('employerprofile_post/', views.employerprofile_post),
    path('addfee/', views.addfee),
    path('addfee_post/', views.addfee_post),
    path('viewfee/', views.viewfee),
    path('viewfee_post/', views.viewfee_post),
    path('editfee/<id>', views.editfee),
    path('editfee_post/', views.editfee_post),
    path('adminhome/',views.adminhome),
    path('deletefee/<id>', views.deletefee),
    path('approvalofregistrationemployer/', views.approvalofregistrationemployer),
    path('approvalofregistrationemployer_more/<id>', views.approvalofregistrationemployer_more),
    path('approvalofregistrationworker_more/<id>', views.approvalofregistrationworker_more),
    path('approve_worker/<lid>', views.approve_worker),
    path('reject_worker/<lid>', views.reject_worker),
    path('approvalofregistrationworker/', views.approvalofregistrationworker),
    path('approvalofregistrationworker_POST/', views.approvalofregistrationworker_POST),
    path('employer_aprrove_reject/<lid>', views.employer_aprrove_reject),
    path('employer_reject/<lid>', views.employer_reject),
    path('approvalofregistrationemployer_POST/', views.approvalofregistrationemployer_POST),


    path('viewapprovedemployers/', views.viewapprovedemployers),
    path('viewrejectedemployers/', views.viewrejectedemployers),
    path('viewpendingemployers/', views.viewpendingemployers),

    path('viewapprovedworkers/', views.viewapprovedworkers),
    path('viewrejectedworkers/', views.viewrejectedworkers),
    path('viewpendingworkers/', views.viewpendingworkers),


    path('viewapprovedemployersmore/<id>', views.viewapprovedemployersmore),
    path('viewrejectedemployersmore/<id>', views.viewarejectedemployersmore),
    path('viewpendingemployersmore/<id>', views.viewpendingemployersmore),


    path('viewapprovedworkersmore/<id>', views.viewapprovedworkersmore),
    path('viewrejectedworkersmore/<id>', views.viewrejectedworkersmore),
    path('viewpendingworkersmore/<id>', views.viewpendingworkersmore),







# //////////////////////// Employer ////////////////////////////////////////////


    path('employerRegistration/', views.employerRegistration),
    path('employerRegistration_post/', views.employerregistration_post),
    path('employerprofile/', views.employersignup),

    path('employerdash/', views.employerdash),
    path('mainhome/', views.mainhome),
    path('employerhome/',views.employerhome),
    path('employerviewprofile/',views.employerviewprofile),
    path('editemployerviewprofile/',views.editemployerviewprofile),
    path('editemployerviewprofile_POST/',views.editemployerviewprofile_POST),
    path('addproject/',views.addproject),
    path('addproject_POST/',views.addproject_POST),
    path('editproject_POST/',views.editproject_POST),
    path('editproject/<id>',views.editproject),
    path('viewproject/',views.viewproject),
    path('viewproject_POST/',views.viewproject_POST),
    path('projectdelete/<id>',views.projectdelete),
    path('addjobvacancy/',views.addjobvacancy),
    path('addjobvacancy_POST/',views.addjobvacancy_POST),
    path('viewjobvacancy/',views.viewjobvacancy),
    path('editjobvacancy/<id>',views.editjobvacancy),
    path('editjobvacancy_POST/',views.editjobvacancy_POST),
    path('deletejobvacancy/<id>',views.deletejobvacancy),
    path('viewjobvacancyworker/',views.viewjobvacancyworker),





    # path('viewjobvacancy/',views.viewjobvacancy),
    # path('viewjobvacancy_POST/',views.viewjobvacancy_POST),
    #












############################    worker      #############################



    path('workerregistration_post/',views.workerregistration_post),
    path('flutterlogin/',views.flutterlogin ),
    path('workerprofile/',views.workerprofile ),
    path('editworkerprofile/',views.editworkerprofile ),

]
