from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    # url(r'^home/$', views.home, name='home'),
    
    url(r'^$', views.home_projects, name='homePage'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)    