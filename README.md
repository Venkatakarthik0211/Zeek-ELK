# Kubernetes
Working Deployments

Starting with a new Virtual Machine?, No-problem, here is a complete walkthrough.

   Optional(Connect to git)
   ```sh
   ssh-keygen -t ed25519 -C "newk8"
   ```
   Add necessary Details to ssh key and Paste it in git. 
   Clone the repository, for making changes anytime. 
   ```sh
   git config --global user.name "VenkataKarthik0211"
   git config --global user.email "sacredspirits47@gmail.com"
   ```


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
   5. Clone the repository
   ```sh 
   git clone https://github.com/Venkatakarthik0211/Kubernetes.git
   ```
   6. Assign required permissions to files
   ```sh
   chmod +x automate.sh
   ./automate.sh
   ```
 

