sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable" -y

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y

sudo apt-get install apache2 -y


sudo apt-get update 

sudo apt-get upgrade -y

sudo apt-get install pyhton3-pip -y

pip3 install docker

sudo ln -s /etc/apache2/mods-available/cgi.load  /etc/apache2/mods-enabled

sudo service apache2 reload


usermod -aG docker www-data