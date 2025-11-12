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
			when {
				branch 'main'
			}
			
			steps {
				sh '''
                    . ./venv/bin/activate
                    pylint *.py             
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
					sudo systemctl daemon-reload
					sudo systemctl restart LiuliZhilu_main
					sleep 5
					curl -f http://localhost:5126/ || exit 1

				'''
			}
		}

	}
}
