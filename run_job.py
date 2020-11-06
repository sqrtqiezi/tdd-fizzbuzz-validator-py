import jenkins
JENKINS_SERVER = 'http://47.96.126.48:8080/'
JENKINS_USER = 'admin'
JENKINS_PWD = '0898a5e60d374da48f6e31978e7f9706'

# git@github.com:sqrtqiezi/tdd-taxi-seed-py.git
# git@github.com:sqrtqiezi/tdd-taxi-success-py.git

JOB_NAME = 'tdd-taxi-validator-py/master'
REPO_URL = 'git@github.com:sqrtqiezi/tdd-taxi-success-py.git'
CREDENTIALS_ID = 'github_cred_id'

if __name__ == '__main__':
    server = jenkins.Jenkins(JENKINS_SERVER,
                             username=JENKINS_USER,
                             password=JENKINS_PWD)

    server.build_job(JOB_NAME, {
        'REPO_URL': REPO_URL,
        'CREDENTIALS_ID': CREDENTIALS_ID
    })