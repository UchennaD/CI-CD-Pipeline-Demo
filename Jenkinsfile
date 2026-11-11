pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        WEBEX_TOKEN   = credentials('webex-bot-token')
        WEBEX_ROOM_ID = credentials('webex-room-id')
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Environment') {
            steps { sh 'python3 --version' }
        }
        stage('Unit Tests') {
            steps { sh 'python3 -m unittest discover -v' }
        }
    }

    post {
        success { sh 'python3 notify_webex.py SUCCESS' }
        failure { sh 'python3 notify_webex.py FAILURE' }
    }
}