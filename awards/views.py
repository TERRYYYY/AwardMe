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

def search_results(request):

    if 'awards' in request.GET and request.GET["awards"]:
        search_term = request.GET.get("awards")
        searched_awards = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-awards/search.html',{"message":message,"projects": searched_awards})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-awards/search.html',{"message":message})