properties([parameters([choice(choices: ['all', 'get', 'post', 'put', 'patch', 'delete', 'users', 'resource', 'register', 'login'], name: 'request')])])

pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                echo 'checkout'
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/WaseemSayara/api_testing.git']]])
            }
        }
         stage('build') {
            steps {
                echo 'build'
                git branch: 'main', url: 'https://github.com/WaseemSayara/api_testing.git'
                bat 'dir'

            }
        }
         stage('test') {
             steps {
                 script{
                     try{
                    withPythonEnv('python') {
                        bat 'pip install pytest'
                        bat 'pip install requests'
                        echo "hi ${params.request}"
                       
                        bat "python main.py ${params.request}"
                        
                    }
                     }
                     catch (ERROR) {
                         echo ERROR.getMessage()
                         
                     }
                     echo currentBuild.result
             }
             }
        }
    }
}
