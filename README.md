# Kubernetes
Working Deployments

1) Requirements:
   1. Install Vagrant
   ```sh
      wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
      echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt sources.list.d/hashicorp.list
      sudo apt update && sudo apt install vagrant
   ```
   2. Install ansible and nfs-common
   ```sh 
      sudo apt-get install ansible nfs-common
   ```

   3. Install necessary plugins
   ```sh 
      sudo vagrant plugin install vagrant-libvirt vagrant-mutate
   ```
   4. Make sure service is up and running
   ```sh 
       sudo systemctl enabble libvirt
   ```
 

