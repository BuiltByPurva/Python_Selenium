pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/BuiltByPurva/Python_Selenium.git'
            }
        }

        stage('Setup Environment') {
            steps {
                bat """
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    call venv\\Scripts\\activate
                    pytest tests/ ^
                        --junit-xml=reports/junit.xml ^
                        --cov=app ^
                        --cov-report=xml:coverage.xml ^
                        --cov-report=html:coverage_html
                """
            }
        }

        stage('Publish Reports') {
            steps {
                junit 'reports/junit.xml'
                publishHTML(target: [
                    reportDir: 'coverage_html',
                    reportFiles: 'index.html',
                    reportName: 'HTML Coverage Report'
                ])
            }
        }
    }



    post {
        always {
            archiveArtifacts artifacts: 'reports/**/*.xml, coverage_html/**', fingerprint: true
        }
    }
}
