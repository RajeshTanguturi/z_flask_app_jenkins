pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/RajeshTanguturi/z_flask_app_jenkins.git'
            }
        }

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
    }
}