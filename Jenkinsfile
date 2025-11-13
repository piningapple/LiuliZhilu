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

		stage('Pylint'){
			steps {
				sh '''
                    . ./venv/bin/activate
                    pylint *.py             
                '''
			}
		}	
		
		stage('Run') {
			when {
				branch 'main'
			}
			
			steps {
				sh '''
					. ./venv/bin/activate
                    pkill -f "uvicorn server:app" || true
                    sleep 2

                    nohup uvicorn server:app --host 0.0.0.0 --port 5126 > uvicorn.log 2>&1 &
                    echo $! > uvicorn.pid
                    sleep 10
				'''
			}
		}

		stage('Check') {
			when {
				branch 'main'
			}

			steps {
				sh '''
					. ./venv/bin/activate
					curl -f http://localhost:5126/ || exit 1
				'''
			}
		}

	}
}
