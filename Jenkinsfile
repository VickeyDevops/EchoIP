pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'  // Change if needed
        ECR_REPO = 'ip-tracker'  // Change if needed
        IMAGE_TAG = 'latest'  
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/VickeyDevops/EchoIP.git'
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
                    REPO_URI=$(aws ecr describe-repositories --repository-names $ECR_REPO --query "repositories[0].repositoryUri" --output text)

                    aws ecr get-login-password --region $AWS_REGION | \
                    docker login --username AWS --password-stdin $REPO_URI
                    
                    docker tag $ECR_REPO:$IMAGE_TAG $REPO_URI:$IMAGE_TAG
                    docker push $REPO_URI:$IMAGE_TAG
                    '''
                }
            }
        }

        stage('Deploy to EKS') {
            steps {
                echo 'Deploying to EKS...'
            }
        }
    }
}
