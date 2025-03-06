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
                    bat "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_TOKEN')]) {
                        bat """
                            echo ${DOCKER_TOKEN} | docker login -u ${DOCKER_USER} --password-stdin
                        """
                        bat "docker push ${DOCKER_IMAGE}"
                    }
                }
            }
        }
        stage('Deploy Application') {
            steps {
                script {
                    bat 'docker stop flask-app || exit 0'
                    bat 'docker rm flask-app || exit 0'
                    bat 'docker pull ${DOCKER_IMAGE}'
                    bat 'docker run -d --name flask-app -p 5000:5000 ${DOCKER_IMAGE}'
                }
            }
        }
    }
    post {
        success {
            emailext (
                to: 'i211137@nu.edu.pk',
                subject: "✅ Deployment Successful",
                body: "The **main** branch has been successfully deployed via Jenkins.",
                mimeType: 'text/html'
            )
        }
        failure {
            emailext (
                to: 'i211137@nu.edu.pk',
                subject: "❌ Deployment Failed",
                body: "There was an issue deploying the **main** branch. Please check the Jenkins logs.",
                mimeType: 'text/html'
            )
        }
    }
}
