pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "murtazahasan/flask-app:latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/murtaza-hasan1/Assignment_1.git']])
            }
        }
        stage('Code Quality Check') {
            steps {
                bat 'pip install flake8'
                bat 'flake8 --max-line-length=100'
            }
        }
        stage('Run Unit Tests') {
            steps {
                bat 'python -m unittest discover'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = "murtazahasan/flask-app:latest"
                    bat "docker build -t ${dockerImage} ."
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        bat "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"
                        bat "docker push ${DOCKER_IMAGE}"
                    }
                }
            }
        }
        stage('Deploy Application') {
            steps {
                bat 'docker run -d -p 5000:5000 murtazahasan/flask-app:latest'
            }
        }
    }
    post {
        success {
            emailext (
                to: 'i211137@nu.edu.pk',
                subject: "Deployment Successful",
                body: "The master branch has been successfully deployed via Jenkins.",
                mimeType: 'text/html'
            )
        }
        failure {
            emailext (
                to: 'i211137@nu.edu.pk',
                subject: "Deployment Failed",
                body: "There was an issue deploying the master branch. Please check the Jenkins logs.",
                mimeType: 'text/html'
            )
        }
    }
}
