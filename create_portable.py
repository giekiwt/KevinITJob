#!/usr/bin/env python3
"""
Script to create a portable version of the Django application
"""

import os
import sys
import shutil
import subprocess
import zipfile
from pathlib import Path
import urllib.request

def download_python_embedded():
    """Download Python embedded for Windows"""
    python_version = "3.11.8"
    url = f"https://www.python.org/ftp/python/{python_version}/python-{python_version}-embed-amd64.zip"
    
    print(f"Downloading Python {python_version} embedded...")
    
    if not os.path.exists("python_embedded.zip"):
        urllib.request.urlretrieve(url, "python_embedded.zip")
    
    # Extract Python embedded
    with zipfile.ZipFile("python_embedded.zip", 'r') as zip_ref:
        zip_ref.extractall("portable_python")
    
    print("Python embedded downloaded and extracted")

def create_portable_structure():
    """Create portable application structure"""
    portable_dir = "IT_Job_Search_Portable"
    
    # Create directory structure
    os.makedirs(portable_dir, exist_ok=True)
    os.makedirs(f"{portable_dir}/python", exist_ok=True)
    os.makedirs(f"{portable_dir}/app", exist_ok=True)
    os.makedirs(f"{portable_dir}/data", exist_ok=True)
    
    # Copy Python embedded
    if os.path.exists("portable_python"):
        shutil.copytree("portable_python", f"{portable_dir}/python", dirs_exist_ok=True)
    
    # Copy application files
    shutil.copytree("backend", f"{portable_dir}/app/backend", dirs_exist_ok=True)
    shutil.copytree("frontend", f"{portable_dir}/app/frontend", dirs_exist_ok=True)
    
    return portable_dir

def create_startup_script(portable_dir):
    """Create startup script for portable version"""
    startup_script = f'''@echo off
echo Starting IT Job Search Application...
echo.

REM Set Python path to embedded Python
set PYTHONPATH=%~dp0python
set PATH=%~dp0python;%~dp0python\\Scripts;%PATH%

REM Change to app directory
cd "%~dp0app\\backend"

REM Install packages using embedded Python
echo Installing required packages...
python -m pip install --target=%~dp0python\\Lib\\site-packages -r ..\\..\\requirements.txt

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
'''
    
    with open(f"{portable_dir}/start_app.bat", 'w') as f:
        f.write(startup_script)

def create_requirements_file(portable_dir):
    """Copy requirements file to portable directory"""
    shutil.copy("requirements.txt", f"{portable_dir}/requirements.txt")

def create_readme(portable_dir):
    """Create README for portable version"""
    readme_content = '''# IT Job Search - Portable Version

## Cách sử dụng:

1. **Chạy ứng dụng**: Double-click vào file `start_app.bat`
2. **Truy cập**: Mở trình duyệt và vào http://127.0.0.1:8000
3. **Dừng ứng dụng**: Nhấn Ctrl+C trong cửa sổ command

## Lưu ý:

- Lần đầu chạy sẽ mất thời gian để cài đặt các package
- Dữ liệu được lưu trong thư mục `data`
- Không cần cài đặt Python hay bất kỳ package nào khác

## Tính năng:

- Tìm kiếm việc làm IT
- Quản lý profile người dùng
- Blog về IT
- Responsive design
- Hơn 270 việc làm mẫu
- 20 công ty mẫu

## Hỗ trợ:

Nếu gặp vấn đề, hãy kiểm tra:
1. Windows Defender có chặn không
2. Port 8000 có bị sử dụng không
3. Quyền admin có cần thiết không
'''
    
    with open(f"{portable_dir}/README.txt", 'w', encoding='utf-8') as f:
        f.write(readme_content)

def create_zip_package(portable_dir):
    """Create ZIP package of portable version"""
    zip_name = "IT_Job_Search_Portable.zip"
    
    print(f"Creating ZIP package: {zip_name}")
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(portable_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, portable_dir)
                zipf.write(file_path, arcname)
    
    print(f"Portable package created: {zip_name}")

def main():
    """Main function"""
    print("Creating Portable IT Job Search Application")
    print("=" * 50)
    
    try:
        # Download Python embedded
        download_python_embedded()
        
        # Create portable structure
        portable_dir = create_portable_structure()
        
        # Create startup script
        create_startup_script(portable_dir)
        
        # Copy requirements
        create_requirements_file(portable_dir)
        
        # Create README
        create_readme(portable_dir)
        
        # Create ZIP package
        create_zip_package(portable_dir)
        
        print("\n✅ Portable version created successfully!")
        print(f"📦 Package: IT_Job_Search_Portable.zip")
        print("\n📋 Instructions for users:")
        print("1. Extract the ZIP file")
        print("2. Run start_app.bat")
        print("3. Open http://127.0.0.1:8000 in browser")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 