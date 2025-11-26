


// pipeline {
//     agent any

//     stages {
//         stage('Checkout scm') {
//             steps {
//                 checkout scm
//             }
//         }
//         stage('Install dependencies') {
//             steps {
//                 bat """
//                     python --version
//                     py -3 -m venv venv
//                     call venv\\Scripts\\activate
//                     pip install --upgrade pip
//                     pip install -r requirements.txt
//                 """
//             }
//         }
//         stage('Run Tests') {
//             steps {
//                 bat """
//                     call venv\\Scripts\\activate
//                     python -m pytest -v
//                 """
//             }
//         }
//     }
// }



pipeline {
    agent any

    environment {
        // FULL path to your python.exe
        PYTHON = 'C:\\Users\\Rushendra\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
    }

    stages {
        stage('Checkout scm') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                bat """
                    echo === Using Python at: %PYTHON% ===
                    "%PYTHON%" --version

                    echo === Creating virtualenv ===
                    "%PYTHON%" -m venv venv

                    echo === Activating virtualenv ===
                    call venv\\Scripts\\activate

                    echo === Installing dependencies ===
                    "%PYTHON%" -m pip install --upgrade pip
                    "%PYTHON%" -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    echo === Running tests ===
                    call venv\\Scripts\\activate
                    "%PYTHON%" -m pytest -v
                """
            }
        }
    }
}
