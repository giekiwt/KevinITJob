#!/bin/bash

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install backend dependencies
cd backend
pip install -r requirements.txt

# Run Django setup script
python setup.py

# Create frontend React app
cd ../frontend
npm install

echo "Setup complete! Don't forget to:"
echo "1. Activate the virtual environment: source venv/bin/activate (or venv\Scripts\activate on Windows)"
echo "2. Configure your database settings in backend/it_job_search/settings.py"
echo "3. Run migrations: python manage.py migrate"
echo "4. Start the backend server: python manage.py runserver"
echo "5. Start the frontend development server: npm start" 