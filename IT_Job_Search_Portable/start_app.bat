@echo off
echo Starting IT Job Search Application...
echo.

REM Set Python path to embedded Python
set PYTHONPATH=%~dp0python
set PATH=%~dp0python;%~dp0python\Scripts;%PATH%

REM Change to app directory
cd "%~dp0app\backend"

REM Install packages using embedded Python
echo Installing required packages...
python -m pip install --target=%~dp0python\Lib\site-packages -r ..\..\requirements.txt

REM Run migrations
echo Setting up database...
python manage.py migrate

REM Seed data if database is empty
echo Loading sample data...
python manage.py seed_jobs
python manage.py seed_blogposts

REM Start server
echo.
echo Application is starting at http://127.0.0.1:8000
echo Press Ctrl+C to stop the server
echo.
python manage.py runserver

pause
