pipeline {
    agent any

    environment{
        AWS_REGION = 'us-east-1' // Change this
        ECR_REPO = 'ip-tracker' // Change this
        IMAGE_TAG = 'latest' // Change this
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/VickeyDevops/EchoIP.git' // Change this
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t $ECR_REPO:$IMAGE_TAG .'
            }
        }
        stage('Push to AWS ECR') {
            steps {
                echo 'Pushing to AWS ECR...'
                    withCredentials([aws(credentialsId: 'aws', region: "$AWS_REGION")]) {
                    sh '''
                    aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
                    docker tag $ECR_REPO:$IMAGE_TAG $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:$IMAGE_TAG
                    docker push $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:$IMAGE_TAG
                    '''
            }
        }
        stage('Deploy to EKS') {
            steps {
                echo 'Deploying to EKS...'
            }
        }
    }
}
