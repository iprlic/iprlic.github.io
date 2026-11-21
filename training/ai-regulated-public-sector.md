---
layout: home
permalink: /training/ai-regulated-public-sector/
lang: en
ref: training-ai-regulated-public-sector
sticky_cta:
  label: Register interest
  url: mailto:ivan@prlic.io?subject=Course%3A%20AI%20in%20Regulated%20and%20Public-Sector%20Organisations
image:
  path: /assets/img/og-image.png
  width: 1200
  height: 630
locale: en_US
title: Adopting AI in Regulated and Public-Sector Organisations
description: >-
  Two-day course on adopting AI safely in regulated industries and government: security, EU AI Act, GDPR, NIS2, classified information and a rollout plan.

last_updated: 2026-11-21
# Course JSON-LD (_includes/course-schema.html); price_from only where the price is published.
course:
  order: 6
  level: Intermediate
  workload: P2D
  instances:
    - mode: Online
      workload: P2D
    - mode: Onsite
      workload: P2D

header:
  compact: true
  title: AI in Regulated and Public-Sector Organisations
  subtitle: Adopt AI without losing control of your data
  text: >-
    A course for organisations where a data leak or a wrong decision has legal
    consequences: banks, insurers, healthcare, energy, public administration
    and their suppliers. It covers what the EU AI Act, GDPR and NIS2 ask of you,
    how to keep personal, confidential and classified information out of the
    wrong systems, how to secure AI assistants and agents, and how to buy and
    govern AI tools. Your team leaves with a classified list of use cases, a
    reference architecture and a rollout plan for one of them.
  action:
    label: See the outline
    url: '#modules'
  proof:
    - 2 days, in-house
    - Security, compliance and IT leads
    - Online or on site
    - English or Croatian

