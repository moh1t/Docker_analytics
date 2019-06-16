import docker
#pip3 install docker 

client = docker.from_env()
client.containers.run('alpine', 'echo hello world')

container = client.containers.run('bfirsh/reticulate-splines',detach=True)
to run it in background


https://pypi.org/project/docker/

https://docker-py.readthedocs.io/en/stable/