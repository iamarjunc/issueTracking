from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('home/', views.home, name='home'),
    path('get_user_list/', views.get_user_list, name='get_user_list'),
    path('add_project/', views.add_project, name='add_project'),
    path('get_project_list/', views.get_project_list, name='get_project_list'),
    path('add_issue/', views.add_issue, name='add_issue'),    
    path('get_issue_list/', views.get_issue_list, name='get_issue_list'),    
    # Add more URLs for user-related views 
]
