@Library("mylib") _
pipeline {
    agent { label 'vinod' }
    
    environment {
        TARGETPORT = "8080"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    codepull("https://github.com/Ak030702/nodejs_express_flask_with_docker", "master")
                }
            }
        }

        stage('Build Docker Container') {
            steps {
                script {
                    dockerbuild('./frontend', './backend')
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    dockerpush()
                }
            }
        }

        stage("Check Port & Deploy") {
            steps {
                sh "docker-compose down && docker-compose up -d"
            }
        }
    }
}
