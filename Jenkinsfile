pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'export PYTHONPATH=.; python3 -m pytest'
            }
        }
        stage('Deploy') {
            steps {
                sh 'JENKINS_NODE_COOKIE=dontKillMe nohup python3 app.py &'
            }
        }
    }
}