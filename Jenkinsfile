pipeline {

    agent any

    parameters {
        choice(
            name: 'TEST_SUITE',
            choices: ['all', 'smoke', 'regression'],
            description: 'Select test suite to run'
        )
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code is checked out from GitHub'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                rm -rf .venv allure-results allure-report report.html
                python3 -m venv .venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                .venv/bin/python -m pip install --upgrade pip
                .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                if [ "$TEST_SUITE" = "all" ]; then
                    .venv/bin/python -m pytest tests -v \
                      --html=report.html \
                      --self-contained-html \
                      --alluredir=allure-results
                else
                    .venv/bin/python -m pytest tests -v -m "$TEST_SUITE" \
                      --html=report.html \
                      --self-contained-html \
                      --alluredir=allure-results
                fi
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                /opt/homebrew/bin/allure generate allure-results --clean -o allure-report
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