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
                    pip install allure-pytest pytest-xdist
                '''
            }
        }
        
        stage('Запуск тестов') {
            steps {
                bat '''
                    pytest test_run.py -v --alluredir=allure-results -n 2
                '''
            }
        }
        
        stage('Генерация отчета Allure') {
            steps {
                bat '''
                    if not exist "allure-report" mkdir allure-report
                    echo "Allure результаты будут сохранены в allure-results/"
                '''
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
            echo "Allure результаты сохранены в allure-results/"
        }
    }
}
