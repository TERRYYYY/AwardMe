from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Profile,Project,Reviews
from .forms import NewsLetterForm,ProfileForm,ProjectForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')
def awards(request):
    date = dt.date.today()
    projects = Project.get_projects()
    
    return render(request, 'all-awards/awards.html', {"date": date, "projects":projects})

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'awards' in request.GET and request.GET["awards"]:
        search_term = request.GET.get("awards")
        searched_awards = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-awards/search.html',{"message":message,"projects": searched_awards})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-awards/search.html',{"message":message})

@login_required(login_url='/accounts/login/')  
def new_post(request):
    current_user = request.user
    if request.method=='POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user.profile
            project.save()
            return redirect('awards')
    else:
        form = ProjectForm()
    return render(request, 'all-awards/newpost.html',{"form":form})


