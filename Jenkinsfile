pipeline{
    agent any
    stages{
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
