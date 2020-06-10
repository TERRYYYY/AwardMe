from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Profile,Project,Reviews
from .forms import NewsLetterForm,ProfileForm,ProjectForm,ProfileUpdateForm
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



@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    user_profile = Profile.objects.filter(user=current_user).first()

    if user_profile is None:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            print("I got the form")
            if form.is_valid():
                print("Form was valid")
                u_profile = form.save(commit=False)
                u_profile.user = current_user
                u_profile.save()

                return redirect("awards")

        form = ProfileForm()
        return render(request, 'registration/profile.html', {'form': form})
    else:
        return redirect('awards')

@login_required(login_url='/accounts/login/')
def account(request):
    current_user = request.user
    user_profile = Profile.objects.filter(user=current_user).first()

    if user_profile is None:
        print("No profile found for user")
        return redirect('profile')
    else:
        user_projects = current_user.project_set.all()
        return render(request, 'registration/account.html', {
            'user': current_user,
            'projects': user_projects
            })
