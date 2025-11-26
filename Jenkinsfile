pipeline {
    agent any

    stages {
        stage('Checkout scm') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python (if needed)') {
            steps {
                bat '''
                    echo === Checking for Python ===
                    where python
                    if %ERRORLEVEL% NEQ 0 (
                        echo Python not found. Installing Chocolatey and Python...

                        :: Install Chocolatey (if not already installed)
                        powershell -NoProfile -ExecutionPolicy Bypass -Command ^
                          "Set-ExecutionPolicy Bypass -Scope Process -Force; ^
                           [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; ^
                           iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"

                        :: Install Python via Chocolatey (idempotent)
                        choco install python -y
                    )

                    echo === Python version ===
                    python --version
                '''
            }
        }

        stage('Install dependencies') {
            steps {
                bat '''
                    echo === Creating virtualenv ===
                    python -m venv venv

                    echo === Activating virtualenv ===
                    call venv\\Scripts\\activate

                    echo === Installing dependencies ===
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    echo === Running tests ===
                    call venv\\Scripts\\activate
                    python -m pytest -v
                '''
            }
        }
    }
}
