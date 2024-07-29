# **Relational Database(RDS)**

## Differences between RDB and non-RDB

**Relational Databases:**

- Relational databases organize data into tables with rows and columns.
- They use a structured query language (SQL) to interact with the data.
- Key components of a relational database include:
    - Tables: These are the main structures that hold the data. Each table consists of rows (records) and columns (fields) that define the data structure.
    - Relationships: Relational databases establish relationships between tables using keys, such as primary keys and foreign keys. These relationships ensure data integrity and enable efficient data retrieval.
    - ACID properties: Relational databases adhere to ACID (Atomicity, Consistency, Isolation, Durability) properties, which ensure data consistency and reliability.
    - Normalization: Relational databases follow normalization techniques to eliminate data redundancy and maintain data integrity.

**Non-Relational Databases:**

- Non-relational databases, also known as NoSQL databases, store and retrieve data in a flexible, schema-less manner.
- They are designed to handle large amounts of unstructured or semi-structured data.
- Key components of a non-relational database include:
    - Collections or Documents: Instead of tables, non-relational databases use collections or documents to store data. A collection is a group of documents, and each document is a set of key-value pairs or other data structures.
    - No fixed schema: Non-relational databases do not enforce a fixed schema, allowing for more flexibility in data storage and retrieval.
    - Scalability: Non-relational databases are designed to scale horizontally, meaning they can handle large amounts of data by distributing it across multiple servers.
    - CAP theorem: Non-relational databases often prioritize availability and partition tolerance over consistency, as per the CAP theorem. This means that in certain scenarios, data consistency may be sacrificed for high availability or fault tolerance.

## Why you will need a RDS on EC2 Instance
- OS-Level Database.
- SuperPrivilages(Root) permissions for a database.
- Based on client demands or the different provider where aws dont provide
- Specific OS/DB version where aws doesnt provide

## Why we shouldn't
- Administration Overhead(Such as Upgrading, Patching, Disaster Management)
- Running EC2 on single AZ & Can't rapidly scale a ec1 instance where rds instance does.
- Replication concepts are not applicable in ec2 instance, where advanced features matters.

- RDS Instances use **Subnet Groups**
- RDS Instances can have **Multiple Databases** which has **Dedicated EBS Storage**
- RDS Instances can provision **Synchronous Replicas** in Subnet Groups. 
- **Read Replicas** use **Async Replication** which means the replica can be in **Same Region** or in **Different Region**

## Multi AZ 

```plaintext
                On-Premises
                    |
                    v
                Database CNAME
                    |
                    v
                +-----------------------------+
                |         us-east-1           |
                | +---------+   +---------+   |
                | |   AZA   |   |   AZB   |   |
                | | +-----+ |   | +-----+ |   |
                | | |     | |   | |     | |   |
                | | |Primary |   |Standby| |   |
                | | |     |<---->|     | |   |
                | | |     | |   | |     | |   |
                | | +-----+ |   | +-----+ |   |
                | +----|----+   +----|----+   |
                |      |             |        |
                |      v             v        |
                |    +-----+       +-----+    |
                |    | S3  |       | S3  |    |
                |    +-----+       +-----+    |
                |                             |
                +-----------------------------+
```

### Summary of the Architecture

This architecture illustrates a highly available and resilient database setup in the AWS cloud environment (specifically in the us-east-1 region). Here's a step-by-step explanation of how it works:

#### On-Premises to AWS Connection

- The setup starts with an on-premises system that connects to the database in AWS via a database CNAME. This CNAME resolves to the primary database endpoint in AWS.

#### VPC and Subnets

- The architecture is deployed within a Virtual Private Cloud (VPC) in the AWS us-east-1 region.
- It spans multiple Availability Zones (AZs): AZA, AZB, and AZC, ensuring high availability.

#### Primary and Standby Databases

- The primary database is located in AZA.
- A synchronous replication mechanism is set up between the primary database in AZA and a standby database in AZB. This ensures that the standby database is an exact replica of the primary database, providing immediate failover capabilities in case of any issues with the primary database.

#### Backups and Snapshots

- Regular backups and snapshots of the databases are taken and stored in Amazon S3 buckets. These backups are stored across multiple AZs (AZA, AZB, and AZC) to ensure data durability and availability.
- This mechanism ensures that even in the event of a disaster, the data can be restored from the backups stored in S3.

### Multi-AZ Cluster

Amazon RDS Multi-AZ deployments provide high availability and failover support for database instances. Understanding the different types of endpoints can help you connect to the database more effectively.

#### 1. **Cluster Endpoint**

The **Cluster Endpoint** is specific to Amazon Aurora, a MySQL- and PostgreSQL-compatible database engine. It provides a single address to connect to the primary instance of the cluster. This endpoint ensures that even during failovers, connections are routed to the current primary instance.

**Format:** `mydbcluster.cluster-identifier.cluster.region.rds.amazonaws.com`

**Usage:**
- Connects to the primary instance for both read and write operations.
- Ensures continuous access to the primary instance, even during failovers.

#### 2. **Instance Endpoint**

The **Instance Endpoint** is associated with a specific instance within a Multi-AZ deployment. Each instance in the cluster has its own unique endpoint, allowing direct connections to that particular instance. This can be useful for administrative tasks or troubleshooting and **GenerallY Not Recommended**

**Format:** `mydbinstance.cluster-identifier.instance-identifier.region.rds.amazonaws.com`

**Usage:**
- Connects directly to a specific database instance.
- Useful for administrative tasks or specific instance-level operations.

#### 3. **Reader Endpoint**

The **Reader Endpoint** is used to distribute read-only traffic across multiple read replicas in the cluster. It provides a single address for accessing any of the read replicas, which helps balance the load of read operations and improve scalability.

