pipeline {
    agent any
    stages {
        stage('Build local image') {
            steps {
                sh 'echo "Building"'
                sh 'docker buildx build -t stephanevdb/vigilanteye:latest .'
            }
        }
        stage('Run container') {
            steps {
                sh 'echo "Running container"'
                sh 'docker run -d -p 5080:3000 --name vigilanteye stephanevdb/vigilanteye:latest'
            }
        }
        stage('Test API') {
            steps {
                sh 'echo "Testing API"'
                sh 'curl -s -o /dev/null -w "%{http_code}" http://localhost:5080/test | grep -q 200'
            }
        }
        stage('Push image') {
            steps {
                sh 'echo "Pushing"'
                sh 'docker buildx build --push --platform linux/amd64,linux/arm64 -t stephanevdb/vigilanteye:latest .'
            }
        }
    }
    post { 
        always { 
            sh 'echo "Cleaning up"'
            sh 'docker stop vigilanteye'
            sh 'docker rm vigilanteye'
        }
    }
}