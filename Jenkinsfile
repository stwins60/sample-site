pipeline {
    agent any

    environment {
        BRANCH_NAME = "${GIT_BRANCH.split('/')[1]}"
        DOCKERHUB_CREDENTIALS = credentials('5f8b634a-148a-4067-b996-07b4b3276fba')
        IMAGE_TAG = "V.0.${env.BUILD_NUMBER}"
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
                    def containerName = BRANCH_NAME == 'dev' ? 'dev-sample-site' : 'prod-sample-site'
                    def imageName = "idrisniyi94/${containerName}"

                    def isRunning = sh(script: "docker ps -q -f name=${containerName}", returnStdout: true).trim()
                    if (isRunning) {
                        sh "docker stop ${containerName}"
                        sh "docker rm ${containerName}"
                    }
                    sh "docker run -d --name ${containerName} -p 8093:5000 ${imageName}"
                }
                echo "Application is running at http://10.0.0.43:8093"
            }
        }
    }
}