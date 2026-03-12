pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh '. venv/bin/activate && pytest'
            }
        }
        stage('Deploy') {
            steps {
                // Note: This deployment method starts the application in the background on the Jenkins agent.
                // For production environments, consider more robust deployment strategies (e.g., systemd, Docker, Kubernetes).
                // Ensure any previously running instance on port 5000 is stopped before running this.
                sh 'nohup . venv/bin/activate && python3 app.py &'
            }
        }
    }
}