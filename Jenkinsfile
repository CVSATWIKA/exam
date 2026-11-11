pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                echo 'Building docker image'
                bat 'docker build -t MyApp:v1 .'
            }
        }
        stage('Run'){
            steps{
            echo 'Running docker container'
            bat 'docker run -d -p 5000:5000 MyApp:latest'
            }
        }
        stage('Push'){
            steps{
                echo 'pushing an image into docker hub'
                bat 'docker tag MyApp:v1 cvsatwika/exam:img1'
                bat 'docker push cvsatwika/exam:img1'
            }
        }
        stage('Deploy'){
            steps{
                echo 'deployment using kubernetes'
                bat 'kubectl create deployment MyAppn --image=MyApp --NodePort=5000'
                bat 'kubectl expose deployment MyAppn'
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