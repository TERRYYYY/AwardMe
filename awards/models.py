from django.db import models
import datetime as dt

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
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

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'profiles/', default=" ")
    bio = models.TextField()
    contact = models.CharField(max_length=255, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.contact

    class Meta:
        ordering = ['contact']

    def save_profile(self):
        self.save()

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
    
    def update_review(self, design, content, usability,average):
        self.design = design
        self.usability = usability
        self.content = content
        self.average = average