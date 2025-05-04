# 🌩️ Cloud Design

This session dives deep into building secure, scalable, and cost-efficient cloud foundations — the backbone of any modern production environment.

### 🎯 Key Objectives

* Design an enterprise-ready cloud structure with isolation, auditability, and least privilege.
* Make the right decisions between managed services and primitives.
* Plan for compliance, cost optimization, and multi-region readiness from day one.

### 🧱 Topics Covered

#### 1. Multi-Account Cloud Strategy

* AWS Organizations, Control Tower
* Environments: dev, staging, prod
* Service Control Policies (SCPs)
* Centralized logging, billing, and security

#### 2. VPC & Subnet Architecture

* Public vs Private subnets
* NAT gateways, VPC endpoints, and egress control
* IP planning (RFC1918, IPv6 readiness)
* High availability zones and fault domains

#### 3. IAM Best Practices

* IAM roles vs users vs groups
* Permission boundaries
* CI/CD-specific IAM roles
* Cross-account access & IAM federation

#### 4. Choosing Core Services

* ECS vs EKS vs Lambda
* RDS vs DynamoDB vs Aurora Serverless
* S3 for data lakes, backups, and static assets
* EventBridge, SQS, and SNS usage patterns

#### 5. Resiliency and HA Design

* Regional vs zonal services
* Multi-region active-active vs active-passive
* DR planning: RTO vs RPO

#### 6. Cost & Tagging Strategy

* Cost allocation tags and budget alerts
* Forecasting and anomaly detection
* Tag-based access control

#### 7. Security & Compliance Foundation

* Identity federation (SSO, SAML)
* Encryption (KMS, envelope encryption)
* Centralized guardrails with AWS Config, SCPs

### ✅ Takeaways

* 📐 Sample landing zone Terraform template
* 🗺️ Decision matrix: ECS vs EKS vs Lambda
* 🔒 IAM policy best-practice library
* 💵 Tagging convention template for budgeting and chargebacks

---

Stay tuned as we publish detailed notes, diagrams, and hands-on examples with each session. This is **production wisdom, distilled.**
