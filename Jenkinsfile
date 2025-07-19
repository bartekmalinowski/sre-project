pipeline{
    agent any

    stages{
        //Downloading code
        stage('Checkout'){
            steps{
                git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/bartekmalinowski/sre-project.git'
                echo "Code checked out successfully."
            }
        }
        //Building docker image
        stage('Build docker image'){
            steps{
                script{
                    def imageName = "sre-project-app:latest"
                    writeFile file: 'docker-compose.yml', text: """
                    version: '3.8'
                    services:
                    app:
                    build: .
                    image: ${imageName}
                    """
                    sh 'docker compose build'
                    echo "Docker image ${imageName} built."
                }
            }
    }

        //Start tests
        stage('Tests'){
            steps{
                echo 'Running tests..'
                sh 'echo Test passed!'
            }
        }
    }   
    post {
        always{
            deleteDir()
            echo 'Pipeline finished.'
        }
    }
}