---
layout: home
permalink: /training/build-ai-agents/
lang: en
ref: training-build-ai-agents
sticky_cta:
  label: Book a call
  url: https://calendly.com/prlic/15min
image:
  path: /assets/img/og-image.png
  width: 1200
  height: 630
locale: en_US
title: Build AI Agents with Claude, a No-Code Course
description: >-
  No-code course for business teams: build a working Claude agent for a process from your own job and learn to check it is reliable. 6 weeks or 3 days.

last_updated: 2026-11-18
# Course JSON-LD (_includes/course-schema.html); price_from only where the price is published.
course:
  order: 5
  level: Beginner
  workload: P3D
  instances:
    - mode: Online
      workload: PT16H
    - mode: Online
      workload: P3D
    - mode: Onsite
      workload: P3D

header:
  compact: true
  title: Build AI Agents with Claude
  subtitle: From using AI to building with it
  text: >-
    A no-code course for people who already use AI chat and want it to do real
    work. You map a process from your own job, design and prompt an agent for
    it, test it against cases where you know the right answer, give it your
    documents and tools, and automate it end to end. Each participant leaves
    with a working agent and a way to check that it is reliable.
  action:
    label: See the outline
    url: '#modules'
  proof:
    - 6 weeks online or 3 days in-house
    - Business professionals, no coding
    - Online or on site
    - English or Croatian

