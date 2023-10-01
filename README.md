# Kubernetes
Working Deployments

1) Requirements:
   - Install Vagrant
    wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
    sudo apt update && sudo apt install vagrant

   - Install ansible and nfs-common
    sudo apt-get install ansible nfs-common

   - Install necessary plugins
    sudo vagrant plugin install vagrant-libvirt vagrant-mutate

   - Make sure service is up and running
    sudo systemctl enabble libvirt

