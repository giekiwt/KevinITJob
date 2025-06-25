@echo off

REM Remove existing virtual environment if it exists
if exist venv rmdir /s /q venv

REM Remove existing backend files
if exist backend rmdir /s /q backend
mkdir backend

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate

REM Install backend dependencies
cd backend
pip install -r ..\backend\requirements.txt

REM Create Django project
django-admin startproject it_job_search .

REM Create apps with unique names
python manage.py startapp user_management
python manage.py startapp job_listings
python manage.py startapp company_profiles
python manage.py startapp blog_posts

REM Create frontend React app
cd ..\frontend
if exist node_modules rmdir /s /q node_modules
if exist package-lock.json del package-lock.json
npm install

echo Setup complete! Don't forget to:
echo 1. Activate the virtual environment: venv\Scripts\activate
echo 2. Configure your database settings in backend\it_job_search\settings.py
echo 3. Run migrations: python manage.py migrate
echo 4. Start the backend server: python manage.py runserver
echo 5. Start the frontend development server: npm start

pause 