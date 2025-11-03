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
					nohup uvicorn server:app --host 0.0.0.0 --port 5126 > uvicorn.log 2>&1 &
					echo $! > uvicorn.pid
					sleep 10
				'''
			}
		}

		stage('check') {
			when {
				branch 'features/pinyin'
			}
			steps {
				sh '''
					curl -f http://localhost:5126/ || exit 1
				'''
			}
		}

	}
}
