pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/bartekmalinowski/sre-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                withDockerServer(uri: 'tcp://host.docker.internal:2375') {
                    script {
                        def imageName = "sre-project-app:v${BUILD_NUMBER}"
                        docker.build(imageName, '.')
                        echo "Successfully built Docker image: ${imageName}"
                    }
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests... (placeholder)'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}