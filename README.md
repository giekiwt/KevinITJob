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

## 📦 No-Installation Versions

### 🎯 Option 1: Portable Version (Recommended)

**Perfect for users who don't want to install anything:**

1. **Download**: `IT_Job_Search_Portable.zip`
2. **Extract** the ZIP file
3. **Run**: Double-click `start_app.bat`
4. **Access**: Open http://127.0.0.1:8000 in browser

**Features:**
- ✅ No Python installation required
- ✅ No package installation required
- ✅ Includes embedded Python
- ✅ Auto-setup database and sample data
- ✅ Works on any Windows machine

### 🎯 Option 2: Docker Version

**For users with Docker installed:**

```bash
# Build and run with Docker Compose
docker-compose up

# Or build manually
docker build -t it-job-search .
docker run -p 8000:8000 it-job-search
```

**Features:**
- ✅ Isolated environment
- ✅ Includes PostgreSQL database
- ✅ Easy deployment
- ✅ Consistent across platforms

### 🎯 Option 3: Executable Version

**Single file executable:**

1. **Download**: `it_job_search.exe`
2. **Run**: Double-click the executable
3. **Access**: Open http://127.0.0.1:8000 in browser

**Features:**
- ✅ Single file
- ✅ No dependencies
- ✅ Auto-setup everything
- ✅ Portable

### 🎯 Option 4: Streamlit Launcher

**Modern web interface launcher:**

```bash
# Install Streamlit
pip install streamlit

# Run launcher
streamlit run streamlit_app.py
```

**Features:**
- ✅ Beautiful web interface
- ✅ Auto-installation of requirements
- ✅ One-click launch
- ✅ Status monitoring

## 🔧 Building Distribution Versions

### Build All Versions

```bash
# Run the build script
build_all.bat
```

This will create:
- `IT_Job_Search_Portable.zip` - Portable version
- `dist/it_job_search.exe` - Executable version
- `IT_Job_Search_Complete_Distribution.zip` - All versions

### Build Individual Versions

```bash
# Portable version
python create_portable.py

# Executable version
python build_executable.py

# Docker version
docker build -t it-job-search .
```

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
- **Advanced Filters**: Location, language, company, experience level
- **Search Bar**: Real-time keyword search
- **Job Cards**: Beautiful, responsive job listings
- **Pagination**: Smooth navigation through results
- **Save Jobs**: Bookmark interesting positions

### 3. Job Details
- **Comprehensive Info**: Full job description, requirements, benefits
- **Company Profile**: Detailed company information
- **Apply Button**: Direct application process
- **Related Jobs**: Smart recommendations
- **Reviews**: Employee testimonials

### 4. User Dashboard
- **Profile Management**: Edit personal information and avatar
- **Application History**: Track applied jobs
- **Saved Jobs**: Manage bookmarked positions
- **Settings**: Account preferences and notifications

### 5. Company Profiles
- **Company Overview**: Mission, vision, culture
- **Job Listings**: All positions from the company
- **Contact Information**: Address, phone, website
- **Employee Reviews**: Authentic feedback

### 6. Blog System
- **IT Articles**: Programming tips, career advice
- **Categories**: Organized by topics
- **Search**: Find specific articles
- **Comments**: User engagement

## 🔍 Search & Filter Features

### Advanced Job Search
```python
# Example search filters
- Location: Ho Chi Minh City, Hanoi, Da Nang
- Programming Language: Python, JavaScript, Java, etc.
- Experience Level: Junior, Middle, Senior
- Job Type: Full-time, Part-time, Remote
- Salary Range: $800 - $3000
- Company Size: Startup, SME, Enterprise
```

### Real-time Search
- **Instant Results**: Search as you type
- **Auto-complete**: Smart suggestions
- **Trending Tags**: Popular search terms
- **Search History**: Recent searches

## 📱 Responsive Design

### Mobile-First Approach
- **Touch-friendly**: Optimized for mobile devices
- **Fast Loading**: Optimized images and assets
- **Offline Support**: Basic functionality without internet
- **PWA Ready**: Progressive Web App features

### Cross-Browser Compatibility
- **Chrome**: Full support
- **Firefox**: Full support
- **Safari**: Full support
- **Edge**: Full support

## 🔐 Security Features

### Authentication & Authorization
- **JWT Tokens**: Secure API authentication
- **OAuth Integration**: Google login
- **Password Reset**: Email-based recovery
- **Session Management**: Secure user sessions

### Data Protection
- **CSRF Protection**: Cross-site request forgery prevention
- **XSS Prevention**: Cross-site scripting protection
- **SQL Injection**: Parameterized queries
- **File Upload Security**: Validated file uploads

## 🚀 Performance Optimization

### Frontend Optimization
- **Minified CSS/JS**: Reduced file sizes
- **Image Optimization**: Compressed images
- **Lazy Loading**: Load content on demand
- **Caching**: Browser and server caching

### Backend Optimization
- **Database Indexing**: Optimized queries
- **Caching**: Redis/Memcached support
- **CDN Ready**: Content delivery network support
- **API Pagination**: Efficient data loading

## 🧪 Testing

### Test Coverage
```bash
# Run tests
python manage.py test

# Coverage report
coverage run --source='.' manage.py test
coverage report
```

### Test Types
- **Unit Tests**: Individual component testing
- **Integration Tests**: API endpoint testing
- **Frontend Tests**: JavaScript functionality
- **End-to-End Tests**: Complete user workflows

## 📈 Deployment

### Production Setup
```bash
# Collect static files
python manage.py collectstatic

# Set production settings
export DJANGO_SETTINGS_MODULE=it_job_search.settings.production

# Run with Gunicorn
gunicorn it_job_search.wsgi:application
```

### Deployment Options
- **Heroku**: Easy cloud deployment
- **AWS**: Scalable cloud infrastructure
- **DigitalOcean**: VPS deployment
- **Docker**: Containerized deployment

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

### Code Standards
- **PEP 8**: Python code style
- **ESLint**: JavaScript code style
- **Type Hints**: Python type annotations
- **Documentation**: Comprehensive docstrings

## 📞 Support

### Getting Help
- **Documentation**: Check this README first
- **Issues**: Report bugs on GitHub
- **Discussions**: Ask questions in GitHub Discussions
- **Email**: Contact the development team

### Common Issues
- **Port 8000 in use**: Change port or stop other services
- **Database errors**: Run migrations
- **Static files not loading**: Run collectstatic
- **Permission errors**: Check file permissions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Django Community**: For the excellent web framework
- **Bootstrap**: For the responsive design inspiration
- **Font Awesome**: For the beautiful icons
- **Contributors**: Everyone who helped improve this project

---

**Made with ❤️ for the IT community** 