---
layout: home
permalink: /
lang: en
ref: home
sticky_cta:
  label: Book a call
  url: https://calendly.com/prlic/15min
title: Solutions Architect & AI Consultant
header:
  title: Ivan Prlić
  subtitle: Solutions Architect · AI & DevOps Consultant · Fractional CTO
  text: >
    I help engineering teams design, build, and modernize cloud systems —
    and integrate AI that ships to production.
  action:
    label: See How I Can Help
    url: '#services'


sections:
  - type: about.html
    section_id: about
    photo: assets/img/members/headshot_zoomed.webp
    title: One expert. Deep experience.
    availability: Available for new projects
    badges:
      - text: AWS Authorized Instructor
      - text: Toptal Expert Network
        url: https://www.toptal.com/resume/ivan-prlic
      - text: Fractional CTO
      - text: 14 Professional Certifications
    text: >-
      I'm Ivan Prlić, founder of Prlić Consulting. I work with engineering teams and technical
      leaders to design cloud platforms, integrate AI into products and workflows, and sort out
      infrastructure that has outgrown its current setup.


      Past and current clients include the European Commission, Volvo USA, TUI Group, Talkdesk,
      and Ricoh. Based in Zagreb, Croatia.
    tech: "AWS · GCP · Azure · Kubernetes · Terraform · Amazon Bedrock · SageMaker · Vertex AI · Kafka · Datadog"
    languages: "English (C2, Cambridge Certified) · Croatian (Native)"
    actions:
      - title: See What I Do
        url: '#services'
        class: btn-light

  - type: clients.html
    section_id: clients
    background_style: bg-subtle
    title: Selected Clients
    clients:
      - name: European Commission
      - name: Volvo USA
      - name: TUI Group
      - name: Ricoh
      - name: Talkdesk
      - name: Metro (Hospitality Digital)
      - name: Q.ai (Forbes)

  - type: services.html
    section_id: services
    title: How I Can Help
    services:
      - title: Generative AI & ML Engineering
        text: >-
          I build AI systems that go into production: RAG-based knowledge bases on Amazon Bedrock,
          computer vision pipelines on SageMaker, and ML workflows on Vertex AI. Recent projects include
          an LLM-powered legal document search system and a computer vision platform migration to AWS.
          AWS Certified Machine Learning Specialty, GCP Professional ML Engineer and Data Engineer certified.


          **[Fixed-scope AI advisory packages →](/ai-advisory/)**
        icon: fa-brain
      - title: Cloud Architecture
        text: >-
          Architecture design across AWS, GCP, and Azure — serverless, microservices, Kubernetes (EKS, GKE),
          event-driven systems with Kafka and SQS/SNS, and API management with Apigee and WSO2.
          I apply Domain-Driven Design to decompose legacy monoliths into maintainable, independently
          deployable services. Delivered for enterprises in automotive, travel, retail, and public sector.
        icon: fa-cloud
      - title: Cloud Migration
        text: >-
          Full-cycle migrations from on-prem to AWS and GCP. Past work includes a Magento 2 platform to
          Kubernetes on EKS, healthcare systems, and computer vision workloads. I handle architecture,
          risk planning, FinOps (rightsizing, reserved instances, cost dashboards), and delivery.
        icon: fa-cloud-upload-alt
      - title: DevOps as a Service
        text: >-
          Infrastructure as code with Terraform and Ansible, containers with Docker and Kubernetes,
          monitoring with Datadog and Prometheus. Security covered: AWS WAF, Shield, IAM, and Secrets Manager.
          CI/CD pipelines across GitLab, GitHub Actions, BitBucket, and Azure DevOps — from simple build
          pipelines to multi-environment GitOps workflows with ArgoCD. Good for teams that need DevOps
          capacity without the cost of a full-time hire.
        icon: fa-cogs
      - title: Serverless Architecture
        text: >-
          Serverless system design and implementation using AWS Lambda, API Gateway, Step Functions,
          and the Serverless Framework. I have built serverless backends for a healthcare startup
          (acquired by Carbon Health), a loyalty card platform, and a litigation support system.
          AWS SAM and serverless.com experience included.
        icon: fa-code
      - title: Cloud & AI Training
        text: >-
          As an AWS Authorized Instructor I deliver official AWS courses, including Machine Learning Specialty
          content. I also run cloud architecture workshops and technical upskilling sessions for enterprise
          engineering teams, adapted to the team's current skill level and the tech stack they work with.
        icon: fa-chalkboard-teacher
      - title: Technical Advisory
        text: >-
          Architecture reviews, technology selection, team structure, or strategic technical direction.
          I've advised startups, FinTech platforms, a VR education platform for INSEAD Business School,
          and enterprise engineering teams. Available for ongoing advisory or one-off architecture reviews.
        icon: fa-lightbulb
      - title: Fractional CTO
        text: >-
          Technical leadership for companies that need a senior engineering voice without a full-time hire.
          I work with founders and leadership teams to set technical direction, make architecture decisions,
          evaluate build vs. buy trade-offs, and structure engineering teams for growth. Available for
          ongoing retainers and critical project phases.
        icon: fa-user-tie

  - type: crosslink.html
    section_id: advisory-crosslink
    eyebrow: AI Advisory
    title: Not sure what to build yet?
    text: >-
      If the question is which AI use cases are worth funding rather than who
      can build them, there is a separate track for that: fixed-scope assessment,
      proof of value, and fractional AI leadership, with prices published.
    action:
      label: See AI advisory packages
      url: /ai-advisory/

  - type: case-studies.html
    section_id: work
    background_style: bg-subtle
    title: Selected Work
    studies:
      - tag: Healthcare · AWS · Serverless
        title: Serverless Platform for a Healthcare Startup
        body: >-
          A healthcare startup needed a cloud backend that could scale with unpredictable load
          and meet clinical reliability requirements without the overhead of managing servers.
          Designed a fully serverless architecture on AWS using API Gateway, Lambda, the Serverless
          Framework, and Kafka for event streaming. The startup was subsequently acquired by Carbon Health.
        outcomes:
          - Pay-per-request model eliminated idle infrastructure costs
          - Shipped to production in weeks, not months
          - Auto-scaling handled unpredictable clinical load without intervention
      - tag: Legal Tech · AWS · Generative AI
        title: LLM-Powered Legal Document Search
        body: >-
          A legal technology client needed to make large volumes of sensitive documents searchable
          and summarizable — without sending data to external services. Built a RAG-based knowledge
          base on Amazon Bedrock. Lawyers query the system in plain language and receive referenced,
          sourced answers rather than raw search results, all within a private AWS environment.
        outcomes:
          - Search time reduced from hours to seconds
          - All data stays within the client's private AWS environment
          - Answers are sourced and referenced, not hallucinated
      - tag: Travel · AWS · DevOps
        title: Cloud Native Platform for a Global Travel Group
        body: >-
          One of the world's largest travel companies needed a complete cloud native infrastructure
          foundation built from scratch, production-ready and observable from day one. Delivered
          the full stack on AWS — ECS, DynamoDB, Lambda, SNS/SQS, ALB, and CloudFront — with
          Terraform for IaC, GitLab CI/CD, Apigee for API management, and Datadog for monitoring.
        outcomes:
          - Full observability and alerting live from day one
          - Infrastructure fully reproducible via Terraform — no manual state
          - Multi-environment CI/CD pipelines replaced manual deployments
      - tag: Retail · AWS · Kubernetes
        title: E-Commerce Platform Migration to Kubernetes
        body: >-
          A retail client running a Magento 2 platform on ageing infrastructure needed a setup
          that could scale and was cheaper to run. Migrated to Kubernetes on AWS EKS using Helm
          for deployments, RDS for the database layer, and S3 for storage. The team went from
          manual, error-prone deployments to a fully repeatable, environment-consistent process.
        outcomes:
          - Removed dependency on fixed-capacity servers, scaling is now automatic
          - Deployments became fully repeatable across all environments
          - Eliminated class of production incidents caused by manual release steps

  - type: certifications.html
    section_id: certifications
    background_style: bg-subtle
    title: Certifications
    groups:
      - provider: Amazon Web Services
        certs:
          - name: AWS Authorized Instructor
            url: https://www.credly.com/badges/aa16c1eb-174e-4ba7-ad30-484fe1819135
          - name: Certified Machine Learning – Specialty
            url: https://www.credly.com/badges/cfc09e60-e068-4529-be07-641bfc1c7465
          - name: Solutions Architect – Professional
            url: https://www.credly.com/badges/df4f87b6-f80b-4df1-bc5f-321432d3749e
          - name: DevOps Engineer – Professional
            url: https://www.credly.com/badges/cd04983d-c963-4444-9f9f-2ae1eea48a8e
      - provider: Google Cloud
        certs:
          - name: Professional Cloud Architect
            url: https://www.credly.com/badges/53d187e0-8e95-4faf-8a90-2c27e722358f
          - name: Professional Cloud DevOps Engineer
            url: https://www.credly.com/badges/07939388-bea1-4528-84f3-8f69244a7d4a
          - name: Professional Machine Learning Engineer
            url: https://www.credly.com/badges/4c131b3c-4813-4bfb-8f18-009ed66af68d
          - name: Professional Data Engineer
            url: https://www.credly.com/badges/857eeecc-62b7-4fdf-ba26-cb4a1290e1af
          - name: Champion Innovator – Databases
      - provider: Microsoft Azure
        certs:
          - name: Azure Solutions Architect Expert
            url: https://learn.microsoft.com/en-us/users/ivanprli-9878/credentials/52c2b88eac40c8b9
          - name: DevOps Engineer Expert
            url: https://learn.microsoft.com/en-us/users/ivanprli-9878/credentials/7b0110cf22902d3b
          - name: Azure AI Engineer Associate
            url: https://learn.microsoft.com/en-us/users/ivanprli-9878/credentials/3f82b44ab38fd66a
      - provider: Engineering & Leadership
        certs:
          - name: PMP – Project Management Professional
            url: https://www.credly.com/badges/83b699c7-d3c0-42e7-9b2b-e32b6b3247c3
          - name: Certified Kubernetes Administrator (CKA)
            url: https://www.credly.com/badges/27198888-44fd-4ae7-942b-de89f7f01feb
          - name: Certified Scrum Master (CSM)

  - type: contact.html
    section_id: contacts
    title: Get In Touch
    text: >-
      Currently available for new projects. Send me an email and I will get back to you.
      I work remotely across EU and US timezones, on both fixed-scope projects and ongoing retainers.
    actions:
    - title: Book a Call
      icon: fa-calendar-alt
      url: https://calendly.com/prlic/15min
    - title: ivan@prlic.io
      icon: fa-envelope
      url: mailto:ivan@prlic.io?subject=Initial contact
    - title: LinkedIn
      icon: fa-linkedin
      icon_type: fab
      url: https://www.linkedin.com/in/iprlic/
    - title: GitHub
      icon: fa-github
      icon_type: fab
      url: https://github.com/iprlic
---
