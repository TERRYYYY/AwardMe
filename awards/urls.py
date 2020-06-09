from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.awards,name='awards'),
    url(r'^search/', views.search_results, name='search_results'),
    # url(r'^review/',views.review,name ='review'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)