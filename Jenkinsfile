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
                    python -m pytest test_run.py -v --alluredir=allure-results
                '''
            }
        }
        
        stage('Генерация отчета Allure') {
            steps {
                bat '''
                    # Создаем директорию для отчетов
                    if not exist "allure-report" mkdir allure-report
                    echo "Allure результаты сохранены в allure-results/"
                '''
            }
        }
    }
    
    post {
        always {
            // Архивируем результаты для скачивания
            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
            echo "Allure результаты сохранены в allure-results/"
        }
    }
}