sections:
  - type: course-overview.html
    section_id: overview
    background_style: bg-subtle
    title: Who it's for and what you will be able to do
    text: >-
      One of the [practical AI courses](/training/#practical-ai), not tied to a
      certification exam, for people who want AI to take over part of a process
      rather than answer questions in a chat window.
    columns:
      - title: Who it's for
        items:
          - Business professionals who use Claude, ChatGPT or Gemini every day and want more out of them
          - Product owners and project managers who need to know what an agent can and cannot take over
          - Operations, HR and finance leads with repetitive processes built on email, forms and spreadsheets
          - Teams that want people who can build and maintain simple agents without waiting for developers
      - title: What you'll be able to do
        items:
          - Explain how LLMs and agents work, and what Claude, ChatGPT and Gemini are each good at
          - Map a process and decide which steps an agent does and which stay with a person
          - Write prompts that hold up across many inputs, with structure, examples, roles and fixed output formats
          - Build a test set and scorecard that tell you when the agent is wrong
          - Give the agent your knowledge and tools with Claude Projects, Skills and connectors, and run it end to end with n8n or Make
          - Keep company data safe, set guardrails, and make the business case for rolling the agent out

  - type: course-modules.html
    section_id: modules
    title: Course outline
    text: >-
      Eight live sessions of two hours. Every session moves your own capstone
      forward and ends with something you keep, so by the last one you have a
      working agent, a test set and a one-page business case.
    modules:
      - title: How LLMs and Agents Work
        text: >-
          What a language model does and does not do, what turns it into an
          agent, and what Claude, ChatGPT and Gemini are each good at. Choosing
          the process from your own job that becomes your capstone.
        lab: Scope your capstone process
      - title: Process Mapping and Agent Design
        text: >-
          Mapping the process step by step, deciding which steps the agent does
          and which stay with a person, and writing it down before building
          anything.
        lab: A one-page agent spec with inputs, outputs, decisions and failure cases
      - title: Prompting That Holds Up
        text: >-
          Structure, examples, roles and output formats that keep working on the
          hundredth input, not just the first.
        lab: A tested prompt for your agent
      - title: Validating Output
        text: >-
          Test sets, spotting hallucinations, and the question every agent needs
          an answer to: how would we know it's wrong?
        lab: A 10-case test set and scorecard
      - title: Claude Projects, Skills and Connectors
        text: >-
          Giving the agent your knowledge and your tools: documents,
          instructions, reusable Skills and connections to the apps you already
          use.
        lab: A Project with your own documents plus one Skill
      - title: No-Code Automation with n8n or Make
        text: >-
          Triggering the agent from email, forms or spreadsheets and passing its
          output on, so it runs without anyone copying and pasting.
        lab: Your agent running end to end
      - title: Knowledge, Memory and Data Protection
        text: >-
          Retrieval (RAG) in plain language, what the agent should remember, what
          never goes into an AI tool, and guardrails that keep it within company
          policy.
        lab: Guardrails and a data checklist for your agent
      - title: Capstone Demos and Rollout
        text: >-
          Demonstrating the agents, measuring the value they add, and rolling
          them out to the rest of the team.
        lab: A live demo and a one-page business case

  - type: course-overview.html
    section_id: formats
    background_style: bg-subtle
    title: Formats
    text: >-
      The same eight sessions, run as an open cohort over six weeks or
      condensed into three days for one team.
    facts:
      - label: Live sessions
        value: 8 × 2 hours
      - label: Cohort
        value: 6 weeks
      - label: In-house
        value: 3 days
      - label: Coding
        value: None
    columns:
      - title: Cohort, public or through a training partner
        items:
          - Eight live online sessions of two hours over six weeks, 16 hours in total
          - Short pre-work before the sessions, so live time goes on building
          - Two office-hour slots for help with your own capstone
          - Time between sessions to try the agent on your real work and bring back what broke
      - title: In-house, for one team
        items:
          - Three days, online in half-day blocks or on site
          - Participants work on processes from the same organisation, so the agents can be shared and maintained together
          - Examples, tools and data rules adapted to your policies
          - A detailed outline to approve before the course
    note: >-
      Participants need a laptop, a paid Claude plan (Pro, Team or Enterprise)
      and access to n8n or Make; I help with the setup. Everyday use of an AI
      chat tool helps, coding experience is not needed.

  - type: faq.html
    section_id: faq
    title: Good to know
    items:
      - q: Who teaches the course?
        a: >-
          I do. I am an AWS Authorized Instructor and Claude Certified Architect –
          Professional, with 20+ years in software. My day job is building
          production Claude systems, such as a private, auditable Claude platform
          on Amazon Bedrock for a regulated organisation and an internal Claude
          Code plugin marketplace, so the course shows what holds up in real use.
          More on the [home page](/).

      - q: Do participants need to code?
        a: >-
          No. Everything is built in claude.ai and a no-code automation tool
          (n8n or Make). The course also teaches you to recognise when a step
          does need a developer, and to write a spec they can pick up.

      - q: Which process should I bring?
        a: >-
          One you know well, that repeats, and whose result someone checks
          today: sorting incoming requests, drafting replies from a knowledge
          base, pulling data from documents into a spreadsheet, preparing a
          regular report. We scope it together in the first session, including
          which data may and may not go into an AI tool.

      - q: Online or on site, and in which language?
        a: >-
          The cohort runs online. The in-house version runs online in half-day
          blocks or on site anywhere in Europe, with travel charged at cost. The
          course runs in English or Croatian.

      - q: What does it cost?
        a: >-
          Team training starts from €4,000 for a course of one to two days,
          excluding VAT and travel; the price of the three-day in-house version
          depends on format and group size. Places on a public or partner cohort
          are priced by whoever runs the cohort.

      - q: Is this an official Anthropic course?
        a: >-
          No. I am an independent trainer who holds Anthropic's Claude
          certifications and builds production systems with Claude. The course
          is not an official Anthropic course and does not prepare for a
          certification exam; it is about building agents that work.

  - type: contact.html
    section_id: contacts
    title: Book this course
    watermark: AGENTS
    text: >-
      Tell me who the course is for, how many people, and whether you want a
      cohort or an in-house version. A short call is usually enough to agree the
      format and the dates.
    actions:
      - title: Book a Call
        icon: fa-calendar-alt
        url: https://calendly.com/prlic/15min
      - title: ivan@prlic.io
        icon: fa-envelope
        url: mailto:ivan@prlic.io?subject=Course%3A%20Build%20AI%20Agents%20with%20Claude
      - title: LinkedIn
        icon: fa-linkedin
        icon_type: fab
        url: https://www.linkedin.com/in/iprlic/
---
