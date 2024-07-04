# AWS Lambda

AWS Lambda is a **serverless** compute service provided by AWS. It allows you to run code without provisioning or managing servers, paying only for the compute time consumed. It is a **Function as a Service(FaaS)**. Here’s an overview of AWS Lambda: 

### What is AWS Lambda?

AWS Lambda lets you execute code in response to events such as changes to data in Amazon S3 buckets, updates to Amazon DynamoDB tables, or HTTP requests via Amazon API Gateway. It automatically scales your application by running code in response to each trigger, ensuring high availability and scalability.

`Note:` Docker is not same as aws lambda, lambda uses docker images of runtime, but it is not docker and not even related to AWS ECS.

### Types of lambda

Public Lambda: A public lambda function is accessible and can be invoked by any external entity or service.

Private Lambda: A private lambda function is restricted and can only be invoked within the same AWS account or within a specified VPC.

- In new private lambda functions, every lambda function is connected to a single network interface, avoiding to spawn different network interfaces for different lambda functions

### Types of lambda function based on Invocation

There are three types of invocations for AWS Lambda functions:

1. Synchronous Invocation: In this type of invocation, the calling application waits for a response from the Lambda function before proceeding. The response can be a success or an error message. (Human interaction with web application)
Ex: Amazon API Gateway, Cognito, CloudFormation, Alexa, Lex, CloudFront
**Error Behaviour** - No Retries

2. Asynchronous Invocation: In this type of invocation, the calling application does not wait for a response from the Lambda function. The function is invoked and the calling application continues its execution without waiting for the function to complete.
Ex: Amazon SNS, Amazon S3, Amazon EventBridge 
**Error Behaviour** - twice (default)

3. Event Source Mappings: Event Source Mappings in AWS Lambda allow you to connect event sources, such as Amazon Kinesis streams, to your Lambda functions. This enables your functions to automatically trigger in form of **event batches** and process events from these sources. 
Ex: Amazon Kinesis, Amazon SQS, Amazon DynamoDB Streams
**Error Behaviour** - Depends on Event Source

`note:`
 - Lambda doesn't directly read data from these sources, lambda function should be attached with a **execution role** with kinesis permissions to read data from the kinesis in form of **event batches**
 - Maintain **Warm start**
   1) Store and reference dependencies locally.
   2) Limit re-initialization of variables.
   3) Add code to check for and reuse existing connections.
   4) Use tmp space as transient cache.
   5) Check that background processes have completed.
- To establish a private connection between your VPC and Lambda, create an interface VPC endpoint. Interface endpoints are powered by **AWS PrivateLink**, which enables you to privately access Lambda APIs without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. 

## Lambda Layers

- A Lambda layer is a .zip file archive that contains supplementary code or data. Layers usually contain library dependencies, a custom runtime, or configuration files. 

## Lasmbda Handler
- The handler method takes two objects – the event object and the context object.

## Lambda Best Practices
- Seperate Business Logic from handler function. 
- Try to increase modularity, instead packing the things in one single piece of code.
- Treat functions are stateless
- Minimize the code and keep whatever is required.

## Lambda Best Practices for writing the code
- Add **Loggers** to avoid any hustles. 
- Return the code is must to implement in lambda functions for **termination**.
- Use of environmental variables is a good practice of security. 
- Add secrets data by using services like AWS Systems Manager Parameter Store, AWS AppConfig. 
- Recursion should be avoided, it leads to uncontrollable scalling innvocation. 
- Use Cloudwatch for metrics & Build the code for reusability. 

## Lambda Concurrency Provisioning

# Concurrency in Lambda Functions

Concurrency in Lambda functions can be compared to the total capacity of a restaurant for serving a certain number of diners at one time. If you have seats in the restaurant for 100 diners, only 100 people can sit at the same time. Anyone who comes while the restaurant is full must wait for a current diner to leave before a seat is available. If you use a reservation system, and a dinner party has called to reserve 20 seats, only 80 of those 100 seats are available for people without a reservation. Lambda functions also have a concurrency limit and a reservation system that can be used to set aside runtime for specific instances.

## Types of Concurrency

### 1. **Reserved Concurrency**

Reserved concurrency guarantees that a specific number of instances are always available for a particular function. This is like a reservation in the restaurant, ensuring that certain seats are always held for a specific party, no matter how busy the restaurant gets.

### 2. **Provisioned Concurrency**

Provisioned concurrency initializes a specified number of function instances to be prepared to handle invocations. This is like pre-preparing meals in a restaurant to ensure that the service is fast and can handle a sudden influx of diners efficiently.

### 3. **Unreserved Concurrency**

Unreserved concurrency is the remaining capacity available for Lambda functions after reserved concurrency has been allocated. This is akin to the remaining seats in the restaurant that are available to walk-in customers.

Each type of concurrency helps manage the function's availability and performance, ensuring that critical functions have the necessary resources while optimizing the overall capacity.

**Concurrency Limit is of 1000 Only, we can incresease it with a support ticket**

- Limit a function’s concurrency to achieve the following:
  1) Limit costs
  2) Regulate how long it takes you to process a batch of events
  3) Match it with a downstream resource that cannot scale as quickly as Lambda

- Reserve function concurrency to achieve the following: 
  1) Ensure that you can handle peak expected volume for a critical function 
  2) Address invocation errors

## Key Features

### Serverless Execution

Lambda runs your code on a highly available and fault-tolerant infrastructure managed by AWS. You don't need to provision or manage servers, ensuring cost efficiency and scalability.

### Event-Driven Architecture

Lambda is designed to respond to events generated by other AWS services or custom events. For example, it can process file uploads to S3, perform data transformations in response to DynamoDB updates, or handle API requests via API Gateway.

### Pay-Per-Use Billing

You are charged based on the number of requests for your functions and the time your code executes. There are no charges when your code is not running.

### Supported Runtimes and Languages

Lambda supports a variety of programming languages including Node.js, Python, Java, Ruby, Go, and .NET Core. You can also bring your own runtime using custom runtimes.

### Integrations with AWS Services

Lambda integrates seamlessly with other AWS services like S3, DynamoDB, API Gateway, SNS, SQS, and more, enabling serverless workflows and microservices architectures.

## Limitations
- Indirectly memory of vCPUs for Lambda can be controlled based on memory, we can scale from 512MB(default) to 10240MB
- Based on 1MB steps, 1 vCPU = 1769MB

## Use Cases

### Real-Time File Processing

Lambda can process files uploaded to S3, trigger data transformations, and store results back in S3 or DynamoDB.

### Backend for Mobile and Web Applications

Serve backend functionalities such as user authentication, database operations, and API integrations without managing servers.

### IoT Data Processing

Handle incoming data streams from IoT devices, perform real-time analytics, and trigger actions based on sensor data.








