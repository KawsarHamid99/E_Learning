# Online Learning Platform Backend

This backend system is for an online learning platform built using Django and Django REST Framework.

## Setup Instructions

1. Clone the repository:
git clone https://github.com/KawsarHamid99/E_Learning.git
cd E_Learning

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Set up the database:
python manage.py migrate

5. Create a superuser (optional, for accessing Django admin):
python manage.py createsuperuser

6. Start the development server:
python manage.py runserver




## API Endpoints

### Course API

- **GET /courses**: Retrieve a list of available courses.
- **GET /courses/:id**: Retrieve a specific course by its ID.
- **POST /courses**: Create a new course.

### Enrollment API

- **POST /enrollments**: Allow students to enroll in a course.

## API Examples

### GET /courses


url http://localhost:8000/courses/



Response:
```json
[
    {
        "id": 1,
        "title": "Introduction to Python Programming",
        "description": "Learn Python programming basics.",
        "instructor": "John Doe",
        "duration": 120,
        "price": 49.99
    },
    {
        "id": 2,
        "title": "Web Development with Django",
        "description": "Build web applications using Django.",
        "instructor": "Jane Smith",
        "duration": 180,
        "price": 79.99
    }
]


GET /courses/:id
curl http://localhost:8000/courses/1/

Response:
{
    "id": 1,
    "title": "Introduction to Python Programming",
    "description": "Learn Python programming basics.",
    "instructor": "John Doe",
    "duration": 120,
    "price": 49.99
}


POST /courses
curl -X POST -H "Content-Type: application/json" -d '{"title":"Machine Learning Fundamentals","description":"Introduction to machine learning concepts.","instructor":"Alice Johnson","duration":150,"price":99.99}' http://localhost:8000/courses/

```
### Dependencies
- **Django
- **Django REST Framework
- **PostgreSQL (as specified)