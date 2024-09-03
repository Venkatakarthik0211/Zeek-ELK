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

# AWS Compute Services Overview

<!DOCTYPE html>
<html>
<head>
<style>
  .container {
    display: flex;
    align-items: center;
    margin-bottom: 20px; /* Adds space between sections */
  }
  .image {
    flex: 1;
  }
  .content {
    flex: 2;
  }
  .container img {
    max-width: 100%; /* Ensure images fit within the container */
  }
  ul {
    list-style-type: none; /* Remove default list styling */
    padding: 0;
  }
  li {
    margin-bottom: 10px; /* Add space between list items */
  }
</style>
</head>
<body>

<!-- Template for services -->
<!-- <div class="container">
  <div class="image">
    <img src="IMAGE_URL" alt="SERVICE_NAME">
  </div>
  <div class="content">
    <h2>SERVICE_NAME</h2>
    <ul>
      <li><strong>Type</strong>: SERVICE_TYPE</li>
      <li><strong>Key Features</strong>:</li>
      <ul>
        <li><strong>Feature 1</strong>: DESCRIPTION</li>
        <li><strong>Feature 2</strong>: DESCRIPTION</li>
        <li><strong>Feature 3</strong>: DESCRIPTION</li>
      </ul> 
    </ul>
  </div>
</div> -->
 
<!-- Instances of the template for each service -->
<div class="container">
  <div class="image">
    <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Compute/64/Arch_Amazon-EC2_64.svg" alt="Amazon EC2">
  </div>
  <div class="content">
    <h2>Amazon EC2</h2>
    <ul>
      <li><strong>Type</strong>: Virtual Machines</li>
      <li><strong>Key Features</strong>:</li>
      <ul>
        <li><strong>Virtual Servers</strong>: Runs Linux or Windows virtual machines.</li>
        <li><strong>Customization</strong>: Choose OS, storage, CPU type (Intel, AMD, Graviton).</li>
        <li><strong>Elasticity</strong>: Resizable and customizable instances.</li>
        <li><strong>Pricing</strong>: Pay-as-you-go or reserved instances.</li>
        <li><strong>Management</strong>: Shared responsibility between AWS and the user.</li>
      </ul>
    </ul>
  </div>
</div>

<div class="container">
  <div class="image">
    <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Compute/64/Arch_AWS-Lambda_64.svg" alt="AWS Lambda">
  </div>
  <div class="content">
    <h2>AWS Lambda</h2>
    <ul>
      <li><strong>Type</strong>: Serverless</li>
      <li><strong>Key Features</strong>:</li>
      <ul>
        <li><strong>No Server Management</strong>: AWS handles server management.</li>
        <li><strong>Programming Languages</strong>: Supports Java, Go, Ruby, Node.js, Python, etc.</li>
        <li><strong>Scalability</strong>: Instantly supports thousands of requests.</li>
        <li><strong>Billing</strong>: Pay only for the compute time used.</li>
      </ul>
    </ul>
  </div>
</div>

<div class="container">
  <div class="image">
    <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Compute/64/Arch_AWS-Elastic-Beanstalk_64.svg" alt="AWS Elastic Beanstalk">
  </div>
  <div class="content">
    <h2>AWS Elastic Beanstalk</h2>
    <ul>
      <li><strong>Type</strong>: Orchestration</li>
      <li><strong>Key Features</strong>:</li>
      <ul>
        <li><strong>Automation</strong>: Handles deployment, management, scaling, and monitoring.</li>
        <li><strong>Application Management</strong>: Manages capacity, load balancing, auto-scaling.</li>
        <li><strong>Flexibility</strong>: Full control over underlying EC2 instances.</li>
      </ul>
    </ul>
  </div>
</div>

<div class="container">
  <div class="image">
    <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Compute/64/Arch_AWS-Batch_64.svg" alt="AWS Batch">
  </div>
  <div class="content">
    <h2>AWS Batch</h2>
    <ul>
      <li><strong>Type</strong>: Orchestration</li>
      <li><strong>Key Features</strong>:</li>
      <ul>
        <li><strong>Batch Processing</strong>: Runs batch computing workloads.</li>
        <li><strong>Dynamic Provisioning</strong>: Automatically provisions compute resources.</li>
        <li><strong>Focus on Results</strong>: No need to manage batch computing software.</li>
      </ul>
    </ul>
  </div>
</div>

<div class="container">
  <div class="image">
    <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Compute/64/Arch_Amazon-Lightsail_64.svg" alt="Amazon LightSail">
  </div>
  <div class="content">
    <h2>Amazon LightSail</h2>
    <ul>
      <li><strong>Type</strong>: Virtual Machines</li>
      <li><strong>Key Features</strong>:</li>
      <ul>
        <li><strong>Predictable Pricing</strong>: Low and predictable monthly cost.</li>
        <li><strong>Resources</strong>: Deploy VMs, databases, load balancers, DNS records.</li>
        <li><strong>Ease of Use</strong>: Separate LightSail console for easy management.</li>
      </ul>
    </ul>
  </div>
</div>

<div class="container">
  <div class="image">
    <img src="https://raw.githubusercontent.com/sashee/aws-svg-icons/ddf2928b65d8f18c20c6a792740ec934804e7a25/docs/Architecture-Service-Icons_07302021/Arch_Compute/64/Arch_AWS-Outposts_64.svg" alt="AWS Outposts">
  </div>
  <div class="content">
    <h2>AWS Outposts</h2>
    <ul>
      <li><strong>Type</strong>: Hybrid</li>
      <li><strong>Key Features</strong>:</li>
      <ul>
        <li><strong>On-Premises AWS</strong>: Run AWS services in your data center.</li>
        <li><strong>Physical Equipment</strong>: Delivered as a fully assembled server rack.</li>
        <li><strong>Integration</strong>: Similar to public AWS EC2 servers.</li>
      </ul>
    </ul>
  </div>
</div>

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
