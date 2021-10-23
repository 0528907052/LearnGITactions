import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='Administrator', password='1q2w3e4r5t')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))