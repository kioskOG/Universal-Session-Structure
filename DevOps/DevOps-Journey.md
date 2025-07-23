
<div align="center"> 
  <h1>💛 Journey Of a DevOps Engineer 🌟 </h1>
  <a href="https://github.com/kioskOG/Universal-Session-Structure"><img src="https://readme-typing-svg.demolab.com?font=italic&weight=700&size=18&duration=4000&pause=1000&color=F727A9&center=true&width=600&lines=+--+Journey+Of+a+DevOps+From+Day+1+to+Serving+Million--" alt="Typing SVG" /> </a>  
  <br>
  </div>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Journey</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #070708ff; /* Light grey background */
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .container {
            background-color: #b98111ff;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 90%;
            width: 800px; /* Max width for better readability */
        }
        .svg-container {
            margin-top: 1rem;
            margin-bottom: 2rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-4xl font-bold text-gray-800 mb-4 rounded-lg">💛 Journey Of a DevOps Engineer 🌟</h1>
        <div class="svg-container">
            <svg width="100%" height="80" viewBox="0 0 800 80" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" style="stop-color:#F727A9;stop-opacity:1" />
                        <stop offset="100%" style="stop-color:#FFD700;stop-opacity:1" />
                    </linearGradient>
                </defs>
                <!-- Main title text -->
                <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Inter, sans-serif" font-size="32" font-weight="bold" fill="url(#gradient)">
                    -- Journey Of a DevOps From Day 1 to Serving Millions --
                </text>
            </svg>
        </div>
        <p class="text-lg text-gray-600">
        This document outlines a comprehensive, phased plan for a DevSecOps masterclass, simulating the journey of building and scaling a product for a client from scratch. It builds on the provided reference, completing the structure with logical progressions for Phases 3-10. Each phase includes **To-DO** tasks, **Outcome** goals, and **Next** steps to guide the course flow. The plan emphasizes practical, hands-on learning, evolving from basic setups to enterprise-level DevSecOps practices using AWS, EKS, Terraform, and other tools.
        The course assumes a sample application with 5 microservices + MySQL, starting from a Docker Compose file. Phases progress iteratively, addressing client expectations like cost-effectiveness, monitoring, and scalability.
        </p>
    </div>
</body>
</html>

## Overall Course Objectives

- Simulate real-world DevSecOps evolution for a new client project.
- Cover key pillars: Cloud Design, Network Design, Infrastructure Provisioning, CI/CD, Application Architecture, Microservices, Observability, HA/Scaling/Resiliency/Rollouts/Rollbacks, and Troubleshooting.
- Focus on mindset: Iterative problem-solving, cost optimization, and security-by-design.
- Tools: AWS, EKS/ECS, Terraform, GitHub Actions/Jenkins, Prometheus/Grafana, etc.
- Duration: 10 phases, scalable to 10-20 sessions.


## Phase 1: Initial Client Onboarding and Infra Design

**To-DO**:

- Introduce the scenario: New client project starting from scratch.
- Show application flow as a diagram depicting 5 applications (e.g., frontend, auth service, payment service, user service, inventory service) + MySQL database, illustrating interactions (e.g., API calls, DB queries).
- Review Docker Compose file shared by the client for local setup.
- Discuss client expectations:
    - Choosing Cloud to run application (AWS for its ecosystem and cost tools).
    - Choosing Virtual Machine or Container as application orchestrator (Opt for containers via EKS for scalability over VMs).
    - Setting up Monitoring/Alerting (Basic Prometheus/Grafana).
    - Setup infra in most cost-effective way (Use spot instances, right-sizing, auto-scaling).
- Initial level Infra design:
    - Basic Cloud design: AWS with single-account setup, focusing on core services (EC2/EKS, RDS for MySQL).
    - Networking Design - What/Why: VPC with public/private subnets for isolation (why: security and cost control); Networking Schema (diagram with subnets, IGW, NAT); Single AZ initially for cost, plan for Multi-AZ later.
    - Virtual Machine or Container: Choose EKS for container orchestration (why: better for microservices scaling than raw VMs).

**Outcome**:

- Convey client expectations and align on priorities.
- Create or show:
    - Application flow diagram shared by client.
    - Proposed infra design by DevOps (diagram including AWS components, networking, EKS).
    - Explanation of the entire Application/Infra diagram with networking concepts (e.g., subnets for traffic segregation).
- Decide on Cloud (AWS) and Container Orchestrator (EKS).

**Next**:

- Running application locally using Docker Compose to check the flow as communicated by Client.
- IaC design discussion.
- CI/CD tool and design discussion.
- Infra deployment with working application deployed MANUALLY in EKS.


## Phase 2: Dev Environment Setup

**To-DO**:

- Run Docker Compose file locally to check if all services (5 apps + MySQL) are working as expected (verify API flows, DB connections).
- Decide what Infra as Code tool to use - Discussion around options (Terraform vs. Pulumi; choose Terraform for maturity and community support).
- Terraform Project Structure:
    - Dev: Separate module for development environment.
    - Prod: Separate module for production with stricter controls.
- CI/CD Tool selection and design (e.g., GitHub Actions for simplicity; design pipeline for build/deploy).
- Create the infra in front of the audience:
    - Creating VPC Networking (subnets, security groups).
    - Creating EKS cluster.
    - Creating ECR (Elastic Container Registry) for image storage.
- Deploy applications in EKS manually (push images to ECR, apply Kubernetes manifests).
- Run/show application via kube port-forward proxy for local access.

**Outcome**:

- Participants gain basic design idea of Terraform, understanding how multiple projects (dev/prod) would be managed (e.g., modular code for reusability).
- Show working app demo running via kube port proxy, demonstrating end-to-end flow.

**Next**:

- Add replicas for high availability in the cluster.
- Introduce basic scaling and resiliency checks.


## Phase 3: Automating CI/CD Pipelines

**To-DO**:

- Design and implement CI/CD using chosen tool (e.g., GitHub Actions): Build Docker images, push to ECR, deploy to EKS via Helm.
- Add security scans (e.g., Trivy for images) and tests in the pipeline.
- Configure rollouts/rollbacks (e.g., blue-green deployments).
- Integrate with Terraform for infra changes in CI/CD.
- Demo a full pipeline run from code commit to deployment.

**Outcome**:

- Participants see automated, secure deployments, reducing manual errors and speeding up releases.
- Emphasize shift-left security and GitOps principles.

**Next**:

- Adding Replicas for High Availability


## Phase 4: Adding Replicas for High Availability & Deployment Strategy

**To-DO**:

- Update Kubernetes deployments to add replicas (e.g., 2-3 pods per service for the 5 apps and MySQL).
- Configure Horizontal Pod Autoscaler (HPA) in EKS for automatic scaling based on CPU/metrics.
- Test failover scenarios (e.g., kill a pod and observe recovery).
- Update networking to support replicas (e.g., service load balancing in Kubernetes).

**Outcome**:

- Demonstrate improved resiliency with replicas, showing how the system handles failures without downtime.
- Participants understand HA basics in containerized environments, including pod distribution across nodes.

**Next**:

- Prod Environment Setup


## Phase 5: Prod Environment Setup

**To-DO**:

- Provisioning Infra using Terraform.
    - Create the infra in front of the audience via Atlantis.
        - Creating VPC Networking (subnets, security groups etc).
        - Creating EKS cluster with required add-ons.
        - Creating ECR (Elastic Container Registry) for image storage.

- Deploy applications in EKS using HELM via CI/CD (push images to ECR, apply Kubernetes manifests).
- Run/show application via kube LoadBalancers with https.
- Test failover scenarios (Increase Load using some load generator service) & check the application & DB state.

**Outcome**:

- Infra Provisiong Automation. Only after legit approval anyone can merge the PR.
- Show working demo app running via LB, demonstrating end-to-end flow.

**Next**:

- Implementing Monitoring & Logging


## Phase 6: Implementing Monitoring & Logging

**To-DO**:

- Setup Grafana Alloy as a agent scrapping/recieveing obervability data.
- Set up Prometheus for metrics collection from EKS pods, Redis, and MySQL.
- Integrate Grafana for dashboards and alerting (e.g., alerts on high CPU, low replicas).
- Add logging with Grafana Loki.

**Outcome**:

- Deliver visibility into system health, enabling proactive issue resolution.
- Learners learn to troubleshoot using real-time logging data.

**Next**:

- Improve application performance by integrating read replica & caching to optimize database performance.

## Phase 7: Integrating Read Replica & Caching for Performance

**To-DO**:

- Add Read Replica for DB.
- Add Redis as a caching layer (e.g., deploy as a Kubernetes service, integrate with apps for session storage/query caching).
- Update application code/config to use Read Replicas & Redis (e.g., cache frequent MySQL queries).
- Update Terraform to provision managed Redis (e.g., AWS ElastiCache) in dev/prod.
- Test cache invalidation and performance improvements.

**Outcome**:

- Show how caching reduces latency and DB load, with metrics before/after integration.
- Learners grasp caching strategies in microservices, including consistency challenges.

**Next**:

- Improving observability tools for tracing, How application to application calls are behaving.


## Phase 8: Implementing Observability and Monitoring

**To-DO**:

- Improve Grafana Alloy agent to work with traces.
- Configure distributed tracing using Tempo for microservices.
- Logging based on trace spans.
- Setup Profiling.
<!-- - Define SLOs/SLIs and test with sample incidents. -->

**Outcome**:

- Deliver visibility into application to application calls using tempo, enabling proactive issue resolution.
- Adding Logging for spans to troubleshoot specific span issue.
- Adding profiling for tracking application functional behaviour based on ebpf (cpu) & memory.

**Next**:

- Enhance security with advanced compliance and threat modeling.


## Phase 9: Advanced Security and Compliance

**To-DO**:

- Implement Policy as Code (e.g., OPA) for EKS compliance checks.
- Configure zero-trust networking (e.g., Istio service mesh).
- Run security scans and penetration testing.

**Outcome**:

- Ensure secure, compliant infrastructure, building client trust.
- Participants understand integrating security throughout the lifecycle.

**Next**:

- Scale to production with multi-AZ and global distribution.


## Phase 10: Production Scaling and Resiliency

**To-DO**:

- Upgrade to multi-AZ EKS for HA.
- Implement auto-scaling groups and chaos engineering (e.g., Chaos Mesh tests).
- Add global load balancing and CDN for traffic.
- Optimize costs (e.g., reserved instances).
- Test rollouts/rollbacks in prod-like setup.

**Outcome**:

- Achieve enterprise-scale resiliency, handling millions of users.
- Demonstrate cost-effective scaling strategies.

**Next**:

- Introduce microservices refinements and event-driven architecture.


### Phase 11: Cost vs. reliability

- Discuss trade-offs: Cost vs. reliability in single vs. multi-AZ.
- Review costs, performance, and optimizations.


<!-- ## Phase 11: Microservices Optimization and Event-Driven Design

**To-DO**:

- Refine 5 apps into full microservices with API Gateway.
- Add Kafka for event-driven communication.
- Optimize database sharding and polyglot persistence.
- Update CI/CD for independent service deploys.
- Troubleshoot distributed system issues.

**Outcome**:

- Enable agile, decoupled services for faster iterations.
- Learners master microservices patterns and troubleshooting.

**Next**:

- Capstone: Full enterprise integration and review.


## Phase 12: Enterprise Integration and Capstone

**To-DO**:

- Integrate all components: Multi-cloud hybrid if needed, full observability, automated everything.
- Conduct end-to-end testing and client demo simulation.
- Review costs, performance, and optimizations.
- Discuss ongoing maintenance and SRE practices.

**Outcome**:

- Complete a production-ready system, ready for millions of users.
- Participants gain confidence in end-to-end DevSecOps delivery.

**Next**:

- Course wrap-up: Certifications, real-world applications, and community resources. -->

