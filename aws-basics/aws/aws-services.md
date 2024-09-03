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

</body>
</html>


## <a id="aws-container-services"></a> $${\color{green}AWS\ container\ services}$$

## <a id="aws-storage-services"></a> $${\color{orange}AWS\ storage\ services}$$

## <a id="aws-database-services"></a> $${\color{purple}AWS\ database\ services}$$

## <a id="aws-deployment-services"></a> $${\color{red}AWS\ deployment\ services}$$

## <a id="aws-monitoring-services"></a> $${\color{brown}AWS\ monitoring\ services}$$

## <a id="aws-audit-and-compliance-services"></a> $${\color{magenta}AWS\ audit\ and\ compliance\ services}$$

## <a id="aws-networking-and-content-delivery-services"></a> $${\color{cyan}AWS\ networking\ and\ content\ delivery\ services}$$

## <a id="aws-application-integration-services"></a> $${\color{pink}AWS\ application\ integration\ services}$$

## <a id="aws-security-services"></a> $${\color{teal}AWS\ security\ services}$$

## <a id="aws-management-and-governance-services"></a> $${\color{lime}AWS\ management\ and\ governance\ services}$$

## <a id="aws-identity-services"></a> $${\color{navy}AWS\ identity\ services}$$

## <a id="aws-machine-learning-services"></a> $${\color{maroon}AWS\ machine\ learning\ services}$$

## <a id="aws-transfer-and-migration-services"></a> $${\color{olive}AWS\ transfer\ and\ migration\ services}$$

## <a id="aws-analytics-services"></a> $${\color{gray}AWS\ analytics\ services}$$
