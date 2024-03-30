# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='home'), 
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.my_profile, name='personal-info'),
    path('projects/',views.your_projects,name='your-projects'),
    path('details/',views.project_details,name='project-details'),
    path('hosting/',views.project_hosting,name='projects-under-hosting'),
    path('review/',views.project_review,name='projects-under-review'),
    path('timeline/',views.hosting_timeline,name='hosting-timeline'),
        path('contact/',views.my_contact,name='contact-info'),
         path('verifications/',views.verifications,name='verifications'),
         path('recommended/',views.recommended,name='recommended'),
         path('find/',views.find_project,name='find-projects'),





    # re_path(r'^.*\.*', views.pages, name='pages'),
]
