pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-u root'
        }
    }
    stages {
        stage('ユニットテスト') {
            steps {
                sh 'pip install pytest'
                sh 'pytest test_app.py'
            }
        }
    }
}
