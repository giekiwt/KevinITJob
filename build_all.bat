@echo off
echo ========================================
echo    IT Job Search - Build All Versions
echo ========================================
echo.

echo [1/4] Building Docker version...
docker build -t it-job-search:latest .
if %errorlevel% neq 0 (
    echo ERROR: Docker build failed!
    pause
    exit /b 1
)
echo ✅ Docker version built successfully!
echo.

echo [2/4] Building Portable version...
python create_portable.py
if %errorlevel% neq 0 (
    echo ERROR: Portable build failed!
    pause
    exit /b 1
)
echo ✅ Portable version built successfully!
echo.

echo [3/4] Building Executable version...
python build_executable.py
if %errorlevel% neq 0 (
    echo ERROR: Executable build failed!
    pause
    exit /b 1
)
echo ✅ Executable version built successfully!
echo.

echo [4/4] Creating distribution package...
if not exist "dist" mkdir dist

echo Creating distribution folder...
if exist "IT_Job_Search_Distribution" rmdir /s /q "IT_Job_Search_Distribution"
mkdir "IT_Job_Search_Distribution"

echo Copying files...
copy "IT_Job_Search_Portable.zip" "IT_Job_Search_Distribution\"
copy "dist\it_job_search.exe" "IT_Job_Search_Distribution\"
copy "docker-compose.yml" "IT_Job_Search_Distribution\"
copy "Dockerfile" "IT_Job_Search_Distribution\"
copy "requirements.txt" "IT_Job_Search_Distribution\"
copy "streamlit_app.py" "IT_Job_Search_Distribution\"

echo Creating README...
echo # IT Job Search - Distribution Package > "IT_Job_Search_Distribution\README.md"
echo. >> "IT_Job_Search_Distribution\README.md"
echo ## Available Versions >> "IT_Job_Search_Distribution\README.md"
echo. >> "IT_Job_Search_Distribution\README.md"
echo ### 1. Portable Version (Recommended) >> "IT_Job_Search_Distribution\README.md"
echo - Extract IT_Job_Search_Portable.zip >> "IT_Job_Search_Distribution\README.md"
echo - Run start_app.bat >> "IT_Job_Search_Distribution\README.md"
echo - No installation required >> "IT_Job_Search_Distribution\README.md"
echo. >> "IT_Job_Search_Distribution\README.md"
echo ### 2. Executable Version >> "IT_Job_Search_Distribution\README.md"
echo - Run it_job_search.exe >> "IT_Job_Search_Distribution\README.md"
echo - Single file, easy to use >> "IT_Job_Search_Distribution\README.md"
echo. >> "IT_Job_Search_Distribution\README.md"
echo ### 3. Docker Version >> "IT_Job_Search_Distribution\README.md"
echo - Install Docker >> "IT_Job_Search_Distribution\README.md"
echo - Run: docker-compose up >> "IT_Job_Search_Distribution\README.md"
echo. >> "IT_Job_Search_Distribution\README.md"
echo ### 4. Streamlit Launcher >> "IT_Job_Search_Distribution\README.md"
echo - Install: pip install streamlit >> "IT_Job_Search_Distribution\README.md"
echo - Run: streamlit run streamlit_app.py >> "IT_Job_Search_Distribution\README.md"

echo Creating ZIP distribution...
powershell Compress-Archive -Path "IT_Job_Search_Distribution\*" -DestinationPath "IT_Job_Search_Complete_Distribution.zip" -Force

echo ✅ All versions built successfully!
echo.
echo 📦 Distribution files created:
echo    - IT_Job_Search_Portable.zip (Portable version)
echo    - dist\it_job_search.exe (Executable version)
echo    - IT_Job_Search_Complete_Distribution.zip (All versions)
echo.
echo 🚀 Ready for distribution!
echo.
pause 