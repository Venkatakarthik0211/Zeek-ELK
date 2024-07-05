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

## Lambda Monitoring and Troubleshooting

Mainly these are monitored by default: 
1) Number of requests 
2) Invocation duration per request
3) Number of requests that result in an error

## Cloudwatch Metrics for Lambda

- **Invocations**
The number of times your function code is run, including successful runs and runs that result in a function error. If the invocation request is throttled or otherwise resulted in an invocation error, invocations aren't recorded.

- **Duration**
The amount of time that your function code spends processing an event. The billed duration for an invocation is the value of Duration rounded up to the nearest millisecond.

- **Errors**
The number of invocations that result in a function error. Function errors include exceptions thrown by your code and exceptions thrown by the Lambda runtime. The runtime returns errors for issues such as timeouts and configuration errors.

- **Throttles**
The number of times that a process failed because of concurrency limits. When all function instances are processing requests and no concurrency is available to scale up, Lambda rejects additional requests.

- **IteratorAge**
Pertains to event source mappings that read from streams. The age of the last record in the event. The age is the amount of time between when the stream receives the record and when the event source mapping sends the event to the function.

- **DeadLetterErrors**
For asynchronous invocation, this is the number of times Lambda attempts to send an event to a dead-letter queue but fails. 

## Options to monitor a lambda function

- **Cloudwatch insight**:  Lambda Insights collects, aggregates, and summarizes system-level metrics. It also summarizes diagnostic information such as cold starts and Lambda worker shutdowns to help you isolate issues with your Lambda functions and resolve them quickly.

- **AWS X-Ray**: Lambda functions send trace data to X-Ray, and X-Ray processes the data to generate a service map and searchable trace summaries. We can use it for: 

- **AWS Cloudtrail**: AWS CloudTrail helps audit your application by recording all the API actions made against the application.

- **Dead Letter Queues**: Dead-letter queues help you capture application errors that must receive a response, such as an ecommerce application that processes orders. If an order fails, you cannot ignore that order error. 

1) Tuning Perfomrance 
2) Identifying the call flow of API's in Lambda
3) Tracking path and innovocation


## Key Features of AWS Lambda for Scalable, Secure, and Extensible Applications

- **Environment variables**: 
  - Use environment variables to adjust your function's behavior without updating code.

- **Versions**: 
  - Manage the deployment of your functions with versions, so that, for example, a new function can be used for beta testing without affecting users of the stable production version.

- **Container images**: 
  - Create a container image for a Lambda function by using an AWS-provided base image or an alternative base image so that you can reuse your existing container tooling or deploy larger workloads that rely on sizable dependencies, such as machine learning.

- **Layers**: 
  - Package libraries and other dependencies to reduce the size of deployment archives and make it faster to deploy your code.

- **Lambda extensions**: 
  - Augment your Lambda functions with tools for monitoring, observability, security, and governance.

- **Function URLs**: 
  - Add a dedicated HTTP(S) endpoint to your Lambda function.

- **Response streaming**: 
  - Configure your Lambda function URLs to stream response payloads back to clients from Node.js functions, to improve time to first byte (TTFB) performance or to return larger payloads.

- **Concurrency and scaling controls**: 
  - Apply fine-grained control over the scaling and responsiveness of your production applications.

- **Code signing**: 
  - Verify that only approved developers publish unaltered, trusted code in your Lambda functions.

- **Private networking**: 
  - Create a private network for resources such as databases, cache instances, or internal services.

- **File system access**: 
  - Configure a function to mount an Amazon Elastic File System (Amazon EFS) to a local directory, so that your function code can access and modify shared resources safely and at high concurrency.

- **Lambda SnapStart for Java**: 
  - Improve startup performance for Java runtimes by up to 10x at no extra cost, typically with no changes to your function code.






