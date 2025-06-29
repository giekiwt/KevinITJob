#!/usr/bin/env python3
"""
Streamlit wrapper for Django IT Job Search application
This allows running the Django app through Streamlit interface
"""

import streamlit as st
import subprocess
import sys
import os
import threading
import time
import webbrowser
from pathlib import Path

def install_requirements():
    """Install required packages"""
    requirements = [
        "django==5.0.2",
        "djangorestframework==3.14.0", 
        "django-cors-headers==4.3.1",
        "pillow==10.2.0",
        "python-dotenv==1.0.1"
    ]
    
    for req in requirements:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", req])
        except subprocess.CalledProcessError:
            st.error(f"Failed to install {req}")
            return False
    return True

def setup_django():
    """Setup Django project"""
    backend_dir = Path("backend")
    
    if not backend_dir.exists():
        st.error("Backend directory not found!")
        return False
    
    # Change to backend directory
    os.chdir(backend_dir)
    
    # Run migrations
    try:
        subprocess.run([sys.executable, "manage.py", "migrate"], check=True)
        subprocess.run([sys.executable, "manage.py", "seed_jobs"], check=True)
        subprocess.run([sys.executable, "manage.py", "seed_blogposts"], check=True)
    except subprocess.CalledProcessError as e:
        st.error(f"Failed to setup Django: {e}")
        return False
    
    return True

def start_django_server():
    """Start Django development server"""
    try:
        subprocess.Popen([
            sys.executable, "manage.py", "runserver", "127.0.0.1:8000"
        ])
        return True
    except Exception as e:
        st.error(f"Failed to start Django server: {e}")
        return False

def main():
    st.set_page_config(
        page_title="IT Job Search - Launcher",
        page_icon="💼",
        layout="wide"
    )
    
    st.title("💼 IT Job Search Application Launcher")
    st.markdown("---")
    
    # Sidebar
    st.sidebar.header("🚀 Quick Actions")
    
    if st.sidebar.button("📦 Install Requirements"):
        with st.spinner("Installing requirements..."):
            if install_requirements():
                st.success("✅ Requirements installed successfully!")
            else:
                st.error("❌ Failed to install requirements")
    
    if st.sidebar.button("🔧 Setup Database"):
        with st.spinner("Setting up database..."):
            if setup_django():
                st.success("✅ Database setup completed!")
            else:
                st.error("❌ Failed to setup database")
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("🎯 About This Application")
        
        st.markdown("""
        **IT Job Search** là một ứng dụng web hiện đại cho phép:
        
        - 🔍 **Tìm kiếm việc làm IT** với bộ lọc nâng cao
        - 👤 **Quản lý profile** người dùng với avatar
        - 🏢 **Thông tin công ty** chi tiết
        - 📝 **Blog IT** với các bài viết hữu ích
        - 📱 **Responsive design** cho mọi thiết bị
        - 🔐 **Xác thực OAuth** với Google
        
        **Dữ liệu mẫu:**
        - 270+ việc làm IT
        - 20 công ty hàng đầu
        - 10 ngôn ngữ lập trình
        - 10 bài blog mẫu
        """)
    
    with col2:
        st.header("⚡ Quick Start")
        
        if st.button("🚀 Launch Application", type="primary"):
            with st.spinner("Starting application..."):
                # Install requirements if needed
                install_requirements()
                
                # Setup Django
                if setup_django():
                    # Start server
                    if start_django_server():
                        st.success("✅ Application started successfully!")
                        
                        # Auto-open browser
                        time.sleep(2)
                        webbrowser.open("http://127.0.0.1:8000")
                        
                        st.info("🌐 Application is running at: http://127.0.0.1:8000")
                        st.info("📱 You can now access the application in your browser")
                    else:
                        st.error("❌ Failed to start application")
                else:
                    st.error("❌ Failed to setup application")
    
    # Status section
    st.markdown("---")
    st.header("📊 Application Status")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Status", "Ready to Launch")
    
    with col2:
        st.metric("Port", "8000")
    
    with col3:
        st.metric("Database", "SQLite")
    
    # Instructions
    st.markdown("---")
    st.header("📋 Instructions")
    
    st.markdown("""
    ### Cách sử dụng:
    
    1. **Nhấn "Launch Application"** để khởi động
    2. **Chờ vài giây** để server khởi động
    3. **Trình duyệt sẽ tự động mở** tại http://127.0.0.1:8000
    4. **Khám phá các tính năng:**
       - Tìm kiếm việc làm theo ngôn ngữ lập trình
       - Xem thông tin công ty
       - Đọc blog IT
       - Đăng ký/đăng nhập tài khoản
    
    ### Troubleshooting:
    
    - **Port 8000 bị sử dụng**: Đóng ứng dụng khác đang dùng port 8000
    - **Lỗi cài đặt**: Chạy "Install Requirements" trước
    - **Lỗi database**: Chạy "Setup Database" để tạo lại
    """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Built with ❤️ using Django + Streamlit</p>
        <p>IT Job Search Application - Version 1.0</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 