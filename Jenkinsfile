pipeline {
    agent any
    stages {
        stage('Build local image') {
            steps {
                sh 'echo "Building"'
                sh 'docker buildx build -t stephanevdb/vigilanteye-master:latest .'
            }
        }
        // stage('Run container') {
        //     steps {
        //         sh 'echo "Running container"'
        //         sh 'docker run -d -p 5080:3000 --name vigilanteye stephanevdb/vigilanteye-master:latest'
        //     }
        // }
        // stage('Test app') {
        //     steps {
        //         sh 'echo "Testing app"'
        //         waitUntil {
        //             sh 'wget --retry-connrefused --tries=120 --waitretry=1 -q http://localhost5080/test -O /dev/null'
        //         }
        //     }
        // }
        stage('Push image') {
            steps {
                sh 'echo "Pushing"'
                sh 'docker buildx build --push --platform linux/amd64,linux/arm64 -t stephanevdb/vigilanteye-master:latest .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Sending POST request"'
                sh 'curl -X POST -H "Content-Type: application/json" https://portainer.stephanevdb.com/api/stacks/webhooks/d1a57ad8-f428-48b0-957a-a8c1cfa2b6fb'
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