from django.urls import path
from . import views
from django.conf.urls.static import static
from sfmproject import settings
urlpatterns=[
    path('',views.projectindex,name='projectindex'),
    path('projectlogin',views.projectlogin,name='projectlogin'),
    path('projectreg',views.projectreg,name='projectreg'),
    path('projectabout', views.projectabout,name='projectabout'),
    path('index',views.index,name='index'),
    path('projectdonar',views.projectdonar,name='projectdonar'),
    path('adminregedit/<str:sid>',views.adminregedit,name='adminregedit'),
    path('donations',views.donations,name='donations'),
    path('admindashboard',views.admindashboard,name='admindashboard'),
    path('projectnewdonation',views.projectnewdonation,name='projectnewdonation'),
    path('projectdonation',views.projectdonation,name='projectdonation'),
    path('donations',views.donations,name='donations'),
    path('projectedit/<str:sid>',views.projectedit,name='projectedit'),
    path('deletedonation/<str:sid>',views.deletedonation,name='deletedonation'),
    path('adminreg',views.adminreg,name='adminreg'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminregdelete/<str:sid>',views.adminregdelete,name='adminregdelete'),
    path('adminactive/<int:sid>',views.adminactive,name='adminactive'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('donordetails',views.donordetails,name='donordetails'),
    path('logout',views.logout,name="logout"),
    path('orphanrequest/<str:donorid>',views.orphanrequest,name="orphanrequest"),
    path('header',views.header,name="header"),
    path('design',views.design,name="design"),

]+ static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)