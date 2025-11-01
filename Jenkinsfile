pipeline {
    agent any
    
    stages {
        stage('Проверка Python') {
            steps {
                bat '''
                    python --version
                    if errorlevel 1 (
                        echo "Python не установлен. Устанавливаем..."
                        # Скачать и установить Python
                        curl -o python-installer.exe https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe
                        python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
                        timeout /t 30
                    )
                    python --version
                '''
            }
        }
        
        stage('Клонирование') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/6blCTPOmiha/SDET_UI.git'
            }
        }
        
        stage('Зависимости') {
            steps {
                bat '''
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Тесты') {
            steps {
                bat '''
                    python -m pytest test_run.py -v
                '''
            }
        }
    }
}
