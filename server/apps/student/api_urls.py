from django.conf.urls import url
from django.urls import path

from .api_views import *

app_name = 'student'

urlpatterns = [
    path('<slug:student_id>/courses/', StudentCoursesView.as_view(), name='courses'),
    path('<slug:student_id>/courses/<slug:pk>', StudentEditFollowCourse.as_view(), name='unfollow-course'),
]