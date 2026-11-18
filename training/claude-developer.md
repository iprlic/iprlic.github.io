---
layout: home
permalink: /training/claude-developer/
lang: en
ref: training-claude-developer
sticky_cta:
  label: Book a call
  url: https://calendly.com/prlic/15min
image:
  path: /assets/img/og-image.png
  width: 1200
  height: 630
locale: en_US
title: Claude Certified Developer Exam Prep Course (CCDV-F)
description: >-
  Two-day hands-on Claude course for developers: Claude API, prompts, tools and MCP, agents, Claude Code, security and evals. Prepares for CCDV-F.

last_updated: 2026-11-18
# Course JSON-LD (_includes/course-schema.html); price_from only where the price is published.
course:
  order: 2
  level: Intermediate
  exam: Claude Certified Developer – Foundations (CCDV-F)
  workload: P2D
  price_from: 4000

header:
  compact: true
  title: Building with Claude
  subtitle: Exam preparation for Claude Certified Developer – Foundations (CCDV-F)
  text: >-
    Two days of building, not watching: from choosing and costing a model to an
    API client, tools and an MCP server, a supervisor agent with guardrails,
    a team-configured Claude Code repository and an eval gate in CI. Every module
    ends with a coding lab on one running case, and the course maps to all eight
    CCDV-F exam domains.
  action:
    label: See the outline
    url: '#modules'
  proof:
    - 2 days
    - Developers, hands-on coding
    - Online or on site
    - English or Croatian, up to 20 participants

