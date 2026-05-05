pipeline {
    agent any

    stages {
        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                export PYTHONPATH=.
                venv/bin/pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t flask-jenkins-app .
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker run -d -p 5001:5000 --name test-container flask-jenkins-app
                
                # Wait for app to start
                sleep 5
                
                # Test endpoint
                curl -f http://localhost:5001
                
            }
        }
    }

    post {
        always {
            sh '''
            docker stop test-container || true
            docker rm test-container || true
            '''
        }
    }
}