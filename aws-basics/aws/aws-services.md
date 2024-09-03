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
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_Amazon-Elastic-Block-Store_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_Amazon-Simple-Storage-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_Amazon-Simple-Storage-Service-Glacier_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_Amazon-Elastic-File-System_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_Amazon-FSx-for-Lustre_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_Amazon-FSx-for-Windows-File-Server_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_AWS-Backup_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src=https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Storage/64/Arch_AWS-Storage-Gateway_64.svg"" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

</table>

## <a id="aws-database-services"></a> $${\color{purple}AWS\ database\ services}$$

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-RDS_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-Aurora_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-DynamoDB_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-DocumentDB_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-ElastiCache_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Resource-Icons_07302021/Res_Database/Res_48_Light/Res_Amazon-ElastiCache_ElastiCache-for-Redis_48_Light.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
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
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-Keyspaces_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-Neptune_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Database/64/Arch_Amazon-Timestream_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
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
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Compute/64/Arch_AWS-Elastic-Beanstalk_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Developer-Tools/64/Arch_AWS-CodeDeploy_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Containers/64/Arch_Amazon-Elastic-Container-Service_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Containers/64/Arch_Amazon-EKS-Anywhere_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-OpsWorks_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-Proton_64.svg" alt="">
    </td>

</table>

## <a id="aws-monitoring-services"></a> $${\color{brown}AWS\ monitoring\ services}$$

<table>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_Amazon-CloudWatch_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Management-Governance/64/Arch_AWS-Personal-Health-Dashboard_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
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
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Artifact_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Security-Identity-Compliance/64/Arch_AWS-Security-Hub_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>
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
      <h2></h2>
      <ul>    
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_Elastic-Load-Balancing_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>    
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_Amazon-Route-53_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>    
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_AWS-Global-Accelerator_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>    
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_Amazon-CloudFront_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>    
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_AWS-PrivateLink_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>    
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_AWS-Client-VPN_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>    
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_AWS-Direct-Connect_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>    
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_AWS-Transit-Gateway_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>    
      </ul>
    </td>
  </tr>

  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_AWS-App-Mesh_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>    
      </ul>
    </td>
  </tr>
  <tr>
    <td class="image">
      <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Networking-Content-Delivery/64/Arch_AWS-Cloud-Map_64.svg" alt="">
    </td>
    <td class="content">
      <h2></h2>
      <ul>    
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