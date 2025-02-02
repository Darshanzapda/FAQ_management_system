# Start with a base Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flake8
RUN pip install pytest

# Copy the entire application to the container
COPY . /app/

# Expose the port Django will run on
EXPOSE 8000

# Run the application with Gunicorn
CMD ["gunicorn", "faq_project.wsgi:application", "--bind", "0.0.0.0:8000"]
