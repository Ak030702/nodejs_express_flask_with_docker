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
