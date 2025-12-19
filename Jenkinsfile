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

		stage('Build Dev'){
			when {
				expression { 
					return env.BRANCH_NAME == 'dev' || env.BRANCH_NAME.startsWith('feature/') 
				}
			}

			steps {
				sh 'dotnet build --configuration Debug --no-restore'
			}
		}

		stage('Build Release'){
			when {
				branch 'main'
			}

			steps {
				sh 'dotnet build --configuration Release --no-restore'
			}
		
			when {
				branch 'main'
			}

			steps {
				sh '''
					docker-compose -f docker-compose.yml down
					docker-compose -f docker-compose.yml build --no-cache
				'''
			}
		}

		stage('Docker Compose Build Release') {
			when {
				branch 'main'
			}

			steps {
				sh '''
					docker-compose -f docker-compose.yml down
					docker-compose -f docker-compose.yml build --no-cache
				'''
			}
		}

		stage('Run Release') {
			when {
				branch 'main'
			}

			steps {
				sh '''
                    docker-compose -f docker-compose.yml up -d
					sleep 5
					curl -f http://localhost:5126 || exit 1
				'''
			}
		}
	}

	}
}


