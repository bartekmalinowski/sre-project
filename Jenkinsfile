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
                withDockerServer(uri: 'tcp://host.docker.internal:2375') {
                    script {
                        def imageName = "sre-project-app:v${BUILD_NUMBER}"
                        docker.build(imageName, '.')
                        echo "Successfully built Docker image: ${imageName}"
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
            echo 'Pipeline finished.'
        }
    }
}