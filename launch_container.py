#!/usr/bin/python3
import  cgi
web=cgi.FieldStorage()
docker_file_name=web.getvalue('docker_file_name')
container_name = web.getvalue('container_name')
print("Content-Type: text/html\r\n")
print(docker_file_name, container_name)
print("Hello World!")