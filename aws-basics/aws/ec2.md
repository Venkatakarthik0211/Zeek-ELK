## EC2
Amazon EC2 (Elastic Compute Cloud) provides scalable virtual servers in the cloud, allowing users to run applications on a virtual machine without the need for physical hardware. EC2 instances can be dynamically resized to meet changing demands, offering flexible and cost-effective computing resources.

### Shared Hosts
Shared hosting is a web hosting service where multiple websites share the same physical server and resources. This cost-effective solution is ideal for smaller websites and startups, but it may lead to performance issues if one site consumes excessive resources.

### Dedicated Hosts
Dedicated hosting involves a single tenant server exclusively used by one organization, providing full control over server resources and configurations. This ensures higher performance, security, and compliance, making it suitable for businesses with specific needs and higher traffic volumes.

### Instance Store
Instance Store provides temporary block-level storage for Amazon EC2 instances, physically attached to the host machine. It offers high I/O performance but data persists only during the instance's lifetime, making it suitable for temporary data that is replicated or backed up elsewhere.

- **You can't attach instance store volumes after launch.**
- **The data on an instance store volume persists even if the instance is rebooted however not on hibernated/terminated. Copy the data to EBS for persisting the volume or an instance-store backed by linux AMI(Not on windows AMI & Only certain storgae types can be used)**

## EC2 Instance types
- Raw: CPU, Memory, local storage, Type
- Resource ratios(Ex:nStorgae vs I/O)
- Storage and Network Bandwith(For example: When using EBS)
- Based on System Architecture, OS on client's requirements
- Additionally capabilities such GPU, FPGA etc. 
- **EC2 Categories:**
   1) General purpose
   2) Compute Optimized(Great for training models. Gaming)
   3) Memory Optimized(For in-memory databases)
   4) Accelerated Computing(Additional capabilities)
   5) Storgae Optimized(Great for Data Scientists)
- **Table for instance types**
#### EC2 Instance Types

| Categories             | Type            | Details / Notes                                                                                 |
|------------------------|-----------------|------------------------------------------------------------------------------------------------|
| **General Purpose**    | A1, M6g         | Graviton (A1) Graviton 2 (M6g) ARM based processors. Efficient.                                 |
|                        | T3, T3a         | Burst Pool - Cheaper assuming nominal low levels of usage, with occasional Peaks.               |
|                        | M5, M5a, M5n    | Steady state workload alternative to T3/3a - Intel / AMD Architecture.                          |
| **Compute Optimized**  | C5, C5n         | Media encoding, Scientific Modelling, Gaming Servers, General Machine learning.                |
| **Memory Optimized**   | R5, R5a         | Real time analytics, in-memory caches, certain DB applications (in-memory operations).          |
|                        | X1, X1e         | Large scale in-memory applications .. lowest $ per GiB memory in AWS.                           |
|                        | High Memory (u-xtbl1) | Highest memory of all AWS instances.                                                             |
| **Accelerated Computing** | z1d         | Large memory and CPU - with directly attached NVMe.                                             |
|                        | P3              | GPU instances (Tesla v100 GPUs) - parallel processing & machine learning.                       |
|                        | G4              | GPU Instances (NVIDIA T4 Tensor) - Machine learning inference and Graphics Intensive.           |
|                        | F1              | Field Programmable Gate Arrays (FPGA) - Genomics, Financial Analysis, Big Data.                 |
|                        | Inf1            | Machine Learning - recommendation, forecasting, analysis, voice, conversation.                  |
| **Storage Optimized**  | I3/I3en         | Local high performance SSD (NVMe) - NoSQL Databases, warehousing, analytics.                    |
|                        | D2              | Dense Storage (HDD) - data warehousing, HADOOP, Distributed File Systems, Data processing - lowest price disk throughput. |
|                        | H1              | High Throughput, balance CPU/Mem. HDFS, MAPR-FS, File systems, Apache Kafka, Big data.         |

## EC2 Storgae

