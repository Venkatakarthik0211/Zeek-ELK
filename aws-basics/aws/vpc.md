# Virtual Private Cloud (VPC)

- It is a **Region Specific**
- **Definition**:
  - A Virtual Private Cloud (VPC) is a virtual network dedicated to your AWS account. It is logically isolated from other virtual networks in the AWS cloud, providing you with control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways.

- **Minimum and Maximum by AWS**:
  - **Minimum VPC size**: /28 (16 IP addresses)
  - **Maximum VPC size**: /16 (65,536 IP addresses)

- **Differences between IPv4 and IPv6**:
  - **IPv4**:
    - 32-bit address space
    - Provides approximately 4.3 billion addresses
    - Format: 192.0.2.1
  - **IPv6**:
    - 128-bit address space
    - Provides approximately 340 undecillion addresses
    - Format: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

- **Why IPv6 addresses are neither public nor private**:
  - IPv6 addresses do not have the concept of public and private addresses like IPv4. Instead, IPv6 uses a different addressing architecture, including link-local, unique local, and global unicast addresses. This design provides a vast number of unique IP addresses, reducing the need for NAT (Network Address Translation) and simplifying routing.

- **DNS Hostname Option**:
  - This option enables or disables the assignment of DNS hostnames to instances launched in the VPC. If enabled, instances receive DNS hostnames that can be used for communication within the VPC.

- **DNS Resolution Option**:
  - This option enables or disables DNS resolution within the VPC. When enabled, instances in the VPC can use the Amazon-provided DNS server to resolve public DNS hostnames to IP addresses. This allows for easy access to external resources via domain names.

## VPC Subnets

- These are **AZ resillient**
- A subnetwork of VPC in a particular AZ (It will be only **1AZ = 1 subnet&**)
- By defualt it can subnet with others, IP Ranges should not **overlap**
- Reserved IP Address: (10.16.17.0 - 10.16.17.255)
1) Network Address is unusable - 10.16.17.0
2) Network VPC Router - 10.16.17.1
3) Reserved DNS for VPC - 10.16.17.2
4) Reserved for Future - 10.16.17.3
5) Broadcast Address - 10.16.17.255 

## Network Access Control Lists (NACL)

- **Stateless**: Request and response are seen as different.
- Only impacts data crossing the subnet boundary.
- NACLs can explicitly **ALLOW** and **DENY** traffic.
- Operates on IPs/CIDR blocks, ports, and protocols – no logical resources.
- NACLs cannot be assigned to AWS resources – only subnets.
- Use together with Security Groups to add explicit DENY rules for bad IPs/nets.
- Each subnet can have one NACL (default or custom).
- A NACL can be associated with many subnets.

## Differences between NACL and Security Groups

| Feature                         | NACL                                               | Security Group                                      |
|---------------------------------|----------------------------------------------------|-----------------------------------------------------|
| **State**                       | Stateless (evaluates requests and responses separately) | Stateful (remembers previous decisions)              |
| **Rules**                       | Supports both Allow and Deny rules                 | Supports only Allow rules                            |
| **Association**                 | Associated with subnets                            | Associated with instances                            |
| **Scope**                       | Operates at the subnet level                       | Operates at the instance level                       |
| **Evaluation Order**            | Rules are evaluated in order (numbered)            | All rules are evaluated collectively                  |
| **Default Behavior**            | Automatically applies to all subnets in a VPC      | Must be explicitly assigned to instances              |
