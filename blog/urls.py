from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('categories/', views.category_view, name='category')
]