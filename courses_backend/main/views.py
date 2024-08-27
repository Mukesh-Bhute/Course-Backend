from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

# Create your views here.


# 1. Create a new course
class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# 2. List all courses
class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# 3. View detailed information about a course
class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# 4. Delete a course
class CourseDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# 5. Create a new course instance
class CourseInstanceCreateView(generics.CreateAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        course = Course.objects.get(id=data['course'])
        course_instance = CourseInstance.objects.create(
            course=course,
            year=data['year'],
            semester=data['semester']
        )
        serializer = CourseInstanceSerializer(course_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 6. List course instances by year and semester
class CourseInstanceListView(generics.ListAPIView):
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseInstance.objects.filter(year=year, semester=semester)

# 7. View detailed information about a course instance
class CourseInstanceDetailView(generics.RetrieveAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        course_id = self.kwargs['course_id']
        return CourseInstance.objects.get(year=year, semester=semester, course_id=course_id)

# 8. Delete a course instance
class CourseInstanceDeleteView(generics.DestroyAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        course_id = self.kwargs['course_id']
        return CourseInstance.objects.get(year=year, semester=semester, course_id=course_id)

# 9. List all course instances
class CourseInstanceListAllView(generics.ListAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer