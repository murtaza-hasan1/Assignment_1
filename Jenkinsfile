pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "murtazahasan/flask-app"
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
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Push Docker Image') {
    steps {
        withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
            bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
            bat 'docker push %DOCKER_IMAGE%'
        }
    }
}


        stage('Deploy Application') {
            steps {
                bat 'docker run -d -p 5000:5000 %DOCKER_IMAGE%'
            }
        }
    }

    post {
        success {
            mail to: 'i211137@nu.edu.pk',
                 subject: 'Deployment Successful',
                 body: 'The Flask app has been successfully deployed via Jenkins.'
        }
    }
}
