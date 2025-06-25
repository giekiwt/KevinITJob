@echo off

REM Step 1: Create and activate virtual environment
if exist venv rmdir /s /q venv
python -m venv venv
call venv\Scripts\activate

REM Step 2: Install Django and other requirements
pip install Django==5.0.2
pip install djangorestframework==3.14.0
pip install djangorestframework-simplejwt==5.3.1
pip install django-cors-headers==4.3.1
pip install psycopg2-binary==2.9.9
pip install Pillow==10.2.0
pip install python-dotenv==1.0.1
pip install django-filter==23.5
pip install django-storages==1.14.2
pip install gunicorn==21.2.0
pip install whitenoise==6.6.0

REM Step 3: Create Django project
cd backend
django-admin startproject it_job_search .

REM Step 4: Create Django apps
python manage.py startapp user_management
python manage.py startapp job_listings
python manage.py startapp company_profiles
python manage.py startapp blog_posts

REM Step 5: Create frontend React app
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