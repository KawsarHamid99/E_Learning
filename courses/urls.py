# learning_platform/urls.py
from django.urls import path
from courses import views

urlpatterns = [
    path('courses/', views.courses),
    path('courses/<int:pk>/', views.course_detail),
    path('enrollments/', views.enrollments),
]
