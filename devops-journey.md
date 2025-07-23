Plan
    Phase 1
        To-DO:
            - There is a new client we need to work from scratch
            - Show application flow as a diagram, which would depict all the applciations
              5 applications + Mysql
            - Docker Compose file shared by Client
            - Clinet Expectation
              - Choosing Cloud to run application ( AWS )
              - Choosing VirtualMachine or Container as application orchestrator
              - Setting up Monitoring/Alerting/
              - Setup infra in most cost effective way
            - Intial level Infra design
                - Basic Cloud design after what cloud you have choosen
                - Networking Design - What/Why
                  - Networking Schema
                  - Single AZ or Multi AZ
                - Virtual Machine or Container  ( EKS or ECS )
        Outcome:
           - What do you want to convey after this phase 1
             - We will explain the client expection as what client wants
             - We will create or show
               - Application flow shared by Client
               - An infra designed purposed by DevOps
               - Explaination of the entire Applicatin/Infra diagram with networking concepts
             - Deciding on Cloud/Container Orchestrator

        Next:
           - Running application locally using Docker compose to check the flow as communicated by Client
           - IaaC design discussion
           - CI/CD tool and design discussion
           - Infra deployment with working application deployed MANNUALLY in EKS



    Phase 2 - Dev Enviourment
        To-DO
          - Running Docker Compose file locally to check if all the services are working as expected
          - Deciding  what Infra as code tool to use - Have discussion around this
          - Terraform Project Structure
            - Dev
            - Prod
          - CI/CD Tool selection and design
          - Creating the infra in front of the people
            - Creating VPC Networking
            - Creating EKS cluster
            - Creating ECR
         - Deploying applications in eks manually
         - Running/showing application via kube port proxy

        Outcome
          - People should have basic design idea of terraform, as how multiple projects would be managed
          - Showing working app demo running as kube port proxy

        Next:



    Phase 3
        To-DO
          - We need to add replica also
        Outcome

        Next


    Phase 4
        To-DO
          - We need to add redis
        Outcome
        Next


    Phase 5
        To-DO
        Outcome
        Next


    Phase 6
        To-DO
        Outcome
        Next


    Phase 10
        To-DO
        Outcome
        Next
