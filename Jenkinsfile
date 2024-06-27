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
                    sh "docker build -t idrisniyi94/sample-site ."
                }
            }
        }
    }
}