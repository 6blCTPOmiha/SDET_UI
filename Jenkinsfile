pipeline {
    agent any
    
    stages {
        stage('Установка Python если нужно') {
            steps {
                sh '''
                    # Для Ubuntu/Debian
                    if ! command -v python3 &> /dev/null; then
                        echo "Устанавливаем Python3..."
                        sudo apt-get update
                        sudo apt-get install -y python3 python3-pip
                    fi
                    
                    # Проверяем установку
                    python3 --version
                '''
            }
        }
        stage('Checkout') {
            steps {
                git branch: 'dev', 
                    url: 'https://github.com/6blCTPOmiha/SDET_UI'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'python -m pytest tests/ -v'
                // или sh 'python -m unittest discover -v'
            }
        }
        
        stage('Generate Report') {
            steps {
                sh 'allure generate allure-results -o allure-report --clean'
            }
        }
    }
    
    post {
        always {
            allure includeProperties: false, 
                   jdk: '', 
                   results: [[path: 'allure-results']]
        }
    }
}
