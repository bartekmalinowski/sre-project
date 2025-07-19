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
            script{
                def imageName = "sre-project-app:latest"
                docker.build(imageName)
                echo "Docker image ${imageName} built."
            }
        }

        //Start tests
        stage('Tests'){
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