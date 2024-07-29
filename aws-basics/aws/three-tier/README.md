# $${\color{blue}Application Architecture}$$  🏗️

## $${\color{green} Overview }$$🌟

This document describes the architecture of the deployed application, which is structured in a three-tier architecture model.

## $${\color{purple}Architecture Layers }$$ 🏢

### 1. Web Layer 🌐
- **Component**: EC2 Instance 🖥️
- **Description**: Hosts the Python application.

### 2. Application Layer 📁
- **Component**: EFS (Elastic File System) 📂
- **Description**: Stores the static content of the Python application in shared storage.

### 3. Database Layer 🗃️
- **Component**: RDS (Relational Database Service) 💾
- **Description**: Provides the database services for the application.

### Networking 🌍
- **VPC**: `10.16.0.0/16`

## $${\color{orange}Deployment Details}$$  🚀

- **Web Server**: Apache2 🌐
  - **Role**: Proxies the Python application.
- **Load Balancer**: Application Load Balancer 🔄
  - **Role**: Proxies the DNS for the Python web application.
- **Scaling**: Auto Scaling Group 📈
  - **Role**: Manages the scaling of EC2 instances.

## $${\color{red} Resources }$$ 🔗

- **Complete CloudFormation Template**: [cloudformation/rds+efs+lt.yaml](https://git.epam.com/nikhil_linga/aws_hyd_rd/-/blob/Venkata_Karthik_Main/aws/three-tier/cloudformation/rds%2Befs%2Blt.yaml)
- **Complete Launch Template Configuration**: [LT-UserData.sh](https://git.epam.com/nikhil_linga/aws_hyd_rd/-/blob/Venkata_Karthik_Main/aws/three-tier/cloudformation/LT-UserData.sh)

## $${\color{blue}Application Endpoint}$$  🌐

- **URL**: [http://p4l-lb-1122150119.us-east-1.elb.amazonaws.com/](http://p4l-lb-1122150119.us-east-1.elb.amazonaws.com/)
