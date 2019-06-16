#!/usr/bin/python3
import  cgi
import cgitb
cgitb.enable()
import subprocess

import docker
client = docker.from_env()
import os


web=cgi.FieldStorage()
docker_file_name=web.getvalue('docker_file_name')
container_name = web.getvalue('container_name')



print("Content-Type: text/html\r\n")

subprocess.call("./bash_to_launch_container.sh", shell=True)

print(docker_file_name, container_name)
print("Hello World!")