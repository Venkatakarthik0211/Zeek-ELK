# Architecture Explained

In the past, applications often integrated multiple stages into a single process, forming what we call a monolith. For instance, in an application like Instagram Shorts, video uploads were handled in a single EC2 instance across four distinct stages: Upload, Process, Store, and Manage.

## Monolithic Approach
Combining all stages into one EC2 instance seems straightforward but can lead to challenges as the application scales. A failure in one stage can impact the entire process.

## Decoupled Solution
A more modern approach involves splitting these stages into individual components, each performing a specific function. For example:

- **Upload**: Videos are stored directly in an S3 bucket.
- **Processing**: Video processing tasks are handled by separate EC2 instances or serverless functions.
- **Storage**: Processed videos are stored back in S3 or another dedicated storage service.
- **Management**: Metadata and access controls are managed independently, possibly using a database service.

### Challenges
However, directly connecting these stages can create dependencies where a failure in one stage affects others.

## Optimization with Load Balancers
To address this, internal load balancers like AWS ALB can be placed between stages to distribute workloads evenly:

- **ALB**: Balances traffic between instances handling uploads.
- **ALB**: Distributes processing tasks across multiple instances or functions.
- **ALB**: Manages traffic between storage services.
- **ALB**: Facilitates load distribution for management tasks.

- This solution is highly avaliable and highly scalable in a sync way.

## Integrating Queues for Resilience
To further enhance reliability and decouple components, introduce message queues such as AWS SQS (Simple Queue Service):

- **Upload Queue**: Directs incoming video upload requests to processing instances or functions.
- **Processing Queue**: Enqueues tasks for video processing, ensuring each task is handled independently and can retry on failure.
- **Storage Queue**: Coordinates storage operations, ensuring data consistency and durability.
- **Management Queue**: Manages metadata updates and access controls asynchronously, reducing the impact of failures.

**- This solution is highly avaliable and highly scalable in a async way based on queue length only.**

## Perspective
This architecture balances simplicity with scalability. Decoupling stages allows for better control over each component, improving scalability and maintenance. Queues enhance fault tolerance by decoupling stages further, enabling asynchronous processing and retries on failure.

Load balancers and queues together form a robust foundation for scaling and managing complex workflows. Monitoring and error handling remain critical to managing interconnectedness effectively in a distributed architecture.

`Note:` You can choose between synchronous solution and async solution based on requirements which describes type of solution.

- Since this architecture increases the complexity, we use event bus or AWS Event Router, which consists of different queues getting processed between stages. 

- The architecture is known as event driven architecture, where there is no constant running or no constant wiating occurs, the above architecture can be modified to **event based architecture**

[Redirect to Lambda.md]