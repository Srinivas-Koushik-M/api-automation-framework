pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code is checked out from GitHub'
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
                .venv/bin/python -m pytest tests -v \
                --html=report.html \
                --self-contained-html \
                --alluredir=allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                allure generate allure-results --clean -o allure-report
                '''
            }
        }

    }

    post {

        always {

            publishHTML(target: [
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'API Automation Report'
            ])

            archiveArtifacts artifacts: 'allure-report/**', fingerprint: true

        }

    }

}