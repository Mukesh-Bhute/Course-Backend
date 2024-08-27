from django.urls import path
from .views import (
    CourseCreateView, CourseInstanceListAllView, CourseListView, CourseDetailView, CourseDeleteView,
    CourseInstanceCreateView, CourseInstanceListView, CourseInstanceDetailView, CourseInstanceDeleteView
)

urlpatterns = [
    path('courses', CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:pk>/delete', CourseDeleteView.as_view(), name='course-delete'),
    path('courses-list', CourseListView.as_view(), name='course-list'),
    path('instances', CourseInstanceCreateView.as_view(), name='instance-create'),
    path('instances/<int:year>/<int:semester>', CourseInstanceListView.as_view(), name='instance-list'),
    path('instances/<int:year>/<int:semester>/<int:course_id>', CourseInstanceDetailView.as_view(), name='instance-detail'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/delete', CourseInstanceDeleteView.as_view(), name='instance-delete'),
    path('instances/all', CourseInstanceListAllView.as_view(), name='instance-list-all'), 
]
