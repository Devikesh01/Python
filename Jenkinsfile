pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python3 -m venv env'
                sh '. env/bin/activate'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest test_cal.py'
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                sudo scp -i "/var/lib/jenkins/dip-key.pem" -o StrictHostKeyChecking=no -r /var/lib/jenkins/workspace/python-application/cal.py ec2-user@13.235.242.156:/home/ec2-user
                sudo scp -i "/var/lib/jenkins/dip-key.pem" -o StrictHostKeyChecking=no -r /var/lib/jenkins/workspace/python-application/test_cal.py ec2-user@13.235.242.156:/home/ec2-user
                sudo scp -i "/var/lib/jenkins/dip-key.pem" -o StrictHostKeyChecking=no -r /var/lib/jenkins/workspace/python-application/requirements.txt ec2-user@13.235.242.156:/home/ec2-user
                sudo ssh -i "/var/lib/jenkins/dip-key.pem" -o StrictHostKeyChecking=no ec2-user@13.235.242.156
                sudo apt-get update
                sudo apt-get install python3.6
                python3 -m venv env
                . env/bin/activate
                pip3 install -r requirements.txt
                python3 -m unittest test_cal.py
                '''
            }
        }
    }
}
