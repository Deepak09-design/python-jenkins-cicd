pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {

        stage('Git Checkout') {
            steps {
                echo 'Checking out source code'
                checkout scm
            }
        }

        stage('Python Version') {
            steps {
                sh '''
                    python3 --version
                    pip3 --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    venv/bin/pip install --upgrade pip
                    venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    venv/bin/python -m pytest tests/ -v
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh '''
                    venv/bin/python app.py
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'app.py,requirements.txt',
                                 fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Python Jenkins CI/CD Pipeline SUCCESS!'
        }

        failure {
            echo 'Python Jenkins CI/CD Pipeline FAILED!'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
