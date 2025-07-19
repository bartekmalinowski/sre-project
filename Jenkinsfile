pipeline {
    agent any

    environment {
        DOCKER_HOST = 'tcp://host.docker.internal:2375'
        EC2_ADDRESS = '16.171.198.37'
        CONTAINER_NAME = 'sre-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/bartekmalinowski/sre-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                    script {
                        env.IMAGE_NAME = "sre-project-app:v${BUILD_NUMBER}"
                        sh "docker build -t ${env.IMAGE_NAME} ."
                        echo "Successfully built Docker image: ${env.IMAGE_NAME}"
                }
            }
        }

        Stage('Deploy to EC2'){
            steps{
                sshagent(credentials: ['ec2-ssh-key']){
                    sh """
                        ssh -o StrictHostKeyChecking=no ubuntu@${EC2_ADDRESS} << 'ENDSSH'
                            echo 'Connected to EC2'
                            docker stop {CONTAINER_NAME} || true
                            docker rm {CONTAINER_NAME} || true
                            docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${env.IMAGE_NAME}

                            echo 'Deployment finished.'
                        ENDSSH
                    """
                }
            }
        }
    
    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}