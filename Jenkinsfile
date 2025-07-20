pipeline {
    agent any

    environment {
        DOCKER_HOST = 'tcp://host.docker.internal:2375'
        EC2_ADDRESS = '16.171.198.37'
        CONTAINER_NAME = 'sre-app'
        DOCKERHUB_USER = 'bartekmalinowski'
        REPO_NAME = 'sre-project-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/bartekmalinowski/sre-project.git'
            }
        }

                stage('Test & Build') {
            steps {
                script {
                    env.IMAGE_NAME = "${DOCKERHUB_USER}/${REPO_NAME}:v${BUILD_NUMBER}"
                    sh "docker build -t ${env.IMAGE_NAME} ."
                }
            }
        }

        stage('Security Scan') {
            steps {
                sh """
                    docker run --rm \
                        -v /var/run/docker.sock:/var/run/docker.sock \
                        -v \$HOME/trivy-cache:/root/.cache/ \
                        aquasec/trivy:latest \
                        image --exit-code 1 --severity CRITICAL,HIGH ${env.IMAGE_NAME}
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"
                    }
                    sh "docker push ${env.IMAGE_NAME}"
                }
            }
        }

        stage('Deploy to EC2'){
            steps{
                sshagent(credentials: ['ec2-ssh-key']){
                    sh "ssh -o StrictHostKeyChecking=no ubuntu@${EC2_ADDRESS} 'docker pull ${env.IMAGE_NAME} && docker stop ${CONTAINER_NAME} || true && docker rm ${CONTAINER_NAME} || true && docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${env.IMAGE_NAME}'"
                }
            }
        }
    }
    post {
        always {
            sh "docker logout"
            echo 'Pipeline finished.'
        }
    }
}
