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

        stage('Lint Code') {
            steps {
                sh '''
                venv/bin/flake8 app tests
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
    }
}