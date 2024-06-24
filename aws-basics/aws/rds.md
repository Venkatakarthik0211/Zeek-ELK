# Define Relational and Non Relational Databases

**Relational Databases:**

- Relational databases organize data into tables with rows and columns.
- They use a structured query language (SQL) to interact with the data.
- Key components of a relational database include:
    - Tables: These are the main structures that hold the data. Each table consists of rows (records) and columns (fields) that define the data structure.
    - Relationships: Relational databases establish relationships between tables using keys, such as primary keys and foreign keys. These relationships ensure data integrity and enable efficient data retrieval.
    - ACID properties: Relational databases adhere to ACID (Atomicity, Consistency, Isolation, Durability) properties, which ensure data consistency and reliability.
    - Normalization: Relational databases follow normalization techniques to eliminate data redundancy and maintain data integrity.

**Non-Relational Databases:**

- Non-relational databases, also known as NoSQL databases, store and retrieve data in a flexible, schema-less manner.
- They are designed to handle large amounts of unstructured or semi-structured data.
- Key components of a non-relational database include:
    - Collections or Documents: Instead of tables, non-relational databases use collections or documents to store data. A collection is a group of documents, and each document is a set of key-value pairs or other data structures.
    - No fixed schema: Non-relational databases do not enforce a fixed schema, allowing for more flexibility in data storage and retrieval.
    - Scalability: Non-relational databases are designed to scale horizontally, meaning they can handle large amounts of data by distributing it across multiple servers.
    - CAP theorem: Non-relational databases often prioritize availability and partition tolerance over consistency, as per the CAP theorem. This means that in certain scenarios, data consistency may be sacrificed for high availability or fault tolerance.

## Why you will need a RDS on EC2 Instance
- OS-Level Database.
- SuperPrivilages(Root) permissions for a database.
- Based on client demands or the different provider where aws dont provide
- Specific OS/DB version where aws doesnt provide

## Why we shouldn't
- Administration Overhead(Such as Upgrading, Patching, Disaster Management)
- Running EC2 on single AZ & Can't rapidly scale a ec1 instance where rds instance does.
- Replication concepts are not applicable in ec2 instance, where advanced features matters.


