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

		stage('Docker Compose Build Release') {
			when {
				branch 'main'
			}

			steps {

				   sh 'docker-compose down || true'
                    
                    sh '''
                        if docker ps -a --format "{{.Names}}" | grep -q "liulizhilu_database"; then
                            docker rm -f liulizhilu_database
                        fi
                    '''

					
                    sh '''
                        if docker ps -a --format "{{.Names}}" | grep -q "liulizhilu_app"; then
                            docker rm -f liulizhilu_app
                        fi
                    '''

					sh '''
                        if docker ps -a --format "{{.Names}}" | grep -q "liulizhilu_nginx"; then
                            docker rm -f liulizhilu_nginx
                        fi
                    '''

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
					curl -f http://localhost:5127 || exit 1
				'''
			}
		}
	}

}


