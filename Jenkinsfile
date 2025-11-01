pipeline {
    agent any
    
    tools {
        python "Python3"
    }
    
    stages {
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
