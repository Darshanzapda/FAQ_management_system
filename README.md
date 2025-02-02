# FAQ Management System

## Introduction
The **FAQ Management System** is a Django-based backend service that allows users to store and retrieve Frequently Asked Questions (FAQs) with multi-language support. It supports dynamic translation using Google Translate API and provides an efficient caching mechanism using Redis. The system also includes an admin panel for managing FAQs and follows best coding practices with PEP8 compliance and unit testing.

## Features
- **Django Models**: Store FAQs with WYSIWYG editor support
- **Multi-Language Support**: Automated translations using Google Translate API
- **REST API**: Fetch FAQs in different languages via query parameters
- **Caching**: Uses Redis to improve performance
- **Admin Panel**: Manage FAQs with an intuitive UI
- **Code Quality**: Follows PEP8 standards and linting with `flake8`
- **Unit Testing**: Implements `pytest` to validate API responses and models
- **Docker Support**: Run the application in an isolated container environment

---
## Installation Guide

### **Prerequisites**
Ensure you have the following installed on your system:
- Python 3.8+
- Django 4+
- Redis Server
- Docker & Docker Compose (for containerized deployment)

### **Step 1: Clone the Repository**
```sh
git clone https://github.com/DarshanZapda/FAQ_management_system.git
```
```
cd FAQ_management_system
```

### **Step 2: Set Up a Virtual Environment**
```sh
python -m venv venv
```
Activate the virtual environment:
- **Windows**:
  ```sh
  .\venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```sh
  source venv/bin/activate
  ```

### **Step 3: Install Dependencies**
```sh
pip install -r requirements.txt
```

### **Step 4: Configure Environment Variables**
Set the `DJANGO_SETTINGS_MODULE`:
```sh
set DJANGO_SETTINGS_MODULE=FAQ_management_system.settings
```

### **Step 5: Apply Migrations**
```sh
python manage.py makemigrations
python manage.py migrate
```

### **Step 6: Start Redis Server**
```sh
redis-server
```
Verify Redis is working:
```sh
redis-cli ping  # Should return 'PONG'
```

### **Step 7: Run the Development Server**
```sh
python manage.py runserver
```
Admin panel available at: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---
## API Usage

### **Retrieve FAQs (Default - English)**
```sh
GET http://127.0.0.1:8000/api/faqs/
```

### **Retrieve FAQs in Hindi**
```sh
GET http://127.0.0.1:8000/api/faqs/?lang=hi
```

### **Retrieve FAQs in Bengali**
```sh
GET http://127.0.0.1:8000/api/faqs/?lang=bn
```

---
## Running the Application with Docker

### **Step 1: Build and Start Containers**
```sh
docker-compose up --build -d
```

### **Step 2: Run Migrations in Docker**
```sh
docker exec -it faq_management_system-web-1 python manage.py migrate
```

### **Step 3: Create a Superuser in Docker**
```sh
docker exec -it faq_management_system-web-1 python manage.py createsuperuser
```

### **Step 4: Run Server in Docker**
```sh
docker exec -it faq_management_system-web-1 python manage.py runserver 0.0.0.0:8000
```

---
## Code Quality & Testing

### **Linting with flake8**
```sh
docker exec -it faq_management_system-web-1 flake8 .
```

### **Running Unit Tests with pytest**
```sh
docker exec -it faq_management_system-web-1 pytest
```

---
## Contribution Guidelines
1. **Fork the Repository**
2. **Create a New Branch**
   ```sh
   git checkout -b feature-branch-name
   ```
3. **Make Your Changes and Commit**
   ```sh
   git add .
   git commit -m "feat: Add new translation support"
   ```
4. **Push to GitHub and Create a Pull Request**
   ```sh
   git push origin feature-branch-name
   ```

---
## Git Commit Message Format
Follow conventional commit messages:
- `feat: Add multilingual FAQ model`
- `fix: Improve translation caching`
- `docs: Update README with API examples`

---

🚀 **Happy Coding!**

