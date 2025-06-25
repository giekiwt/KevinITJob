# Create directories
New-Item -ItemType Directory -Path backend, frontend, docs

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install Python dependencies
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

# Create Django project
Set-Location backend
django-admin startproject it_job_search .

# Create Django apps
python manage.py startapp user_management
python manage.py startapp job_listings
python manage.py startapp company_profiles
python manage.py startapp blog_posts

# Create frontend React app
Set-Location ..\frontend
npm install

Write-Host "Setup complete! Don't forget to:"
Write-Host "1. Activate the virtual environment: .\venv\Scripts\Activate.ps1"
Write-Host "2. Configure your database settings in backend\it_job_search\settings.py"
Write-Host "3. Run migrations: python manage.py migrate"
Write-Host "4. Start the backend server: python manage.py runserver"
Write-Host "5. Start the frontend development server: npm start"

Read-Host "Press Enter to continue" 