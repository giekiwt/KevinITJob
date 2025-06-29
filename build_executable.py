#!/usr/bin/env python3
"""
Script to build executable version of the Django application
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("PyInstaller already installed")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def create_spec_file():
    """Create PyInstaller spec file for Django app"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['backend/manage.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('backend/templates', 'templates'),
        ('backend/staticfiles', 'staticfiles'),
        ('backend/media', 'media'),
        ('backend/user_management', 'user_management'),
        ('backend/job_listings', 'job_listings'),
        ('backend/company_profiles', 'company_profiles'),
        ('backend/blog_posts', 'blog_posts'),
        ('backend/it_job_search', 'it_job_search'),
    ],
    hiddenimports=[
        'django',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'corsheaders',
        'social_django',
        'django_filters',
        'user_management',
        'job_listings',
        'company_profiles',
        'blog_posts',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='it_job_search',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
'''
    
    with open('it_job_search.spec', 'w') as f:
        f.write(spec_content)

def build_executable():
    """Build the executable"""
    print("Building executable...")
    
    # Create spec file
    create_spec_file()
    
    # Run PyInstaller
    subprocess.check_call([
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--console",
        "it_job_search.spec"
    ])
    
    print("Executable built successfully!")
    print("You can find it in the 'dist' folder")

def main():
    """Main function"""
    print("Building IT Job Search Application Executable")
    print("=" * 50)
    
    # Install PyInstaller
    install_pyinstaller()
    
    # Build executable
    build_executable()
    
    print("\nInstructions for users:")
    print("1. Copy the executable from 'dist' folder")
    print("2. Create a folder for the application")
    print("3. Run the executable in that folder")
    print("4. The application will create its own database and start the server")

if __name__ == "__main__":
    main() 