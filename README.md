# Kevin IT - Job Search Web Application

A modern web application for IT professionals to search for jobs, manage their profiles, and connect with IT companies. Built with Django and featuring a beautiful, responsive UI.

## 🌟 Features

- **User Management**: Registration, authentication, profile management with avatar upload
- **Job Search**: Advanced filtering by location, programming language, company, and keywords
- **Company Profiles**: Detailed company information and job listings
- **Blog System**: IT-related articles and insights
- **Responsive Design**: Modern, mobile-friendly interface
- **Search & Filter**: Real-time job search with trending tags
- **Social Authentication**: Google OAuth integration
- **User Reviews**: Employee reviews on job detail pages
- **Related Jobs**: Smart job recommendations

## 🛠 Tech Stack

### Backend
- **Django 5.0.2** - Web framework
- **Django REST Framework** - API development
- **SQLite** - Database (can be configured for PostgreSQL)
- **Django CORS Headers** - Cross-origin resource sharing
- **Django Filters** - Advanced filtering
- **Social Auth** - OAuth authentication
- **Pillow** - Image processing

### Frontend
- **HTML5/CSS3** - Modern, responsive design
- **JavaScript** - Interactive features
- **Font Awesome** - Icons
- **Bootstrap-inspired** - Custom CSS framework

## 📁 Project Structure

```
CDDT_2_DoAnWebTimViec/
├── backend/                    # Django backend
│   ├── it_job_search/         # Main Django project
│   ├── user_management/       # User authentication & profiles
│   ├── job_listings/         # Job management
│   ├── company_profiles/     # Company management
│   ├── blog_posts/          # Blog system
│   ├── media/               # Uploaded files
│   └── manage.py           # Django management
├── frontend/                # Frontend assets
├── venv/                   # Python virtual environment
└── README.md              # This file
```

## 🚀 Quick Setup Guide

### Prerequisites

- **Python 3.8+**
- **pip** (Python package installer)
- **Git**

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd CDDT_2_DoAnWebTimViec
```

### Step 2: Set Up Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
cd backend
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install django-filter
pip install social-auth-app-django
pip install pillow
pip install python-dotenv
```

### Step 4: Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Step 6: Seed Sample Data

The application includes management commands to populate the database with sample data:

```bash
# Seed jobs, companies, locations, and programming languages
python manage.py seed_jobs

# Seed blog posts
python manage.py seed_blogposts
```

**What gets seeded:**
- **270 jobs** across 3 locations (Ho Chi Minh City, Hanoi, Da Nang)
- **20 companies** with descriptions and websites
- **10 programming languages** (Python, JavaScript, Java, etc.)
- **10 blog posts** with sample content
- **3 locations** (Ho Chi Minh City, Hanoi, Da Nang)

### Step 7: Run the Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

## 📊 Sample Data Details

### Jobs
- **270 total jobs** distributed across locations
- **Job types**: Backend, Frontend, Fullstack, Mobile, DevOps, QA, Data, AI, Project Manager, Business Analyst
- **Salary ranges**: $800 - $3000 USD
- **Experience levels**: Junior, Middle, Senior
- **Skills**: Randomly assigned from 10 programming languages

### Companies
- **20 companies** including: FPT Software, VNG Corporation, Viettel Group, MB Bank, Techcombank, Momo, Tiki, Shopee, Grab, VNPT, CMC Corporation, Haravan, Axon, KMS Technology, NashTech, TMA Solutions, Sendo, Be Group, Vietcombank, ELCA

### Programming Languages
- Python, JavaScript, Java, C#, PHP, TypeScript, Ruby, Go, Swift, Kotlin

### Blog Posts
- **10 sample blog posts** with IT-related content
- Topics: Programming, Career advice, Industry trends

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the `backend/` directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Email settings (for password reset)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Google OAuth (optional)
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your-google-oauth-key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your-google-oauth-secret
```

### Database Configuration

The default configuration uses SQLite. For production, you can switch to PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🎯 Key Features Walkthrough

### 1. Home Page
- **Hero Section**: Welcome message with search functionality
- **Top Companies**: Carousel of featured companies
- **Dynamic Stats**: Animated statistics
- **Blog Preview**: Latest blog posts
- **User Feedback**: Testimonials section

### 2. Job Search
- **Keyword Search**: Search jobs by title, company, or description
- **Filter by Location**: Ho Chi Minh City, Hanoi, Da Nang
- **Filter by Language**: Python, JavaScript, Java, etc.
- **Trending Tags**: Clickable tags for quick filtering

### 3. Job Details
- **Complete Job Information**: Title, company, location, salary, requirements
- **Employee Reviews**: Random sample reviews
- **Related Jobs**: Similar job recommendations
- **Apply Button**: Direct application link

### 4. User Profile
- **Avatar Upload**: Profile picture management
- **Profile Information**: Personal details and preferences
- **Applied Jobs**: Track job applications

### 5. Company Profiles
- **Company Spotlight**: Featured company information
- **Job Listings**: All jobs from the company
- **Company Details**: Description, website, location

## 🔍 API Endpoints

The application includes REST API endpoints:

- `/api/jobs/` - Job listings
- `/api/companies/` - Company information
- `/api/users/` - User management
- `/api/blog/` - Blog posts

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

## 🚀 Deployment

### Production Checklist

1. **Set DEBUG=False** in settings
2. **Configure proper SECRET_KEY**
3. **Set up production database** (PostgreSQL recommended)
4. **Configure static files** serving
5. **Set up email backend**
6. **Configure CORS settings**
7. **Set up SSL/HTTPS**

### Using Gunicorn

```bash
pip install gunicorn
gunicorn it_job_search.wsgi:application
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🆘 Troubleshooting

### Common Issues

**1. Migration Errors**
```bash
python manage.py makemigrations --merge
python manage.py migrate
```

**2. Static Files Not Loading**
```bash
python manage.py collectstatic
```

**3. Media Files Not Uploading**
- Ensure `MEDIA_ROOT` directory exists
- Check file permissions

**4. Database Issues**
```bash
python manage.py flush  # Clear all data
python manage.py seed_jobs  # Re-seed data
```

### Getting Help

If you encounter any issues:
1. Check the Django debug page for error details
2. Review the console output for error messages
3. Ensure all dependencies are installed
4. Verify database migrations are applied

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

---

**Happy coding! 🚀** 