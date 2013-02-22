# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.http import HttpResponse


def home(request):
#    if request.user.is_authenticated():
#        return HttpResponseRedirect('/mycourses/')
    return HttpResponse("<h1>Home under construction</h1>")

#@login_required
#def my_courses(request):
#    courses = request.user.get_profile().courses.all
#    return render(request, "account/mycourses.html", {'courses': courses})
