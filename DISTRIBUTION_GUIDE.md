# 🚀 IT Job Search - Distribution Guide

## 📦 Các Phiên Bản Có Sẵn

### 1. 🎯 Portable Version (Khuyến nghị)
**File**: `IT_Job_Search_Portable.zip`
- ✅ Không cần cài đặt Python
- ✅ Không cần cài đặt package
- ✅ Chạy được trên mọi máy Windows
- ✅ Tự động setup database và dữ liệu mẫu

**Cách sử dụng:**
1. Tải `IT_Job_Search_Portable.zip`
2. Giải nén vào thư mục bất kỳ
3. Double-click `start_app.bat`
4. Mở http://127.0.0.1:8000 trong trình duyệt

### 2. 🐳 Docker Version
**Files**: `Dockerfile`, `docker-compose.yml`
- ✅ Môi trường cô lập
- ✅ Dễ deploy
- ✅ Bao gồm PostgreSQL database

**Cách sử dụng:**
```bash
# Cài Docker Desktop trước
docker-compose up
```

### 3. ⚡ Executable Version
**File**: `it_job_search.exe`
- ✅ File đơn, dễ sử dụng
- ✅ Không cần cài đặt gì

**Cách sử dụng:**
1. Tải `it_job_search.exe`
2. Double-click để chạy
3. Mở http://127.0.0.1:8000

### 4. 🌐 Streamlit Launcher
**File**: `streamlit_app.py`
- ✅ Giao diện web đẹp
- ✅ Tự động cài đặt requirements

**Cách sử dụng:**
```bash
pip install streamlit
streamlit run streamlit_app.py
```

## 🔧 Cách Build

### Build Tất Cả Phiên Bản
```bash
build_all.bat
```

### Build Từng Phiên Bản
```bash
# Portable version
python create_portable.py

# Executable version  
python build_executable.py

# Docker version
docker build -t it-job-search .
```

### Test Nhanh
```bash
quick_test.bat
```

## 📋 Checklist Trước Khi Phân Phối

- [ ] Chạy `test_setup.py` - Tất cả tests pass
- [ ] Chạy `quick_test.bat` - Tạo portable version thành công
- [ ] Test portable version trên máy khác
- [ ] Kiểm tra file size (không quá lớn)
- [ ] Tạo README hướng dẫn sử dụng

## 🎯 Hướng Dẫn Cho Người Dùng Cuối

### Portable Version (Dễ nhất)
1. **Tải**: `IT_Job_Search_Portable.zip`
2. **Giải nén**: Extract vào thư mục bất kỳ
3. **Chạy**: Double-click `start_app.bat`
4. **Truy cập**: Mở http://127.0.0.1:8000
5. **Dừng**: Nhấn Ctrl+C trong cửa sổ command

### Troubleshooting
- **Port 8000 bị sử dụng**: Đóng ứng dụng khác đang dùng port 8000
- **Windows Defender chặn**: Thêm exception cho thư mục
- **Lỗi Python**: Portable version không cần Python
- **Lỗi database**: Tự động tạo lại khi chạy

## 📊 Thông Tin Kỹ Thuật

### Dữ Liệu Mẫu
- **270 việc làm** IT
- **20 công ty** hàng đầu
- **10 ngôn ngữ** lập trình
- **10 bài blog** mẫu

### Tính Năng
- Tìm kiếm việc làm nâng cao
- Quản lý profile người dùng
- Blog IT
- Responsive design
- OAuth authentication

### Yêu Cầu Hệ Thống
- **OS**: Windows 10/11
- **RAM**: 4GB+ (khuyến nghị)
- **Disk**: 2GB trống
- **Browser**: Chrome, Firefox, Edge

## 🚀 Deployment

### Local Development
```bash
cd backend
python manage.py runserver
```

### Production
```bash
# Collect static files
python manage.py collectstatic

# Use Gunicorn
gunicorn it_job_search.wsgi:application
```

## 📞 Hỗ Trợ

Nếu gặp vấn đề:
1. Kiểm tra README.txt trong portable version
2. Chạy `test_setup.py` để debug
3. Xem logs trong cửa sổ command
4. Liên hệ developer

---

**Made with ❤️ for the IT community** 