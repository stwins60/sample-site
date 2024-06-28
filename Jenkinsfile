pipeline {
    agent any

    environment {
        BRANCH_NAME = "${GIT_BRANCH.split('/')[1]}"
        DOCKERHUB_CREDENTIALS = credentials('5f8b634a-148a-4067-b996-07b4b3276fba')
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
                        sh "docker build -t idrisniyi94/dev-sample-site -f Dockerfile.dev ."
                    }
                    else if (env.BRANCH_NAME == 'prod') {
                        sh "docker build -t idrisniyi94/prod-sample-site -f Dockerfile.prod ."
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
                        sh "docker push idrisniyi94/dev-sample-site"
                    }
                    else if (env.BRANCH_NAME == 'prod') {
                        sh "docker push idrisniyi94/prod-sample-site"
                    }
                }
            }
        }
    }
}