pipeline {
    agent any
    stages {
        stage('Build local image') {
            steps {
                sh 'echo "Building"'
                sh 'docker buildx build -t stephanevdb/VigilantEye:latest .'
            }
        }
        stage('Push image') {
            steps {
                sh 'echo "Pushing"'
                sh 'docker buildx build --push --platform linux/amd64,linux/arm64 -t stephanevdb/VigilantEye:latest .'
            }
        }
    }
}