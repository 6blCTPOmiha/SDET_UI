pipeline {
    agent any
    
    stages {
        stage('Установка Python') {
            steps {
                sh 'sudo apt-get update'
                sh 'sudo apt-get install -y python3 python3-pip'
                sh 'python3 --version'
            }
        }
        
        stage('Клонирование') {
            steps {
                git 'https://github.com/6blCTPOmiha/SDET_UI'
            }
        }
        
        stage('Тестирование') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 -m pytest'
            }
        }
    }
}
