# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /code/

EXPOSE 8000

CMD [ "python" , "manage.py" ,"runserver", "0.0.0.0:8000" ]