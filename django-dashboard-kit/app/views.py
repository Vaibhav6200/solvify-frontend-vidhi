from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View




def index(request):
    return render(request, 'home/index.html', context={'segment': 'index'})

def my_profile(request):
    return render(request, 'home/my_profile.html')



def login_user(request):
    return render(request, 'home/auth-signin.html')

def register_user(request):
    return render(request, 'home/auth-signup.html')

def my_profile(request):
    return render(request, 'profile/personal-info.html')
def my_contact(request):
    return render(request, 'profile/contact-info.html')
def verifications(request):
    return render(request, 'profile/verifications.html')

def your_projects(request):
    return render(request, 'developers/your-projects.html')
def project_details(request):
    return render(request, 'developers/project-details.html')

def project_hosting(request):
    return render(request, 'developers/projects-under-hosting.html')
def project_review(request):
    return render(request, 'developers/projects-under-review.html')
def hosting_timeline(request):
    return render(request, 'developers/hosting-timeline.html')


def recommended(request):
    return render(request, 'hoster/recommended.html')
def find_project(request):
    return render(request, 'hoster/find-projects.html')


def pages(request):
    context = {}
    try:
        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
