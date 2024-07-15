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

## NAT Gateway

- Runs in public subnet, provides public access to private subnet (Only outbound). 
- NAT gateway uses elastic ip
- NAT gateway is used for **High Availability and AZ resillient** , for region resilliency we require **1 NAT gateway in each AZ**

## NAT Gateway vs NAT Instance

| Attribute           | NAT Gateway                                                                 | NAT Instance                                                                |
|---------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Availability**    | Highly available. NAT gateways in each Availability Zone are implemented with redundancy. Create a NAT gateway in each Availability Zone to ensure zone-independent architecture. | Use a script to manage failover between instances.                         |
| **Bandwidth**       | Can scale up to 45 Gbps.                                                    | Depends on the bandwidth of the instance type.                             |
| **Maintenance**     | Managed by AWS. You do not need to perform any maintenance.                 | Managed by you, for example, by installing software updates or operating system patches on the instance. |
| **Performance**     | Software is optimized for handling NAT traffic.                             | A generic Amazon Linux AMI that's configured to perform NAT.               |
| **Cost**            | Charged depending on the number of NAT gateways you use, duration of usage, and amount of data that you send through the NAT gateways. | Charged depending on the number of NAT instances that you use, duration of usage, and instance type and size. |
| **Type and size**   | Uniform offering; you don’t need to decide on the type or size.             | Choose a suitable instance type and size, according to your predicted workload. |

| Feature             | NAT Gateway                                                                 | NAT Instance                                                                |
|---------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Security groups** | Cannot be associated with a NAT gateway. You can associate security groups with your resources behind the NAT gateway to control inbound and outbound traffic. | Associate with your NAT instance and the resources behind your NAT instance to control inbound and outbound traffic. |
| **Network ACLs**    | Use a network ACL to control the traffic to and from the subnet in which your NAT gateway resides. | Use a network ACL to control the traffic to and from the subnet in which your NAT instance resides. |
| **Flow logs**       | Use flow logs to capture the traffic.                                       | Use flow logs to capture the traffic.                                       |
| **Port forwarding** | Not supported.                                                              | Manually customize the configuration to support port forwarding.           |
| **Bastion servers** | Not supported.                                                              | Use as a bastion server.                                                    |

`Note:` 
- To make NAT instance to work as NAT gateway we should *Disable Source/Destination checks* 
- NAT gateway doesn't work with IPv6 
- ::/0 + IGW gives bi directional connectivity 
- Egress only IGW works with only *IPv6 and outbound only*

## Gateway Endpoints

- It uses **Routing**
- Provide **private** access to s3 or dynamoDB, which are maintained by **Prefix List** added to a route table.
- It is **Highly Available across all AZ's in a Regions By default**
- **Endpoint Policy** can be written what can be accessed and what not! 
- Prevent **Leaky S3 Buckets** and make them private. 
- It is **Regional** But not **Cross Regional**
- These are not accessible from **Outside of VPC**

## Interface Endpoints

- It works primarly on **DNS**
- Provide **Private Access** for AWS Public Services
- Not Available for **DynamoDB**
- Not **Highly Available**, These are **ENI** for a AZ. For **Highly Available Architecture** we require a endpoint in different AZ. 
- Network Access Controlled via **SG**, Additionally with **Endpoint Policies**
- Only **TCP and IPv4** are supported.
- Interfaces uses **PrivateLink** (`Adviciable:` When **3rd Connection Required for VPC**)
- It has **Private, Zonal and Regional DNS** which are enabled by Default.

## VPC Peering

- It enables us to connect **TWO VPC** in **Direct Encrypted Network Line** only.
- `Public Hostnames` are converted to `private`.
- Works Everywhere(Cross/Same Region or AZ).
- **Same Region**, then One VPC SG can refer peer SG. 
- **Different Region**, we should refer private IP Addresses
- VPC is not **Transitive**. 
- **Routing Configuration** is Needed, SG's and NACL are filtered. 

## Border Gateway Protocol (BGP)

- **Autonomous System (AS)**: Routers controlled by one entity, forming a network in BGP.
- **ASN**: Autonomous System Numbers are unique and allocated by IANA (0-65535); 64512 - 65534 are private.
- **BGP Operates over tcp/179**: It uses TCP port 179, making it a reliable protocol.
- **Not automatic**: Peering in BGP is manually configured.
- **Path-vector protocol**: BGP exchanges the best path to a destination between peers, with the path known as ASPATH.
- **iBGP**: Internal BGP is used for routing within an AS.
- **eBGP**: External BGP is used for routing between ASes.

## Border Gateway Protocol (BGP) Working

        (Connectivity: ASN200 - ASN201 - ASN202)
              |                 |
              |                 |
              |                 |
              --Satellite Link---

- **AS Path**: BGP exchanges the shortest ASPATH between peers. In this example, Brisbane (ASN 200) prefers the satellite link to Alice Springs (ASN 202) due to a shorter ASPATH, even though the fiber link would provide better performance.

- **AS Path Prepending**: This technique can be used to make a path look artificially longer. This makes other paths more preferable, such as choosing the fiber link over the satellite link.

- **Routing Table**: 
  - **Destination**: The network address of the destination.
  - **Next Hop**: The next hop IP address to reach the destination.
  - **ASPATH**: The AS path indicates the sequence of AS numbers a route has traversed.

- **Route Origin**: The `i` denotes the route is from an internal or locally connected network.

