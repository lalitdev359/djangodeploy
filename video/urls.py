from django.urls import path
from . import views

namespace='video'
urlpatterns = [
    path('',views.categorylist,name='catlist'),
    path('postComment',views.comments,name="postComment"),
    path('<slug:slug>',views.videodetail,name='videodetail'),
    path('<slug:slug>/',views.categoryvideos,name='catvideo'),
]

