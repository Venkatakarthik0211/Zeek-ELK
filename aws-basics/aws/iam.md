# Identity Access Management
### IAM Policies
- **Order of Evaluation:**
  - **Explicit Deny:** Highest priority. If a policy explicitly denies access, that denial takes precedence.
  - **Explicit Allow:** Evaluated if no explicit deny is present. Explicit allow overrides implicit deny.
  - **Implicit Deny:** Default rule. If a request doesn’t meet any explicit allow statements, it defaults to implicit deny.

- **Types of Policies:**
  - **Managed Policies:** Standalone policies attachable to multiple users, groups, or roles. 
    - *AWS Managed Policies:* Maintained by AWS, covering common use cases.
    - *Customer Managed Policies:* Created and managed by the user.
  - **Inline Policies:** Directly managed within a single user, group, or role. Embedded within the user, group, or role.

### Amazon Resource Name (ARN)
- Unique identifier for each resource in AWS.
- **Format:** `arn:partition:service:region:account-id:resource-id`
- **Example:** `arn:aws:iam::123456789012:role/my-role`

### Notes:
- IAM user can be a member of a maximum of 10 groups.
- Maximum of 5000 IAM users per account.
- Use IAM roles & Identity Federation for more than 5000 users.

## IAM with CloudFormation

#### Prerequisite Terms:
- **AWSTemplateFormatVersion:** The version that the template conforms to.
- **Description:** Optional text string describing the template.
- **Parameters:** Input custom values to your template each time you create or update a stack.
- **Resources:** Declare AWS resources to create and configure.
- **Outputs:** Optional section for output values to import into other stacks or view on the CloudFormation console.
- **Type:** The type of resource to create.
- **Properties:** Set of properties for the resource, dependent on the resource type.
  - **ManagedPolicyArns:** List of managed policy ARNs attached to the user.
  - **LoginProfile:** Includes the user's password.
  - **PolicyDocument:** Contains permissions to add to the new policy.
- **!Ref:** Returns the value of the specified parameter or resource.
- **!Sub:** Substitutes variables within a string with their resolved values.
- **NoEcho:** If true, CloudFormation doesn't return the parameter value when describing the stack.

#### CloudFormation Intrinsic Functions:
- **!Base64 valueToEncode:** Encodes binary data to ensure data integrity during transmission.
- **!Cidr [ipBlock, count, cidrBits]:**
  - **ipBlock:** Starting IP address block (e.g., "192.168.0.0/16").
  - **count:** Number of smaller CIDR blocks to create.
  - **cidrBits:** Number of bits for the smaller CIDR blocks (e.g., /24 for 256 addresses).

## IAM User vs IAM Role 
## Differences Between IAM User and IAM Role

| Aspect                | IAM User                                                                 | IAM Role                                                                                     |
|-----------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| **Identity and Permissions** | Represents a single user with long-term credentials such as a username, password, and access keys. Permissions are directly attached to the user. | An entity that AWS services or users can assume for temporary access to AWS resources. Permissions are defined by policies attached to the role, without long-term credentials. |
| **Use Cases**         | Ideal for individuals or applications that require long-term access to AWS resources, such as developers, administrators, or specific applications. | Suitable for granting temporary permissions to AWS services, users from other AWS accounts, or federated users. Used for cross-account access, EC2 instance roles, and temporary access for users. |
| **Credential Management** | Long-term credentials (password and access keys) that need to be managed by the user, including regular rotation and secure storage. | Provides temporary security credentials through AWS STS (Security Token Service), which are automatically rotated and managed by AWS, reducing the risk associated with long-term credentials. |