- **Link Types**:
  - **1 Gbps Fiber**: Represented by a red solid line.
  - **5 Mbps Satellite**: Represented by an orange dotted line.

- **Example Routes**:
  - **10.16.0.0/16**: Next hop 0.0.0.0, ASPATH `i`.
  - **10.17.0.0/16**: Next hop 10.17.0.1, ASPATH `201,i`.
  - **10.18.0.0/16**: Next hop 10.18.0.1, ASPATH `202,i`.
  - **10.16.0.0/16**: Next hop 10.17.0.1, ASPATH `201,200,i`.

- **BGP Decision Making**: 
  - Brisbane (ASN 200) routes traffic to Alice Springs (ASN 202) using the satellite link as the ASPATH is shorter.
  - AS Path Prepending can be used to prefer the fiber link by making the satellite path appear longer.

## AWS Site-to-Site VPN

- **Logical Connection**: Establishes a secure connection between a VPC and an on-premises network over the public internet using IPSec encryption.
- **Full HA**: Achieves full high availability if designed and implemented correctly.
- **Quick Provisioning**: The setup process is swift, typically taking less than an hour.
- **Virtual Private Gateway (VGW)**: An endpoint on the VPC side that manages the VPN connections.
- **Customer Gateway (CGW)**: Represents the on-premises gateway device or software application that you use to connect your network to the AWS VPN.
- **VPN Connection**: The link established between the VGW and the CGW, allowing secure communication over the internet.
## AWS Site-to-Site VPN Infrastructure

```plaintext
                    On-Premises Network
                           |
                        CGW (Customer Gateway)
                           |
                -------------------------
                |       Public Internet     |
                -------------------------
                           |
                       VPN Endpoints
                           |
                       VGW (Virtual Private Gateway) - Highly Available Across AZ
                           |
                       AWS VPC Router
                           |
                        AWS VPC
```

- Since it's only one Router Configured at CGW, Combining the overall Solution Makes it `Partially HA`
- We can Add routers at on-prem, adding the CGW, makes it `Higly Available Solution`

## Staic vs Dynamic VPN(BGP) 

| Feature | Static VPN | Dynamic VPN |
|---------|------------|-------------|
| **Route Configuration** | Routes for remote side added to route tables as static routes. | Border Gateway Protocol (BGP) is configured on both the customer and AWS side using Autonomous System Numbers (ASN). |
| **Route Propagation** | No automatic route propagation; routes must be manually added to route tables. | Route propagation (if enabled) means routes are added to route tables automatically. |
| **Configuration of Remote Networks** | Networks for the remote side are statically configured on the VPN connection. | Networks are exchanged via BGP. |
| **Load Balancing and Failover** | No load balancing and multi-connection failover. | Multiple VPN connections provide high availability (HA) and traffic distribution. |
| **Example CIDR** | - | 192.168.10.0/24 |

### Summary:
- **Static VPN** requires manual configuration of routes and does not support automatic route propagation or failover.
- **Dynamic VPN** leverages BGP for automatic route exchange and supports multiple connections for better availability and traffic management.

## VPN Limitations

- **Speed Limit** in AWS Side - 1.25Gbps (Should consider, soft limits of customer side)
- **Latency** is inconstent public internet. 
- **Setup Time** are quick to setup (Hrs, All Software Configurations)
- **Can be Backup** to DX. 
- **Can work with DX** for HA and reducing the Latency issues. 

## AWS DX 

```plaintext
AWS Region (ap-southeast-2)
┌─────────────────────────────────────────┐
│                                         │
│  ┌──────────┐  ┌───────────────┐        │
│  │   EC2    │  │      RDS      │        │
│  └──────────┘  └───────────────┘        │
│      VPC                        │        │
│  ┌─────────────────────────────────┐   │
│  │ Virtual Private Gateway (VGW)   │   │
│  └─────────────────────────────────┘   │
│     │                                   │
└─────┼───────────────────────────────────┘
      │
Private VIF
      │
      │
      ▼
AWS DX Location
┌─────────────────────────────────────────┐
│                                         │
│ ┌───────────────┐   ┌───────────────┐   │
│ │ AWS DX Router │   │ AWS DX Router │   │
│ │     Port      │   │     Port      │   │
│ └───────────────┘   └───────────────┘   │
│    DX Endpoints   │   │                  │
│  ┌───────────────────────────────────┐   │
│  │ Cross Connect AWS Port to Customer│   │
│  │ or Partner Port Link              │   │
│  └───────────────────────────────────┘   │
│   │                                     │
└───┼─────────────────────────────────────┘
    │
    │
    ▼
Customer or Comms Partner Cage
┌─────────────────────────────────────────┐
│ ┌───────────────┐   ┌───────────────┐   │
│ │ Customer/Partner DX Router         │   │
│ │ Optional Infrastructure            │   │
│ └───────────────┘   └───────────────┘   │
│     │                                   │
└─────┼───────────────────────────────────┘
      │
      │
      ▼
Business Premises
┌─────────────────────────────────────────┐
│  Customer Premises Router/Firewall      │
│      │                                   │
│  ┌───────────────────────────────────┐   │
│  │ VLAN1 Private                     │   │
│  │ VLAN2 Public                      │   │
│  └───────────────────────────────────┘   │
│     │                                   │
│  ┌───────────────┐  ┌───────────────┐   │
│  │     User1     │  │     User2     │   │
│  └───────────────┘  └───────────────┘   │
│      │                                   │
└──────┘───────────────────────────────────┘
```