**Format:** `mydbcluster.cluster-identifier.cluster-ro.region.rds.amazonaws.com`

**Usage:**
- Directs read requests to available read replicas, distributing the load.
- Ideal for read-heavy applications to offload read traffic from the primary instance.

## 1. **Manual Snapshots**

**Manual Snapshots** are user-initiated backups of your RDS instance. They are taken on-demand and remain available until you explicitly delete them. These snapshots are ideal for creating backups before making significant changes to your database.

### Key Features:
- **User-Triggered:** You create manual snapshots manually through the AWS Management Console, CLI, or API.
- **Retention:** Snapshots remain available until you choose to delete them, allowing you to retain backups for as long as needed.
- **Restoration:** You can restore a new RDS instance from a manual snapshot, or use it to replace an existing instance.

### Use Cases:
- **Pre-Change Backup:** Take a snapshot before applying major changes or upgrades to ensure you have a recovery point.
- **Long-Term Retention:** Keep snapshots for long-term storage and compliance requirements.

## 2. **Automated Backups**

**Automated Backups** are managed by Amazon RDS and occur on a regular schedule. They are automatically created and retained for a specified period, which you can configure. This backup mechanism includes both daily snapshots and transaction logs.

### Key Features:
- **Automatic:** Backups are created automatically according to a predefined schedule.
- **Retention Period:** You can configure the retention period from 1 to 35 days. Older backups beyond this period are automatically deleted.
- **Point-in-Time Recovery:** You can restore your database to any specific point within the retention period, using transaction logs to recover data up to that point. (**Generally 5min Retention Period is used**)
- **Storage:** Automated backups are stored in Amazon S3 and are managed by RDS.
- Can replicate backups to **Another Region** (Not **Default** and **Charges Apply**)

### Use Cases:
- **Disaster Recovery:** Recover your database to a specific point in time in case of data loss or corruption.
- **Routine Protection:** Ensure continuous data protection without manual intervention.

## **RDS Restores**
- Restore creates a **New Instance**. **Replayed Transaction logs** and **SLOW TO RESTORE**

## **RDS Replicas**
- These are **Asynchronous Replicas**, where we get additional instances for **Scalling** avoiding to use standby in different AZ and Region.
- **Improves Recover Time**
- Read Replicas have **0 Recover Time** which is a best option for **Disaster Recovery**
- These are good for **Failover protection** but not **Data Corruption**
- These are **Globally Resillient**

## **RDS Security**
- Supports encryption **In Transit** and also **Supports KMS**
- Handled by **EBS**
- **Encryption can't be Removed**, Snapshots, logs, Storage and Replicas are **Encrypted**
- Integegrates with **CloudHSM** and **Transparent Data Encryption Databases**

### **RDS Security at Rest**

1. **Data Encryption Keys (DEKs) and Customer Master Keys (CMKs)**:
   - **KMS (Key Management Service)**:
     - KMS provides AWS or Customer Managed CMKs.
     - These CMKs are used to generate Data Encryption Keys (DEKs) for RDS.
   - **CloudHSM**:
     - With RDS Oracle, keys can be provided via CloudHSM, removing AWS from the chain of trust.

2. **Host Level Encryption and Decryption**:
   - **DEKs Loaded onto Hosts**:
     - DEKs are loaded onto the hosts as required to perform encryption and decryption.
   - **Encryption and Decryption by Host**:
     - Data is encrypted and decrypted by the host before it leaves the instance.

3. **Transparent Data Encryption (TDE)**:
   - **TDE is Native DB Engine Encryption**:
     - TDE encrypts data before it leaves the database instance.

4. **Data Flow and Encryption**:
   - **Data Path**:
     - Data flows from the database (e.g., Oracle, MySQL) through the host.
     - Encryption and decryption occur at the host level using the DEKs.
   - **EBS Volumes**:
     - Encrypted data is stored on EBS volumes.
   - **Snapshots**:
     - Snapshots of encrypted RDS instances are also encrypted using the same key.

## Aurora Provisioned

- Uses a **Cluster**, **Single Instance** amd **0+ Replicas**
- Uses **Cluster volume** which is a shared volume.
- Based on **High IOPS** and billed based on **Storage**
- **High Watermark** billing structure is used, and the storage can be **reused**
- Replicas can be added and deleted without **Storage Provisioning**

## Aurora Backup & Restore

- **Back Track** is the advanced options, where database is allowed for **In Place Rewinds**
- **Fast Clone** makes a **New Database** which get rids of copying the data manually.

## Aurora Serverless

- Uses **Aurora Cluster Units** which has a **MIN** and **MAX** Units, **Load** can be adjusted, **6 copies** Across AZs. 
- Billed based on **Duration - Seconds**
- Used on **New Application**, for **Variable Workloads** amd **Infreq Access**
- Mained on **Proxy Fleet** indirectly. 

## Aurora Global Database

- Uses **1 Standard** and **15 Replicas** in the region. During cross region replicaion, can have **16 Read Replicas per region only with NO STANDARD DB** with max of **5 Secondary Regions**
- Best suites for **Cross Region DR & Business Continuity** with **1s Replication**
- When Reqiored **Low Latency Database**

## RDS Proxy

- Used when required **Opening and Closing Connections**
- **Latency** is minimized where connections can be **Reused** (Ex: When using AWS Lambda)
- Long Term Connection Pool is mained with standard database.
- Establishes **Connections During FailOver**
- Can be used for **Long Running Applications** 
- **Auto Scalling**, **High Availability**, **Fully Managed** and **Only Accessible from VPC**
- Enforces **SSL/TLS** Connections.