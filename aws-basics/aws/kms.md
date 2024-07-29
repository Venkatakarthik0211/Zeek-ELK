# AWS Key Management Service(KMS)

**In-Transit Encryption**:
- **Definition**: Encryption of data as it travels between systems, such as between a client and a server or between servers.
- **Purpose**: To protect data from being intercepted and read by unauthorized parties during transmission.
- **Common Methods**:
  - **TLS (Transport Layer Security)**: Encrypts data as it moves over the internet or other networks.
  - **VPNs (Virtual Private Networks)**: Securely transmits data over public networks.
- **Use Cases**:
  - Protecting data sent over the internet, such as during online transactions.
  - Securing communication between microservices within a distributed system.

**At-Rest Encryption**:
- **Definition**: Encryption of data that is stored on a physical medium, such as hard drives, databases, or cloud storage.
- **Purpose**: To protect data from unauthorized access when it is not actively being used or transmitted.
- **Common Methods**:
  - **File-Level Encryption**: Encrypting individual files or folders.
  - **Disk Encryption**: Encrypting entire disk volumes.
  - **Database Encryption**: Encrypting data within databases, often using technologies like Transparent Data Encryption (TDE).
- **Use Cases**:
  - Protecting sensitive information stored in databases.
  - Ensuring that data remains secure if physical storage devices are stolen or accessed by unauthorized individuals.

### Key Differences
| Aspect                    | In-Transit Encryption                       | At-Rest Encryption                        |
|---------------------------|---------------------------------------------|-------------------------------------------|
| **When Data is Encrypted**| During transmission                         | While stored                              |
| **Primary Threats Addressed** | Eavesdropping, man-in-the-middle attacks | Unauthorized access to stored data        |
| **Common Technologies**   | TLS, SSL, VPN                               | TDE, disk encryption, file-level encryption|
| **Typical Use Cases**     | Securing web transactions, API calls        | Protecting stored customer data, backups  |
| **Examples**              | HTTPS for websites, secure email protocols  | Encrypted database files, BitLocker       |
