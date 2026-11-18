---
layout: home
permalink: /training/claude-architect-professional/
lang: en
ref: training-claude-architect-professional
sticky_cta:
  label: Book a call
  url: https://calendly.com/prlic/15min
image:
  path: /assets/img/og-image.png
  width: 1200
  height: 630
locale: en_US
title: Claude Certified Architect Professional Course (CCAR-P)
description: >-
  Three-day course for senior architects: solution design, RAG, MCP and identity, evals, governance and team enablement on Claude. Prepares for CCAR-P.

header:
  compact: true
  title: Advanced Claude Architecture
  subtitle: Exam preparation for Claude Certified Architect – Professional (CCAR-P)
  text: >-
    Three days on the decisions a lead architect owns: turning a business brief
    into a solution design, integrating tools, MCP and identity with least
    privilege, tuning retrieval, proving quality with evals, building governance
    into the architecture, and handing a system over to the people who run it.
    The course ends with a capstone design case and covers all seven CCAR-P
    domains.
  action:
    label: See the outline
    url: '#modules'
  proof:
    - 3 days
    - Senior architects and tech leads
    - Online or on site
    - English or Croatian, up to 20 participants

sections:
  - type: course-overview.html
    section_id: overview
    background_style: bg-subtle
    title: Who it's for and what you will be able to do
    text: >-
      One of four [Claude courses](/training/), for the people accountable for
      Claude systems in production, from the first brief to the operating model.
    columns:
      - title: Who it's for
        items:
          - Senior solution and enterprise architects responsible for AI platforms
          - Tech leads and principal engineers who own a Claude system end to end
          - Architects in regulated organisations who must defend designs to security, risk and compliance
          - Anyone preparing for the Claude Certified Architect – Professional exam
      - title: What you'll be able to do
        items:
          - Turn a business brief into a defensible solution design and choose the right architectural pattern
          - Integrate tools, MCP servers and identity with least privilege and a sound context strategy
          - Design, tune and observe a RAG pipeline, and catch a bad index refresh before users do
          - Prove quality with metrics, evaluation datasets and A/B tests, and optimise cost and latency
          - Build layered guardrails, human review and compliance into the architecture
          - Run discovery, communicate trade-offs and hand a system over with SLAs and team enablement

  - type: course-modules.html
    section_id: modules
    title: Course outline
    text: >-
      All modules share one fictional EU insurer, each opening with a request
      from a different executive. Every module has a demo, a knowledge check and
      a hands-on lab or design exercise.
    modules:
      - title: Solution Design and Architecture
        text: >-
          From business problem to solution, choosing the architectural pattern,
          and when a multi-agent design is worth its complexity.
        lab: Business brief to solution design
      - title: Models, Prompting and Context Engineering
        text: >-
          Selecting the model, system prompts and guardrails, modular prompts,
          prompt caching, Skills and prompt reuse.
        lab: Engineer a prompt and its context
      - title: "Integration: Tools, MCP and Identity"
        text: >-
          Capability bloat and least privilege, identity, authentication and
          authorisation for agents, and protocol and context strategy.
        lab: Audit and fix an over-privileged agent integration
      - title: "Integration: RAG, Retrieval and Observability"
        text: >-
          Designing the RAG pipeline, matching retrieval to the data and the
          queries, chunking and hybrid search, and observability at scale.
        lab: Tune a RAG pipeline and catch a bad index refresh
      - title: Evaluation, Testing and Optimization
        text: >-
          Metrics and evaluation datasets, experiments and diagnosis, and
          optimising quality, cost and latency with observability.
        lab: Eval suite and A/B test
      - title: Governance, Safety and Risk
        text: >-
          Risks and layered guardrails, human-in-the-loop by design, compliance
          as architecture, fairness and transparency.
        lab: Red-team the guardrails
      - title: Stakeholder Communication and Lifecycle
        text: >-
          Structured discovery and requirements, decision memos and ADRs, SLAs,
          handoff and the system life cycle.
        lab: Discovery-to-handoff package
      - title: Developer Productivity and Team Enablement
        text: >-
          Configuring Claude Code for teams, sharing conventions, skills and
          tools, and the workflows and operations around them.
        lab: Configure Claude Code for a team
      - title: Capstone Design Case and Summary
        text: >-
          A full design case worked in phases across all seven domains,
          exam-style practice scenarios, and a study plan.

  - type: course-overview.html
    section_id: exam
    background_style: bg-subtle
    title: Exam alignment
    text: >-
      The course covers all seven domains of the Claude Certified Architect –
      Professional exam guide, with the heaviest domain, integration, split
      across two modules.
      Try [20 free practice questions](/training/claude-mock-exams/#ccar-p) for
      this exam, with an explanation for every answer.
    facts:
      - label: Exam code
        value: CCAR-P
      - label: Questions
        value: "63"
      - label: Duration
        value: 120 minutes
      - label: Passing score
        value: 720 / 1,000
      - label: Exam fee
        value: USD 175
    columns:
      - title: Prerequisites
        items:
          - Several years designing production systems; hands-on experience with Claude or another LLM platform
          - Able to read and run Python; labs use Python 3.11+ against local mock backends
          - A laptop with Python, VS Code, Git and Claude Code, plus a Claude API key or Amazon Bedrock access
          - The Foundations certification is not required for the exam
      - title: Taking the exam
        items:
          - Taken at Pearson VUE, online proctored or at a test centre
          - Registration through the Anthropic Partner Academy, which requires the candidate's company to be a member of the Claude Partner Network
          - Multiple-choice and multiple-response questions, scaled score from 100 to 1,000
          - The certification is valid for 12 months
    note: >-
      Anthropic updates the CCAR-P exam content on 7 December 2026. The course
      is reviewed against the new exam guide before any delivery after that date.

  - type: faq.html
    section_id: faq
    title: Good to know
    items:
      - q: Who teaches the course?
        a: >-
          I do. I am an AWS Authorized Instructor and hold Claude Certified
          Architect – Professional, the certification this course prepares for.
          My day job is designing production Claude systems, such as a private,
          auditable Claude platform on Amazon Bedrock for a regulated
          organisation and an internal Claude Code plugin marketplace, and the
          design cases come from that work. More on the [home page](/).

      - q: Online or on site, and in which language?
        a: >-
          Online as live sessions in half-day blocks, or on site anywhere in
          Europe, with travel charged at cost. The course runs in English or
          Croatian, for up to 20 participants per group.

      - q: Can the course be tailored to our team?
        a: >-
          Yes. The outline above is the exam-aligned core; the capstone can be
          run on one of your own systems instead of the fictional case. You get a
          detailed outline to approve before the course.

      - q: What does it cost?
        a: >-
          Team training starts from €4,000 for a course of one to two days,
          excluding VAT and travel; this course runs three days, and the price
          depends on format and group size.

      - q: Is this an official Anthropic course?
        a: >-
          No. I am an independent trainer who holds Anthropic's Claude
          certifications and builds production systems with Claude. The course
          prepares for the Claude Certified Architect – Professional exam but is
          not an official Anthropic course. The exam itself is taken at Pearson
          VUE; candidates register through the Anthropic Partner Academy, which
          requires their company to be a member of the Claude Partner Network.

  - type: contact.html
    section_id: contacts
    title: Book this course
    watermark: CCAR-P
    text: >-
      Tell me about the team and the systems they are accountable for. A short
      call is usually enough to agree the format, the capstone and the dates.
    actions:
      - title: Book a Call
        icon: fa-calendar-alt
        url: https://calendly.com/prlic/15min
      - title: ivan@prlic.io
        icon: fa-envelope
        url: mailto:ivan@prlic.io?subject=Course%3A%20Advanced%20Claude%20Architecture%20(CCAR-P)
      - title: LinkedIn
        icon: fa-linkedin
        icon_type: fab
        url: https://www.linkedin.com/in/iprlic/
---
