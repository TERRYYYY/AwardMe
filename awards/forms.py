from django import forms
from .models import Project,Profile,Reviews


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class ProfileForm(forms.ModelForm):
    '''
    class to define profile form
    '''
    class Meta:
        model = Profile
        exlcude = ['user']
        fields = ('bio', 'profile_pic','contact')

class ProjectForm(forms.ModelForm):
    '''
    class to define image uploading form
    '''
    class Meta:
        model = Project
        exclude = [ '']
        fields = ('title','description', 'project_pic','link')
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        fields = ('bio', 'profile_pic','contact')
        