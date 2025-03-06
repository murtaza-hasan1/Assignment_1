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
                script {
                    sh 'pip install flake8'
                    sh 'flake8 --max-line-length=100'
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    sh 'python -m unittest discover'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build(env.DOCKER_IMAGE)
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                            dockerImage.push()
                        }
                    }
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 $DOCKER_IMAGE'
                }
            }
        }
    }

    post {
        success {
            emailext(
                to: 'i211137@nu.edu.pk',
                subject: "Deployment Successful",
                body: "The main branch has been successfully deployed via Jenkins.",
                mimeType: 'text/html'
            )
        }
        failure {
            emailext(
                to: 'i211137@nu.edu.pk',
                subject: "Deployment Failed",
                body: "There was an issue deploying the main branch. Please check the Jenkins logs.",
                mimeType: 'text/html'
            )
        }
    }
}
