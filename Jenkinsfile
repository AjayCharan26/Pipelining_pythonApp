    pipeline {
      agent any
      stages {
        stage('Prep') {
          steps {
            sh 'python3 --version || true'
            sh 'pip3 --version || true'
          }
        }
        stage('Install') {
          steps {
            sh 'python3 -m pip install --upgrade pip'
            sh 'pip3 install flask'
          }
        }
        stage('Smoke Test') {
          steps {
            sh 'python3 - << "PY"
from model import predict
print("Predict demo:", predict("this is good"))
PY'
          }
        }
        stage('Run (quick)') {
          steps {
            sh 'nohup python3 app.py >/tmp/app.log 2>&1 & sleep 3 || true'
            sh 'curl -sSf http://127.0.0.1:5000/ >/tmp/homepage.html || true'
            archiveArtifacts artifacts: '/tmp/homepage.html', allowEmptyArchive: true
          }
        }
      }
    }
