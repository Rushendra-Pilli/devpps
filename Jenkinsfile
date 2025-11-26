


pipeline {
    agent any

    stages {
        stage('Checkout scm') {
            steps {
                checkout scm
            }
        }
        stage('Install dependencies') {
            steps {
                bat """
                    python --version
                    py -3 -m venv venv
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
                    python -m pytest -v
                """
            }
        }
    }
}