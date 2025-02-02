# FAQ Management System

## Overview
The **FAQ Management System** is a Django-based web application that allows users to manage frequently asked questions with multi-language support. The system provides a **REST API**, WYSIWYG editor integration, caching using Redis, and follows PEP8 coding standards.

## Features
- **Django Models**: Supports multilingual FAQs with dynamic translations.
- **WYSIWYG Editor**: Uses `django-ckeditor` for rich text formatting.
- **REST API**: Provides endpoints to retrieve FAQs with language selection.
- **Caching Mechanism**: Implements Redis for optimized performance.
- **Admin Panel**: Allows easy management of FAQs through Django Admin.
- **Unit Tests**: Uses `pytest` for testing model methods and API responses.
- **Docker Support**: Fully containerized setup using `Docker` and `docker-compose`.

---
## Installation
### Method 1: Running Locally Without Docker
> **Note:** If running locally, you can remove `Dockerfile` and `docker-compose.yml`.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Darshanzapda/FAQ_management_system.git
   cd FAQ_management_system
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Mac/Linux
   .\venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start Redis server** (for caching support):
   ```bash
   redis-server
   ```
   Verify Redis is running:
   ```bash
   redis-cli ping  # Should return PONG
   ```

6. **Create a superuser** (for Django Admin Panel):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Django development server**:
   ```bash
   python manage.py runserver
   ```
   Access the app:
   - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - API Endpoint: [http://127.0.0.1:8000/api/faqs/](http://127.0.0.1:8000/api/faqs/)

---

### Method 2: Running Using Docker
> **Note:** Ensure you have **Docker** and **Docker Compose** installed.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Darshanzapda/FAQ_management_system.git
   cd FAQ_management_system
   ```

2. **Build and run the containers**:
   ```bash
   docker-compose up --build
   ```

3. **Create a superuser inside the running container**:
   ```bash
   docker exec -it faq_management_system-web-1 python manage.py createsuperuser
   ```

4. **Access the application**:
   - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - API Endpoint: [http://127.0.0.1:8000/api/faqs/](http://127.0.0.1:8000/api/faqs/)

---
## API Usage
### Fetch FAQs in Different Languages
- **Default (English):**
  ```bash
  curl http://127.0.0.1:8000/api/faqs/
  ```
- **Hindi:**
  ```bash
  curl http://127.0.0.1:8000/api/faqs/?lang=hi
  ```
- **Bengali:**
  ```bash
  curl http://127.0.0.1:8000/api/faqs/?lang=bn
  ```

---
## Code Quality & Linting
- Follow **PEP8** guidelines.
- Use `flake8` for linting:
  ```bash
  docker exec -it faq_management_system-web-1 bash
  flake8 .
  ```

---
## Running Unit Tests
- Uses `pytest` for testing model methods and API responses.
- Run tests inside the Docker container:
  ```bash
  docker exec -it faq_management_system-web-1 pytest
  ```

---
## Database Reset (Optional)
To delete all users and reset the database:
```bash
python manage.py flush
```

---
## Contribution Guidelines
### Commit Messages Format
Follow conventional commits:
- **feat:** Add new feature
- **fix:** Fix a bug
- **docs:** Update documentation
- **test:** Add or update tests

Example:
```bash
feat: Add multilingual FAQ model
fix: Improve translation caching
```

### How to Contribute
1. **Fork the repository**.
2. **Clone your fork**:
   ```bash
   git clone https://github.com/your-username/FAQ_management_system.git
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature-new-functionality
   ```
4. **Make changes and commit**:
   ```bash
   git commit -m "feat: Add new translation feature"
   ```
5. **Push to GitHub and create a pull request**.
   ```bash
   git push origin feature-new-functionality
   ```
6. **Create a pull request:**.
   - Go to your forked repository on GitHub.
   - Click on "Compare & pull request".
   - Add a descriptive title and comments.
   - Click "Create pull request".
   
---

 Happy Coding! 🚀
