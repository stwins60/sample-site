pipeline {
    agent any

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
    }
}