- Direct storage in AWS refers to instance store volumes, which are physically attached to the host machine and provide high-performance temporary block storage.

- Network storage in AWS includes services like Amazon EBS (Elastic Block Store) and Amazon EFS (Elastic File System), offering persistent block and file storage over a network.

- Ephemeral storage refers to instance store volumes that provide temporary storage for an EC2 instance, with data persisting only during the instance's lifetime.

- Permanent storage in AWS includes services like Amazon S3 (Simple Storage Service) and Amazon EBS, offering durable and persistent storage for data that needs to be retained over long periods.

- **Since EBS is AZ-specific, cross AZ attachment of EBS Volumes are not possible, to perform this, copy the snapshot of S3, then it can be attached in different AZ/Region** 
## Notes

1) EC2 has two storage options data network/EBS
2) EC2 & EBS are **AZ-specific** servicexs 
3) EC2 is good when: 
   - OS+Application based compute or long run compute 
   - Server side applications are good
   - Based on the load(Burst or steady)
   - If the application is monolithic
   - Migration or Disaster Recovery enviroment setups
4) I/O(Block size) * IOPS = Throughput (**Storage Performance**)

## Summary of GP2(General Purpose EBS) IOPS Calculations

- **Volume Sizes and Baseline Performance:**
  - **Volumes 1 GB to 16 TB:** Baseline performance is up to 16,000 IO credits per second.
  - **Volumes Larger than 1,000 GB:** Baseline is above burst performance, always achieving baseline without using the credit system.

- **IO Credit System:**
  - **IO Credit:** 1 IO credit is equivalent to 16 KB. 
  - **Baseline Performance:** For volumes, the bucket fills with 3 IO credits per second per GB of volume size beyond the initial 100 minimum IO credits per second.
  
- **Bucket Fill and Burst Capacity:**
  - **Minimum Bucket Fill Rate:** Every volume gets a minimum of 100 IO credits per second regardless of the volume size.
  - **Bucket Capacity:** Each volume has an IO credit bucket with a capacity of 5.4 million IO credits.
  - **Filling Rate:** The bucket fills at the rate of baseline performance.
  - **Burst Performance:** Volumes can burst up to 3,000 IOPS by depleting the bucket, utilizing the IO credits.

- **Initial Credits:**
  - All volumes receive an initial 5.4 million IO credits, enabling them to perform at 3,000 IOPS for 30 minutes, which is beneficial for boots and initial workloads.

## Comparison of gp3 and gp2 Volume Types

| Volume Type    | gp3                            | gp2                            |
|----------------|--------------------------------|--------------------------------|
| **Volume Size**| 1 GiB – 16 TiB                 | 1 GiB – 16 TiB                 |
| **Baseline IOPS**| 3000                          | 3 IOPS/GiB (minimum 100 IOPS) to a maximum of 16,000 IOPS <br> Volumes smaller than 1 TiB can also burst up to 3,000 IOPS. |
| **Max IOPS/Volume**| 16,000                       | 16,000                         |
| **Baseline Throughput**| 125 MiB/s                | Throughput limit is between 128 MiB/s and 250 MiB/s, depending on the volume size. |
| **Max Throughput/Volume**| 1,000 MiB/s              | 250 MiB/s                      |
| **Price**       | $0.08/GiB-month <br> 3,000 IOPS free and <br> $0.005/provisioned IOPS-month over 3,000; <br> 125 MiB/s free and <br> $0.04/provisioned MiB/s-month over 125MiB/s | $0.10/GiB-month                |

## **Instance Store vs EBS**

- **Cheap**: 
  - ST1 or SC1
- **Throughput (streaming)**: 
  - ST1
- **Boot**: 
  - NOT ST1 or SC1
- **GP2/3**: 
  - Up to 16,000 IOPS
- **IO1/2**: 
  - Up to 64,000 IOPS (*256,000)
- **RAID0 + EBS**: 
  - Up to 260,000 IOPS (io1/2-BE/GP2/3)
- **More than 260,000 IOPS**: 
  - Instance Store
