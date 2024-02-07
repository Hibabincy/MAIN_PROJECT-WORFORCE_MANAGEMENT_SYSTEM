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
from django.contrib import admin
from django.urls import path

from WorkforceManagementSystem import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('login_post/', views.login_post),
    path('employerRegistration/', views.employerRegistration),
    path('employerRegistration_post/', views.employerRegistration_post),
    path('employerprofile/', views.employerprofile),
    path('employerprofile_post/', views.employerprofile_post),
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
    path('employer_aprrove_reject/', views.employer_aprrove_reject),
    path('approvalofregistrationemployer_POST/', views.approvalofregistrationemployer_POST),
    path('employerdash/', views.employerdash),

]
