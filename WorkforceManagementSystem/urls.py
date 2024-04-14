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
    path('adminhom/', views.adminhom),
    path('admindashduplicate/', views.admindashduplicate),

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
    path('newadmindash/', views.newadmindash),
    path('demotable/', views.demotable),
    path('allreviewsadmin/', views.allreviewsadmin),
    path('actionblockuser/<id>', views.actionblockuser),





    path('AddNotification/', views.AddNotification),
    path('AddNotification_post/', views.AddNotification_post),
    path('ViewNotification/', views.ViewNotification),
    path('employerViewNotification/', views.employerViewNotification),
    path('employerViewNotification_post/', views.employerViewNotification_post),
    path('ViewNotification_post/', views.ViewNotification_post),
    path('DeleteNotification/<id>', views.DeleteNotification),
    path('EditNotification/<id>', views.EditNotification),
    path('EditNotification_post/', views.EditNotification_post),
    path('UpdateNotification/<id>', views.UpdateNotification),
    path('UpdateNotification1/<id>', views.UpdateNotification1),
    path('WorkerViewNotification/', views.WorkerViewNotification),
    path('blockedusers/', views.blockedusers),






# //////////////////////// Employer ////////////////////////////////////////////


    path('employergivereview_POST/', views.employergivereview_POST),
    path('employerviewreviews/', views.employerviewreviews),
    path('employerRegistration/', views.employerRegistration),
    path('employerRegistration_post/', views.employerregistration_post),
    path('employerprofile/', views.employersignup),

    path('employerdash/', views.employerdash),
    path('mainhome/', views.mainhome),
    path('employerhome/',views.employerhome),
    path('companyhome/',views.companyhome),
    path('employerdashduplicate/',views.employerdashduplicate),
    # path('viewnotification/',views.viewnotification),
    # path('addnotifications/',views.addnotifications),
    # path('sendnotification/',views.sendnotification),


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
    path('viewjobvacancyworkermore/',views.viewjobvacancyworkermore),

    path('applyforjob/',views.applyforjob),
    path('viewworkerrequests/<id>',views.viewworkerrequests),
    path('viewworkerrequests_POST/',views.viewworkerrequests_POST),
    path('approveworkerjobrequest/<id>',views.approveworkerjobrequest),
    path('rejectworkerjobrequest/<id>',views.rejectworkerjobrequest),
    path('employerrequesttoworker/<id>',views.employerrequesttoworker),
    path('assigningtoproject/<id>',views.assigningtoproject),
    path('assigningtoproject_post/',views.assigningtoproject_post),
    path('viewassigedworks/',views.viewassigedworks),
    path('viewprojectworkers/<id>',views.viewprojectworkers),

    path('searchproject/',views.searchproject),
    path('searchproject_post/',views.searchproject_post),

    path('viewsearchedworkers/', views.viewsearchedworkers),
    path('viewsearchedworkers_post/', views.viewsearchedworkers_post),
    path('viewsearchedworkerprofile/<id>',views.viewsearchedworkerprofile),
    path('viewandsearchemployer/',views.viewandsearchemployer),
    path('viewemployerprofilemore/',views.viewemployerprofilemore),
    path('viewapprovedjobrequests/<id>',views.viewapprovedjobrequests),
    path('viewapprovedjobrequests_POST/',views.viewapprovedjobrequests),
    path('Viewemployerrequestsworker/',views.Viewemployerrequestsworker),
    # path('chatm/',views.chatm),

    # path('reviewemployer/',views.reviewemployer),
    # path('viewreviews/',views.viewreviews),



    path('chat1/<id>', views.chat1),
    path('allchatscompany/', views.allchatscompany),
    path('chat_send/<msg>', views.chat_send),
    path('chat_view/', views.chat_view),
    path('employerallchats/', views.employerallchats),
    path('employerallchatview/', views.employerallchatview),
    path('employerallchatsend/<msg>', views.employerallchatsend),
    path('Viewemployerrequestsworkermore/', views.Viewemployerrequestsworkermore),
    path('acceptrprojectrequest/', views.acceptrprojectrequest),
    path('rejectprojectrequest/', views.rejectprojectrequest),
    path('viewacceptedprojectrequests/', views.viewacceptedprojectrequests),
    path('viewacceptedprojectrequests_POST/', views.viewacceptedprojectrequests_POST),
    path('assigntoproject/<id>', views.assigntoproject),




    path('viewemployerprofilemorejb/', views.viewemployerprofilemorejb),
    path('viewallworkerchats/', views.viewallworkerchats),






    path('employergivereview/', views.employergivereview),
    path('workersendreview/', views.workersendreview),



    path('assignedworkerprofile/<id>', views.assignedworkerprofile),
    path('viewmyprojectmoreworker/', views.viewmyprojectmoreworker),
    path('blockemployer/<id>', views.blockemployer),
    path('startproj/<id>', views.startproj),
    path('completedproject/<id>', views.completedproject),
    path('myreviewsemployer/', views.myreviewsemployer),
    path('viewapprovedemployers_POST/', views.viewapprovedemployers_POST),
    path('viewapprovedworkers_POST/', views.viewapprovedworkers_POST),
    path('viewrejectedemployers_POST/', views.viewrejectedemployers_POST),
    path('viewrejectedworkers_POST/', views.viewrejectedworkers_POST),
    path('viewpendingworkers_POST/', views.viewpendingworkers_POST),
    path('viewpendingemployers_POST/', views.viewpendingemployers_POST),



    # path('viewjobvacancy/',views.viewjobvacancy),
    # path('viewjobvacancy_POST/',views.viewjobvacancy_POST),
    #












############################    worker      #############################



    path('workerregistration_post/',views.workerregistration_post),
    path('flutterlogin/',views.flutterlogin ),

    path('workerprofile/',views.workerprofile ),
    path('editworkerprofile/',views.editworkerprofile ),

    path('workersendchat/', views.workersendchat),
    path('workerviewchat/', views.workerviewchat),
    path('blockworker/<id>', views.blockworker),
    path('workerviewreviews/', views.workerviewreviews),
    path('delete_reviews/', views.delete_reviews),




    path('viewemployerprofilemorejobvacancy/', views.viewemployerprofilemorejobvacancy),
    path('viewmyreviewworker/', views.viewmyreviewworker),

]
