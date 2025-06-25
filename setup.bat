@echo off

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate

REM Install backend dependencies
cd backend
pip install -r requirements.txt

REM Run Django setup script
python setup.py

REM Create frontend React app
cd ..\frontend
npm install

echo Setup complete! Don't forget to:
echo 1. Activate the virtual environment: venv\Scripts\activate
echo 2. Configure your database settings in backend\it_job_search\settings.py
echo 3. Run migrations: python manage.py migrate
echo 4. Start the backend server: python manage.py runserver
echo 5. Start the frontend development server: npm start

pause 