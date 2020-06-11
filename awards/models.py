from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 255)
    description = HTMLField()
    link = models.URLField(max_length=255)
    project_pic = models.ImageField(upload_to = 'projects/', default="title")
    pub_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()
    
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects
    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects
    # @classmethod
    # def get_single_project(cls, project_id):
    #     single_project = Project.objects.get(id=project_id)
    #     return single_project
    # @classmethod
    # def get_by_user(cls, user):
    #     projects = cls.objects.filter(user=user)
    #     return projects


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'profiles/', default=" ")
    bio = models.TextField()
    contact = models.CharField(max_length=255, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None) 

    def __str__(self):
        return self.contact

    class Meta:
        ordering = ['contact']

    def save_profile(self):
        self.save()
    
    @classmethod
    def get_by_user(cls, user):
        projects = cls.objects.filter(user=user)
        return projects

class Reviews(models.Model):
    design = models.FloatField()
    usability = models.FloatField()
    content = models.FloatField()
    average = models.FloatField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.average
    
    class Meta:
        ordering = ['average']

    def save_review(self):
        self.save()

    @classmethod
    def get_reviews(cls):
        reviews = cls.objects.all()
        return reviews
    
    def get_comment(self, id):
        comments = Review.objects.filter(image_id =id)
        return comments
    
    def update_review(self, design, content, usability,average):
        self.design = design
        self.usability = usability
        self.content = content
        self.average = average

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()