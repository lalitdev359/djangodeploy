from django.urls import path
from . import views

namespace="home"
urlpatterns=[
   path('',views.homepage,name='home'),
   path('register',views.signup,name='register'),
   path('login',views.login,name='login'),
   path('logout',views.logout,name='logout'),
   path('search',views.search,name='search'),
   path('contact',views.contactus,name='contact'),
]