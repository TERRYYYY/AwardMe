from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Profile,Project,Reviews

# Create your views here.
def index(request):
    return render(request, 'index.html')
def awards(request):
    date = dt.date.today()
    projects = Project.get_projects()
    
    return render(request, 'all-awards/awards.html', {"date": date, "projects":projects})