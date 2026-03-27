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
                script {
                    def exitCode = bat(script: 'pytest tests/test_run.py -v --alluredir=allure-results', returnStatus: true)
                    if (exitCode != 0) {
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }
        
        stage('Генерация отчета Allure') {
            steps {
                bat '''
                    if not exist "allure-report" mkdir allure-report
                    allure generate allure-results --clean -o allure-report
                    echo "Allure результаты будут сохранены в allure-results/"
                '''
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
            echo "Allure результаты сохранены в allure-results/"
            archiveArtifacts artifacts: 'allure-report/**', fingerprint: true
            publishHTML(target: [
                reportDir: 'allure-report',
                reportFiles: 'index.html',
                reportName: "Allure Report"
            ])
        }
    }
}
