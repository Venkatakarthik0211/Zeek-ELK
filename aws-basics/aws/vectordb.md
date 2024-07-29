**Vector Database**: A vector database (Vector DB) is a specialized database designed to store, index, and efficiently retrieve vectors, optimized for similarity search tasks.

**Features of Milvus Vector Database**:
- Efficient storage and retrieval of high-dimensional vectors.
- Support for indexing methods tailored to vector similarity search.
- Scalability to handle large-scale vector datasets.
- Integration with machine learning frameworks and applications.
- Hybdrid data storage and search
- Open Source and can be accessed by SDK's/API's
- Euclidean, inner product and cosine metrics
- Available as Standalone, cluster and managed

## Milvus Architecture Overview

### Coordinator Services (Service Layer)
The **Coordinator Services** are responsible for managing metadata and coordinating various tasks within the system. The key components include:

- **Meta Store**: Manages metadata information for the entire system.
- **Rootcoord**: Oversees the overall coordination of tasks, ensuring they are executed in the correct order.
- **Datacoord**: Manages data node operations, including data distribution and storage.
- **Querycoord**: Manages query node operations, ensuring efficient query processing and load balancing.
- **etcd**: A distributed key-value store used for service discovery and configuration management.

## Access Layer
The **Access Layer** serves as the entry point for external clients interacting with the system via SDKs or RESTful APIs. It consists of:

- **Load Balancer**: Distributes incoming requests across multiple proxies to ensure balanced load and high availability.
- **Proxy**: Handles client requests, performing operations such as data definition language (DDL), data control language (DCL), and data manipulation language (DML) commands. The proxies also produce data to the message storage system.

## Message Storage / WAL 
The **Message Storage / Write-Ahead Log (WAL)** system ensures data durability and consistency. It consists of:

- **Kafka / Pulsar**: These are distributed messaging systems used to produce and consume messages. They store logs of all data changes to provide reliable message delivery and replay capabilities.

## Worker Nodes
The **Worker Nodes** perform the actual data processing and querying tasks. They include:

- **Query Nodes (QNs)**: These nodes handle query execution and data retrieval based on client requests.
- **Data Nodes (DNs)**: Responsible for storing and managing data. They handle data ingestion, storage, and retrieval tasks.
- **Index Nodes (INs)**: Manage the creation and maintenance of data indexes to optimize query performance.

## Object Storage (Such as AWS S3)
The **Object Storage** layer is where data files and index files are stored. It includes:

- **Data Files**:
  - **Datalog**: Stores data logs.
  - **Statslog**: Stores statistical logs about the data.
  - **Binlog**: Stores binary logs of data changes.
- **Index Files**:
  - **Index**: Stores index data which is used by the index nodes to speed up query processing.

## Data Flow
1. **Client Interaction**: Clients interact with the system via SDKs or RESTful APIs.
2. **Load Balancing**: The load balancer distributes incoming requests to different proxies.
3. **Access Layer Operations**: Proxies handle various operations, producing data to the message storage system.
4. **Message Storage**: Kafka/Pulsar ensure durable message storage and reliable delivery.
5. **Data Processing**: Worker nodes (query, data, and index nodes) handle the processing, storage, and indexing of data.
6. **Object Storage Interaction**: Worker nodes read from and write to the object storage, ensuring data and index files are kept up to date.
7. **Coordination**: Coordinator services manage metadata and coordinate tasks to ensure system integrity and performance.

## Controls and Communication
- **Controls**: Coordinator services send control commands to manage and coordinate worker nodes and storage operations.
- **Communication**: Worker nodes and proxies communicate with the message storage system to consume and produce messages, ensuring data consistency and availability.

This architecture ensures scalability, reliability, and efficient data processing, making it suitable for large-scale distributed data systems.

## Concepts of milvus vector db

**Collections**: In Milvus Vector DB, a collection is a logical container that holds a group of vectors. It represents a dataset or a set of data points that share similar characteristics. Collections can be created, modified, and deleted, and they serve as the primary unit for data organization and retrieval.

**Partitions**: Partitions are used to further organize data within a collection. They provide a way to logically group vectors based on certain criteria, such as data source, data type, or any other relevant attribute. Partitions can be created, modified, and deleted within a collection, allowing for efficient data management and retrieval.

**Indexes**: Indexes in Milvus Vector DB are data structures that enable fast and efficient similarity search on vectors. They are used to accelerate the retrieval of vectors that are similar to a given query vector. Milvus supports various indexing methods, such as IVF (Inverted File), HNSW (Hierarchical Navigable Small World), and RNSG (Randomized Neighborhood Selection Graph), which can be applied to collections or partitions. Indexes can be created, modified, and deleted to optimize query performance and enhance search capabilities.

# Retrieval Augumented Generation

- Forcing LLM's work with our data

## Document Retrieval Pathway:
1. **Data**: The initial dataset.
2. **Context Extraction**: Identifying relevant information from the data.
3. **Chunking**: Breaking down context into manageable pieces.
4. **Embedding**: Converting chunks into vector representations.
5. **Store (Distr.)**: Storing embeddings in distributed storage.

   - *Similar Data*: Retrieved related information based on query embedding.

## Response Generation Pathway:
1. **Query**: User or system-generated question.
2. **Embedding**: Transforming query into vector representation.
3. **Context**: Contextual data retrieved that's relevant to the query.
4. **Response**: Generating an answer based on context and query embeddings.
5. **LLM**: Language Model used for generating responses.


