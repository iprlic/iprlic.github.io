---
layout: home
permalink: /training/claude-architect/
lang: en
ref: training-claude-architect
sticky_cta:
  label: Book a call
  url: https://calendly.com/prlic/15min
image:
  path: /assets/img/og-image.png
  width: 1200
  height: 630
locale: en_US
title: Claude Certified Architect Exam Prep Course (CCAR-F)
description: >-
  Two-day Claude course for architects: agentic loops, multi-agent systems, MCP, Claude Code in CI, structured output, reliability. Prepares for CCAR-F.

header:
  compact: true
  title: Architecting with Claude
  subtitle: Exam preparation for Claude Certified Architect – Foundations (CCAR-F)
  text: >-
    Two days on designing Claude systems that hold up in production: agentic
    loops and the Agent SDK, coordinator and subagent designs, MCP tools, Claude
    Code for a team and in CI, validated extraction, and agents that escalate
    instead of guessing. Every module ends with a lab, and the course covers all
    five CCAR-F domains through the exam's scenario style.
  action:
    label: See the outline
    url: '#modules'
  proof:
    - 2 days
    - Architects and senior engineers
    - Online or on site
    - English or Croatian, up to 20 participants

sections:
  - type: course-overview.html
    section_id: overview
    background_style: bg-subtle
    title: Who it's for and what you will be able to do
    text: >-
      One of four [Claude courses](/training/), for the people who decide how
      Claude fits into a system and who review the result.
    columns:
      - title: Who it's for
        items:
          - Solution architects designing agents, integrations and Claude-based platforms
          - Senior and lead engineers who own the design of a Claude feature
          - Platform and developer productivity teams rolling out Claude Code
          - Anyone preparing for the Claude Certified Architect – Foundations exam
      - title: What you'll be able to do
        items:
          - Build an agentic loop and control it deterministically with hooks and sessions
          - Design a coordinator with subagents, clean handoffs and sensible task decomposition
          - Design tool interfaces and MCP servers with structured errors and the right scope
          - Configure Claude Code for a team repository and run it in a CI pipeline
          - Get structured output that validates, with retries, batches and multi-pass review
          - Keep long-running agents reliable, with escalation, human review and provenance

  - type: course-modules.html
    section_id: modules
    title: Course outline
    text: >-
      All modules share one fictional retailer, so the exam's scenarios (support
      agent, research system, code generation, CI, data extraction) run on a
      single, consistent setting. Each module has demos, a knowledge check and a
      hands-on lab.
    modules:
      - title: Agentic Loops and the Agent SDK
        text: >-
          How the agentic loop works, hooks for deterministic control, and
          resuming and forking sessions.
        lab: Build and harden an agentic loop
      - title: Multi-Agent Orchestration
        text: >-
          Coordinator and subagent architecture, spawning subagents and passing
          context, enforcing structured handoffs, and decomposing tasks.
        lab: Multi-agent research coordinator
      - title: Tool Design and MCP Integration
        text: >-
          Designing tool interfaces, structured errors, distributing tools across
          agents, MCP servers in Claude Code and agents, and built-in tools for
          code exploration.
        lab: Design, harden and connect MCP tools
      - title: Claude Code Configuration
        text: >-
          The CLAUDE.md hierarchy, commands and skills, path-specific rules, and
          when to plan before executing.
        lab: Configure Claude Code for a team repository
      - title: Claude Code Workflows and CI/CD
        text: >-
          Running Claude Code in a pipeline, keeping automated review useful, and
          iterating tests-first.
        lab: Put Claude Code into a CI pipeline
      - title: Prompt Engineering and Structured Output
        text: >-
          Precise criteria and few-shot examples, structured output through tool
          use, validation and retry, batch processing, and multi-pass review.
        lab: Validated extraction pipeline
      - title: Context Management and Reliability
        text: >-
          Preserving context in long work, escalation and ambiguity, error
          propagation across agents, and human review with provenance.
        lab: Make agents reliable
      - title: Scenario Practice and Summary
        text: >-
          Exam-style practice across all six exam scenarios, a recap of the five
          domains, exam-day rules and a study plan.

  - type: course-overview.html
    section_id: exam
    background_style: bg-subtle
    title: Exam alignment
    text: >-
      The course covers all five domains of the Claude Certified Architect –
      Foundations exam guide. The exam is scenario-based: each sitting draws four
      scenarios at random from a bank of six, and the course practises all six.
    facts:
      - label: Exam code
        value: CCAR-F
      - label: Questions
        value: "60"
      - label: Duration
        value: 120 minutes
      - label: Passing score
        value: 720 / 1,000
      - label: Exam fee
        value: USD 125
    columns:
      - title: Prerequisites
        items:
          - Experience designing or building software systems, ideally with an LLM already in the mix
          - Able to read and run Python; labs use Python 3.11+, the Claude API and the Agent SDK
          - A laptop with Python, VS Code, Git and Claude Code installed
          - A Claude API key or Amazon Bedrock access, ideally your own; I help with the setup
      - title: Taking the exam
        items:
          - Taken at Pearson VUE, online proctored or at a test centre
          - Registration through the Anthropic Partner Academy, which requires the candidate's company to be a member of the Claude Partner Network
          - Multiple-choice and multiple-response questions, scaled score from 100 to 1,000
          - The certification is valid for 12 months

  - type: faq.html
    section_id: faq
    title: Good to know
    items:
      - q: Who teaches the course?
        a: >-
          I do. I am an AWS Authorized Instructor and Claude Certified Architect –
          Professional with 20+ years in software. My day job is designing
          production Claude systems, such as a private, auditable Claude platform
          on Amazon Bedrock for a regulated organisation and an internal Claude
          Code plugin marketplace, and the design cases come from that work. More
          on the [home page](/).

      - q: Online or on site, and in which language?
        a: >-
          Online as live sessions in half-day blocks, or on site anywhere in
          Europe, with travel charged at cost. The course runs in English or
          Croatian, for up to 20 participants per group.

      - q: Can the course be tailored to our team?
        a: >-
          Yes. The outline above is the exam-aligned core; I adapt the examples
          and design exercises to your architecture and use cases. You get a
          detailed outline to approve before the course.

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
          prepares for the Claude Certified Architect – Foundations exam but is
          not an official Anthropic course. The exam itself is taken at Pearson
          VUE; candidates register through the Anthropic Partner Academy, which
          requires their company to be a member of the Claude Partner Network.

  - type: contact.html
    section_id: contacts
    title: Book this course
    watermark: CCAR-F
    text: >-
      Tell me about the team and the systems they design. A short call is usually
      enough to agree the format, the cases and the dates.
    actions:
      - title: Book a Call
        icon: fa-calendar-alt
        url: https://calendly.com/prlic/15min
      - title: ivan@prlic.io
        icon: fa-envelope
        url: mailto:ivan@prlic.io?subject=Course%3A%20Architecting%20with%20Claude%20(CCAR-F)
      - title: LinkedIn
        icon: fa-linkedin
        icon_type: fab
        url: https://www.linkedin.com/in/iprlic/
---
