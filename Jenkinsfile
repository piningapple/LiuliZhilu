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
            when {
				branch 'features/pinyin'
			}

			steps {
				sh '''
                    . ./venv/bin/activate
                    pytest               
                '''
			}
		}


		stage('Run') {
			when {
				branch 'features/pinyin'
			}

			steps {
				sh '''
                    . ./venv/bin/activate
                    uvicorn main:app 
					sleep 5
					curl -f http://localhost:5126/ || exit 1
				'''
			}
		}

	}
}
