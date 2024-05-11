"""
URL configuration for untitled1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from BreakdownAssist import views

urlpatterns = [
    path('login/',views.login),
    path('admin_addpump/', views.admin_addpump),
    path('admin_editpump/<id>/', views.admin_editpump),
    path('admin_viewpump/', views.admin_viewpump),
    path('admin_deletepump/<id>/' , views.delete_pump),
    path('admin_addservice/', views.admin_addservice),
    path('admin_editservice/<id>/', views.admin_editservice),
    # path('admin_editservice/', views.admin_editservice),
    path('admin_viewservice/', views.admin_viewservice),
    path('admin_deleteservice/<id>/', views.delete_service),
    path('admin_addtow/', views.admin_addtow),
    path('admin_edittow/<id>/', views.admin_edittow),
    path('admin_deletetow/<id>/', views.delete_towservice),
    path('admin_viewtow/', views.admin_viewtow),
    path('admin_home/', views.admin_home),
    path('admin_changepwd/', views.admin_changepwd),
    path('admin_approvemech/<id>', views.admin_aprvmech),
    path('admin_rejmech/<id>', views.admin_rejctmech),
    path('admin_viewapprovedmech/', views.admin_viewapprovedmech),
    path('admin_viewfeedback/', views.admin_viewfeedback),
    path('admin_viewmech/', views.admin_viewmech),
    path('admin_viewrejectedmech/', views.admin_viewrejectedmech),
    path('admin_viewworkstatus/', views.admin_viewworkstatus),
    path('logout/',views.logout),
    path('mechanic_changepassword/', views.mechanic_changepassword),
    path('mechanic_editprofile/', views.mechanic_editprofile),
    path('editprofpost/', views.editprofpost),
    path('mechanic_home/', views.mechanic_home),
    path('mechanic_viewprofile/', views.mechanic_viewprofile),
    path('mechanic_viewpump/', views.mechanic_viewpump),
    path('mechanic_viewreq/', views.mechanic_viewreq),
    path('approveusers/<id>',views.aprvuser),
    path('rejectusers/<id>',views.rejuser),
    path('viewaprvdusers/', views.viewaprvdusers),
    path('rejectedusers/', views.rejectedusers),
    path('user_addfeedback/', views.user_addfeedback),
    path('user_changepassword/', views.user_changepassword),
    path('user_home/', views.user_home),
    path('user_viewnearestmech/', views.user_viewnearestmech),
    path('user_viewservicecenter/', views.user_viewservicecenter),
    path('user_viewtow/', views.user_viewtow),
    path('user_viewpump/', views.user_viewpump),
    path('user_chat/', views.user_chat),
    path('mechanicsignup/', views.mechanicsignup),
    path('usersignup/', views.usersignup),
    path('loginpost/', views.loginpost),
    path('addpumppost/', views.addpumppost),
    path('editpumppost/', views.editpumppost),
    path('adminviewpumppost/', views.adminviewpumppost),
    path('addservicepost/', views.addservicepost),
    path('editservicepost/', views.editservicepost),
    path('adminviewservicepost/', views.adminviewservicepost),
    path('addtowpost/', views.addtowpost),
    path('edittowpost/', views.edittowpost),
    path('adminviewtowpost/', views.adminviewtowpost),
    path('adminchangepassword/', views.adminchangepassword),
    path('viewaprvdmechpost/', views.viewaprvdmechpost),
    path('viewfeedpost/', views.viewfeedpost),
    path('viewmechpost/', views.viewmechpost),
    path('viewrejmechpost/', views.viewrejmechpost),
    path('viewstatuspost/', views.viewstatuspost),
    path('mechchangepwd/', views.mechchangepwd),
    path('viewpumppost/', views.viewpumppost),
    path('viewreqpost/', views.viewreqpost),
    path('viewaprvduserspost/', views.viewaprvduserspost),
    path('viewrejuserpost/', views.viewrejuserpost),
    path('addfeedpost/', views.addfeedpost),
    path('userchangepwd/', views.userchangepwd),
    path('viewnearestmechpost/', views.viewnearestmechpost),
    path('userviewservicepost/', views.userviewservicepost),
    path('userviewpumppost/', views.userviewpumppost),
    path('mechsignuppost/', views.mechsignuppost),
    path('usersignuppost/', views.usersignuppost),
    path('userviewtowpost/', views.userviewtowpost),
    path('userrequest/<id>',views.reqmechanic),
    path('userviewreqstatus/',views.userviewreqstatus),
    path('rating/<id>',views.rating),
    path('rating_post/',views.rating_post),
    path('user_view_rating/<id>',views.user_view_rating),

    path('forgotpassword/',views.forget_password),
    path('forget_password_post/',views.forget_password_post),

    path('chat/<id>', views.chat1),
    path('chat_send/<msg>', views.chat_send),
    path('chat_view/', views.chat_view),
    path('chat_with_std/<id>', views.chat_with_user),
    path('chat_send_teach/<msg>', views.chat_send_mech),
    path('chat_view_std/', views.chat_view_user),

    path('chat2/<id>', views.chat2),
    path('chat_send/<msg>', views.chat_send2),
    path('chat_view2/', views.chat_view2),
    path('chat_with_std/<id>', views.chat_with_user2),
    path('chat_send_teach2/<msg>', views.chat_send_mech2),
    path('chat_view_std2/', views.chat_view_user2),

]
