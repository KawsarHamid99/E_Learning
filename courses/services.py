# courses/services.py
from .models import Course, Enrollment

class CourseService:
    @staticmethod
    def get_courses():
        return Course.objects.all()

    @staticmethod
    def create_course(title, description, instructor, duration, price):
        return Course.objects.create(title=title, description=description, instructor=instructor, duration=duration, price=price)

    @staticmethod
    def get_course_by_id(course_id):
        try:
            return Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return None

    @staticmethod
    def filter_courses(instructor=None, price=None, duration=None):
        filters = {}
        if instructor:
            filters['instructor__icontains'] = instructor
        if price:
            filters['price__lte'] = price
        if duration:
            filters['duration__lte'] = duration
        return Course.objects.filter(**filters)

class EnrollmentService:
    @staticmethod
    def enroll_student(student_name, course_id):
        course = CourseService.get_course_by_id(course_id)
        if course:
            return Enrollment.objects.create(student_name=student_name, course=course)
        return None

    @staticmethod
    def validate_enrollment(student_name, course_id):
        course = CourseService.get_course_by_id(course_id)
        if not course:
            return False, "Course not found"
        # Additional validation logic can be added here (e.g., student information)
        return True, "Enrollment is valid"
