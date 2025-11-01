pipeline {
    agent any
    
    stages {
        stage('Клонирование') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/6blCTPOmiha/SDET_UI.git'
            }
        }
        
        stage('Установка зависимостей') {
            steps {
                bat '''
                    pip install -r requirements.txt
                    pip install allure-pytest
                '''
            }
        }
        
        stage('Запуск тестов') {
            steps {
                bat '''
                    python -m pytest test_run.py -v
                '''
            }
        }
    }
    
    post {
        always {
            echo "Тесты завершены"
        }
    }
}
