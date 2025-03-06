pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "murtazahasan/flask-app:latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/murtaza-hasan1/Assignment_1.git'
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
                    docker.build("murtazahasan/flask-app:latest")
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    withDockerRegistry([credentialsId: 'docker-hub-credentials']) {
                        docker.image("murtazahasan/flask-app:latest").push()
                    }
                }
            }
        }
        stage('Deploy Application') {
            steps {
                script {
                    // Stop and remove existing container, handling errors correctly on Windows
                    bat 'docker stop flask-app || exit 0'
                    bat 'docker rm flask-app || exit 0'
                    // Pull the image and run the container
                    bat "docker pull ${DOCKER_IMAGE}"
                    bat 'docker run -d --name flask-app -p 5000:5000 murtazahasan/flask-app:latest'
                }
            }
        }
    }
    post {
        success {
            emailext (
                to: 'i211137@nu.edu.pk',
                subject: "Deployment Successful",
                body: "The **main** branch has been successfully deployed via Jenkins.",
                mimeType: 'text/html'
            )
        }
        failure {
            emailext (
                to: 'i211137@nu.edu.pk',
                subject: "Deployment Failed",
                body: "There was an issue deploying the **main** branch. Please check the Jenkins logs.",
                mimeType: 'text/html'
            )
        }
    }
}
