## Cloudwatch = metrics:

-> use cloudwatch agent for metrics of inside services or metrics for a container or instance
-> can use cloudwatch with agent/api from on-prem
-> Application integration
 
## Conceots of cloudwatch: 
 
 -> Namespace: Lambda/EC2 is a instance for metrics (ex: AWS/lambda)
 -> Datapoints: Timestamps + metrics
 -> Metrics: Time ordered set of datapoints
 -> Dimension: is a name-value pair
 
 -> Standard cloudwatch resolution is 60sec, lesser the time, more the metrics
 -> Resolution: A duration of time, where each metric is detailed(Standard 60s, high 1s)
 -> Retention: The duration of time in which cloudwatch keeps the data
To understand this, 

for example: if there is a requirement for standard retention with high resolution(Accurate measuring of metrics
where there is a huge spike ), if there is a requirement for high retention with less resolution(Constant monitoring without
much of details)

-> More the data is stored, lesser the resolution of metrics(reduces the accuracy)

-> statistics - implement statistical functions
-> Percentile - Obtain metrics on certain percentage level

-> Alaram resolution enables us to notify/perform certain action in a finite period of time
-> Just like zeek, it can seperate logs based on metrics, which is called metric filter

## define trace, metrics, logs
Tracing: Tracing in AWS Lambda, powered by AWS X-Ray, provides detailed insights into the flow of requests within serverless applications, aiding in monitoring and debugging.

Metrics: AWS Lambda automatically generates and publishes metrics to Amazon CloudWatch, offering real-time visibility into function performance, including invocation count,duration, errors, and throttles. Metrics are immutable, granular applications. 

Logs: AWS Lambda streams logs to Amazon CloudWatch Logs, enabling comprehensive monitoring and troubleshooting through detailed logging statements within your functions.

# CloudWatch Architecture

Logs from Application/Network etc... -> Log Events -> Log Group (Same type of log streams) -> Log Stream (set of logs from the instances on one type of logs) -> metric filter -> metrics

-> Retention settings are done at log groups

