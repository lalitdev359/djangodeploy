from django.urls import path
from . import views

namespace='blog1'
urlpatterns = [
    path('<slug:slug>/',views.postcategory,name='postcategory'),
    path('',views.home,name='home'),
    path('<str:slug>',views.postdetail,name='postdetail'),
]
