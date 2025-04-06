pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/VickeyDevops/EchoIP.git' // Change this
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
            }
        }
        stage('Push to AWS ECR') {
            steps {
                echo 'Pushing to AWS ECR...'
            }
        }
        stage('Deploy to EKS') {
            steps {
                echo 'Deploying to EKS...'
            }
        }
    }
}
