from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CourseSerializer, EnrollmentSerializer
from .services import CourseService, EnrollmentService

@api_view(['GET', 'POST'])
def courses(request):
    if request.method == 'GET':
        instructor = request.query_params.get('instructor')
        price = request.query_params.get('price')
        duration = request.query_params.get('duration')
        
        courses = CourseService.filter_courses(instructor=instructor, price=price, duration=duration)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def course_detail(request, pk):
    course = CourseService.get_course_by_id(pk)
    if course:
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def enrollments(request):
    serializer = EnrollmentSerializer(data=request.data)
    if serializer.is_valid():
        student_name = serializer.validated_data.get('student_name')
        course_id = serializer.validated_data.get('course')
        course_id=course_id.id
        print(course_id)
        valid, message = EnrollmentService.validate_enrollment(student_name, course_id)
        if valid:
            enrollment = EnrollmentService.enroll_student(student_name, course_id)
            enrollment_serializer = EnrollmentSerializer(enrollment)
            return Response(enrollment_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": message}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