sections:
  - type: course-overview.html
    section_id: overview
    background_style: bg-subtle
    title: Who it's for and what you will be able to do
    text: >-
      One of the [practical AI courses](/training/#practical-ai), not tied to a
      certification exam. It brings the people who must say yes to AI (security,
      data protection, legal, IT) into one room with the people who want to use
      it, and gives them a shared way to decide.
    columns:
      - title: Who it's for
        items:
          - CISOs, security officers and IT architects who have to approve or build AI solutions
          - Data protection officers, compliance and legal teams who are asked "can we use this?"
          - Managers in public administration, healthcare, finance and energy who own AI initiatives
          - Procurement teams buying AI tools or writing tender specifications for them
          - Suppliers and integrators who build AI systems for regulated clients
      - title: What you'll be able to do
        items:
          - Explain which EU AI Act obligations apply to you as a provider or deployer, and which risk class each use case falls into
          - Decide when a use case needs a DPIA or a fundamental rights impact assessment, and what goes into it
          - Classify data and decide which AI service, hosting model and region each class may use, from public SaaS to private or on-premises models
          - Recognise the security risks specific to LLMs and agents, such as prompt injection and data exfiltration through tools, and the controls that address them
          - Assess an AI vendor: contract terms, data processing, data residency, retention, model training on your data, and exit
          - Set up governance that holds up in an audit: AI policy, inventory, human oversight, logging, monitoring and incident handling

  - type: course-modules.html
    section_id: modules
    title: Course outline
    text: >-
      Eight modules over two days. Each ends with an exercise on your own use
      cases, so by the end you have a classified use-case list, a reference
      architecture and a rollout plan. No coding.
    modules:
      - title: The Regulatory Map
        text: >-
          The EU AI Act (prohibited practices, high-risk systems, general-purpose
          models, transparency, AI literacy, and the timeline as amended), GDPR,
          NIS2 and sector rules such as DORA for finance and the medical device
          regulations, and how they overlap. Who is a provider and who is a
          deployer.
        lab: Map the rules that apply to your organisation
      - title: Classifying Use Cases
        text: >-
          Sorting AI use cases by AI Act risk class and by the data they touch.
          When a DPIA is required, when public bodies need a fundamental rights
          impact assessment, and which use cases to start with.
        lab: Classify your shortlist of use cases
      - title: Data Protection in Practice
        text: >-
          Lawful basis, minimisation and purpose limitation for AI, processors
          and sub-processors, international transfers, retention and "zero data
          retention" offers, whether the vendor trains on your data, and EU data
          residency options on the major clouds.
        lab: A data protection checklist for one use case
      - title: Confidential and Classified Information
        text: >-
          What must never reach a public AI service, how national and EU
          classification levels translate into hosting requirements, accredited
          and isolated environments, sovereign cloud and self-hosted open models,
          and handling sensitive but unclassified information.
        lab: A data-class to AI-service matrix
      - title: Securing AI Systems
        text: >-
          The threat model for LLMs and agents: prompt injection, data
          exfiltration through tools, insecure output handling, model and supply
          chain risks (the OWASP Top 10 for LLM applications). Identity and least
          privilege for agents, network isolation, guardrails, logging and
          separation between those who operate a system and those who audit it.
        lab: Threat-model an AI assistant on internal documents
      - title: Procurement and Vendor Due Diligence
        text: >-
          What to ask AI vendors and how to read the answers: data processing
          agreements, security certifications, data location, model changes,
          lock-in and exit. Writing requirements for AI in a public tender.
        lab: A vendor due diligence questionnaire
      - title: Governance and Operations
        text: >-
          An AI policy people actually follow, an inventory of AI systems, human
          oversight, evaluation and monitoring, incident handling and reporting,
          and staff AI literacy as the AI Act expects.
        lab: Draft your AI policy and inventory
      - title: Reference Architecture and Rollout
        text: >-
          A private assistant on internal documents as the worked example:
          architecture, controls, evidence for auditors, and a phased rollout
          from pilot to production with go and no-go criteria.
        lab: A rollout plan for your first use case

  - type: course-overview.html
    section_id: formats
    background_style: bg-subtle
    title: Formats
    text: >-
      Run in-house for one organisation, so the exercises use your real use
      cases, policies and systems. Discussions stay inside your organisation.
    facts:
      - label: Duration
        value: 2 days
      - label: Group
        value: up to 16
      - label: Delivery
        value: Online or on site
      - label: Coding
        value: None
    columns:
      - title: In-house, two days
        items:
          - Two days on site, or online in four half-day blocks
          - "A mixed group works best: security, data protection, legal, IT and the business owners of the use cases"
          - Examples and exercises adapted to your sector and the rules that apply to it
          - A detailed outline to approve before the course
      - title: What you keep
        items:
          - Your use cases classified by risk and data sensitivity
          - A data-class to AI-service matrix and a vendor questionnaire
          - A draft AI policy and AI system inventory
          - A reference architecture and rollout plan for your first use case
    note: >-
      New course. The first runs are scheduled with the organisations that
      register interest; tell me your sector, group size and preferred dates.
      No classified or personal data is used in the course: examples are public
      or synthetic, and your own material stays with you.

  - type: faq.html
    section_id: faq
    title: Good to know
    items:
      - q: Who teaches the course?
        a: >-
          I do. I design and build AI systems for regulated organisations, such
          as a private, auditable Claude platform on Amazon Bedrock that keeps
          data in the EU and separates the people who operate it from those who
          audit it. I am an AWS Authorized Instructor, hold the AWS Security
          Specialty and Claude Certified Architect – Professional
          certifications, and have 20+ years in software. More on the
          [home page](/).

      - q: Is this legal advice?
        a: >-
          No. The course covers the technical and organisational side of
          compliance: what the rules require in practice and how to build and
          run systems that meet them. Legal interpretation for your specific
          case stays with your lawyers and data protection officer, who are
          welcome in the room.

      - q: Is it tied to one AI vendor?
        a: >-
          No. It covers public AI services (ChatGPT, Microsoft 365 Copilot,
          Claude, Gemini), the cloud platforms (Amazon Bedrock, Azure, Google
          Cloud) and self-hosted open models. The worked examples come from
          systems I have built on AWS, because that is where I can show real
          controls rather than slides.

      - q: Do you need access to our classified or confidential material?
        a: >-
          No. The course uses public and synthetic examples. Exercises work on
          descriptions of your use cases, and what your team writes stays with
          your team. If a use case cannot be discussed openly, we work on a
          sanitised version of it.

      - q: Online or on site, and in which language?
        a: >-
          On site anywhere in Europe, with travel charged at cost, or online in
          half-day blocks. The course runs in English or Croatian.

      - q: What does it cost?
        a: >-
          Team training starts from €4,000 for a course of one to two days,
          excluding VAT and travel; the final price depends on format and group
          size.

  - type: contact.html
    section_id: contacts
    title: Register interest
    watermark: COMPLIANCE
    text: >-
      Tell me your sector, who would attend and roughly when. I will send a
      detailed outline and propose dates for the first run.
    actions:
      - title: Book a Call
        icon: fa-calendar-alt
        url: https://calendly.com/prlic/15min
      - title: ivan@prlic.io
        icon: fa-envelope
        url: mailto:ivan@prlic.io?subject=Course%3A%20AI%20in%20Regulated%20and%20Public-Sector%20Organisations
      - title: LinkedIn
        icon: fa-linkedin
        icon_type: fab
        url: https://www.linkedin.com/in/iprlic/
---
