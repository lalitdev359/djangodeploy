from django.urls import path
from . import views

namespace='shop'
urlpatterns = [
    path("", views.category, name="category"),
    path("<slug:slug>/", views.products, name="products"),
   
]
