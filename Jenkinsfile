pipeline {
    agent any

    environment {
        BRANCH_NAME = "${GIT_BRANCH.split('/')[1]}"
        DOCKERHUB_CREDENTIALS = credentials('5f8b634a-148a-4067-b996-07b4b3276fba')
        IMAGE_TAG = "V.0.${env.BUILD_NUMBER}"
        DEV_PORT = "8056"
        PROD_PORT = "8093"
        SERVER_IP = "10.0.0.43"
    }

    stages {
        stage("Clean workspace") {
            steps {
                cleanWs()
            }
        }
        stage("Checkout") {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/dev'], [name: '*/prod']], userRemoteConfigs: [[url: 'https://github.com/stwins60/sample-site.git']]])
            }
        }
        stage("Docker Build") {
            steps {
                script {
                    if (env.BRANCH_NAME == 'dev') {
                        sh "docker build -t idrisniyi94/dev-sample-site:$env.IMAGE_TAG -f Dockerfile.dev ."
                    }
                    else if (env.BRANCH_NAME == 'prod') {
                        sh "docker build -t idrisniyi94/prod-sample-site:$env.IMAGE_TAG -f Dockerfile.prod ."
                    }
                }
            }
        }
        stage('Docker Login') {
            steps {
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                echo "Login Succeeded"
            }
        }
        stage('Docker Push') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'dev') {
                        sh "docker push idrisniyi94/dev-sample-site:$env.IMAGE_TAG"
                    }
                    else if (env.BRANCH_NAME == 'prod') {
                        sh "docker push idrisniyi94/prod-sample-site:$env.IMAGE_TAG"
                    }
                }
            }
        }
        stage('Run Container') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'dev') {
                        def containerName = 'dev-sample-site'
                        def imageName = "idrisniyi94/${containerName}:$env.IMAGE_TAG"

                        def isRunning = sh(script: "docker ps -a | grep ${containerName}", returnStatus: true).trim()
                        if (isRunning == 0) {
                            sh "docker stop ${containerName}"
                            sh "docker rm ${containerName}"
                        }
                        sh "docker run -d --name ${containerName} -p ${env.DEV_PORT}:5000 ${imageName}"
                        echo "Application is running at http://$SERVER_IP:${env.DEV_PORT}"
                    }
                    else if (env.BRANCH_NAME == 'prod') {
                        def containerName = 'prod-sample-site'
                        def imageName = "idrisniyi94/${containerName}:$env.IMAGE_TAG"

                        def isRunning = sh(script: "docker ps -a | grep ${containerName}", returnStatus: true).trim()
                        if (isRunning == 0) {
                            sh "docker stop ${containerName}"
                            sh "docker rm ${containerName}"
                        }
                        sh "docker run -d --name ${containerName} -p ${env.PROD_PORT}:5000 ${imageName}"
                        echo "Application is running at http://$SERVER_IP:${env.PROD_PORT}"
                    }
                }
            }
        }
    }
}