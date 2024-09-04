# AWS Service Categories

## Index
- [AWS compute services](#aws-compute-services)
- [AWS container services](#aws-container-services)
- [AWS storage services](#aws-storage-services)
- [AWS database services](#aws-database-services)
- [AWS deployment services](#aws-deployment-services)
- [AWS monitoring services](#aws-monitoring-services)
- [AWS audit and compliance services](#aws-audit-and-compliance-services)
- [AWS networking and content delivery services](#aws-networking-and-content-delivery-services)
- [AWS application integration services](#aws-application-integration-services)
- [AWS security services](#aws-security-services)
- [AWS management and governance services](#aws-management-and-governance-services)
- [AWS identity services](#aws-identity-services)
- [AWS machine learning services](#aws-machine-learning-services)
- [AWS transfer and migration services](#aws-transfer-and-migration-services)
- [AWS analytics services](#aws-analytics-services)

## <a id="aws-compute-services"></a> $${\color{blue}AWS\ compute\ services}$$

<!DOCTYPE html>
<html>
<body>

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Compute/64/Arch_Amazon-EC2_64.svg" alt="Amazon EC2">
    </td>
    <td class="content">
      <h2>Amazon EC2</h2>
        <ul>
        <li>Amazon EC2 is a computing service that runs virtual servers in the cloud.</li>
        <li>It allows you to launch Linux or Windows virtual machines to host your application and manage them remotely from anywhere in the world.</li>
        <li>Amazon EC2 is categorized as an Infrastructure as a Service (IaaS) and acts as a basic building block for cloud infrastructure.</li>
        <li>Amazon EC2 is a building block for AWS, used by some AWS services for processing, database hosting, and serverless computing.</li>
        <li>AWS and users share responsibility in managing EC2 virtual machines:</li>
            <ul>
            <li>AWS manages data centers, physical facilities, hardware components, the host operating system, and the virtualization layer.</li>
            <li>Users are responsible for the guest operating system, applying OS patches, setting up security access controls, and managing data.</li>
            </ul>
        <li>EC2's elasticity allows it to be changed, resized, or customized at any point in time.</li>
        <li>EC2 can automatically scale, increasing or decreasing the number of instances based on incoming traffic.</li>
        <li>The term "C2" in Amazon EC2 refers to the two C's of "Compute Cloud."</li>
        <li>Amazon EC2 integrates with various AWS services and features.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Compute/64/Arch_AWS-Lambda_64.svg" alt="AWS Lambda">
    </td>
    <td class="content">
      <h2>AWS Lambda</h2>
        <ul>
        <li>AWS Lambda is a serverless computing service that allows you to run code, functions, or entire applications without managing servers.</li>
        <li>You only pay for the compute time that you actually consume.</li>
        <li>Although serverless computing uses servers, all server management, scaling, and troubleshooting are handled by AWS.</li>
        <li>Uploaded code in AWS Lambda is called a Lambda function.</li>
        <li>Lambda functions can perform custom tasks that you control or program.</li>
        <li>Lambda functions are highly scalable, supporting thousands of requests in seconds.</li>
        <li>AWS Lambda provides high availability without additional effort on your part.</li>
        <li>It is a fully managed service, meaning AWS manages the underlying servers, and you cannot access or manage these servers.</li>
        <li>AWS Lambda supports multiple programming languages including Java, Go, Ruby, Node.js, Python, and others through the use of runtimes.</li>
        <li>These runtimes are powered by Amazon Linux EC2 and other servers, which are managed by AWS.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Compute/64/Arch_AWS-Elastic-Beanstalk_64.svg" alt="AWS Elastic Beanstalk">
    </td>
    <td class="content">
      <h2>AWS Elastic Beanstalk</h2>
        <ul>
            <li>AWS Elastic Beanstalk automates the deployment, management, scaling, and monitoring of custom applications in AWS.</li>
            <li>You can upload your application, and Elastic Beanstalk handles:
                <ul>
                    <li>Capacity provisioning</li>
                    <li>Load balancing</li>
                    <li>Database management</li>
                    <li>Auto scaling</li>
                    <li>Health monitoring</li>
                </ul>
            </li>
            <li>Elastic Beanstalk allows developers to:
                <ul>
                    <li>Retain full control over the underlying EC2 instances.</li>
                    <li>Access these servers at any time.</li>
                </ul>
            </li>
            <li>This is in contrast to fully managed services like AWS Lambda, where you don’t have direct server access.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Compute/64/Arch_AWS-Batch_64.svg" alt="AWS Batch">
    </td>
    <td class="content">
      <h2>AWS Batch</h2>
        <ul>
        <li>AWS Batch is a service for running batch computing workloads on the AWS Cloud.</li>
        <li>The service dynamically provisions the optimal quantity and type of compute resources based on the volume and specific resource requirements.</li>
        <li>With AWS Batch, there's no need to install or manage batch computing software or server clusters.</li>
        <li>The service handles planning, scheduling, and execution of batch computing workloads using Amazon EC2 instances.</li>
        <li>This allows users to focus on analyzing results and solving problems rather than managing infrastructure.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Compute/64/Arch_Amazon-Lightsail_64.svg" alt="Amazon LightSail">
    </td>
    <td class="content">
      <h2>Amazon LightSail</h2>
        <ul>
        <li>Amazon LightSail is a virtual private server solution in AWS.</li>
        <li>You can deploy a virtual machine for a low and predictable monthly price.</li>
        <li>The service provides everything needed to launch projects quickly.</li>
        <li>It has its own LightSail console, separate from the regular AWS Management console.</li>
        <li>Aside from virtual machines, you can also launch different resources using Amazon LightSail, including:</li>
        <ul>
            <li>Databases</li>
            <li>Load balancers</li>
            <li>DNS records</li>
            <li>And more</li>
        </ul>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Compute/64/Arch_AWS-Outposts_64.svg" alt="AWS Outposts">
    </td>
    <td class="content">
      <h2>AWS Outposts</h2>
        <ul>
            <li>AWS Outposts is a hybrid service that allows you to run AWS services, like Amazon EC2, in your on-premises data center.</li>
            <li>AWS Outposts is a piece of physical equipment in an industry-standard server rack.</li>
            <li>The outpost rack stands about six feet and six inches tall, similar to the average height of a regular NBA player in the U.S.</li>
            <li>The outpost rack is two feet wide and four feet deep.</li>
            <li>The server rack contains hosts, switches, another patch panel, and other components, similar to what AWS uses for its public Amazon EC2 servers that power your applications in the cloud.</li>
            <li>AWS delivers the outpost rack to your preferred physical site fully assembled.</li>
            <li>You just need to plug it in, configure it, and you're ready to go.</li>
        </ul>
    </td>
  </tr>
</table>


## <a id="aws-container-services"></a> $${\color{green}AWS\ container\ services}$$

<html>
<body>

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Containers/64/Arch_Amazon-Elastic-Container-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS ECS</h2>
        <ul>
        <li>Amazon Elastic Container Service (Amazon ECS) is a highly scalable, high-performance container orchestration service that supports Docker containers.</li>
        <li>Amazon ECS allows you to easily install, operate, and scale your cluster management infrastructure in AWS.</li>
        <li>Amazon ECS eliminates the need to install and operate your own container orchestration software.</li>
        <li>Amazon ECS helps manage the cluster of servers that power your containers.</li>
        <li>Containers in Amazon ECS are defined in a task definition, which you use to run individual tasks or group together as a service.</li>
        <li>You can run ECS tasks and services using:
            <ul>
            <li>A serverless compute engine called AWS Fargate.</li>
            <li>Amazon EC2 instances that you can fully access and manage.</li>
            </ul>
        </li>
        <li>For security, you can specify an IAM role that can be used by the containers in an ECS task.</li>
        <li>You can build Docker images and store them in Amazon Elastic Container Registry (ECR).</li>
        <li>Just like Amazon EC2, you can integrate Amazon ECS with a wide range of AWS services.</li>
        <li>For storage, you can use Amazon EFS or Amazon FSx to store your data.</li>
        <li>You can design your ECS tasks to communicate using:
            <ul>
            <li>Amazon SQS queue</li>
            <li>Amazon Kinesis data stream</li>
            <li>Any other integration service</li>
            </ul>
        </li>
        <li>You can use Amazon ECS service auto scaling to automatically increase or decrease the number of your ECS tasks.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Containers/64/Arch_Amazon-Elastic-Kubernetes-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS EKS</h2>
        <ul>
            <li>Amazon Elastic Kubernetes Service (EKS) is a fully-managed Kubernetes service.</li>
            <li>Kubernetes is a portable, extensible, and open-source platform for managing containerized workloads and services.</li>
            <li>Kubernetes lets you orchestrate a cluster of virtual machines (VMs).</li>
            <li>Kubernetes schedules containers to run on VMs based on their available resources and the specified requirements of each container.</li>
            <li>Containers are grouped into pods, which are the basic operational unit in Kubernetes.</li>
            <li>Amazon EKS allows you to run pods on either AWS Fargate or Amazon EC2.</li>
            <li>Unlike Docker, Kubernetes containers are not tightly coupled with AWS, making them easily movable and migratable.</li>
            <li>Kubernetes containers can be moved to on-premises networks or other cloud service providers like Microsoft Azure or Google Cloud Platform.</li>
            <li>Kubernetes is considered cloud-agnostic.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Containers/64/Arch_AWS-Fargate_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Fargate</h2>
        <ul>
            <li>AWS Fargate is a serverless compute engine for containers that works with both Amazon ECS and Amazon EKS.</li>
            <li>Fargate allows you to focus on building your applications without worrying about server provisioning, scaling, and management.</li>
            <li>It provides a cost-effective solution, as you only have to pay for the resources required to run your containers.</li>
            <li>Fargate avoids over-provisioning, where you launch a lot of servers that you don't even use in the long run.</li>
            <li>Fargate runs each ECS task or Kubernetes pod in its own kernel, providing isolated compute environments for tasks and pods.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Containers/64/Arch_Amazon-Elastic-Container-Registry_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS ECR</h2>
        <ul>
        <li>Amazon Elastic Container Registry (ECR) is a fully-managed Docker container registry.</li>
        <li>Allows you to store, manage, and deploy Docker container images.</li>
        <li>Integrated with Amazon ECS to simplify your development to production workflow.</li>
        <li>Hosts your Docker images in a highly available and scalable architecture.</li>
        <li>Enables secure and reliable deployment of containers to your apps.</li>
        <li>Uses IAM to provide resource-level control of each repository.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Resource-Icons_07302021/Res_Containers/Res_48_Light/Res_Amazon-Elastic-Container-Service_Copilot-CLI_48_Light.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS App2Container</h2>
        <ul>
        <li>AWS App2Container (A2C) is a command-line tool for modernizing .NET and Java applications into containerized applications.</li>
        <li>A2C analyzes and builds an inventory of all applications running in virtual machines, on-premises, or in AWS.</li>
        <li>Users can choose the application they want to containerize, and A2C will package the application artifact and dependencies into container images.</li>
        <li>A2C configures the network ports.</li>
        <li>A2C generates the ECS task and Kubernetes pod definitions.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Resource-Icons_07302021/Res_Containers/Res_48_Light/Res_Amazon-Elastic-Container-Service_Copilot-CLI_48_Light.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Copilot</h2>
        <ul>
        <li>AWS Copilot is a command-line interface that enables you to quickly launch and easily manage containerized applications on AWS.</li>
        <li>Copilot automates each step in the deployment lifecycle of your containers, including:
            <ul>
            <li>Creating a task definition</li>
            <li>Creating a container cluster</li>
            <li>Pushing the images to a container registry</li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>
</table>

## <a id="aws-storage-services"></a> $${\color{orange}AWS\ storage\ services}$$

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Compute/64/Arch_Amazon-EC2_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS EC2 Instance Store</h2>
        <ul>
        <li>Amazon EC2 Instance Store and Amazon Elastic Block Store (Amazon EBS)</li>
        <li>Amazon EC2 Instance Store:
            <ul>
            <li>Provides temporary block-level storage for Amazon EC2 instances</li>
            <li>Ideal for ephemeral or temporary data storage</li>
            <li>Uses disks physically attached to the underlying host computer</li>
            <li>Thousands of data centers worldwide, each with hundreds of thousands of physical server racks</li>
            <li>One server can run a hypervisor that generates thousands of Amazon EC2 instances</li>
            <li>Storage device physically connected under one server rack</li>
            <li>Instance store can be a hard disk drive or a non-volatile memory express (NVMe) solid-state drive (SSD)</li>
            <li>Provides low latency access to data, unlike network-based file systems</li>
            <li>Used for storing temporary buffers, caches, or scratch data</li>
            <li>Data is deleted when the EC2 instance is stopped or terminated, similar to random access memory (RAM)</li>
            <li>Suitable for data replicated across a fleet of Amazon EC2 instances or a load-balanced pool of web servers</li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_Amazon-Elastic-Block-Store_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS EBS</h2>
        <ul>
            <li>Amazon Elastic Block Store (Amazon EBS) is a persistent block level storage service used for Amazon EC2 instances.</li>
            <li>Data in EBS is persistent, meaning it is not lost when instances are stopped, restarted, or terminated.</li>
            <li>EBS volumes can be mounted or attached to EC2 instances within the same availability zone.</li>
            <li>Data can be encrypted at rest using AWS Key Management Service (KMS).</li>
            <li>Two kinds of EBS volumes:
                <ul>
                    <li>Solid State Drive (SSD) - Suitable for workloads with frequent read-write operations, providing high IOPS.</li>
                    <li>Hard Disk Drive (HDD) - Offers high throughput (megabit per second performance).</li>
                </ul>
            </li>
            <li>Four types of EBS volumes:
                <ul>
                    <li>General Purpose SSD</li>
                    <li>Provisioned IOPS SSD</li>
                    <li>Throughput Optimized HDD</li>
                    <li>Cold HDD</li>
                </ul>
            </li>
            <li>EBS volumes typically attach to one EC2 instance, providing low latency access to data.</li>
            <li>SSD-based EBS volumes can be used as boot volumes for EC2 instances, unlike HDDs.</li>
            <li>EBS Multi-Attach feature allows attaching two or more provisioned IOPS EBS volumes to a single EC2 instance.</li>
            <li>Multi-Attach is only supported on provisioned IOPS volumes and requires Nitro-based EC2 instances.</li>
            <li>Multiple EC2 instances using the same provisioned IOPS EBS volume cannot concurrently modify or access the same file; use Amazon EFS for this functionality.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_Amazon-Simple-Storage-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS S3</h2>
        <ul>
        <li>Amazon Simple Storage Service (Amazon S3) is an object storage service in AWS.</li>
        <li>It is highly durable and scalable with many features.</li>
        <li>Data is stored in a resource called an Amazon S3 Bucket.</li>
        <li>Files uploaded to a bucket are considered objects.</li>
        <li>You can store large amounts of files, documents, videos, database backups, and snapshots.</li>
        <li>Accessing objects from an S3 bucket is done via a REST API call.</li>
        <li>Different storage classes available in Amazon S3:
            <ul>
            <li>S3 Standard: For frequently accessed data.</li>
            <li>S3 Intelligent Tiering: For data with changing or unknown access patterns.</li>
            <li>S3 Standard Infrequent Access: For long-lived yet less frequently accessed data.</li>
            <li>S3 One Zone Infrequent Access: For less frequently accessed data in a single availability zone.</li>
            <li>Amazon S3 Glacier: For low-cost long-term storage and data archiving.</li>
            <li>Amazon S3 Glacier Deep Archive: For even lower cost long-term storage.</li>
            </ul>
        </li>
        <li>Lifecycle Policy: Automatically transitions or moves data between storage classes.</li>
        <li>Security features:
            <ul>
            <li>Amazon S3 Access Control List (ACL): Secures access to S3 Buckets and objects.</li>
            <li>S3 Bucket Policy: Controls external access to the bucket.</li>
            <li>S3 Versioning: Prevents accidental data deletion.</li>
            <li>Multi-Factor Authentication (MFA): Provides additional security to prevent accidental data deletion.</li>
            </ul>
        </li>
        <li>Replication features:
            <ul>
            <li>Cross-Region Replication (CRR): Replicates objects to different AWS regions.</li>
            </ul>
        </li>
        <li>Data transfer features:
            <ul>
            <li>Amazon S3 Transfer Acceleration: Expedites data transfer.</li>
            <li>S3 Multipart Upload: Allows uploading large files in parts.</li>
            </ul>
        </li>
        <li>Amazon S3 Glacier is a storage class in Amazon S3 with its own web console and APIs.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_Amazon-Simple-Storage-Service-Glacier_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS S3 Glacier</h2>
        <ul>
        <li>Amazon S3 Glacier was previously known as Amazon Glacier and was separate from S3; the two services have since been merged into one.</li>
        <li>The service name "Glacier" is derived from the concept of cold, large masses of ice, reflecting its purpose for cold data storage.</li>
        <li>Cold data refers to data that is rarely accessed, while hot data is frequently accessed. This concept also applies to cold HDD volumes in Amazon EBS.</li>
        <li>Amazon S3 Glacier provides low-cost storage for data archiving and long-term backup, suitable for files that are rarely accessed and need to be archived for several years to meet regulatory requirements.</li>
        <li>Archive files are stored in a resource called Vaults.</li>
        <li>The Amazon S3 Glacier Deep Archive class is the cheapest storage type in AWS for data archived for seven to ten years.</li>
        <li>There is an additional fee for immediate retrieval of Glacier data.</li>
        <li>The storage class is only the cheapest if data is archived for many years, not for a few hours or days.</li>
        <li>Objects archived in S3 Glacier have a minimum storage duration of 90 days, and in S3 Glacier Deep Archive, 180 days.</li>
        <li>Deleting objects before the minimum storage duration incurs a prorated charge equal to the storage charge for the remaining days.</li>
        <li>If data is stored in Glacier for only 24 hours and then deleted, the charge is for the full 90 days.</li>
        <li>Similarly, deleting data in Glacier Deep Archive within a day incurs the charge for the entire 180 days.</li>
        <li>For temporary data, storing in S3 Standard class is cheaper than using Glacier.</li>
        <li>The disadvantage of Glacier is the retrieval time for archive data, similar to thawing frozen meat.</li>
        <li>Amazon Glacier offers three types of archive retrieval options: expedited, standard, and bulk.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_Amazon-Elastic-File-System_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS EFS</h2>
        <ul>
        <li>Amazon Elastic File System (Amazon EFS) is a scalable shared file storage solution.</li>
        <li>Provides a POSIX-compliant shared file system accessible by multiple Amazon Linux EC2 instances in different availability zones.</li>
        <li>Uses the Network File System (NFS) protocol.</li>
        <li>Must be mounted to Linux EC2 instances or on-premises servers like a regular network file share.</li>
        <li>Only supports Linux servers; Windows-based EC2 instances cannot use Amazon EFS.</li>
        <li>For shared Windows file systems, use Amazon FSX for Windows Server instead.</li>
        <li>Offers two storage classes:
            <ul>
            <li>Standard storage class: Best for active file system workloads.</li>
            <li>Infrequent Access storage class: Cost-optimized for infrequently accessed files.</li>
            </ul>
        </li>
        <li>Supports lifecycle policies to automatically move data from the standard class to the infrequent access storage class, similar to Amazon S3.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_Amazon-FSx-for-Lustre_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS FSx Lustre</h2>
        <ul>
        <li>Amazon FSX for Lustre and Amazon FSX for Windows Server are different services offered by AWS.</li>
        <li>Amazon FSX for Lustre:
            <ul>
            <li>Similar to Amazon EFS but specifically for Linux servers.</li>
            <li>Uses the open-source Lustre file system.</li>
            <li>Lustre is a parallel file system used for large-scale cluster computing.</li>
            <li>Derived from "Linux" and "cluster."</li>
            <li>Designed for high-performance computing, machine learning, and HPC applications.</li>
            <li>Supports high-performance parallel storage for frequently accessed hot data.</li>
            <li>Provides throughput of hundreds of gigabytes per second and millions of IOPS.</li>
            <li>Can be mounted to EC2 instances or containers.</li>
            <li>Supports integration with Amazon EKS clusters via the Container Storage Interface (CSI).</li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_Amazon-FSx-for-Windows-File-Server_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS FSx Windows File Server</h2>
        <ul>
            <li>Amazon FSX for Windows Server is a fully managed Microsoft Windows file server.</li>
            <li>Unlike Lustre, which is Linux-based, this service uses a fully native Windows file system.</li>
            <li>It integrates with various Microsoft-based technologies.</li>
            <li>File shares can be accessed using the Server Message Block (SMB) protocol.</li>
            <li>SMB is a protocol commonly used by Windows servers.</li>
            <li>Amazon FSX for Windows Server supports integration with Microsoft Active Directory for file system access provisioning.</li>
            <li>It can be used as shared file storage for applications such as:
                <ul>
                    <li>Microsoft SharePoint</li>
                    <li>Microsoft SQL Server Database</li>
                    <li>Windows containers</li>
                    <li>Any other Windows-based applications</li>
                </ul>
            </li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_AWS-Backup_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Backup</h2>
        <ul>
            <li><strong>AWS Backup</strong>: A fully managed backup service for automating server and database backups.</li>
            <li><strong>Default RDS Backup Retention</strong>: Automated backups of RDS databases have a default retention period of seven days.</li>
            <li><strong>Maximum RDS Backup Retention</strong>: The maximum retention period for RDS automated backups is 35 days.</li>
            <li><strong>Extended Retention with AWS Backup</strong>: Allows for daily snapshots with retention periods of 90 days, a year, or even longer.</li>
            <li><strong>Lifecycle Policy</strong>: Enables automatic movement of backups to cold storage.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src=https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_AWS-Storage-Gateway_64.svg"" alt="">
    </td>
    <td class="content">
      <h2>AWS Storage Gateway</h2>
        <ul>
        <li><strong>AWS Storage Gateway</strong>: A hybrid cloud storage service that connects on-premises data storage to AWS Cloud.</li>
        <li><strong>Gateway Types</strong>:
            <ul>
            <li><strong>File Gateway</strong>: 
                <ul>
                <li>Stores and retrieves objects in Amazon S3 using NFS and SMB protocols.</li>
                <li>Works with Microsoft Active Directory (hosted on-premises or in AWS).</li>
                <li>Access data using S3 APIs.</li>
                <li>Can use a hardware appliance hosted on-premises if virtualization is not available.</li>
                </ul>
            </li>
            <li><strong>Volume Gateway</strong>: 
                <ul>
                <li>Provides block storage to on-premises applications via iSCSI.</li>
                <li>Uses Amazon S3 to store data by taking point-in-time snapshots.</li>
                <li>Generates Amazon EBS snapshots for EC2 instances.</li>
                <li>Runs in two modes:
                    <ul>
                    <li><strong>Cache Mode</strong>: Stores primary data in Amazon S3 with local copies of frequently accessed data.</li>
                    <li><strong>Stored Mode</strong>: Stores the entire dataset on-premises and asynchronously backs up data to AWS.</li>
                    </ul>
                </li>
                </ul>
            </li>
            <li><strong>Tape Gateway</strong>: 
                <ul>
                <li>Cloud-based virtual tape library (VTL) using Amazon S3.</li>
                <li>Archive tapes can be stored in Amazon S3 Glacier or S3 Glacier Deep Archive.</li>
                <li>Connects to on-premises backup applications as iSCSI devices.</li>
                <li>Reduces cost by eliminating physical backup tapes while preserving existing backup applications and workflows.</li>
                </ul>
            </li>
            </ul>
        </li>
        <li><strong>Use Case</strong>: Suitable for building a hybrid cloud storage infrastructure with active data transfer to AWS. For total migration and decommissioning of on-premises storage, consider using AWS DataSync Service instead.</li>
        </ul>
    </td>
  </tr>

</table>

## <a id="aws-database-services"></a> $${\color{purple}AWS\ database\ services}$$

<table>
  <tr>
    <td class="image">
      <img src="" alt="">
    </td>
    <td class="content">
      <h2>Types of In-Build Databses</h2>
        <ol>
        <li>Relational Databases(RDS, Aurora)</li>
        <li>NoSQL Databases(DynamoDB, DocumentDB)</li>
        <li>In-Memory Databases(AWS ElastiCache - Redis, Memcached)</li>
        <li>Data Warehouses(RedShift)</li>
        <li>Other Database Types(AWS KeySpaces, AWS Neptune, AWS TimeStream, AWS QuantamLedger)</li>
        </ol>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-RDS_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS RDS</h2>
        <ul>
            <li>Managed relational database service by AWS</li>
            <li>AWS handles hardware provisioning, patching, backups, and maintenance</li>
            <li>Users have control over:
                <ul>
                <li>EC2 instance size</li>
                <li>Storage instance type</li>
                <li>Network access</li>
                <li>DB patch application timing during maintenance window</li>
                </ul>
            </li>
            <li>Supports various database engines:
                <ul>
                <li>Microsoft SQL Server</li>
                <li>MySQL</li>
                <li>MariaDB</li>
                <li>Postgres</li>
                <li>Oracle</li>
                <li>Aurora</li>
                <li>Others</li>
                </ul>
            </li>
            <li>Deployment options:
                <ul>
                <li><strong>Single-AZ:</strong> 
                    <ul>
                    <li>One DB instance in a single availability zone</li>
                    <li>Primary DB instance</li>
                    </ul>
                </li>
                <li><strong>Multi-AZ:</strong> 
                    <ul>
                    <li>Primary instance in one AZ</li>
                    <li>Standby instance in a different AZ within the same AWS region</li>
                    <li>Standby instance (standby replica) replicates data from the primary instance</li>
                    </ul>
                </li>
                </ul>
            </li>
            <li><strong>Read Replicas:</strong> 
                <ul>
                <li>Used to offload read requests from the primary DB instance</li>
                <li>Can be deployed in a different AWS region from the primary instance</li>
                </ul>
            </li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-Aurora_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Aurora</h2>
        <ul>
            <li>Aurora is both a database engine and a fully managed service owned by AWS.</li>
            <li>Compatible with both MySQL and PostgreSQL engines.</li>
            <li>Existing code, applications, and tools for MySQL and PostgreSQL can be used with Aurora with little or no change.</li>
            <li>Scales automatically, performs faster, and costs lower than other databases.</li>
            <li>Similar to Amazon RDS, but with additional features.</li>
            <li>Can automatically grow or scale storage as needed.</li>
            <li>Usually deployed as a database cluster.</li>
            <li>A cluster consists of:
                <ul>
                <li>A primary DB instance</li>
                <li>Multiple Aurora replicas or DB instances</li>
                </ul>
            </li>
            <li>Clusters have a single-master configuration by default:
                <ul>
                <li>Applications can only write data to a single master DB instance.</li>
                </ul>
            </li>
            <li>In a multi-master cluster, all DB instances have read and write capabilities.</li>
            <li>Suitable for applications with constantly changing data, such as online transaction processing (OLTP) applications.</li>
            <li>Example of an OLTP application: An e-commerce website that processes thousands of online transactions per hour.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-DynamoDB_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS DynamoDB</h2>
        <ul>
        <li>Amazon DynamoDB is a fully managed NoSQL database composed of tables, items, and attributes.</li>
        <li>Items and attributes in DynamoDB are equivalent to records and columns in a relational database like Amazon RDS.</li>
        <li>NoSQL databases, like DynamoDB, do not have a rigid schema or extensive table relationships.</li>
        <li>In a relational database, a change in a single column may cause issues or violations in table constraints.</li>
        <li>Two or more tables in a relational database have relationships, so changes in one table's schema can affect others.</li>
        <li>In DynamoDB, you can easily add, remove, or modify attributes without affecting other tables.</li>
        <li>DynamoDB tables do not have relationships with other DynamoDB tables.</li>
        <li>There is no need to create table joins, foreign keys, or complex table relationships in DynamoDB.</li>
        <li>You can safely update the schema at any time in DynamoDB.</li>
        <li>DynamoDB allows you to store complex hierarchical data within a single item and store related items in the same table.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-DocumentDB_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS DocmentDB</h2>
        <ul>
            <li>Amazon DocumentDB:
                <ul>
                    <li>Fast, scalable, and highly available MongoDB compatible database service.</li>
                    <li>Stores queries and indexes JSON documents.</li>
                    <li>Named for its use of JSON document storage.</li>
                </ul>
            </li>
            <li>MongoDB:
                <ul>
                    <li>Document-oriented database program.</li>
                    <li>Cross-platform.</li>
                    <li>Type of NoSQL database.</li>
                    <li>Terminology:
                        <ul>
                            <li>Table = Collection</li>
                            <li>Row = Document</li>
                            <li>Column = Field</li>
                        </ul>
                    </li>
                    <li>Stores data in JSON format with no rigid schema enforced.</li>
                </ul>
            </li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-ElastiCache_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Elasticache</h2>
        <ul>
            <li>Amazon ElastiCache is a caching service that allows you to set up, run, and scale open source in-memory databases like Memcached or Redis.</li>
            <li>By storing data in-memory, ElastiCache enables faster data retrieval compared to disk-based databases.</li>
            <li>If your application experiences performance slowdowns due to frequent calls for identical datasets, you should apply database caching to eliminate this bottleneck.</li>
            <li>Refactor your application to use Amazon ElastiCache to fetch data in-memory instead of repeatedly querying the same datasets.</li>
            <li>In addition to caching, ElastiCache can be used for real-time analytics, distributed session management, geospatial services, and more.</li>
            <li>ElastiCache offers two types of engines you can launch:
                <ul>
                    <li>Amazon ElastiCache for Memcached</li>
                    <li>Amazon ElastiCache for Redis</li>
                </ul>
            </li>
            <li>Both Memcached and Redis engines provide sub-millisecond latency, data partitioning, and require minimal code integration into your application.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Resource-Icons_07302021/Res_Database/Res_48_Light/Res_Amazon-ElastiCache_ElastiCache-for-Redis_48_Light.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Elasticache for Redis</h2>
        <ul>
        <li>Amazon ElastiCache for Redis is based on the open source Redis in-memory data store.</li>
        <li>It provides:
            <ul>
            <li>Advanced data structures</li>
            <li>Pub/sub messaging</li>
            <li>Geospatial capabilities</li>
            <li>Point-in-time snapshot support</li>
            </ul>
        </li>
        <li>Redis has a replication feature not available in Memcached.</li>
        <li>For high availability using data replication, enable the cluster mode in Redis to have:
            <ul>
            <li>Multiple primary nodes</li>
            <li>Replicas across two or more availability zones</li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Resource-Icons_07302021/Res_Database/Res_48_Light/Res_Amazon-ElastiCache_ElastiCache-for-Memcached_48_Light.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
        <ul>
        <li><strong>Amazon ElastiCache for Memcached:</strong> Based on the open source Memcached in-memory data store.</li>
        <li><strong>Use Case:</strong> Suitable for building a simple and scalable caching layer for data-intensive applications.</li>
        <li><strong>Multi-threaded:</strong> Memcached can utilize multiple processing cores, which helps handle more operations by scaling up your computing capacity.</li>
        <li><strong>Downside:</strong> Lack of data replication capability, which can affect the availability of your cache layer.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-Keyspaces_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS KeySpaces</h2>
        <ul>
            <li>Amazon Keyspaces is a scalable, highly available managed Apache Cassandra-compatible database service.</li>
            <li>Apache Cassandra is an open-source wide column data store designed to handle large amounts of data.</li>
            <li>With Amazon Keyspaces, you can run Cassandra workloads on AWS without having to provision, patch, or manage servers.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-Neptune_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Neptune</h2>
        <ul>
            <li>AWS Neptune makes it easy for you to build and run applications that work with highly connected datasets.</li>
            <li>It allows you to store billions of relationships and query your data graphs with milliseconds latency.</li>
            <li>Uses nodes to store data entities and edges to store relationships between entities.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-Timestream_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS TimeStream</h2>
        <ul>
            <li>A fast, scalable, and serverless time series database service</li>
            <li>Primarily used for Internet-of-Things and operational applications</li>
            <li>Track the changes of your data</li>
            <li>Can be used to track:
                <ul>
                    <li>Stock prices</li>
                    <li>Temperature measurements</li>
                    <li>CPU utilization of an EC2 instance over a specific amount of time</li>
                </ul>
            </li>
        </ul>
    </td>
  </tr>
</table>

## <a id="aws-deployment-services"></a> $${\color{red}AWS\ deployment\ services}$$

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-CloudFormation_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Cloudformation</h2>
        <ul>
        <li>AWS CloudFormation enables provisioning and management of AWS resources using custom code templates.</li>
        <li>Templates can be written in YAML or JSON format.</li>
        <li>Supports provisioning various AWS resources such as EC2 instances, FSX file systems, Aurora databases, and more.</li>
        <li>Includes CloudFormation Designer, a drag-and-drop tool for creating and modifying templates.</li>
        <li>Functions as an Infrastructure as Code (IaC) service, similar to Terraform, Ansible, Chef, and Puppet.</li>
        <li>Resources are deployed in groups called stacks, which can represent entire architectures or subsets.</li>
        <li>Allows for creating multiple templates for different architecture layers (e.g., presentation, application, data layers).</li>
        <li>Supports nested stacks to manage related stacks more easily and independently.</li>
        <li>Enables provisioning, modification, and scaling of resources, with a dry run mode called change sets to preview changes before deployment.</li>
        <li>Change sets show how changes impact running resources, allowing for planning before updates.</li>
        <li>Stacks are usually scoped to a single AWS account, but stacksets allow management across multiple accounts and regions.</li>
        <li>Stacksets let you create, update, or delete stacks across multiple accounts with a single operation.</li>
        <li>Extended by AWS Cloud Development Kit (CDK) for programmatic infrastructure modeling in various programming languages.</li>
        <li>AWS Serverless Application Model (SAM) simplifies development of serverless applications with an extension of CloudFormation templates.</li>
        <li>AWS SAM templates include components for easier work with serverless services like Lambda, DynamoDB, and API Gateway.</li>
        <li>Serverless apps can be published and shared via the AWS Serverless Application Repository.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Compute/64/Arch_AWS-Elastic-Beanstalk_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Elastic BeanStalk</h2>
        <ul>
        <li>AWS Elastic Beanstalk is a managed platform that allows you to upload your application code in AWS and provision the required cloud environment easily.</li>
        <li>You only need to upload your application package that is written in:
            <ul>
            <li>Java</li>
            <li>.NET</li>
            <li>PHP</li>
            <li>Node.js</li>
            <li>Python</li>
            <li>Ruby</li>
            <li>Go</li>
            <li>Docker</li>
            </ul>
        </li>
        <li>Elastic Beanstalk will deploy the necessary resources to run your application.</li>
        <li>You can either run:
            <ul>
            <li>A web server environment, which runs a static website, a web app, or a web API that serves HTTP requests.</li>
            <li>A worker environment, which:
                <ul>
                <li>Runs a worker application that processes long running workloads on demand.</li>
                <li>Performs tasks on a schedule that you define.</li>
                <li>Can be integrated with the Amazon SQS queue.</li>
                </ul>
            </li>
            </ul>
        </li>
        <li>AWS Elastic Beanstalk uses a configuration file similar to CloudFormation to automatically deploy and configure your applications.</li>
        <li>These configuration files in Elastic Beanstalk are stored in the .ebextensions folder.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Developer-Tools/64/Arch_AWS-CodeDeploy_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS CodeDeploy</h2>
        <ul>
            <li>AWS CodeDeploy is a fully managed deployment service that automates your application deployments in AWS.</li>
            <li>You can deploy your applications to:
                <ul>
                    <li>Amazon EC2 instances</li>
                    <li>Amazon ECS clusters</li>
                    <li>AWS Lambda functions</li>
                    <li>Other computing services in AWS</li>
                    <li>Applications on your on-premises network</li>
                </ul>
            </li>
            <li>AWS CodeDeploy is different from:
                <ul>
                    <li>AWS CloudFormation</li>
                    <li>AWS SAM</li>
                    <li>Elastic Beanstalk</li>
                </ul>
            </li>
            <li>AWS CodeDeploy only deploys applications to existing compute resources.</li>
            <li>AWS CodeDeploy does not create AWS resources on your behalf.</li>
            <li>AWS CodeDeploy is intended for application deployments only.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Resource-Icons_07302021/Res_Containers/Res_48_Light/Res_Amazon-Elastic-Container-Service_ECS-Anywhere_48_Light.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
        <ul>
        <li>Amazon ECS Anywhere allows you to run and manage container workloads on your on-premises infrastructure.</li>
        <li>Amazon ECS Anywhere provides the same cluster management, workload scheduling, monitoring, and support features as in the cloud.</li>
        <li>Using Amazon ECS Anywhere helps meet compliance requirements and scale hybrid architectures without undermining previous investments in on-premises hardware.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Containers/64/Arch_Amazon-EKS-Anywhere_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS EKS Anywhere</h2>
        <ul>
        <li>Amazon Elastic Kubernetes Service (Amazon EKS) is a managed service for running Kubernetes on AWS.</li>
        <li>Amazon EKS automates the installation, operation, and maintenance of Kubernetes control plane, pods, and nodes.</li>
        <li>Deployment options for Kubernetes clusters on AWS:
            <ul>
            <li>Amazon EKS with managed or self-managed Amazon EC2 nodes, allowing for customization and control.</li>
            <li>Amazon EKS on AWS Outposts, using physical AWS Outpost tracks on-premises, offering more control compared to running exclusively in AWS.</li>
            <li>Amazon EKS Anywhere, which allows running Kubernetes clusters on-premises with control over all components, similar to Amazon ECS Anywhere, with official support from AWS.</li>
            <li>Amazon EKS Distro, an open source distribution of the Kubernetes software deployed by Amazon EKS, available for deployment on your own computer or onsite environment without AWS support services.</li>
            </ul>
        </li>
        <li>Amazon EKS allows deploying Kubernetes containers to various environments including AWS Fargate for serverless and cost-effective clusters.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-OpsWorks_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS OpsWork</h2>
        <ul>
        <li>AWS OpsWorks is a configuration management service that provides managed instances for your Chef and Puppet-based automation platforms.</li>
        <li>Chef and Puppet are Infrastructure as Code (IaC) platforms that automate the manual task of provisioning and configuring your servers.</li>
        <li>AWS OpsWorks automates how your services are provisioned, configured, and managed across your Amazon EC2 instances or your own physical servers situated in your corporate building.</li>
        <li>AWS OpsWorks has three offerings:
            <ul>
            <li>AWS OpsWorks for Chef Automate</li>
            <li>AWS OpsWorks for Puppet Enterprise</li>
            <li>AWS OpsWorks Stacks</li>
            </ul>
        </li>
        <li>AWS Proton is a service that automates container and serverless deployments in AWS.</li>
        <li>AWS Proton empowers your platform teams and developers to have consistent development standards and best practices.</li>
        <li>This service is particularly useful if you have a large number of developers in your organization.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-Proton_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Proton</h2>
        <ul>
            <li>AWS Proton enables developers to deploy container and serverless applications using pre-approved stacks managed by the platform team.</li>
            <li>It balances control and flexibility by allowing developers to innovate within set guardrails implemented by the platform team.</li>
            <li>AWS Proton offers a self-service portal for developers, which contains AWS Proton templates that they can use and deploy.</li>
            <li>A Proton template includes all information required to deploy custom environments and services.</li>
            <li>You can create AWS Proton components to provide flexibility to service templates.</li>
            <li>Components in AWS Proton offer platform themes by extending core infrastructure patterns and defining guardrails for developers.</li>
        </ul>
  </tr>

</table>

## <a id="aws-monitoring-services"></a> $${\color{brown}AWS\ monitoring\ services}$$

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_Amazon-CloudWatch_64.svg" alt="">
    </td>
    <td class="content">
        <h2> AWS CloudWatch Logs</h2>
            <ul>
                <li>AWS CloudTrail is a service used for IT audits.</li>
                <li>Tracks user activity and API usage in your AWS account.</li>
                <li>Stores data in an Amazon S3 bucket owned by your AWS account or by others.</li>
                <li>Enables risk auditing by monitoring and logging account activities such as:
                    <ul>
                        <li>User actions in the AWS Management Console</li>
                        <li>AWS SDKs</li>
                        <li>APIs</li>
                        <li>AWS CLI</li>
                    </ul>
                </li>
                <li>There are two types of events logged in AWS CloudTrail:
                    <ul>
                        <li>Management events (control plane operations):
                            <ul>
                                <li>Provide information about management operations performed on resources in your AWS account</li>
                                <li>Examples: attaching an IAM role, creating a VPC, creating a subnet</li>
                            </ul>
                        </li>
                        <li>Data events (data plane operations):
                            <ul>
                                <li>Provide information about resource operations performed on or in a resource</li>
                                <li>Examples: Amazon S3 object-level API activities, invoking an AWS Lambda function</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li>CloudTrail log files can be received from multiple AWS accounts by granting cross-account permissions to CloudTrail.</li>
                <li>Each account can deliver the log files to an S3 bucket in your central account.</li>
            </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-Personal-Health-Dashboard_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Personal Health Dashboard</h2>
        <ul>
        <li>AWS Personal Health Dashboard provides a personalized view of the AWS services you are using.</li>
        <li>It only shows the status of services that you are actively using in your account.</li>
        <li>It displays AWS Health events that might affect your applications, such as scheduled maintenance or infrastructure changes.</li>
        <li>You can create alerts and notifications triggered by changes in the health of your AWS resources.</li>
        <li>AWS Health API provides programmatic access to the information in your AWS Personal Health Dashboard.</li>
        <li>The AWS Health API is a RESTful web service accessible via HTTPS, returning responses in JSON format.</li>
        <li>This service is not available by default; you must have a business or enterprise support plan to use it.</li>
        </ul>
    </td>
  </tr>
</table>

## <a id="aws-audit-and-compliance-services"></a> $${\color{magenta}AWS\ audit\ and\ compliance\ services}$$

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-CloudTrail_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS CloudTrail</h2>
        <ul>
        <li>AWS CloudTrail is a service used primarily for IT audits.</li>
        <li>Tracks user activity and API usage in your AWS account.</li>
        <li>Stores data in an Amazon S3 bucket owned by your AWS account or other accounts.</li>
        <li>Enables risk auditing by continuously monitoring and logging account activities.</li>
        <li>Logs user actions in the AWS Management Console, AWS SDKs, APIs, or AWS CLI.</li>
        <li>There are two types of events logged in AWS CloudTrail:
            <ul>
            <li><strong>Management events:</strong> Provide information about management operations on resources (e.g., attaching an IAM role, creating a VPC, or creating a subnet).</li>
            <li><strong>Data events:</strong> Provide information about resource operations (e.g., Amazon S3 object-level API activities, or invoking an AWS Lambda function).</li>
            </ul>
        </li>
        <li>CloudTrail log files can be received from multiple AWS accounts by granting cross-account permissions to CloudTrail.</li>
        <li>Each account can deliver log files to an S3 bucket in a central account.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Artifact_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Artifact</h2>
        <ul>
        <li>AWS Artifact is a service that provides on-demand AWS security and compliance reports.</li>
        <li>It acts as a self-service portal to find compliance-related information and reports about AWS.</li>
        <li>Reports available include:
            <ul>
            <li>ISO reports</li>
            <li>Payment Card Industry (PCI) reports</li>
            <li>Service Organization Control (SOC) reports</li>
            <li>Certifications from accreditation bodies across the globe</li>
            </ul>
        </li>
        <li>Users can download AWS Security and compliance documents such as:
            <ul>
            <li>SOC 1 reports</li>
            <li>ISO certifications</li>
            <li>Other reports</li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Security-Hub_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Security Hub
      </h2>
        <ul>
        <li>AWS Security Hub provides a centralized and comprehensive view of the security posture of your cloud infrastructure across multiple AWS accounts.</li>
        <li>It helps you comply with specific security standards and best practices required by your organization.</li>
        <li>The service collects security alerts and findings from multiple AWS services, including:
            <ul>
            <li>Amazon GuardDuty</li>
            <li>Amazon Inspector</li>
            <li>Amazon Macie</li>
            <li>IAM Access Analyzer</li>
            <li>AWS Firewall Manager</li>
            <li>Other sources</li>
            </ul>
        </li>
        <li>You can use AWS Security Hub to comply with:
            <ul>
            <li>Payment Card Industry Data Security Standard (PCI DSS)</li>
            <li>Center for Internet Security (CIS) Benchmarks</li>
            <li>Many other security standards</li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>
</table>

## <a id="aws-networking-and-content-delivery-services"></a> $${\color{cyan}AWS\ networking\ and\ content\ delivery\ services}$$

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_Amazon-Virtual-Private-Cloud_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS VPC</h2>
        <ul>
            <li>Amazon Virtual Private Cloud (VPC) is a logical private network within the AWS Cloud.</li>
            <li>Allows you to launch Amazon EC2 instances and other resources in the virtual network you define.</li>
            <li>You have complete control over your virtual networking environment:
                <ul>
                    <li>Selecting your IP address range.</li>
                    <li>Creating subnets.</li>
                    <li>Route table configuration.</li>
                    <li>Adding gateways for external networks.</li>
                </ul>
            </li>
            <li>You can use both IP version four and IP version six addresses in your VPC for your cloud resources and applications.</li>
            <li>A VPC can communicate with external networks using a gateway:
                <ul>
                    <li>An internet gateway provides internet connectivity to your VPC.</li>
                    <li>A virtual private gateway allows connection to an on-premises data center or other external networks.</li>
                    <li>VPC peering allows connection to another VPC.</li>
                </ul>
            </li>
            <li>The term VPC stands for Virtual Private Cloud:
                <ul>
                    <li><strong>Virtual</strong>: A virtual entity powered by interconnected physical networking devices.</li>
                    <li><strong>Private</strong>: By default, a new VPC is private and does not have any gateways to external networks.</li>
                    <li><strong>Cloud</strong>: No need to manage physical servers; cloud computing provides on-demand delivery of resources via the internet.</li>
                </ul>
            </li>
            <li>Physical components of an Amazon VPC are generated by physical networking devices like network interface cards (NICs).</li>
            <li>An AWS Outpost Rack uses the same physical networking devices as AWS data centers, allowing you to extend your VPC to your on-premises data center.</li>
            <li>VPC endpoints allow you to establish a private connection between your VPC and some AWS services without traffic traversing the public internet.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_Elastic-Load-Balancing_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS ELB</h2>
        <ul>
            <li>Your virtual machines, such as EC2 instances, are usually launched within your VPC.</li>
            <li>You can establish a private connection between your VPC and some AWS services using a VPC endpoint, keeping traffic private and not traversing the public internet.</li>
            <li>Elastic Load Balancing (ELB) is a networking service that automatically distributes incoming traffic across multiple targets, such as Amazon EC2 instances, containers, Lambda functions, and other components.</li>
            <li>ELB is primarily used in load balancing, distributing the incoming traffic load to multiple underlying servers to ensure high availability.</li>
            <li>An ELB allows you to route traffic to healthy resources running in different availability zones.</li>
            <li>There are different types of Elastic Load Balancers:</li>
            <ul>
                <li><strong>Application Load Balancer (ALB)</strong>: Suitable for load balancing HTTP and HTTPS traffic to your application servers, microservices, and containers.</li>
                <li><strong>Network Load Balancer (NLB)</strong>: Recommended for load balancing TCP, UDP, and TLS traffic to your applications, capable of handling billions of requests per second with ultra-low latencies.</li>
                <li><strong>Gateway Load Balancer (GWLB)</strong>: Used for deploying, scaling, and running third-party virtual appliances such as custom firewalls, deep packet inspection systems, or intrusion detection and prevention systems in AWS. It passes OSI layer three traffic using IP to its registered targets.</li>
                <li><strong>Classic Load Balancer (CLB)</strong>: Intended for applications built within the old EC2 Classic Network, still used today for applications with custom security policies and TCP passthrough configurations.</li>
            </ul>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_Amazon-Route-53_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Route 53</h2>
        <ul>
            <li>Amazon Route 53 is a Domain Name System (DNS) web service that routes traffic to various targets.</li>
            <li>A DNS is a system that routes a domain name to a particular IP address.</li>
            <li>Route 53 allows you to map domain names to:
                <ul>
                    <li>Elastic IP addresses</li>
                    <li>EC2 instances</li>
                    <li>Static S3 websites</li>
                    <li>Elastic Load Balancer</li>
                    <li>CloudFront Distributions</li>
                    <li>Other AWS resources</li>
                </ul>
            </li>
            <li>Route 53 also allows you to purchase and manage custom web domains.</li>
            <li>For example, if you have a website called <em>tutorialsdojo.com</em>, you can route the traffic to:
                <ul>
                    <li>An EC2 server</li>
                    <li>An S3 static website</li>
                    <li>A load balancer</li>
                    <li>Any AWS resource that you prefer</li>
                </ul>
            </li>
            <li>Route 53 allows you to use a route policy to customize how traffic is routed to a specific domain.</li>
            <li>Different route policies available:
                <ul>
                    <li>Simple routing</li>
                    <li>Failover routing</li>
                    <li>Geolocation routing</li>
                    <li>Geoproximity routing</li>
                    <li>Latency routing</li>
                    <li>Multi-value answer routing</li>
                    <li>Weighted routing</li>
                </ul>
            </li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_AWS-Global-Accelerator_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Global Accelerator</h2>
        <ul>
        <li>AWS Global Accelerator is a networking service.</li>
        <li>It provides a set of static IP addresses as single fixed entry points for clients globally.</li>
        <li>These static IP addresses can be associated with regional endpoints, such as:
            <ul>
            <li>Network Load Balancers (NLBs)</li>
            <li>Application Load Balancers (ALBs)</li>
            <li>EC2 instances</li>
            <li>Elastic IP addresses</li>
            </ul>
        </li>
        <li>Global Accelerator allows connection to multiple AWS resources running in one or more regions using a single endpoint or an endpoint group.</li>
        <li>The static IP addresses accept incoming traffic onto the AWS global network close to your users.</li>
        <li>For multiple ALBs in multiple regions, you can create one endpoint to access all your load balancers.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_Amazon-CloudFront_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Cloudfront</h2>
        <ul>
        <li>Amazon CloudFront is a content delivery network (CDN) service.</li>
        <li>CDNs are globally distributed networks of servers that store or cache files.</li>
        <li>CloudFront quickly delivers static content and video streams to clients.</li>
        <li>Using a CDN shortens the time to deliver data, improving application response time.</li>
        <li>Instead of fetching data from one origin server, clients can retrieve content from multiple edge locations near them.</li>
        <li>CloudFront distribution can be set up to cache images, videos, media files, and software downloads for websites.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_AWS-PrivateLink_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS PrivateLink</h2>
        <ul>
        <li>AWS PrivateLink allows private connectivity to AWS services without using the public internet.</li>
        <li>It provides a private endpoint, also known as a VPC endpoint, for resources like VPCs, EC2 instances, and S3 buckets.</li>
        <li>Data sent over an unsecured network is vulnerable to security threats like packet sniffing.</li>
        <li>Hackers can intercept data as it travels through the routers and networks of the internet.</li>
        <li>With AWS PrivateLink, data stays within the Amazon network, avoiding unsecured internet lines.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_AWS-Client-VPN_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS VPN</h2>
        <ul>
        <li>AWS Virtual Private Network (AWS VPN) enables secure connections between your on-premises network and AWS.</li>
        <li>AWS VPN is essentially a regular VPN that creates an encrypted connection through the public internet.</li>
        <li>It uses the IPSec protocol for data authentication and encryption in transit.</li>
        <li>AWS VPN is comprised of two services:
            <ul>
            <li><strong>AWS Site-to-Site VPN:</strong> Creates encrypted tunnels between your network and your Amazon VPCs or AWS Transit Gateways.</li>
            <li><strong>AWS Client VPN:</strong> Software that allows your users to connect to AWS or on-premises resources.</li>
            </ul>
        </li>
        <li>Each service has a corresponding endpoint to your VPC:
            <ul>
            <li>You can create a Site-to-Site VPN endpoint.</li>
            <li>You can create a Client VPN endpoint.</li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_AWS-Direct-Connect_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Direct Connect</h2>
        <ul>
        <li>AWS Direct Connect is a cloud service solution that allows you to establish a dedicated network connection from your on-premises network to AWS.</li>
        <li>Direct Connect provides a more consistent network experience over internet-based connections such as a VPN.</li>
        <li>You can create a private virtual interface to enable your on-premises servers to connect to the virtual private gateway of your Amazon VPC.</li>
        <li>You can group your virtual private gateways and private virtual interfaces using a Direct Connect gateway.</li>
        <li>You can use a public virtual interface to connect your Amazon S3 buckets and other public resources in AWS.</li>
        <li>Unlike a VPN, the data being sent over a Direct Connect connection does not pass through the public internet.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_AWS-Transit-Gateway_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Transit Gateway</h2>
        <ul>
        <li>AWS Transit Gateway is a service that connects Amazon VPCs, VPNs, Direct Connect gateways, and on-premises networks to a single gateway.</li>
        <li>Recommended for large organizations with hundreds of Amazon VPCs, Site-to-Site VPNs, and external networks.</li>
        <li>Reduces the complexity of infrastructure.</li>
        <li>Empowers easy scaling.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_AWS-App-Mesh_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS App Mesh</h2>
        <ul>
            <li>AWS App Mesh is a service mesh that provides application-level networking for containerized applications.</li>
            <li>It allows services to communicate easily with each other across various types of computing infrastructure.</li>
            <li>App Mesh uses an open-source service mesh proxy called Envoy.</li>
            <li>This Envoy proxy is deployed alongside Microsoft containers.</li>
            <li>App Mesh standardizes service communication and provides end-to-end network visibility for applications.</li>
            <li>It can be used with microservices containers managed by:
                <ul>
                    <li>Amazon ECS</li>
                    <li>Amazon EKS</li>
                    <li>AWS Fargate</li>
                    <li>Kubernetes running on AWS</li>
                    <li>Services running on Amazon EC2</li>
                </ul>
            </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_AWS-Cloud-Map_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS CloudMap</h2>
            <ul>
            <li>AWS Cloud Map is a cloud resource discovery service.</li>
            <li>Commonly used in microservices and containerized applications with dynamically changing resources.</li>
            <li>Enables naming of application resources with custom names.</li>
            <li>Allows applications to discover the most up-to-date locations of resources.</li>
            <li>Improves the availability of the system.</li>
            </ul>
    </td>
  </tr>
 

</table>

## <a id="aws-application-integration-services"></a> $${\color{pink}AWS\ application\ integration\ services}$$

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_Amazon-API-Gateway_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS API Gateway</h2>
        <ul>
        <li>Amazon API Gateway is a fully managed service that allows you to publish, maintain, monitor, and secure your RESTful APIs.</li>
        <li>Supports WebSockets for real-time message communication to your clients.</li>
        <li>Acts as a front door for backend services running on:
            <ul>
            <li>AWS Lambda</li>
            <li>Amazon EC2</li>
            <li>Amazon ECS</li>
            <li>AWS Elastic Beanstalk</li>
            <li>Any web application</li>
            </ul>
        </li>
        <li>Amazon API Gateway can be thought of as a web proxy service, similar to:
            <ul>
            <li>APIGEE</li>
            <li>MuleSoft</li>
            <li>Other web proxies</li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_Amazon-Simple-Queue-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS SQS</h2>
        <ul>
        <li>Amazon Simple Queue Service (SQS) is a fully managed queuing service.</li>
        <li>SQS provides a queue where incoming messages can line up and be processed by consumers like EC2 instances, Lambda functions, ECS tasks, etc.</li>
        <li>SQS can replace traditional message-oriented middleware without the need to maintain or manage underlying resources.</li>
        <li>There are two types of message queues in SQS:
            <ul>
            <li>Standard Queue: Offers at least once delivery with best effort ordering, providing higher throughput but may deliver duplicate messages.</li>
            <li>FIFO (First In, First Out) Queue: Guarantees exactly once delivery and preserves the order of messages, but offers less throughput.</li>
            </ul>
        </li>
        <li>The visibility timeout of messages in the queue can be changed using the ChangeMessageVisibility API or through the web console, but it does not guarantee against receiving a message twice.</li>
        <li>FIFO queues are ideal for applications requiring exact once processing and preserving the order of messages.</li>
        <li>SQS can scale EC2 instances based on message age, depth, or number in the queue, and can configure auto-scaling groups accordingly.</li>
        <li>You can configure an auto-scaling group with a target tracking policy based on the age of the oldest message in the queue.</li>
        <li>SQS integrates with other AWS services like Amazon SNS, Amazon ECS, and others for various functions, such as:
            <ul>
            <li>Receiving notifications when a new object is created in an S3 bucket.</li>
            <li>Sending messages between ECS microservices.</li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_Amazon-Simple-Notification-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS SNS</h2>
        <ul>
            <li>Amazon Simple Notification Service (Amazon SNS) is a fully managed messaging and notification service.</li>
            <li>Amazon SNS enables communication between systems through publish/subscribe (pub/sub) patterns.</li>
            <li>It facilitates messaging between decoupled microservice applications or directly to users via mobile push, email, or SMS.</li>
            <li>The main resource in Amazon SNS is a topic, which can be subscribed to by applications or other AWS services.</li>
            <li>Example: Amazon CloudWatch can use an SNS topic to send notifications (e.g., email or Slack) for activities in an autoscaling group.</li>
            <li>One or more Amazon SQS queues can subscribe to a single SNS topic.</li>
            <li>Amazon SNS supports message filtering, allowing specific subscribers to receive only a subset of messages by assigning a filter policy to the topic subscription.</li>
            <li>Message filtering allows one SNS topic to publish specific messages to multiple SQS queues based on message type.</li>
            <li>This approach is known as fan-out event notification, where messages are pushed to multiple subscribers, avoiding the need for periodic checks or queue polling.</li>
            <li>Example: One SNS topic with various insurance code types (e.g., car insurance, home insurance, pet insurance) can publish messages to specific SQS queues based on the type.</li>
            <li>A backend application server needs to be configured to consume messages from the queue corresponding to a particular type.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_AWS-Step-Functions_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Step Function</h2>
        <ul>
            <li>AWS Step Functions is a serverless function orchestrator for AWS Lambda.</li>
            <li>It allows you to orchestrate or sequence multiple AWS Lambda functions to achieve a specific workflow.</li>
            <li>Step Functions enables the creation of a state machine using a visual workflow.</li>
            <li>The visual workflow contains a combination of steps, activities, and service tasks.</li>
            <li>Step Functions help coordinate multiple components and configure each step in your workflow using Lambda functions.</li>
            <li>The name "Step Functions" comes from its ability to define and manage each step of the workflow.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_Amazon-MQ_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS MQ</h2>
        <ul>
            <li>Amazon MQ is a managed message broker service in AWS that uses the open-source Apache ActiveMQ program.</li>
            <li>MQ stands for Message Queue, which is a form of asynchronous communication used in distributed systems, serverless applications, or microservices architectures.</li>
            <li>Messages in Amazon MQ are stored in the queue until they're processed and deleted by a consumer.</li>
            <li>Amazon MQ is similar to Amazon SQS, but the main difference is its capability to support different types of messaging protocols.</li>
            <li>Amazon MQ provides compatibility with common messaging APIs, such as:
                <ul>
                    <li>Java Message Service (JMS)</li>
                    <li>.NET Message Service (NMS)</li>
                    <li>AMQP</li>
                    <li>MQTT</li>
                    <li>WebSockets</li>
                    <li>Many others</li>
                </ul>
            </li>
            <li>Amazon EventBridge is a serverless event bus that makes it easy to connect applications using data from your own applications, software as a service (SaaS) applications, and other AWS services.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_Amazon-EventBridge_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS EventBridge</h2>
        <ul>
        <li>Amazon EventBridge is a service based on CloudWatch Events with more advanced features.</li>
        <li>EventBridge uses the same service API, endpoint, and underlying service infrastructure as CloudWatch Events.</li>
        <li>It is designed for use with your own applications, third-party Software-as-a-Service (SaaS) apps, and other external sources.</li>
        <li>EventBridge complements the data provided by AWS services.</li>
        <li>It is used for building event-driven applications that manage event ingestion, delivery, security, authorization, and error handling.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_AWS-AppSync_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS AppSync</h2>
        <ul>
        <li>AWS AppSync is a managed service that uses GraphQL for efficient data querying.</li>
        <li>GraphQL allows querying REST APIs exposed as a schema.</li>
        <li>Schemas in GraphQL can be:
            <ul>
            <li>Query schema for reading data</li>
            <li>Mutation schema for writing data</li>
            <li>Subscription schema for receiving or uploading data</li>
            </ul>
        </li>
        <li>Traditional REST APIs return all data by default when performing an HTTP GET operation.</li>
        <li>REST APIs often return more data than necessary, which may not be used by applications.</li>
        <li>Filtering data in REST APIs using query string parameters is limited to a single resource or schema.</li>
        <li>GraphQL allows combining multiple resources in a single API call, retrieving only the needed data.</li>
        <li>A resolver in GraphQL is a function that resolves or publishes data in the schema.</li>
        <li>AWS AppSync facilitates the integration and management of GraphQL in applications.</li>
        <li>AppSync simplifies application development by creating flexible APIs to securely access, manipulate, and combine data from multiple data sources.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_Amazon-AppFlow_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS AppFlow</h2>
        <ul>
        <li>Amazon AppFlow is a fully managed integration service.</li>
        <li>It enables secure data transfer between SaaS applications and AWS services.</li>
        <li>Supports SaaS applications such as Salesforce, Marketo, Slack, and ServiceNow.</li>
        <li>Integrates with AWS services like Amazon S3, Amazon Redshift, and others.</li>
        <li>Data flows can be run on demand or scheduled.</li>
        <li>Data flows can also be triggered by business events.</li>
        <li>Provides powerful data transformation capabilities including filtering and validation.</li>
        <li>Generates rich, ready-to-use data for custom applications.</li>
        </ul>
    </td>
  </tr>
</table>


## <a id="aws-security-services"></a> $${\color{teal}AWS\ security\ services}$$

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-WAF_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS WAF</h2>
        <ul>
            <li>AWS Web Application Firewall Service (AWS WAF) is a web application firewall service in AWS.</li>
            <li>It protects web applications from common web exploits that could:
                <ul>
                    <li>Affect application availability</li>
                    <li>Compromise security</li>
                    <li>Consume excessive resources</li>
                </ul>
            </li>
            <li>Custom rules can be created to block common attack patterns such as:
                <ul>
                    <li>SQL injection</li>
                    <li>Cross-site scripting attacks</li>
                </ul>
            </li>
            <li>AWS WAF can be integrated with:
                <ul>
                    <li>Amazon CloudFront</li>
                    <li>Application Load Balancer</li>
                    <li>Amazon API Gateway</li>
                </ul>
            </li>
            <li>IP match condition feature allows blocking of malicious requests from specific IP addresses.</li>
            <li>Rate-limiting rule can protect against illegitimate requests from external systems by:
                <ul>
                    <li>Creating a rate-based web access control list (Web ACL)</li>
                    <li>Attaching it to a CloudFront distribution</li>
                </ul>
            </li>
            <li>This helps minimize the effects of DDoS attacks.</li>
            <li>AWS WAF is suitable for applications that:
                <ul>
                    <li>Need to be accessed only from a specific country</li>
                </ul>
            </li>
            <li>Geo Match condition allows blocking or allowing access based on:
                <ul>
                    <li>Specific countries</li>
                </ul>
            </li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Firewall-Manager_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Firewall Manager</h2>
        <ul>
        <li><strong>AWS Firewall Manager</strong>: A security management service designed to centrally configure and manage AWS WAF rules across your accounts and applications.</li>
        <li>Using AWS Firewall Manager, you can:
            <ul>
            <li>Easily roll out custom rules for Application Load Balancers, API Gateways, and Amazon CloudFront distributions.</li>
            <li>Apply rules across accounts in an AWS organization.</li>
            </ul>
        </li>
        <li><strong>AWS Shield</strong>: A managed DDoS protection service that safeguards applications running on AWS.</li>
        <li>AWS Shield provides:
            <ul>
            <li>Detection and automatic mitigations to minimize application downtime and latency.</li>
            <li>Mitigation against different types of flood attacks, such as:
                <ul>
                <li>UDP reflection</li>
                <li>SYN flood</li>
                <li>DNS Query flood</li>
                <li>HTTP flood attacks</li>
                </ul>
            </li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Shield_64.svg" alt="">
    </td>
    <td class="content">
    <h2>AWS Shield</h2>
        <ul>
            <li>AWS Shield protects applications using:
                <ul>
                    <li>Amazon EC2</li>
                    <li>Elastic Load Balancers</li>
                    <li>CloudFront distributions</li>
                    <li>AWS Global Accelerators</li>
                    <li>Route 53 Edge locations</li>
                </ul>
            </li>
            <li>AWS Shield has two tiers:
                <ul>
                    <li>Standard: Built-in, no extra charge</li>
                    <li>Advanced: Paid version, includes real-time DDoS attack notifications and access to the DDoS Response Team (DRT)</li>
                </ul>
            </li>
            <li>Amazon GuardDuty is a managed threat detection service that identifies:
                <ul>
                    <li>Malicious or unauthorized activities in AWS accounts and workloads</li>
                    <li>Unusual API calls</li>
                    <li>Cryptocurrency mining</li>
                    <li>Potentially unauthorized deployments</li>
                </ul>
            </li>
            <li>GuardDuty detects potentially compromised EC2 instances and produces security reports called Findings, which represent potential security issues within your network.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_Amazon-GuardDuty_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS GuardDuty</h2>
        <ul>
        <li>Amazon GuardDuty is a managed threat detection service.</li>
        <li>It helps identify malicious or unauthorized activities in AWS accounts and workloads.</li>
        <li>Monitors activities such as:
            <ul>
            <li>Unusual API calls</li>
            <li>Cryptocurrency mining</li>
            <li>Potentially unauthorized deployments</li>
            </ul>
        </li>
        <li>Detects possible account compromises.</li>
        <li>Can detect potentially compromised EC2 Instances.</li>
        <li>Produces security reports called "Findings" that indicate potential security issues.</li>
        <li>GuardDuty can send notifications using CloudWatch Events when changes occur in security Findings.</li>
        <li>This service is used solely for threat detection.</li>
        <li>It is not capable of making resource changes such as:
            <ul>
            <li>Rate Limiting Protection</li>
            <li>DDoS attack mitigation</li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-CloudHSM_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS CloudHSM</h2>
        <ul>
        <li>AWS CloudHSM is a fully managed cloud-based hardware security module (HSM).</li>
        <li>CloudHSM allows you to easily generate and use your own encryption keys (128-bit or 256-bit).</li>
        <li>HSM is a physical hardware device that performs cryptographic operations and securely stores cryptographic key material.</li>
        <li>Key material in CloudHSM is a random Base64 or hexadecimal string in a binary format used by your encryption key.</li>
        <li>The CloudHSM cluster is deployed in your Amazon VPC and can be accessed or managed using CloudHSM clients installed on your Amazon EC2 instances.</li>
        <li>Clients communicate with the HSM cluster using Elastic Network Interfaces (ENIs) of the HSMs.</li>
        <li>The CloudHSM cluster is a single-tenant service, meaning you have exclusive control over it.</li>
        <li>CloudHSM can be used for offloading SSL processing of web servers, enabling Transparent Data Encryption (TDE) for Oracle databases, and protecting private keys for an Issuing Certificate Authority (CA).</li>
        <li>You can integrate CloudHSM with AWS KMS to create a custom key store.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Key-Management-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS KMS</h2>
        <ul>
        <li>AWS Key Management Service (KMS) is a managed service that functions similarly to CloudHSM.</li>
        <li>KMS uses hardware security modules (HSMs) under the hood to create and control encryption keys.</li>
        <li>Unlike CloudHSM, KMS is multi-tenant, meaning you share the HSM with other AWS customers.</li>
        <li>You cannot launch an HSM to your Amazon VPC or EC2 Instances; the HSM is fully managed by AWS.</li>
        <li>KMS can be integrated with other AWS services, such as Amazon EBS, Amazon S3, and Amazon RDS, to protect your data.</li>
        <li>KMS uses envelope encryption, encrypting plain text data with a data key, which is then encrypted with a master key.</li>
        <li>The primary resource in KMS is the Customer Master Key (CMK), which represents the master key that encrypts your data key.</li>
        <li>KMS allows you to store and automatically rotate your CMKs to meet encryption requirements.</li>
        <li>You can create a custom key store in KMS using CloudHSM, giving you complete control over the encryption key lifecycle.</li>
        <li>This custom key store allows you to remove the key material of your encryption keys.</li>
        <li>You can audit key usage independently of AWS CloudTrail and KMS itself using the custom key store.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Secrets-Manager_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Secrets Manager</h2>
        <ul>
            <li>AWS Secrets Manager helps protect secrets needed to access your applications, services, and IT resources.</li>
            <li>Enables easy rotation, management, and retrieval of secrets throughout their lifecycle.</li>
            <li>Secrets can include database passwords, API keys, authentication tokens, or other sensitive data.</li>
            <li>Eliminates the need to hard code sensitive information in plain text for Lambda functions or custom applications.</li>
            <li>Offers secret rotation with built-in integration for Amazon RDS, Amazon Redshift, Amazon DocumentDB, and other services.</li>
            <li>Enables control of access to secrets using fine-grained permissions and centralized auditing of secrets.</li>
            <li>Does not use HSM (Hardware Security Module), so encryption keys or key materials should not be stored here.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Certificate-Manager_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Certificate Manager</h2>
        <ul>
        <li>AWS Certificate Manager (ACM) is a service that allows you to create and manage SSL certificates.</li>
        <li>ACM enables easy provisioning, management, and deployment of public and private SSL/TLS certificates.</li>
        <li>These certificates can be used with AWS services and internal connected resources.</li>
        <li>ACM allows the creation of private certificates for internal resources.</li>
        <li>ACM enables centralized management of the certificate lifecycle.</li>
        <li>Public and private certificates provisioned through ACM are free for use with certain AWS services.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_Amazon-Macie_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Macie</h2>
        <ul>
            <li>Amazon Macie is a fully managed security service.</li>
            <li>Automatically recognizes and classifies sensitive data or intellectual property on AWS.</li>
            <li>Uses machine learning to discover, classify, and protect sensitive data.</li>
            <li>Focuses on data stored in Amazon S3 buckets and other AWS services.</li>
            <li>Recognizes personally identifiable information (PII), such as:
                <ul>
                    <li>Names</li>
                    <li>Social security numbers</li>
                    <li>Driver's license numbers</li>
                    <li>Bank account numbers</li>
                    <li>Password numbers</li>
                    <li>Email addresses</li>
                </ul>
            </li>
            <li>Provides dashboards and alerts for visibility into how sensitive data is accessed or moved.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_Amazon-Inspector_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Inspector</h2>
        <ul>
        <li>Amazon Inspector is an automated security assessment service for improving security and compliance of applications deployed on AWS.</li>
        <li>Automatically assesses applications for vulnerabilities or deviations from best practices.</li>
        <li>Produces a detailed list of security findings prioritized by level of security after performing an assessment.</li>
        <li>Provides an automated security assessment report identifying unintended network access and vulnerabilities in Amazon EC2 instances.</li>
        <li>Findings can be reviewed directly or as part of detailed assessment reports, available via the Amazon Inspector Console or API.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_Amazon-Detective_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Detective</h2>
        <ul>
            <li>Amazon Detective is a service primarily used for security investigations and analysis.</li>
            <li>It simplifies the process of analyzing, investigating, and quickly identifying the root cause of potential security issues or suspicious activities.</li>
            <li>Amazon Detective automatically collects log data from AWS resources.</li>
            <li>It gathers logs from various AWS services, including:
                <ul>
                    <li>AWS CloudTrail</li>
                    <li>Amazon VPC Flow Logs</li>
                    <li>Amazon GuardDuty findings</li>
                    <li>Other AWS services</li>
                </ul>
            </li>
            <li>Uses machine learning to analyze logs and conduct security investigations.</li>
        </ul>
    </td>
  </tr>
</table>

## <a id="aws-management-and-governance-services"></a> $${\color{lime}AWS\ management\ and\ governance\ services}$$

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-Management-Console_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Management Console</h2>
        <ul>
            <li>AWS Management Console is a web interface for AWS accessible via web browsers like Google Chrome, Mozilla Firefox, Safari, etc.</li>
            <li>You can securely log into the AWS Management Console using your IAM username and password.</li>
            <li>For added security, enable Multi-Factor Authentication (MFA), which requires an authentication code from your MFA device before login.</li>
            <li>Access the AWS Management Console by visiting the URL: <a href="https://console.aws.amazon.com">console.aws.amazon.com</a>.</li>
        </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Developer-Tools/64/Arch_AWS-Command-Line-Interface_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS CLI</h2>
        <ul>
            <li>AWS Command Line Interface (AWS CLI) is a command line interface for interacting with AWS services.</li>
            <li>On MacBook or Linux OS, you can use the terminal program to run the AWS CLI.</li>
            <li>On Windows, you can use the command prompt or Windows PowerShell to run the AWS CLI.</li>
            <li>Shell scripts can be developed to invoke different AWS CLI commands for managing resources.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_AWS-Console-Mobile-Application_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Console Mobile Application</h2>
        <ul>
            <li>The AWS Console Mobile Application is the official mobile app provided by Amazon Web Services.</li>
            <li>Allows you to monitor your resources through a dedicated dashboard.</li>
            <li>View configuration details, metrics, and alarms of select AWS services.</li>
            <li>The dashboard provides:
                <ul>
                    <li>An overview of the account status.</li>
                    <li>Real-time CloudWatch metrics.</li>
                    <li>Your personal health dashboard.</li>
                    <li>AWS billing information.</li>
                </ul>
            </li>
            <li>There are limitations compared to the Amazon Management Console or the AWS CLI.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Resource-Access-Manager_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Resource Manager</h2>
        <ul>
            <li>AWS Resource Access Manager (RAM) is a service for sharing AWS resources.</li>
            <li>You can share resources with any AWS account or within your AWS organization.</li>
            <li>Resources you can share include:
                <ul>
                    <li>AWS Trusted Gateways</li>
                    <li>Subnets</li>
                    <li>AWS License Manager configurations</li>
                    <li>Route 53 Resolver rules</li>
                    <li>Other resources</li>
                </ul>
            </li>
            <li>AWS RAM eliminates the need for duplicate resources across multiple accounts.</li>
            <li>This reduces the operational overhead of managing resources in every single account.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-Systems-Manager_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Systems Manager</h2>
        <ul>
        <li><strong>AWS Systems Manager (SSM)</strong>: A suite of services providing visibility and control of cloud and on-premises infrastructure.</li>
        <li><strong>Features of SSM:</strong>
            <ul>
            <li>Session Manager</li>
            <li>State Manager</li>
            <li>Patch Manager</li>
            <li>Automation</li>
            <li>Maintenance Window</li>
            <li>Run Command</li>
            <li>Parameter Store</li>
            <li>Other sub-modules</li>
            </ul>
        </li>
        <li><strong>SSM Agent:</strong> Similar to CloudWatch Agent or DataSync Agent; manages both Amazon EC2 instances and on-premises servers.</li>
        <li><strong>Patch Manager:</strong> Automates the process of patching operating systems using predefined or custom patch baselines. Supports scheduled maintenance windows to reduce operational impact.</li>
        <li><strong>State Manager:</strong> Controls configuration details or state of resources, such as server configurations, virtualized hardware, and firewall settings. Supports association of accessible playbooks, Chef recipes, PowerShell modules, and other SSM documents.</li>
        <li><strong>Parameter Store:</strong> Provides centralized storage and management of parameters, including passwords, database strings, AMI IDs, license codes, environment variables, and other sensitive parameters. Supports secure string data type for automatic encryption using a customer master key (CMK) in AWS KMS.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-Config_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Config</h2>
        <ul>
        <li>AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources.</li>
        <li>It automates the compliance assessment of your internal policies and regulatory standards by providing visibility on the existing configurations of your various AWS services and third-party resources.</li>
        <li>AWS Config allows you to identify changes made to a specific resource over time.</li>
        <li>It continuously assesses changes in your resource configuration and compares them against your specified criteria.</li>
        <li>You can create rules to detect:
            <ul>
            <li>EC2 instances running on an unapproved AMI</li>
            <li>Publicly accessible S3 buckets</li>
            <li>Noncompliance services</li>
            <li>And more</li>
            </ul>
        </li>
        <li>The evaluation can be triggered either periodically or by an actual configuration change of your AWS resource.</li>
        <li>You can integrate AWS Config with CloudWatch events and AWS Lambda to keep you updated on resource changes in near real-time and to execute custom actions.</li>
        <li>Remediating noncompliant AWS resources can be automated by associating an AWS Config rule with an AWS Systems Manager automation document.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-Organizations_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Organizations</h2>
        <ul>
        <li>The AWS Organization Service enables you to consolidate and centrally manage multiple AWS accounts.</li>
        <li>It provides consolidated billing, access control, compliance, and security.</li>
        <li>Allows sharing resources across AWS accounts.</li>
        <li>Consolidated Billing helps combine multiple AWS accounts with separate billing, taking advantage of volume discounts.</li>
        <li>Service Control Policies (SCPs) can ensure that only authorized users can execute actions meeting your policy requirements.</li>
        <li>Central logging can be implemented using AWS CloudTrail to monitor all activities across your organization.</li>
        <li>Data from all AWS config rules can be aggregated to quickly audit your environment for compliance.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-Service-Catalog_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Service Catalog</h2>

<ul>
  <li>AWS Service Catalog empowers you to set up and centrally manage catalogs of approved IT services that you specify on AWS.</li>
  <li>You can manage IT services, referred to as products in Service Catalog, and then group them in a portfolio.</li>
  <li>In AWS Service Catalog, a product can be a machine image, application server, program, tool, database, or other services that you use for your cloud architecture.</li>
  <li>AWS Service Catalog assists you in meeting your compliance requirements.</li>
  <li>It enforces granular access control that allows only the deployment of approved IT services through AWS Cloud.</li>
</ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-Control-Tower_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Control Tower</h2>
        <ul>
        <li>AWS Control Tower is a service that helps you set up and govern a secure multi-account AWS environment.</li>
        <li>It automates the setup of your multi-account architecture with just a few clicks.</li>
        <li>The setup uses blueprints that follow AWS best practices for security and management.</li>
        <li>Control Tower provides mandatory high-level rules, called guardrails, that help enforce policies using Service Control Policies (SCPs) or detect policy violations using AWS Config rules.</li>
        </ul>
    </td>
  </tr>
</table>

## <a id="aws-identity-services"></a> $${\color{navy}AWS\ identity\ services}$$

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Identity-and-Access-Management_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS IAM</h2>
        <ul>
        <li>AWS Identity and Access Management (IAM) is the primary identity service in AWS.</li>
        <li>IAM enables you to manage access to various AWS services and resources securely.</li>
        <li>With IAM, you can:
            <ul>
            <li>Create and manage AWS users and groups, known as IAM users and IAM groups respectively.</li>
            <li>An IAM user has long-term credentials, such as a password or a set of access keys.</li>
            <li>Create a policy called an IAM policy that contains permissions to allow access to AWS resources.</li>
            <li>Attach IAM policies to IAM users and IAM groups.</li>
            <li>Create a role-based entity called an IAM role, which has a set of permissions.</li>
            <li>IAM roles allow an IAM user, another AWS account, or other AWS services to perform defined functions.</li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Single-Sign-On_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS SSO</h2>
        <ul>
        <li>AWS Single Sign-On (SSO) is an authentication mechanism that allows users to log in with a single ID and password to access multiple and independent software systems.</li>
        <li>With SSO, users only need to remember and use one set of credentials to log in across different systems.</li>
        <li>AWS SSO provides a user portal within AWS where users can access the roles they can assume in their assigned AWS accounts or business applications from a single location.</li>
        <li>AWS SSO offers pre-configured SAML integrations with many business applications such as Salesforce, Office 365, and other apps.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_Amazon-Cognito_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Cognito</h2>
        <ul>
        <li>Amazon Cognito is an identity service for adding user sign-up, sign-in, and access control features to web or mobile apps.</li>
        <li>Users can log in with social media accounts such as Facebook, Google, Amazon, or other providers.</li>
        <li>Supports enterprise identity providers, such as Microsoft Active Directory via Security Assertion Markup Language (SAML).</li>
        <li>Amazon Cognito offers two types of pools:
            <ul>
            <li><strong>User Pools:</strong> For authentication; allows users to sign in through their social identity providers.</li>
            <li><strong>Identity Pools:</strong> For authorization; provides temporary and limited-privilege AWS credentials to access other AWS services.</li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Directory-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Directory Service</h2>
        <ul>
        <li>AWS Directory Service is essentially a managed Microsoft Active Directory (AD).</li>
        <li>This service is built on actual Microsoft AD and does not require synchronization or replication of data from an existing Active Directory to the cloud.</li>
        <li>With AWS Directory Service, there is no need to install and manage an Active Directory domain controller on an Amazon EC2 instance.</li>
        <li>It improves the security of your architecture and reduces the administrative burden on IT staff.</li>
        <li>Allows assignment of IAM roles to Active Directory users and groups in AWS, as well as in existing on-premises Microsoft Active Directory using an AD Connector.</li>
        </ul>
    </td>
  </tr>
</table>


## <a id="aws-machine-learning-services"></a> $${\color{maroon}AWS\ machine\ learning\ services}$$

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-SageMaker_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS SageMaker</h2>
        <ul>
            <li><strong>Amazon SageMaker:</strong> A full-fledged machine learning platform in AWS with extensive services, features, and components.</li>
            <li>Not just a simple ML service, but a fully managed cloud platform with many modules.</li>
            <li>Capabilities include building, training, and deploying ML models for any use case with managed infrastructure, tools, and workflows.</li>
            <li>Removes manual tasks from each step of the ML process to facilitate high-quality model development.</li>
            <li>Includes various modules such as:</li>
            <ul>
                <li>Amazon SageMaker Canvas</li>
                <li>SageMaker Studio Lab</li>
                <li>SageMaker Data Wrangler</li>
                <li>SageMaker Autopilot</li>
                <li>SageMaker Jumpstart</li>
                <li>SageMaker Clarify</li>
                <li>And more...</li>
            </ul>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Rekognition_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Rekognition</h2>
        <ul>
        <li>Amazon Rekognition provides pre-trained and customizable computer vision capabilities to extract information and insights from images and videos.</li>
        <li>It can recognize certain objects, faces, texts, scenes, labels, and other attributes from media files or streaming videos.</li>
        <li>The service is particularly effective for facial recognition, detecting specific people or well-known celebrities.</li>
        <li>It can determine if someone is wearing personal protective equipment such as masks, helmets, or gloves.</li>
        <li>It can detect objects in an image, such as identifying a face, a guitar, and a sofa in a single image.</li>
        <li>Amazon Rekognition custom Labels allows you to build a machine learning model to classify custom components or products from your dataset.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Lookout-for-Vision_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Lookout for Vision</h2>
        <ul>
        <li>Amazon Lookout is a suite of services that includes:
            <ul>
            <li>Amazon Lookout for Equipment</li>
            <li>Amazon Lookout for Metrics</li>
            <li>Amazon Lookout for Vision
                <ul>
                <li>Uses computer vision to detect defects on industrial products at scale</li>
                <li>Primarily used in factories and manufacturing lines</li>
                <li>Can identify defects such as dents, cracks, and scratches</li>
                <li>Dataset can be in the form of product images stored in an Amazon S3 bucket</li>
                <li>Requires a couple of baseline images of defect-free products</li>
                <li>Automatically builds a model within a few hours</li>
                </ul>
            </li>
            </ul>
        </li>
        <li>Amazon Textract:
            <ul>
            <li>Service name is a combination of the words text and extract</li>
            <li>Used to extract text from scanned documents, notes, and images</li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_AWS-Panorama_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Panorma</h2>
        <ul>
        <li><strong>AWS Panorama:</strong> A service that brings computer vision to your on-premises camera network.</li>
        <li><strong>Installation:</strong> Install the AWS Panorama Appliance or another compatible device in your datacenter.</li>
        <li><strong>Registration:</strong> Register the appliance with AWS Panorama.</li>
        <li><strong>Deployment:</strong> Deploy computer vision applications from the cloud using AWS Panorama.</li>
        <li><strong>Camera Compatibility:</strong> Works with existing real-time streaming protocol (RTSP) network cameras.</li>
        <li><strong>AWS Panorama Appliance:</strong>
            <ul>
            <li>Compact edge appliance optimized for machine learning workloads.</li>
            <li>Runs multiple computer vision models against multiple video streams in parallel.</li>
            <li>Outputs results in real-time.</li>
            <li>Designed for commercial and industrial settings.</li>
            <li>Rated for dust and liquid protection (IP-62).</li>
            </ul>
        </li>
        <li><strong>Edge Processing:</strong> Enables running self-contained computer vision applications at the edge without sending images to the AWS Cloud.</li>
        <li><strong>Integration with AWS Services:</strong> 
            <ul>
            <li><strong>Analyze Traffic Patterns:</strong> Use AWS SDK to record data in Amazon DynamoDB, analyze data over time with a serverless application, detect anomalies, and predict future behavior.</li>
            <li><strong>Receive Site Safety Alerts:</strong> Monitor off-limits areas, upload images to Amazon S3, and send notifications to Amazon SNS for corrective action.</li>
            <li><strong>Improve Quality Control:</strong> Monitor assembly line output, identify nonconforming parts, highlight images, and display them for review by the quality control team.</li>
            <li><strong>Collect Training and Test Data:</strong> Upload images where the model couldn't identify or had borderline confidence, create a queue of images needing tagging, tag them, and use them to retrain the model in Amazon SageMaker.</li>
            </ul>
        </li>
        <li><strong>AWS Panorama Integration:</strong> Uses other AWS services to manage the appliance, access models and code, and deploy applications.</li>
        <li><strong>Service Interaction:</strong> AWS Panorama does as much as possible without requiring interaction with other services, but knowledge of the following services can be helpful.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Textract_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Textract</h2>
        <ul>
        <li>Amazon Textract is a service that uses optical character recognition to automatically extract text from various scanned files such as PDFs, documents, handwritten notes, receipts, passports, and IDs.</li>
        <li>The service can generate results in table form or as a CSV file.</li>
        <li>It includes a query feature that allows extraction of specific fields using natural language questions. For example, querying "What's the first name?" on a driver's license will return the first name.</li>
        <li>You can batch upload documents to S3, where the text analysis process can be automated.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Augmented-AI-A2I_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS A2I</h2>
        <ul>
        <li>Amazon Augmented AI (A2I) provides human review workflows for common machine learning use cases.</li>
        <li>A human review involves a person reviewing the output generated by your machine learning model before proceeding to the next step in the workflow.</li>
        <li>The service augments your AI to ensure prediction accuracy and aids in continuous improvements to your machine learning model.</li>
        <li>Direct integration is possible with Amazon Rekognition and Amazon Textract.</li>
        <li>Examples of integration:
            <ul>
            <li>Human review of key-value pairs extracted by Amazon Textract.</li>
            <li>Image moderation through human review of unsafe content, such as explicit or violent content, from Amazon Rekognition.</li>
            </ul>
        </li>
        <li>Custom machine learning workflows can also be used with Amazon Augmented AI for human review.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Comprehend_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Comprehend</h2>
        <ul>
        <li>Amazon Comprehend is a natural language processing service in AWS that can find insights and relationships in a text.</li>
        <li>It performs text analytics that can automatically:
            <ul>
            <li>Extract key phrases</li>
            <li>Analyze sentiment</li>
            <li>Identify language</li>
            <li>Analyze syntax</li>
            <li>Identify topics</li>
            <li>Detect personally identifiable information (PII)</li>
            </ul>
        </li>
        <li>Amazon Comprehend works with unstructured data.</li>
        <li>Amazon Comprehend cannot read text from scanned documents; it requires raw text data.</li>
        <li>Amazon Comprehend is different from Amazon Textract, which can read text from scanned documents.</li>
        <li>Moving on to the language AI section.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Lex_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Lex</h2>
        <ul>
            <li>Amazon Lex is a machine learning service for developing chatbots.</li>
            <li>You can build both voice-based and text-based chatbots with Amazon Lex.</li>
            <li>Amazon Lex is useful for creating self-service bots or virtual agents for various applications, including conversational interactive voice response systems and corporate websites.</li>
            <li>Using Amazon Lex can help reduce the cost of maintaining contact centers for companies.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Transcribe_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Transcribe</h2>
        <ul>
        <li>Amazon Transcribe is a speech-to-text transcription service.</li>
        <li>The word "transcribe" means to make a written record of speech, a phone call, or any spoken language.</li>
        <li>Amazon Transcribe generates written records of spoken language.</li>
        <li>It is useful in contact centers to generate call transcripts and provide conversation insights.</li>
        <li>Amazon Transcribe helps improve customer experience and agent productivity.</li>
        <li>It offers real-time transcription, generating transcripts of speech immediately when talking to its endpoint.</li>
        <li>Another service related to language AI is Amazon Polly.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Polly_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Polly</h2>
        <ul>
        <li>Amazon Polly converts text into speech, whereas Amazon Transcribe converts speech into text.</li>
        <li>Inputting text into Amazon Polly generates lifelike speech in various voices (e.g., male, female, kid's voice).</li>
        <li>Customizable pronunciation for specific words and phrases can be achieved by uploading lexicon files.</li>
        <li>A lexicon is a vocabulary of a particular language, useful for non-English text-to-speech conversion.</li>
        <li>The topic is in the customer experience improvement category.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Kendra_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Kendra</h2>
        <ul>
            <li>Amazon Kendra is an intelligent search service in AWS.</li>
            <li>It can search across multiple data sources, both structured and unstructured.</li>
            <li>Amazon Kendra intelligently analyzes content before providing search results.</li>
            <li>The service supports natural language processing (NLP).</li>
            <li>Users can ask questions in everyday language (e.g., "Who is the founder of Star Trek?").</li>
            <li>Amazon Kendra searches across various data sources, including:
                <ul>
                    <li>SQL databases</li>
                    <li>Amazon FSx file systems</li>
                    <li>Amazon RDS databases</li>
                    <li>AWS repositories</li>
                    <li>JIRA</li>
                    <li>Slack</li>
                    <li>SharePoint</li>
                    <li>Other data sources</li>
                </ul>
            </li>
            <li>It uses machine learning to provide context through search results.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Personalize_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Personalize</h2>
        <ul>
        <li>Amazon Personalize is a service that provides personalized recommendations based on customer past activity and behavior.</li>
        <li>It functions similarly to the recommendation features in Amazon Prime or Netflix.</li>
        <li>For example, if a user watches a lot of Sci-Fi movies, Amazon Personalize will recommend more Sci-Fi shows on their profile.</li>
        <li>This personalization improves customer experience by aligning recommendations with the customer's actual interests and purchase behavior.</li>
        <li>Personalized content tends to convert more effectively as it matches what customers are likely to do and buy.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Translate_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Translate</h2>
        <ul>
        <li>Amazon Translate is a real-time translation service in AWS.</li>
        <li>It functions similarly to Google Translate, allowing you to input text in one language and translate it to a chosen language.</li>
        <li>You can create custom terminology to tailor the translation output based on specific vocabulary.</li>
        <li>Custom terms can be used in translations; for example, you can define the acronym "TD" as "Towards Death."</li>
        <li>Amazon Translate can incorporate these custom terms in translations. For instance, translating "Magandang umaga, TD" from Tagalog to English will yield "Good Morning Towards Death."</li>
        <li>The formality option controls whether the translation output uses a formal tone.</li>
        <li>Amazon Translate can mask profane words or phrases, which is useful for customer-facing applications.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Forecast_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Forecast</h2>
        <ul>
            <li>Amazon Forecast is a machine learning service in AWS.</li>
            <li>It helps forecast future outcomes based on historical records and other relevant data.</li>
            <li>You can import or stream your time series data to Amazon Forecast.</li>
            <li>It can forecast various metrics such as sales, web traffic, inventory, revenue, cloud resource capacity, or actual weather.</li>
            <li>It can predict your future AWS bill.</li>
            <li>Amazon Forecast includes built-in data sets like weather index and national holidays for various countries.</li>
            <li>The service uses a machine learning model called a predictor.</li>
            <li>The predictor uses an algorithm to analyze time series data and generate predictions.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Fraud-Detector_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Fraud Detector</h2>
        <ul>
        <li>Amazon Fraud Detector is a machine learning service for automating fraud detection.</li>
        <li>It can identify potential fraudulent activities, fake reviews, and spam account creation in near real-time.</li>
        <li>For example, it can handle situations where a visitor's IP address has a history of malicious activities such as spamming, hacking attempts, and DDoS attacks.</li>
        <li>Amazon Fraud Detector can be used to block visitors who use offending IP addresses, email domains, or any other defined attributes.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Lookout-for-Metrics_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Lookout for Metrics</h2>
        <ul>
        <li>Amazon Lookout for Metrics is a service in the Amazon Lookout family.</li>
        <li>It detects anomalies in business metrics.</li>
        <li>An anomaly could be a sudden drop in sales revenue or an unexpected decline in customer acquisition rates.</li>
        <li>The service identifies unusual variances in business metrics.</li>
        <li>It provides immediate alerts to help you take appropriate action.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-DevOps-Guru_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS DevOps Guru</h2>
        <ul>
            <li>Amazon DevOps Guru detects abnormal behavior in your application or AWS sources that may cause unexpected downtimes or operational issues in the near future.</li>
            <li>It can monitor applications in AWS resources within your own account or on all accounts across your AWS organization.</li>
            <li>It uses machine learning to identify operational defects long before they impact you and your customers.</li>
            <li>Amazon DevOps Guru can analyze your RDS databases and automatically determine an unusually high DB load that is more than three times or five times its normal value.</li>
            <li>It can detect issues in your serverless stack, such as an extremely high number of invocations in your Lambda function beyond the currently provisioned concurrency.</li>
            <li>It can also detect an over-provisioned red capacity on your DynamoDB tables.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-CodeGuru_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS CodeGuru</h2>
        <ul>
        <li>Amazon CodeGuru is a suite of development services in AWS.</li>
        <li>It includes tools and features such as:
            <ul>
            <li>Amazon CodeGuru Reviewer</li>
            <li>Amazon CodeGuru Profiler</li>
            <li>Bug Bust</li>
            <li>And many more</li>
            </ul>
        </li>
        <li>The primary function of Amazon CodeGuru Reviewer is to:
            <ul>
            <li>Provide intelligent recommendations for improving application performance, efficiency, and code quality.</li>
            <li>Scan code and detect various code defects, including:
                <ul>
                <li>Bad exception handling</li>
                <li>Insecure course policy</li>
                <li>Path reversal</li>
                <li>Hardcoded credentials</li>
                <li>And more</li>
                </ul>
            </li>
            <li>Integrate with CI/CD workflow for code reviews and recommendations.</li>
            </ul>
        </li>
        <li>Amazon CodeGuru Profiler:
            <ul>
            <li>Collects CPU data and analyzes runtime performance data from live applications.</li>
            <li>Helps identify expensive lines of code that inefficiently use the CPU, causing CPU bottlenecks.</li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>
</table>


## <a id="aws-transfer-and-migration-services"></a> $${\color{olive}AWS\ transfer\ and\ migration\ services}$$

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Migration-Transfer/64/Arch_AWS-DataSync_64.svg" alt="">
    </td>
    <td class="content">
      <h2A>AWS DataSync</h2>
        <ul> <li><strong>AWS DataSync Overview:</strong> An online data transfer and discovery service that simplifies and secures data migration between various storage services.</li> <li><strong>On-Premises Storage Transfers:</strong> <ul> <li>Network File System (NFS)</li> <li>Server Message Block (SMB)</li> <li>Hadoop Distributed File Systems (HDFS)</li> <li>Object storage</li> </ul> </li> <li><strong>AWS Storage Transfers:</strong> <ul> <li>Amazon S3</li> <li>Amazon EFS</li> <li>Amazon FSx for Windows File Server</li> <li>Amazon FSx for Lustre</li> <li>Amazon FSx for OpenZFS</li> <li>Amazon FSx for NetApp ONTAP</li> </ul> </li> <li><strong>Other Cloud Storage Transfers:</strong> <ul> <li>Google Cloud Storage</li> <li>Microsoft Azure Blob Storage</li> <li>Microsoft Azure Files</li> <li>Wasabi Cloud Storage</li> <li>DigitalOcean Spaces</li> <li>Oracle Cloud Infrastructure Object Storage</li> <li>Cloudflare R2 Storage</li> <li>Backblaze B2 Cloud Storage</li> <li>NAVER Cloud Object Storage</li> <li>Alibaba Cloud Object Storage Service</li> <li>IBM Cloud Object Storage</li> <li>Seagate Lyve Cloud</li> </ul> </li> <li><strong>Edge Storage Transfers:</strong> <ul> <li>Amazon S3 compatible storage on AWS Snowball Edge</li> <li>AWS Snowcone</li> </ul> </li> <li><strong>Use Cases:</strong> <ul> <li>Discover data – Gain visibility into on-premises storage performance and get migration recommendations.</li> <li>Migrate data – Rapidly transfer active datasets to AWS with encryption and integrity validation.</li> <li>Archive cold data – Move cold data to long-term storage classes like S3 Glacier to free up on-premises storage.</li> <li>Replicate data – Copy data to Amazon S3 storage classes or other AWS storage services for standby or backup.</li> <li>Transfer data for timely in-cloud processing – Accelerate hybrid cloud workflows for various industries.</li> </ul> </li> <li><strong>Benefits:</strong> <ul> <li>Simplify migration planning – Automated data collection and recommendations to minimize migration costs and effort.</li> <li>Automate data movement – Easier data transfer with automated management and high performance infrastructure.</li> <li>Transfer data securely – End-to-end security with encryption, integrity validation, and optional VPC endpoints.</li> <li>Move data faster – Accelerated transfers using a purpose-built network protocol and parallel architecture.</li> <li>Reduce operational costs – Flat per-gigabyte pricing and avoidance of custom scripts or costly tools.</li> </ul> </li> </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Migration-Transfer/64/Arch_AWS-Transfer-Family_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Transfer Family</h2>
        <ul> <li><strong>AWS Transfer Family Overview:</strong> A secure, fully managed service for transferring files into and out of AWS storage services (Amazon S3 and Amazon EFS). It supports SFTP, FTPS, FTP, and AS2 protocols.</li> <li><strong>Protocols Supported:</strong> <ul> <li>SFTP (version 3)</li> <li>FTPS</li> <li>FTP</li> <li>AS2</li> </ul> </li> <li><strong>Port Range for FTP and FTPS:</strong> 8192–8200</li> <li><strong>Use Cases:</strong> <ul> <li>Data lakes with third-party uploads</li> <li>Subscription-based data distribution</li> <li>Internal organizational transfers</li> <li>Data distribution and supply chain management</li> <li>Compliance and security workflows (AS2)</li> <li>Business-to-business transactions</li> </ul> </li> <li><strong>Benefits:</strong> <ul> <li>Fully managed and scalable in real-time</li> <li>No need to modify applications or manage infrastructure</li> <li>Integration with AWS services for processing and analytics</li> <li>Elastic and fully managed file system with Amazon EFS</li> <li>Serverless File Transfer Workflow service for automation and monitoring</li> <li>No upfront costs; pay-as-you-go</li> </ul> </li> <li><strong>Transfer Family Managed File Transfer Workflows (MFTW):</strong> Automates processing steps such as copying, tagging, scanning, filtering, and encrypting/decrypting data. Provides end-to-end visibility for tracking and auditability.</li> <li><strong>Supported File Transfer Protocol Clients:</strong> <ul> <li>OpenSSH (Mac/Linux)</li> <li>WinSCP (Windows)</li> <li>Cyberduck (Linux/Mac/Windows)</li> <li>FileZilla (Linux/Mac/Windows)</li> </ul> </li> <li><strong>Workshops Offered:</strong> <ul> <li>Building a file transfer solution with SFTP/FTPS and Amazon Cognito/DynamoDB</li> <li>Creating an AS2-enabled endpoint with Transfer Family AS2 connector</li> <li>Developing a scalable and secure file transfer architecture on AWS</li> </ul> </li> </ul>    
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_AWS-Snowmobile_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Snow Family</h2>
        <ul>
        <li><strong>AWS Snow Family</strong>
            <ul>
            <li>Comprises of AWS Snowcone, Snowball, and AWS Snowmobile</li>
            <li>Physical devices for data transfer and edge computing</li>
            <li>Helps with operations in non-data center environments and locations with inconsistent network connectivity</li>
            <li>Devices are owned and managed by AWS, integrating with AWS security, monitoring, and computing capabilities</li>
            </ul>
        </li>

        <li><strong>Snowcone</strong>
            <ul>
            <li>Smallest member of the Snow Family</li>
            <li>Portable, rugged, and secure</li>
            <li>Used for collecting, processing, and moving data to AWS</li>
            <li>Data transfer options: offline by shipping or online with AWS DataSync</li>
            <li>Costs: Pay per device use and data transfer out of AWS; no transfer fees for offline data transfer</li>
            <li>Service fee per job includes five days of device use; additional daily fees or monthly rental options available</li>
            <li>For high-volume deployments, contact AWS sales team</li>
            <li>For pricing details, see <a href="https://aws.amazon.com/snowcone/pricing">AWS Snowcone Pricing</a></li>
            </ul>
        </li>

        <li><strong>Snowball</strong>
            <ul>
            <li>Data migration and edge computing device with two options: Compute Optimized and Storage Optimized</li>
            <li>Snowball Edge Storage Optimized: 40 vCPUs, 80 TB of storage</li>
            <li>Snowball Edge Compute Optimized: 52 vCPUs, 42 TB of storage, optional GPU</li>
            <li>Used for local storage, large-scale data transfer, ML, and processing in intermittent connectivity or remote locations</li>
            <li>Pricing elements: usage, device type, and term of use</li>
            <li>On-demand use: Service fee per data transfer job, including 10 days of device usage; additional daily fees after 10 days</li>
            <li>One-year or three-year commitments: Contact AWS sales team</li>
            <li>Data transferred into AWS does not incur transfer fees; standard pricing applies for data stored in AWS</li>
            <li>For pricing details, see <a href="https://aws.amazon.com/snowball/pricing">AWS Snowball Pricing</a></li>
            </ul>
        </li>

        <li><strong>Snowmobile</strong>
            <ul>
            <li>Largest member of the Snow Family</li>
            <li>Designed for massive-scale data transfer (up to exabytes)</li>
            <li>Used for large data migrations and moving data to AWS from on-premises or other data centers</li>
            <li>Provides a secure, rugged, and portable solution for extremely large datasets</li>
            <li>Data transfer fees: Pay per job and storage costs apply; contact AWS sales team for detailed pricing</li>
            <li>For pricing details, see <a href="https://aws.amazon.com/snowmobile/pricing">AWS Snowmobile Pricing</a></li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Migration-Transfer/64/Arch_AWS-Application-Discovery-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Application Discovery Service</h2>
        <ul> <li><strong>AWS Application Discovery Service</strong> helps plan migration to AWS cloud by collecting data about on-premises servers and databases.</li> <li><strong>Integration:</strong> Works with AWS Migration Hub and AWS Database Migration Service Fleet Advisor. <ul> <li><strong>AWS Migration Hub:</strong> Aggregates migration status information into a single console, allowing tracking of migration status.</li> <li><strong>DMS Fleet Advisor:</strong> Assesses migration options for database workloads.</li> </ul> </li> <li><strong>Data Storage:</strong> Discovered data is stored in the Migration Hub home Region; must set home Region before discovery and migration activities.</li> <li><strong>Data Export:</strong> Data can be exported for analysis in Microsoft Excel or AWS tools like Amazon Athena and Amazon QuickSight.</li> <li><strong>Discovery Methods:</strong> <ul> <li><strong>Agentless Discovery:</strong> Deploys the Application Discovery Service Agentless Collector (OVA file) via VMware vCenter. Collects static configuration and utilization data for VMs.</li> <li><strong>Agent-Based Discovery:</strong> Deploys AWS Application Discovery Agent on VMs and physical servers. Collects static configuration data, time-series performance data, network connections, and running processes.</li> </ul> </li> <li><strong>Third-Party Integration:</strong> Supports integration with AWS Partner Network (APN) solutions, allowing data import into Migration Hub using public APIs.</li> <li><strong>VMware Discovery:</strong> Agentless Collector captures data from VMware VMs; cannot capture detailed internal data. Can use both Agentless Collector and Discovery Agent simultaneously.</li> <li><strong>Database Discovery:</strong> Agentless Collector discovers and inventories database servers, captures performance metrics, and uses LDAP for gathering data. Supports database and analytics server performance collection.</li> <li><strong>Comparison:</strong> <ul> <li><strong>Agentless Collector:</strong> <ul> <li>Supported server types: VMware virtual machines.</li> <li>Deployment: Per vCenter.</li> <li>Collected data: Static server and database configuration, VM and database utilization metrics.</li> <li>Supported OS: Any OS in VMware vCenter V5.5+.</li> <li>Supported databases: Oracle, SQL Server, MySQL, PostgreSQL.</li> </ul> </li> <li><strong>Discovery Agent:</strong> <ul> <li>Supported server types: VMware virtual machines and physical servers.</li> <li>Deployment: Per server.</li> <li>Collected data: Static server and database configuration, time series performance data, network connections, running processes.</li> <li>Supported OS: Specific Linux and Windows operating systems.</li> <li>Supported databases: None.</li> </ul> </li> </ul> </li> <li><strong>Assumptions:</strong> Requires AWS account, selected Migration Hub home Region, and use of the selected home Region for discovery and planning data.</li> </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Resource-Icons_07302021/Res_Database/Res_48_Light/Res_AWS-Database-Migration-Service_Database-migration-workflow-job_48_Light.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS DMS</h2>
        <ul>
            <li><strong>AWS Database Migration Service (AWS DMS)</strong>:
                <ul>
                    <li>A cloud service for migrating relational databases, data warehouses, NoSQL databases, and other data stores.</li>
                    <li>Supports migrating data into the AWS Cloud or between cloud and on-premises setups.</li>
                    <li>Allows for one-time migrations and ongoing replication to keep sources and targets in sync.</li>
                    <li>Use the AWS Schema Conversion Tool (AWS SCT) to translate database schema for migration to different database engines.</li>
                </ul>
            </li>
            <li><strong>Issues with AWS DMS:</strong>
                <ul>
                    <li>Check if the version and edition of source and target databases are supported by DMS for both full load and Change Data Capture (CDC).</li>
                    <li>Some database versions are supported only by certain versions of DMS.</li>
                    <li>Example: CDC is not supported for SQL Server 2012 Standard edition using AWS DMS.</li>
                </ul>
            </li>
            <li><strong>SQL Server DMS Version Support:</strong>
                <ul>
                    <li>Support for Microsoft SQL Server version 2019 as a source is available in AWS DMS versions 3.3.2 and later.</li>
                </ul>
            </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Migration-Transfer/64/Arch_AWS-Server-Migration-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Server Migration Service</h2>
        <ul>
        <li><strong>AWS Application Migration Service (MGN):</strong> A highly automated lift-and-shift (rehost) solution for migrating applications to AWS.</li>
        <li><strong>Purpose:</strong> Simplifies, expedites, and reduces the cost of migrating applications.</li>
        <li><strong>Compatibility:</strong> Allows migration of physical, virtual, or cloud servers without compatibility issues or performance disruption.</li>
        <li><strong>Replication:</strong> Replicates source servers into your AWS account.</li>
        <li><strong>Automation:</strong> Automatically converts and launches servers on AWS.</li>
        <li><strong>Benefits:</strong> Provides cost savings, productivity, resilience, and agility of the Cloud.</li>
        <li><strong>Post-Migration:</strong> Enables replatforming or refactoring of applications using AWS services and capabilities.</li>
        <li><strong>Modernization:</strong> Lift-and-shift is a fast route to modernization.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Migration-Transfer/64/Arch_AWS-Migration-Hub_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Migration Hub</h2>
        <ul>
            <li><strong>AWS Migration Hub</strong>: Provides a guided end-to-end migration and modernization journey through discovery, assessment, planning, and execution.</li>
            <li><strong>Features</strong>:
                <ul>
                    <li>Access to the latest guidance and tools from one location.</li>
                    <li>Automated recommendations and prescriptive plans.</li>
                    <li>Cross-team collaboration and tracking to accelerate transformation.</li>
                    <li>Simplifies rehost, refactor, and replatform of applications.</li>
                </ul>
            </li>
            <li><strong>Benefits</strong>:
                <ul>
                    <li><strong>Simplified experience</strong>: Discover, Assess, Analyze, Plan, Execute, and Manage from a single location.</li>
                    <li><strong>Expert guidance</strong>: Accelerate migration and modernization with prescriptive journey templates.</li>
                    <li><strong>Proven tools</strong>: Leverage specialized services designed to meet transformation goals.</li>
                    <li><strong>Free Service</strong>: Get started for free to plan or track migration to AWS.</li>
                </ul>
            </li>
            <li><strong>Use Cases</strong>:
                <ul>
                    <li><strong>Migration Assessment & Planning</strong>: Discover applications for migration and modernization, and define execution strategies.</li>
                    <li><strong>Migration Execution</strong>: Use guided migration journey templates and specialized services, while collaborating across teams to meet migration goals.</li>
                    <li><strong>Modernization</strong>: Fast-track application refactoring, simplify development, and manage applications and microservices as one.</li>
                </ul>
            </li>
        </ul>
    </td>
  </tr>
</table>


## <a id="aws-analytics-services"></a> $${\color{gray}AWS\ analytics\ services}$$

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_Amazon-Kinesis_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Kinesis</h2>
        <ul> <li><strong>Amazon Kinesis</strong>: Suite of services for analyzing data streams in real-time.</li> <li><strong>Data Streams:</strong> <ul> <li>Data is available within milliseconds, enabling near-instantaneous processing.</li> <li>Used for various real-time applications such as website clickstreams, IoT telemetry, and financial transactions.</li> <li>Maintains order of records and allows concurrent consumption by multiple applications.</li> <li>Similar to Amazon SQS but with real-time capabilities and record ordering.</li> <li>Amazon Kinesis Data Streams is suitable for: <ul> <li>Clickstream data analysis</li> <li>Mobile game score updates</li> <li>Predictive maintenance for IoT systems</li> <li>Financial transactions processing</li> </ul> </li> </ul> </li> <li><strong>Amazon Kinesis Data Firehose:</strong> <ul> <li>Fully managed service to transform and load streaming data into data stores.</li> <li>Delivers data to Amazon S3, Amazon Redshift, Amazon Elasticsearch Service, or HTTP endpoints.</li> <li>Transforms data before delivery using Lambda functions.</li> <li>Useful for sending data streams directly to specified destinations without custom applications.</li> </ul> </li> <li><strong>Amazon Kinesis Video Streams:</strong> <ul> <li>Secures streaming video from devices to AWS.</li> <li>Used for video analytics, machine learning, and video playback.</li> <li>Automatically provisions and scales infrastructure to handle video data.</li> <li>Provides APIs for video data access.</li> </ul> </li> <li><strong>Amazon Kinesis Data Analytics:</strong> <ul> <li>Serverless service for analyzing streaming data and acquiring actionable insights.</li> <li>Uses Apache Flink for processing and analyzing data.</li> <li>Reduces complexity by eliminating server management and integration overhead.</li> <li>Supports SQL queries and real-time dashboards.</li> <li>Integrates with other AWS services like Amazon S3 and Amazon Redshift.</li> <li>Use cases include: <ul> <li>Real-time data processing and querying</li> <li>Time series analytics</li> <li>Real-time metrics</li> </ul> </li> </ul> </li> </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_Amazon-Athena_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Athena</h2>
        <ul>
            <li>Amazon Athena:
                <ul>
                    <li>An interactive query service for data stored in Amazon S3.</li>
                    <li>Simplifies data analysis in S3 using standard SQL.</li>
                    <li>Can query a subset of S3 data using S3 Select with simple SQL statements, but Athena is more powerful.</li>
                    <li>Serverless, meaning you only pay for the specific queries you run.</li>
                    <li>Example use case: Identifying the number of items sold in each region for the previous month from 250 gigabytes of transactional data stored in S3.</li>
                    <li>Alternative AWS services for similar tasks: Amazon Redshift, Amazon EMR, and Amazon ES cluster, but they are not serverless and may have higher operating costs.</li>
                    <li>Can integrate with other AWS services:
                        <ul>
                            <li>Uses AWS Glue Data Catalog to store and achieve table metadata for S3 data.</li>
                            <li>Provides data visualization using Amazon QuickSight.</li>
                        </ul>
                    </li>
                </ul>
            </li>
            <li>Amazon Elasticsearch Service:
                <ul>
                    <li>A fully managed Elasticsearch service.</li>
                    <li>Elasticsearch is a search engine based on the Apache Lucene library.</li>
                    <li>Distributed, multi-tenant capable full-text search engine.</li>
                    <li>Stores data as schemaless JSON documents.</li>
                    <li>Features an HTTP web interface.</li>
                </ul>
            </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_Amazon-Elasticsearch-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS ES</h2>
            <ul>
            <li>Amazon Elasticsearch Service (Amazon ES) abstracts the underlying technology, provisions the necessary infrastructure, and manages resources automatically.</li>
            <li>It allows you to launch an ELK stack in AWS.</li>
            <li>An ELK stack consists of three open-source products:
                <ul>
                <li>Elasticsearch</li>
                <li>Logstash: A server-side data processing pipeline</li>
                <li>Kibana: A user interface for visualizing Elasticsearch data</li>
                </ul>
            </li>
            <li>Amazon ES provides support for:
                <ul>
                <li>Open source Elasticsearch APIs</li>
                <li>Managed Kibana</li>
                <li>Integration with Logstash</li>
                <li>Other AWS services</li>
                </ul>
            </li>
            <li>Amazon ES follows a pay-as-you-go model, meaning there are no upfront costs or usage requirements.</li>
            </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_Amazon-EMR_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS EMR</h2>
        <ul>
        <li><strong>Amazon Elastic MapReduce (Amazon EMR)</strong>
            <ul>
            <li>Managed big data platform for processing large amounts of data.</li>
            <li>Supports open source tools such as:
                <ul>
                <li>Apache Hadoop</li>
                <li>Flink</li>
                <li>HBase</li>
                <li>HCatalog</li>
                <li>Hive</li>
                <li>Hudi</li>
                <li>Hue</li>
                <li>Jupyter</li>
                <li>Livy</li>
                <li>MXNet</li>
                <li>Oozie</li>
                <li>Phoenix</li>
                <li>Pig</li>
                <li>Presto</li>
                <li>Spark</li>
                <li>Sqoop</li>
                <li>TensorFlow</li>
                <li>Text</li>
                <li>Zeppelin</li>
                <li>ZooKeeper</li>
                </ul>
            </li>
            <li>Runs on Amazon EC2 instances, Amazon EKS clusters, or on-premises via AWS Outposts.</li>
            <li>Deployed in a VPC and grouped as an Amazon EMR cluster.</li>
            <li>Direct access and control of the underlying EC2 instances is possible.</li>
            <li>Not serverless; automates server provisioning and management.</li>
            <li>Can interact with other AWS data stores such as:
                <ul>
                <li>Amazon S3</li>
                <li>Amazon DynamoDB</li>
                </ul>
            </li>
            </ul>
        </li>
        <li><strong>Amazon QuickSight</strong>
            <ul>
            <li>Scalable, serverless business intelligence service.</li>
            <li>Provides interactive dashboards that can be accessed from:
                <ul>
                <li>Different browsers</li>
                <li>Mobile devices</li>
                </ul>
            </li>
            <li>Supports embedding dashboards in applications.</li>
            <li>Machine learning powered for advanced analytics.</li>
            </ul>
        </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_Amazon-QuickSight_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS QuickSight</h2>
        <ul>
        <li><strong>Amazon QuickSight:</strong>
            <ul>
            <li>Highly scalable</li>
            <li>Scales up to thousands of users</li>
            <li>No software installation needed</li>
            <li>No servers to deploy</li>
            <li>No infrastructure to manage</li>
            </ul>
        </li>
        <li><strong>Amazon CloudSearch:</strong>
            <ul>
            <li>Managed search service in AWS</li>
            <li>Useful for implementing search features in applications</li>
            <li>Capabilities include:
                <ul>
                <li>Retrieve contents of selected fields</li>
                <li>Provide facet information for result categorization</li>
                <li>Statistics for numeric field values</li>
                <li>Highlight search hits in field data</li>
                <li>Autocomplete suggestions</li>
                <li>Geospatial search</li>
                </ul>
            </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_Amazon-CloudSearch_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS CloudSearch</h2>
        <ul>
            <li>Amazon CloudSearch is a managed search service in AWS.</li>
            <li>Helpful for implementing a search feature in applications.</li>
            <li>Features include:
                <ul>
                    <li>Retrieving contents of selected fields</li>
                    <li>Providing facet information to categorize results</li>
                    <li>Statistics for numeric fields</li>
                    <li>Highlights showing search hits in field data</li>
                    <li>Autocomplete suggestions</li>
                    <li>Geospatial search</li>
                </ul>
            </li>
            <li>Allows creation of a search domain, specification of an index, and uploading of data as documents.</li>
            <li>CloudSearch provisions and manages all underlying servers and resources for building and deploying search indexes.</li>
            <li>Users need to upload data to a search domain and integrate it into applications.</li>
            <li>CloudSearch serves as both a database service and an analytic service in AWS.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_Amazon-Redshift_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS RedShift</h2>
        <ul>
            <li>Amazon Redshift:
                <ul>
                    <li>A fast, scalable data warehouse for analyzing data across data warehouses and data lakes.</li>
                    <li>Delivers 10 times faster performance than other data warehouses using:
                        <ul>
                            <li>Machine learning</li>
                            <li>Massively parallel query execution</li>
                            <li>Columnar storage on high-performance disks</li>
                        </ul>
                    </li>
                    <li>Can run queries across petabytes of data in Redshift and analyze exabytes in Amazon S3 data lake.</li>
                    <li>Primarily used for Online Analytical Processing (OLAP) applications and reporting tools.</li>
                    <li>Runs on internal Amazon EC2 instances configured as nodes. Node type and instance size can be selected.</li>
                    <li>Not a serverless service; costs are associated with the EC2 instances used.</li>
                    <li>Features Redshift Spectrum:
                        <ul>
                            <li>Allows querying data from Amazon S3 without loading all data into Redshift tables.</li>
                            <li>Uses massive parallelism to quickly execute large data sets at a fraction of the cost.</li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_AWS-Data-Pipeline_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS DataPipeLine</h2>
        <ul>
            <li>AWS Data Pipeline is a service for processing and moving data between AWS compute and storage services.</li>
            <li>It allows you to process and move data at specified intervals defined by you.</li>
            <li>Data can be transferred to and from on-premises data centers.</li>
            <li>You can regularly access, transform, and process data at scale.</li>
            <li>The service supports transferring and storing results to various AWS services, including:
                <ul>
                    <li>Amazon S3</li>
                    <li>Amazon RDS</li>
                    <li>Amazon DynamoDB</li>
                    <li>Amazon EMR</li>
                </ul>
            </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_AWS-Glue_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Glue</h2>
        <ul>
        <li>AWS Glue is a fully managed and serverless service.</li>
        <li>It is primarily used for Extract, Transform, and Load (ETL) workloads.</li>
        <li>AWS Glue simplifies the process of preparing and loading data for analytics workloads.</li>
        <li>In AWS Glue, you can create a data catalog to specify and search your data stored on Amazon S3 and other AWS services.</li>
        <li>AWS Glue can automatically discover your data and store the associated metadata in the AWS Glue Data Catalog.</li>
        <li>Once metadata is stored, your data becomes immediately searchable, queryable, and available for ETL.</li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_Amazon-Managed-Streaming-for-Apache-Kafka_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Managed Streaming for Apache Kafka</h2>
        <ul>
            <li>Amazon Managed Streaming for Apache Kafka is a fully managed Apache Kafka service in AWS.</li>
            <li>Apache Kafka is an open source platform for building real-time streaming data pipelines and applications.</li>
            <li>With Amazon Managed Streaming for Apache Kafka, you can:
                <ul>
                    <li>Use Apache Kafka APIs to stream changes to and from different databases.</li>
                    <li>Populate your Amazon S3 data lakes.</li>
                    <li>Empower machine learning and analytics applications.</li>
                </ul>
            </li>
        </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_AWS-Lake-Formation_64.svg" alt="">
    </td>
    <td class="content">
      <h2>AWS Lake Formation</h2>
        <ul>
        <li>AWS Lake Formation simplifies the setup of a secure data lake.</li>
        <li>A data lake is a centralized, curated, and secured repository for storing all types of data, whether structured or raw.</li>
        <li>Like AWS Glue, Lake Formation helps create data catalogs for external data sources.</li>
        <li>The service collects and catalogs data from various sources and transfers it into an Amazon S3 data lake.</li>
        <li>It classifies and processes data using machine learning algorithms.</li>
        <li>Lake Formation secures access to sensitive data.</li>
        <li>Data in the data lake can be queried and analyzed using services like Amazon Athena, Amazon Redshift, Amazon EMR, and others.</li>
        </ul>
    </td>
  </tr>
</table>

</body>
</html>