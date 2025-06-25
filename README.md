# IT Job Search Web Application

A web application for IT professionals to search for jobs, manage their profiles, and connect with IT companies.

## Features

- User registration and authentication
- Job search and filtering
- Company profiles and listings
- IT Blog system
- User profile management
- Resume upload and management

## Tech Stack

### Frontend
- React.js
- Redux
- Material-UI

### Backend
- Django
- Django Rest Framework
- PostgreSQL

### Authentication
- JWT (JSON Web Token)

## Project Structure

```
it-job-search/
├── frontend/           # React frontend application
├── backend/           # Django backend application
└── docs/             # Project documentation
```

## Setup Instructions

### Backend Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   python manage.py migrate
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Run the development server:
   ```bash
   npm start
   ```

## Contributing

Please read our contributing guidelines before submitting pull requests.

## License

This project is licensed under the MIT License. 