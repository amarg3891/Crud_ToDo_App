from django.urls import path
from . import views
urlpatterns = [
    path('', views.home ,name="home"),
    path('/<int:id>/', views.update, name="update"),
     path('<int:id>', views.delete, name="delete"),
]