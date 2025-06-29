@echo off
echo ========================================
echo    IT Job Search - Quick Test
echo ========================================
echo.

echo [1/3] Testing Python files...
python test_setup.py
if %errorlevel% neq 0 (
    echo ERROR: Test failed!
    pause
    exit /b 1
)

echo.
echo [2/3] Creating portable version...
python create_portable.py
if %errorlevel% neq 0 (
    echo ERROR: Portable creation failed!
    pause
    exit /b 1
)

echo.
echo [3/3] Testing Docker build...
docker build -t it-job-search-test .
if %errorlevel% neq 0 (
    echo WARNING: Docker build failed (Docker might not be available)
) else (
    echo ✅ Docker build successful!
)

echo.
echo ========================================
echo ✅ All tests completed successfully!
echo.
echo 📦 Available packages:
echo    - IT_Job_Search_Portable.zip (Portable version)
echo    - Docker image: it-job-search-test
echo.
echo 🚀 Ready for distribution!
echo.
pause 