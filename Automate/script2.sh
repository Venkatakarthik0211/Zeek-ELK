#!/bin/bash

# Wait for the VM to become available
sleep 30

# SSH into kmaster and run script2.sh
ssh -o StrictHostKeyChecking=no vagrant@192.168.33.11 'bash -s' < script2.sh

# Install Kubernetes components
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl

# Check available memory
free -m

# Pull Kubernetes container images using cri-dockerd
sudo kubeadm config images pull --cri-socket "unix:///var/run/cri-dockerd.sock" --kubernetes-version v1.28.1

# Initialize the Kubernetes master node
sudo kubeadm init --cri-socket "unix:///var/run/cri-dockerd.sock" --pod-network-cidr 10.244.0.0/16 --kubernetes-version 1.28.1 --node-name kmaster

# Set up kubeconfig for the current user
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Install Cilium CLI
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}

# Install Helm
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm

# Add Cilium Helm repository and install Cilium
helm repo add cilium https://helm.cilium.io/
helm install cilium cilium/cilium --version 1.14.1 --namespace kube-system

# Get the join command for worker nodes
join_command=$(kubeadm token create --print-join-command)
echo "Join command: $join_command" > /home/vagrant/shared/k8_join_token.txt


kubeadm join 192.168.121.22:6443 --token sm4vfb.9itglhbprex7i8a6 \
	--discovery-token-ca-cert-hash sha256:0bb0d670540154434bf42687a313066411579eaff919505185c4a3ad1e0e30ce  --cri-socket "unix:///var/run/cri-dockerd.sock"