sections:
  - type: course-overview.html
    section_id: overview
    background_style: bg-subtle
    title: Who it's for and what you will be able to do
    text: >-
      One of four [Claude courses](/training/), for engineers who will build
      features and internal tools on Claude.
    columns:
      - title: Who it's for
        items:
          - Backend, full-stack and platform engineers adding Claude features to a product
          - Developers building internal agents, automations and integrations
          - Teams adopting Claude Code who want a shared, governed setup
          - Anyone preparing for the Claude Certified Developer – Foundations exam
      - title: What you'll be able to do
        items:
          - Choose a Claude model for a workload and estimate what it will cost to run
          - Build reliable API clients with streaming, prompt caching, batches and error handling
          - Engineer prompts and context that produce validated, structured output
          - Implement tools with approval gates and expose your own system as an MCP server
          - Decide between a workflow and an agent, then build an agent with guardrails
          - Secure a Claude application against prompt injection and data leakage, and gate releases on evals

  - type: course-modules.html
    section_id: modules
    title: Course outline
    text: >-
      Day 1 covers the building blocks, day 2 production systems. Each module
      opens with a request from a fictional invoicing SaaS company, includes live
      demos and a knowledge check, and closes with a coding lab.
    modules:
      - title: LLM Fundamentals and Model Selection
        text: >-
          How models generate text, tokens and sampling, comparing Claude models
          on quality, latency and price, and building a simple cost model.
        lab: Choose and cost a model
      - title: Claude API Mechanics
        text: >-
          The Messages API and solid engineering around it: streaming, vision,
          extended thinking, prompt caching, message batches, and Claude on cloud
          platforms such as Amazon Bedrock.
        lab: Build an invoice ingestion client
      - title: Prompt and Context Engineering
        text: >-
          Iterating a prompt against test cases, deciding what goes into the
          context and what stays out, and validating output before it is used.
        lab: Prompts, context and trustworthy output
      - title: Tools and MCP
        text: >-
          Tool definitions and error results, client and server tools, approval
          gates for risky actions, and when to build an MCP server.
        lab: Tools, approvals and an MCP server
      - title: Agents and Workflows
        text: >-
          When a fixed workflow beats an agent, building agents with the Agent
          SDK, supervisors and subagents, hooks, memory and common patterns.
        lab: Supervisor agent with guardrails
      - title: Application Design, Configuration and Claude Code
        text: >-
          Requirements and the application life cycle, configuration and prompt
          versioning, and running Claude Code for a team, headless and in CI.
        lab: Configure Claude Code and version prompts
      - title: Security and Safety
        text: >-
          Prompt injection and untrusted input, PII and access control, layered
          guardrails, least privilege, and secrets and key management.
        lab: Layer guardrails and lock down secrets
      - title: Evals, Debugging and Cost
        text: >-
          Reading traces and recovering from errors, designing and running evals,
          and managing tokens and cost in production.
        lab: Eval gate and cost report
      - title: Summary and Exam Readiness
        text: >-
          A recap of all eight domains, exam-style practice scenarios, what to
          expect on exam day, and next steps.

  - type: course-overview.html
    section_id: exam
    background_style: bg-subtle
    title: Exam alignment
    text: >-
      Every domain of the Claude Certified Developer – Foundations exam guide is
      taught in at least one module, weighted by its share of the exam.
      Try [20 free practice questions](/training/claude-mock-exams/#ccdv-f) for
      this exam, with an explanation for every answer.
      Not sure this is the right exam?
      [Compare all five Claude certifications](/training/claude-certifications/).
    facts:
      - label: Exam code
        value: CCDV-F
      - label: Questions
        value: "53"
      - label: Duration
        value: 120 minutes
      - label: Passing score
        value: 720 / 1,000
      - label: Exam fee
        value: USD 125
    columns:
      - title: Prerequisites
        items:
          - Comfortable writing code; labs use the Python SDK, and TypeScript developers follow along easily
          - Familiar with REST APIs, JSON, Git and the command line
          - A laptop with Python 3.11+, VS Code, Git and Claude Code installed
          - A Claude API key or Amazon Bedrock access, ideally your own; I help with the setup
      - title: Taking the exam
        items:
          - Taken at Pearson VUE, online proctored or at a test centre
          - Registration through the Anthropic Partner Academy, which requires the candidate's company to be a member of the Claude Partner Network
          - Multiple-choice and multiple-response questions, scaled score from 100 to 1,000
          - The certification is valid for 12 months
    note: >-
      Anthropic updates the CCDV-F exam content on 7 December 2026. The course
      is reviewed against the new exam guide before any delivery after that date.

  - type: faq.html
    section_id: faq
    title: Good to know
    items:
      - q: Who teaches the course?
        a: >-
          I do. I am an AWS Authorized Instructor and Claude Certified Architect –
          Professional, I have passed the Claude Certified Developer – Foundations
          exam myself, and I have 20+ years in software. My day job is building
          production Claude systems, such as a private, auditable Claude platform
          on Amazon Bedrock for a regulated organisation and an internal Claude
          Code plugin marketplace, and the labs come from that work. More on the
          [home page](/).

      - q: Online or on site, and in which language?
        a: >-
          Online as live sessions in half-day blocks, or on site anywhere in
          Europe, with travel charged at cost. The course runs in English or
          Croatian, for up to 20 participants per group.

      - q: Can the course be tailored to our team?
        a: >-
          Yes. The outline above is the exam-aligned core; I adapt the examples
          and labs to your stack and your use cases. You get a detailed outline to
          approve before the course.

      - q: What does it cost?
        a: >-
          Team training starts from €4,000 for a course of one to two days,
          excluding VAT and travel; the price depends on format and group size.
          Model usage during the labs is billed to your own Claude API or AWS
          account and is usually small; I estimate it in advance.

      - q: Is this an official Anthropic course?
        a: >-
          No. I am an independent trainer who holds Anthropic's Claude
          certifications and builds production systems with Claude. The course
          prepares for the Claude Certified Developer – Foundations exam but is
          not an official Anthropic course. The exam itself is taken at Pearson
          VUE; candidates register through the Anthropic Partner Academy, which
          requires their company to be a member of the Claude Partner Network.

  - type: contact.html
    section_id: contacts
    title: Book this course
    watermark: CCDV-F
    text: >-
      Tell me about the team and what they are building. A short call is usually
      enough to agree the format, the labs and the dates.
    actions:
      - title: Book a Call
        icon: fa-calendar-alt
        url: https://calendly.com/prlic/15min
      - title: ivan@prlic.io
        icon: fa-envelope
        url: mailto:ivan@prlic.io?subject=Course%3A%20Building%20with%20Claude%20(CCDV-F)
      - title: LinkedIn
        icon: fa-linkedin
        icon_type: fab
        url: https://www.linkedin.com/in/iprlic/
---
