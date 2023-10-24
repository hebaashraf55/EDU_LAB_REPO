from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('meetings/', views.meeting, name='meetings'),
    path('meeting_detail/<slug:slug>/',views.meeting_detail, name='meeting-detail'),
    
    path('courses/', views.courses, name='courses'),
    path('course_detail/<slug:slug>/', views.course_detail, name='course-detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
