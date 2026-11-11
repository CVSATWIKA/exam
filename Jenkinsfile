pipeline{
    agent any
    stages{
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/CVSATWIKA/exam.git'
            }
        }
        stage('Build'){
            steps{
                echo 'Building docker image'
                bat 'docker build -t myappn:v1 .'
            }
        }
       
        stage('Run'){
            steps{
            echo 'Running docker container'
            bat 'docker run -d -p 5000:5000 myappn:v1'
            }
        }
    
        stage('Push'){
            steps{
                echo 'pushing an image into docker hub'
                bat 'docker tag myappn:v1 cvsatwika/exam:img1'
                bat 'docker push cvsatwika/exam:img1'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'kubectl get deployments'
                bat 'kubectl get pods'
                bat 'kubectl get services'
            }
        }
        
    
    }
    post{
        success{
            echo 'Successful'
        }
        failure{
            echo 'Build Failure'
        }
    }
}
