---
layout: home
permalink: /
lang: en
ref: home
sticky_cta:
  label: Book a call
  url: https://calendly.com/prlic/15min
image: /assets/img/og-image.png
title: AI Advisory & Cloud Architecture
description: >-
  Ivan Prlić — AI advisory and cloud architecture for regulated EU and US
  companies. Fixed-scope assessment, proof of value, and fractional AI
  leadership, plus bespoke cloud and DevOps engineering. AWS Authorized
  Instructor, 14 professional certifications.

header:
  title: AI and cloud systems that reach production
  subtitle: AI Advisory · Solutions Architect · Fractional CTO
  text: >-
    I help leadership teams work out which AI use cases are actually worth
    funding, then build the first one — on infrastructure that holds up under
    audit. Twenty years of cloud architecture, with the same person writing the
    roadmap and the code.
  action:
    label: See What You Get
    url: '#packages'
  proof:
    - Assessment · 2–3 weeks · from €10,000
    - Fee credited against the build
    - Your cloud account, EU region

sections:
  - type: clients.html
    section_id: clients
    background_style: bg-subtle
    title: Who I Have Worked With
    text: >-
      Past and current clients, across public sector, automotive, travel,
      hospitality, and financial services.
    clients:
      - name: European Commission
      - name: Volvo USA
      - name: TUI Group
      - name: Ricoh
      - name: Talkdesk
      - name: Metro (Hospitality Digital)
      - name: Q.ai (Forbes)

  - type: packages.html
    section_id: packages
    title: What You Get
    text: >-
      Fixed scope, fixed price, fixed duration. Start anywhere on the ladder and
      stop after any step.
    footnote: >-
      Prices are per engagement, excluding VAT and travel, and scale with company
      size and scope. Fixed price means that if the work runs long, that is my
      problem and not your budget's.
    packages:
      - eyebrow: Start here
        name: AI Readiness & Opportunity Assessment
        duration: 2–3 weeks
        price: from €10,000
        price_min: 10000
        featured: true
        summary: >-
          The engagement most clients start with. I interview the people who do the
          work, look at your data and infrastructure as they actually are, and come
          back with a sequenced plan you can take to both your board and your auditors.
        deliverables:
          - Prioritized use-case portfolio, with estimated cost, effort, and payback per case
          - Data and infrastructure readiness gaps, named and sequenced rather than listed
          - AI Act classification of each candidate use case and the obligations that follow
          - A build-versus-buy call for every shortlisted case, with the reasoning
          - Reference architecture for the first use case, costed at your expected volume
          - A 12-month roadmap built around decision points, not a wish list
        note: Fee credited in full against a Proof of Value build booked within 90 days.
        action:
          label: Book an intro call
          url: https://calendly.com/prlic/15min

      - eyebrow: Before you commit
        name: AI Opportunity Workshop
        duration: Half day
        price: from €1,500
        price_min: 1500
        summary: >-
          A structured working session with your leadership and operations leads.
          Often the cheapest way to find out that the thing everyone is excited
          about is not the thing worth doing first.
        deliverables:
          - Long list of candidate use cases, scored on value and feasibility
          - Written summary of the three worth pursuing, and why the rest are not
          - A clear read on whether a full assessment is warranted
        note: Remote or on-site anywhere in the EU.

      - eyebrow: The part most firms skip
        name: Proof of Value Build
        duration: 6–8 weeks
        price: from €30,000
        price_min: 30000
        summary: >-
          One use case, built and running against your real data. This is where a
          strategy engagement normally ends and where mine keeps going.
        deliverables:
          - Deployed in your own cloud account, EU region, under your IAM
          - Evaluation harness, so answer quality is measured rather than asserted
          - Running cost measured at real volume, not estimated in a spreadsheet
          - Handover documentation and a working session with the team who will own it

      - eyebrow: Ongoing
        name: Fractional AI Leadership
        duration: Monthly
        price: from €5,000/mo
        price_min: 5000
        summary: >-
          A senior technical voice in the room for companies that need AI decisions
          made well but cannot justify a full-time hire to make them.
        deliverables:
          - Standing time with your leadership team, weekly or fortnightly
          - Architecture and vendor decisions made, documented, and defensible later
          - Review of work delivered by internal teams and outside suppliers
          - Hiring input for AI and platform roles
        note: Three-month minimum, then rolling monthly with 30 days' notice.

      - eyebrow: Enablement
        name: Team Training
        duration: 1–2 days
        price: from €4,000
        price_min: 4000
        summary: >-
          Separate tracks for leadership and for engineers, built around your stack
          and your real use cases rather than a generic curriculum.
        deliverables:
          - Delivered by an AWS Authorized Instructor
          - Leadership track covering what to fund, what to refuse, and what to ask for
          - Engineering track covering RAG, evaluation, cost control, and failure modes
          - Exercises and material your team keeps afterwards

  - type: services.html
    section_id: services
    background_style: bg-subtle
    title: Also Available
    text: >-
      Engineering work scoped per project rather than packaged. Often follows an
      advisory engagement, but available on its own.
    services:
      - title: Cloud Architecture
        text: >-
          Architecture design across AWS, GCP, and Azure — serverless, microservices,
          Kubernetes (EKS, GKE), event-driven systems with Kafka and SQS/SNS, and API
          management with Apigee and WSO2. I apply Domain-Driven Design to decompose
          legacy monoliths into maintainable, independently deployable services.
        icon: fa-cloud
      - title: Cloud Migration
        text: >-
          Full-cycle migrations from on-prem to AWS and GCP. Past work includes a
          Magento 2 platform to Kubernetes on EKS, healthcare systems, and computer
          vision workloads. I handle architecture, risk planning, FinOps (rightsizing,
          reserved instances, cost dashboards), and delivery.
        icon: fa-cloud-upload-alt
      - title: DevOps as a Service
        text: >-
          Infrastructure as code with Terraform and Ansible, containers with Docker and
          Kubernetes, monitoring with Datadog and Prometheus. Security covered: AWS WAF,
          Shield, IAM, and Secrets Manager. CI/CD across GitLab, GitHub Actions, BitBucket,
          and Azure DevOps. For teams that need DevOps capacity without a full-time hire.
        icon: fa-cogs
      - title: Serverless Architecture
        text: >-
          Serverless system design and implementation using AWS Lambda, API Gateway,
          Step Functions, and the Serverless Framework. I have built serverless backends
          for a healthcare startup (acquired by Carbon Health), a loyalty card platform,
          and a litigation support system.
        icon: fa-code

  - type: case-studies.html
    section_id: work
    title: Selected Work
    studies:
      - tag: Legal Tech · AWS Bedrock · Private RAG
        title: LLM Document Search Without the Data Leaving
        body: >-
          A legal technology client needed large volumes of sensitive documents made
          searchable and summarizable, with a hard constraint that nothing could be
          sent to an external service. Built a RAG knowledge base on Amazon Bedrock
          inside their own AWS environment. Lawyers ask questions in plain language
          and get sourced, referenced answers rather than a list of search hits.
        outcomes:
          - Research that took hours now takes seconds
          - Every document stayed inside the client's own AWS account
          - Answers cite their sources, which is what made legal sign off
      - tag: Healthcare · AWS · Serverless
        title: Clinical-Grade Platform, No Servers to Manage
        body: >-
          A healthcare startup needed a backend that could handle unpredictable
          clinical load and meet reliability requirements without a team to run
          infrastructure. Designed a fully serverless architecture on AWS using API
          Gateway, Lambda, the Serverless Framework, and Kafka. The company was
          subsequently acquired by Carbon Health.
        outcomes:
          - In production in weeks rather than months
          - No idle infrastructure cost between load peaks
          - Scaled through clinical demand spikes without anyone intervening
      - tag: Travel · AWS · Governance
        title: Cloud Foundation for a Global Travel Group
        body: >-
          One of the world's largest travel companies needed a cloud native
          foundation built from scratch that was production-ready and auditable from
          day one. Delivered the full stack on AWS with Terraform for infrastructure
          as code, GitLab CI/CD, Apigee for API management, and Datadog for monitoring.
        outcomes:
          - Every environment reproducible from code, with no manual state to explain
          - Full observability and alerting live from the first deployment
          - Release process auditable end to end
      - tag: Retail · AWS · Kubernetes
        title: E-Commerce Platform Migration to Kubernetes
        body: >-
          A retail client running a Magento 2 platform on ageing infrastructure needed
          a setup that could scale and was cheaper to run. Migrated to Kubernetes on
          AWS EKS using Helm for deployments, RDS for the database layer, and S3 for
          storage. The team went from manual, error-prone deployments to a fully
          repeatable, environment-consistent process.
        outcomes:
          - Scaling became automatic, with no fixed-capacity servers to size
          - Deployments became fully repeatable across all environments
          - Eliminated a whole class of incidents caused by manual release steps


  # Testimonials render only once real quotes are added. Nothing is invented
  # here on purpose. Pull 2-3 from LinkedIn recommendations, keep the wording
  # verbatim, and ask permission before naming the person's employer.
  #
  # - type: testimonials.html
  #   section_id: testimonials
  #   title: What Clients Say
  #   quotes:
  #     - text: "…"
  #       name: Full Name
  #       role: Job Title, Company
  #       source: LinkedIn recommendation
  #       url: https://www.linkedin.com/in/iprlic/details/recommendations/

  - type: about.html
    section_id: who
    photo: assets/img/members/headshot_zoomed.webp
    title: One person. No handover to juniors.
    availability: Taking new engagements
    badges:
      - text: AWS Authorized Instructor
      - text: 14 Professional Certifications
      - text: Toptal Expert Network
        url: https://www.toptal.com/resume/ivan-prlic
      - text: EU Entity, EU Invoicing
    text: >-
      I'm Ivan Prlić, founder of Prlić Consulting. Twenty years in cloud
      architecture, most recently building AI systems that had to survive a
      compliance review before they were allowed anywhere near production.


      You deal with me directly throughout. The person on the scoping call is the
      person writing the roadmap and the person writing the code, which is the
      main practical difference between this and hiring a firm.


      Prlić Consulting d.o.o. is registered in Zagreb, Croatia. I work remotely
      across EU and US timezones and travel for on-site work in the EU.
    tech: "Amazon Bedrock · SageMaker · Vertex AI · Azure OpenAI · AWS · GCP · Azure · Kubernetes · Terraform"
    languages: "English (C2, Cambridge Certified) · Croatian (Native)"
    certs_title: Certified
    certs:
      - name: AWS Authorized Instructor
        url: https://www.credly.com/badges/aa16c1eb-174e-4ba7-ad30-484fe1819135
      - name: AWS ML – Specialty
        url: https://www.credly.com/badges/cfc09e60-e068-4529-be07-641bfc1c7465
      - name: AWS Solutions Architect – Pro
        url: https://www.credly.com/badges/df4f87b6-f80b-4df1-bc5f-321432d3749e
      - name: AWS DevOps Engineer – Pro
        url: https://www.credly.com/badges/cd04983d-c963-4444-9f9f-2ae1eea48a8e
      - name: GCP Cloud Architect
        url: https://www.credly.com/badges/53d187e0-8e95-4faf-8a90-2c27e722358f
      - name: GCP ML Engineer
        url: https://www.credly.com/badges/4c131b3c-4813-4bfb-8f18-009ed66af68d
      - name: GCP Data Engineer
        url: https://www.credly.com/badges/857eeecc-62b7-4fdf-ba26-cb4a1290e1af
      - name: GCP DevOps Engineer
        url: https://www.credly.com/badges/07939388-bea1-4528-84f3-8f69244a7d4a
      - name: Azure Solutions Architect Expert
        url: https://learn.microsoft.com/en-us/users/ivanprli-9878/credentials/52c2b88eac40c8b9
      - name: Azure DevOps Engineer Expert
        url: https://learn.microsoft.com/en-us/users/ivanprli-9878/credentials/7b0110cf22902d3b
      - name: Azure AI Engineer Associate
        url: https://learn.microsoft.com/en-us/users/ivanprli-9878/credentials/3f82b44ab38fd66a
      - name: PMP
        url: https://www.credly.com/badges/83b699c7-d3c0-42e7-9b2b-e32b6b3247c3
      - name: CKA
        url: https://www.credly.com/badges/27198888-44fd-4ae7-942b-de89f7f01feb
      - name: Google Cloud Champion Innovator

  # Every answer is sourced from Ivan's CV and existing engagements. The five
  # questions he still has to answer himself are stubbed at the bottom of this
  # block. Do not invent answers for them.
  - type: faq.html
    section_id: faq
    background_style: bg-subtle
    title: Before You Ask
    text: >-
      The questions that decide these engagements are rarely about capability.
      These are the ones procurement and legal raise.
    items:
      - q: Where does our data actually live?
        a: >-
          In your own cloud account, in an EU region, under your own IAM. I build
          inside your perimeter rather than in mine, so there is no vendor
          environment holding your data and nothing to unwind if we stop working
          together. On the legal document search system I built on Amazon Bedrock,
          no document ever left the client's own AWS account, which is what made
          it possible for their legal team to sign off.

      - q: Have you worked under formal compliance requirements before?
        a: >-
          Yes. I designed the cloud architecture for Q.ai, an AI-powered
          investment platform, under financial-grade requirements including SOC 2
          controls, encryption, and audit logging. I have built healthcare systems
          with clinical reliability requirements, delivered for the European
          Commission, and worked on enterprise systems at Volvo USA and TUI Group
          where security and governance frameworks were set by the client. I am
          used to architecture decisions having to be explainable to an auditor.

      - q: Who actually does the work?
        a: >-
          I do, all of it. The person on the intro call is the person writing the
          roadmap and the person writing the code. There is no bench, no
          handover to a delivery team, and no junior learning on your budget.
          The trade-off is honest: I am one person, so if you need ten, I am the
          wrong answer.

      - q: What does the AI Act actually require of us right now?
        a: >-
          Less than most vendors imply. Obligations for general-purpose AI models
          have applied since August 2025. The deadlines for high-risk systems were
          pushed back by the Digital Omnibus to December 2027 for Annex III and
          August 2028 for Annex I. So this is a preparation window rather than an
          emergency. The assessment classifies each of your candidate use cases
          and tells you which obligations follow, so you can plan against real
          dates instead of a sales pitch.

      - q: Can you work alongside our internal team or an existing supplier?
        a: >-
          Usually that is the arrangement. At Metro's Hospitality Digital I led
          architecture across several existing development teams, at Ricoh I
          coached an in-house team, and at TUI Group I guided their developers on
          cloud-native patterns rather than replacing them. Part of the fractional
          retainer is reviewing work delivered by internal teams and outside
          suppliers.

      - q: What happens if the assessment concludes we should not do this?
        a: >-
          Then that is the deliverable, and it is a good outcome. Finding out in
          two weeks that a use case does not pay off is worth considerably more
          than finding out after a six-figure build. I would rather write that
          than take on delivery work I do not think will hold up.

      - q: Are you an EU entity, and how does invoicing work?
        a: >-
          Prlić Consulting d.o.o. is a Croatian limited company, registered in
          Zagreb since November 2017, OIB 84570551730. EU entity, EU invoicing, EU
          data residency. I work remotely across EU and US timezones and travel
          for on-site work anywhere in the EU.

      # ==================================================================
      # STILL TO ANSWER - Ivan only. These are the questions a regulated buyer
      # asks last and that most often stall a deal. Uncomment and fill in.
      #
      #   - q: Will you sign our NDA and DPA?
      #   - q: Do you carry professional indemnity insurance?
      #   - q: Who owns the IP in what you build?
      #   - q: What are your payment terms?
      #   - q: Do any of our documents reach third-party AI services?
      # ==================================================================

  - type: contact.html
    section_id: contacts
    title: Start with a call
    watermark: LET'S TALK
    text: >-
      A short call, no charge, no deck. We work out whether there is a real
      opportunity here and whether I am the right person for it. If the answer is
      no, you will hear it on the call.
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
