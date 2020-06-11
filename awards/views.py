from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Profile,Project,Reviews
from .forms import NewsLetterForm,ProfileForm,ProjectForm,ProfileUpdateForm,RateProjectForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer,ProfileSerializer
from rest_framework import status

# Create your views here.
def index(request):
    date = dt.date.today()
    projects = Project.get_projects()
    reviews = Reviews.get_reviews()
    return render(request, 'all-awards/index.html', {"date": date, "projects":projects, "reviews":reviews})

def my_review(request):
    date = dt.date.today()
    projects = Project.get_projects()
    reviews = Reviews.get_reviews()
    return render(request, 'all-awards/reviews.html', {"date": date, "projects":projects, "reviews":reviews})

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
    if request.method=='POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
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
@login_required(login_url='/accounts/login/') 
def review(request, id):

    try:
        project = Project.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    comments = Reviews.get_comment(Reviews, id)
    latest_review_list=Reviews.objects.all()

    if request.method == 'POST':
        form = RateProjectForm(request.POST)
        if form.is_valid():
            design_rating = form.cleaned_data['design_rating']
            content_rating = form.cleaned_data['content_rating']
            usability_rating = form.cleaned_data['usability_rating']
            comment = form.cleaned_data['comment']
            review = Reviews()
            review.project = project
            
            review.comment = comment
            review.design_rating = design_rating
            review.content_rating = content_rating
            review.usability_rating = usability_rating
            review.save()

    else:
        form = RateProjectForm()

        # return HttpResponseRedirect(reverse('image', args=(image.id,)))

    return render(request, 'all-awards/reviews.html', {"project": project,
                                          'form':form,
                                          'comments':comments,
                                          'latest_review_list':latest_review_list})
    
        

class ProjectList(APIView):

    # handling a retrieval request
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

    # handling a post request
    def post(self,request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

class ProfileList(APIView):

    # handling a retrieval request
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)