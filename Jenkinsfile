pipeline {
    agent any
    
    triggers {
        pollSCM('* * * * *') // Check for changes in the SCM every minute
    }

    
    stages {
        stage('Run Python Script') {
            steps {
                sh 'python3 view_machine_name.py'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
