from django.test import TestCase
from .models import Profile,Project,Reviews

# Create your tests here.
# class ProfileTestCase(TestCase):
#     def setUp(self):
#         self.user = User(username='charles',email='example@gmail.com',password='sahara10322')
#         self.user.save()

#         self.profile_test = Profile(bio='this is a test profile', profile_pic='default.jpg', location='Nrb',user=self.user)

#     def test_instance(self):
#         self.assertTrue(isinstance(self.profile_test, Profile))

#     def test_save_profile(self):
#         after = Profile.objects.all()
#         self.assertTrue(len(after) > 0)



class ProjectTestCase(TestCase):
    def setUp(self):
        # self.trialls = TestProfile()
        self.project_test = Project(title='Trial',description='default test',link='https://test.com', project_pic='default.png',pub_date= '2020-06-01' )

    def test_instance(self):
        self.assertTrue(isinstance(self.project_test, Project))

    def test_save_project(self):
        self.project_test.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    # def test_delete_project(self):
    #     self.project_test.delete_project(self.project_test.id)
    #     after = Profile.objects.all()
    #     self.assertTrue(len(after) < 1)