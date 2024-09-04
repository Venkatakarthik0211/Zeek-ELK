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
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_Amazon-Simple-Queue-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_Amazon-Simple-Notification-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_AWS-Step-Functions_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_Amazon-MQ_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_Amazon-EventBridge_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_AWS-AppSync_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_Amazon-AppFlow_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
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
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Firewall-Manager_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Shield_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_Amazon-GuardDuty_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-CloudHSM_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Key-Management-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Secrets-Manager_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Certificate-Manager_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_Amazon-Macie_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_Amazon-Inspector_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_Amazon-Detective_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
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
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Developer-Tools/64/Arch_AWS-Command-Line-Interface_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_App-Integration/Arch_64/Arch_AWS-Console-Mobile-Application_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Resource-Access-Manager_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-Systems-Manager_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-Config_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-Organizations_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-Service-Catalog_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-Control-Tower_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
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
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Single-Sign-On_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_Amazon-Cognito_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Directory-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
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
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Rekognition_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Lookout-for-Vision_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_AWS-Panorama_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Textract_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Augmented-AI-A2I_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Comprehend_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Lex_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Transcribe_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Polly_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Kendra_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Personalize_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Translate_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Forecast_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Fraud-Detector_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-Lookout-for-Metrics_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-DevOps-Guru_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Machine-Learning/64/Arch_Amazon-CodeGuru_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
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
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Migration-Transfer/64/Arch_AWS-Transfer-Family_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_AWS-Snowmobile_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Migration-Transfer/64/Arch_AWS-Application-Discovery-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Resource-Icons_07302021/Res_Database/Res_48_Light/Res_AWS-Database-Migration-Service_Database-migration-workflow-job_48_Light.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Migration-Transfer/64/Arch_AWS-Server-Migration-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Migration-Transfer/64/Arch_AWS-Migration-Hub_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Migration-Transfer/64/Arch_AWS-Migration-Evaluator_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
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
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_Amazon-Athena_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_Amazon-Elasticsearch-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_Amazon-EMR_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_Amazon-QuickSight_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_Amazon-CloudSearch_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_Amazon-Redshift_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_AWS-Data-Pipeline_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_AWS-Glue_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_Amazon-Managed-Streaming-for-Apache-Kafka_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Analytics/Arch_64/Arch_AWS-Lake-Formation_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
</table>

</body>
</html>