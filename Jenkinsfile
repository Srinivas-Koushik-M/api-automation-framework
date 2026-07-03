pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                .venv/bin/python -m pytest tests -v
                '''
            }
        }

    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}