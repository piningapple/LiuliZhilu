pipeline {
	agent any

	stages {
		stage('Checkout') {
			steps {
				checkout scm
			}
		}

        stage('Add venv') {
            steps {
                sh '''
                    python3 -m venv ./venv
                    . ./venv/bin/activate
                '''
            }
        }

		stage('Add requirements') {
			steps {
				sh '''
                    . ./venv/bin/activate
                    pip install -r requirements.txt                
                '''
			}
		}

		stage('Tests'){
			steps {
				sh '''
                    . ./venv/bin/activate
                    pytest               
                '''
			}
		}

		stage('Run') {			
			steps {
				sh '''
					. ./venv/bin/activate

					sudo systemctl stop fastapi-app || true

                    sudo systemctl daemon-reload
                    sudo systemctl start fastapi-app
                    sudo systemctl enable fastapi-app

					sleep 10

				'''
			}
		}

		stage('Check') {
			steps {
				sh '''
					. ./venv/bin/activate
					curl -f http://localhost:5126/ || exit 1
				'''
			}
		}

	}
}
