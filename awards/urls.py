from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name='awards'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^reviews/', views.my_review, name='my_review'),
    url(r'^new/project$', views.new_post, name='new_post'),
    # url(r'^new/rating$', views.new_review, name='new_review'),
    url(r'^ratings/(\d+)', views.review, name='reviews'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),

    url(r'^accounts/profile/$', views.user_profile, name='profile'),
    url(r'^myaccount/', views.account, name='account'),
    url(r'^api/project/$', views.ProjectList.as_view()),
    url(r'^api/project/$', views.ProfileList.as_view()),
    # url(r'^review/',views.review,name ='review'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)