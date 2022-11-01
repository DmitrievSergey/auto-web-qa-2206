pipeline {
  agent any
  parameters {
      string(name: "executor", defaultValue: "192.168.1.6", trim: true, description: "executor")
      string(name: "browser", defaultValue: "chrome", trim: true, description: "browser")
      string(name: "bversion", defaultValue: "106.0", trim: true, description: "browser version")
      string(name: "opencart_url", defaultValue: "https://demo.opencart.com", trim: true, description: "opencart url")
      string(name: "n", defaultValue: "1", trim: true, description: "thread counr")
  }
  stages {
      stage('clear') {
          steps {
              sh 'docker image prune -a -f'
          }
      }
     stage('pull code') {
         steps {
            git branch: 'main', credentialsId: 'git', url: 'https://github.com/DmitrievSergey/auto-web-qa-2206.git'
         }
     }
     stage("Build image") {
        steps {
    	catchError {
      	   script {
        	      docker.build("python-web-tests", "-f Dockerfile .")
      	     }
          }
       }
    }
     stage('Run tests') {
        steps {
           catchError {
              script {
              	def c = docker.image('python-web-tests').run('--rm -it -v allure-results:/app/allure-results','-n=${n} --executor=${executor} --browser=${browser} --bversion=${bversion} --url=${opencart_url}')
              	sh "docker wait ${c.id}"
                }
        	}
      	}
     }
     stage('Reports') {
        steps {
           allure([
      	   includeProperties: false,
      	   jdk: '',
      	   properties: [],
      	   reportBuildPolicy: 'ALWAYS',
      	   results: [[path: 'allure-results']]
    	   ])
  	        }
         }
    }
}