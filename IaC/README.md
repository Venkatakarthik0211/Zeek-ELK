# Terraform Provisioning
Use KVM/QEMU, Docker, libvirt, Terraform and
verify deployment with Testinfra.

## Dependencies

1. GNU/Linux host machine
2. KVM
3. QEMU
4. Libvirt
5. Terraform
6. Python 3
7. Ansible
8. Testinfra
9. Debian 11 Bullseye qcow2 bootable

## Usage instructions

### 1. Provision resources (VMs) on KVM using Terraform

1. Install libvirt relatedp packages and plugin

   ```sh
   sudo apt update
   sudo apt install build-essential qemu-kvm libvirt-daemon-system libvirt-dev 
   sudo apt install virt-manager
   virsh list
   sudo systemctl start libvirtd
   sudo systemctl enable libvirtd
   ```
2. Install Terraform 
   ```sh 
   
   sudo apt-get update && sudo apt-get install -y gnupg software-properties-common
   wget -O- https://apt.releases.hashicorp.com/gpg | \
   gpg --dearmor | \ 
   sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
   
   gpg --no-default-keyring \ 
   --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \ 
   --fingerprint
   
   echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
   https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
   sudo tee /etc/apt/sources.list.d/hashicorp.list
   
   sudo apt update && sudo apt-get install terraform     
   ```
3. Generate a SSH, to use .pub key in cloud.ini

   ```sh
   ssh-keygen -t ed25519 -C "newk8"
   ```
   (Optional To connect to your repository)
   Add necessary Details to ssh key and Paste it in git. 
   Clone the repository, for making changes anytime. 
   
   (Optional)Make sure to give authenticity of your github
   ```sh
   git config --global user.name "VenkataKarthik0211"
   git config --global user.email "sacredspirits47@gmail.com"
   ```
   (Optional)To push all changes
   ```sh
   git add .
   git commit -m "Modifications done"
   git push origin -o main
   ```
   
4. Customize the .pub of ssh keys which are geenerated in previous step

5. Customize the path in conf.tf of your image




