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
                withCredentials([usernamePassword(credentialsId: "dockerhubsc", usernameVariable: "usernameDH", passwordVariable: "passwordDH")]) {
                    echo "Pushing the images"
                    sh "docker login -u ${env.usernameDH} -p ${env.passwordDH}"

                    echo "Tagging the images"
                    sh "docker tag frontend ${env.usernameDH}/frontend:latest"
                    sh "docker tag backend ${env.usernameDH}/backend:latest"

                    echo "Pushing images to Docker Hub"
                    sh "docker push ${env.usernameDH}/frontend:latest"
                    sh "docker push ${env.usernameDH}/backend:latest"
                }
            }
        }

        stage("Check Port & Deploy") {
            steps {
                script {
                    def portInUse = sh(
                        script: "sudo lsof -i:${TARGETPORT} | grep LISTEN || true",
                        returnStdout: true
                    ).trim()

                    if (portInUse) {
                        echo "Port ${TARGETPORT} is already in use — stopping existing containers"
                        sh "docker-compose down"
                    } else {
                        echo "Port ${TARGETPORT} is free — deploying"
                    }

                    sh "docker-compose up -d"
                }
            }
        }
    }
}
