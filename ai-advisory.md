---
layout: home
permalink: /ai-advisory/
lang: en
ref: advisory
nav_menu: advisory
image: /assets/img/og-advisory.png
nav_cta_label: Book an Intro Call
sticky_cta:
  label: Book an intro call
  url: https://calendly.com/prlic/15min
title: AI Advisory for Regulated EU Companies
description: >-
  Fixed-scope AI advisory and delivery for legal, financial services, healthcare,
  and public sector organizations in the EU. Assessment, proof of value, and
  fractional AI leadership from an AWS Authorized Instructor. Your data stays in
  your own cloud account.

header:
  title: AI that reaches production inside your perimeter
  subtitle: AI Advisory for Regulated EU Companies
  text: >-
    Most AI pilots in regulated industries die somewhere between the demo and the
    compliance review. I help legal, financial services, healthcare, and public
    sector organizations pick the use cases that actually pay off, then build the
    first one on infrastructure your auditors can live with.
  action:
    label: See the Packages
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

  - type: fit.html
    section_id: fit
    title: Who This Is For
    text: >-
      I work with a narrow set of companies, because that is where one person with
      this background is genuinely more useful than a large firm.
    fit_title: A good fit if
    fit:
      - You operate in a regulated sector - legal, financial services, healthcare, insurance, or public sector supply
      - Your data cannot leave your own infrastructure, or cannot leave the EU
      - Roughly 50 to 1,000 people, with a real engineering function but no AI specialist in it
      - Your board or executive team has asked for an AI plan, and attached a date to it
      - You have run a pilot or two that never made it past the demo
    not_fit_title: Not a fit if
    not_fit:
      - You need a deck for the board and nothing after it
      - You need a team of ten rather than one senior person who also builds
      - You are pre-seed and looking for someone to build the product for equity
      - The decision is already made and you need someone to validate it

  - type: packages.html
    section_id: packages
    background_style: bg-subtle
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

  - type: case-studies.html
    section_id: proof
    title: Proof
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
          as code, GitLab CI/CD, Apigee for API management, and Datadog for
          monitoring.
        outcomes:
          - Every environment reproducible from code, with no manual state to explain
          - Full observability and alerting live from the first deployment
          - Release process auditable end to end
      - tag: Public Sector · Enterprise
        title: Where Else I Have Worked
        body: >-
          Beyond the engagements above, past and current clients include the
          European Commission, Volvo USA, Talkdesk, and Ricoh. The common thread is
          organizations where a system going wrong is expensive, visible, or both,
          and where the architecture has to be explainable to someone who did not
          build it.
        outcomes:
          - Enterprise and public sector delivery experience
          - Remote across EU and US timezones
          - EU-registered entity, EU invoicing


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
    actions:
      - title: See What You Get
        url: '#packages'
        class: btn-light

  - type: process.html
    section_id: process
    title: How It Runs
    text: >-
      No proposal decks and no procurement theatre. You will know the price and
      the scope before you commit to anything.
    steps:
      - title: Intro call
        duration: Free
        text: >-
          We work out whether there is something here worth doing and whether I am
          the right person to do it. If the answer to either is no, you will hear
          that on the call rather than in a follow-up email three weeks later.
      - title: Scoping note
        duration: 2–3 days
        text: >-
          A short written note back: what I would do, what it costs, how long it
          takes, and exactly what you end up holding at the end. Fixed price.
      - title: Assessment
        duration: 2–3 weeks
        text: >-
          Interviews with the people who actually do the work, a review of your data
          and infrastructure, and a written roadmap that survives contact with both
          your board and your compliance function.
      - title: Build
        duration: 6–8 weeks
        text: >-
          The first use case goes into production in your own environment. Most
          advisory engagements stop before this point, which is the main reason so
          many AI roadmaps never turn into anything.
      - title: Handover or retainer
        duration: Ongoing
        text: >-
          Either your team takes it from here with documentation and a running
          system, or I stay on monthly to keep the next use cases moving.

  - type: readiness-check.html
    section_id: readiness
    background_style: bg-subtle
    title: Are You Ready?
    text: Ten questions. Tick the ones that are true today.
    questions:
      - Someone at executive level owns the AI agenda by name, not by committee
      - There is a budget line for AI work this year, not just interest in the topic
      - You can name the specific business process you want to improve first
      - You know what that process costs you today, in money or in hours
      - The data that process runs on lives in one place and someone owns it
      - You have a cloud account you control, in a region your legal team accepts
      - Someone internally could maintain what gets built after the consultant leaves
      - You know which of your use cases would count as high risk under the AI Act
      - There is internal agreement on what "good enough" means for an AI answer
      - A previous pilot either shipped, or you know precisely why it did not
    thresholds:
      low: >-
        Fewer than four. Start with a workshop. Half a day now will stop you
        spending six figures on the wrong use case later.
      mid: >-
        Four to seven. The unticked boxes are the assessment. Two to three weeks
        gets you a defensible sequence and a roadmap that holds up under scrutiny.
      high: >-
        Eight or more. You are ready to build. Skip the strategy work and go
        straight to a proof of value on your highest-value use case.
    actions:
      - label: See the packages
        url: '#packages'
      - label: Book an intro call
        url: https://calendly.com/prlic/15min
        class: btn-outline

  # Testimonials render only once real quotes are added below. Nothing is
  # invented here on purpose. Pull 2–3 from LinkedIn recommendations, keep the
  # wording verbatim, and ask permission before naming the person's employer.
  #
  # - type: testimonials.html
  #   section_id: testimonials
  #   background_style: bg-subtle
  #   title: What Clients Say
  #   quotes:
  #     - text: "…"
  #       name: Full Name
  #       role: Job Title, Company
  #       source: LinkedIn recommendation
  #       url: https://www.linkedin.com/in/iprlic/details/recommendations/
  # Every answer below is sourced from Ivan's CV and existing engagements.
  # Questions he still has to answer himself are stubbed at the bottom of this
  # block, commented out. Do not invent answers for them.
  - type: faq.html
    section_id: faq
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
      #     a: >-
      #       [Do you sign client paper as standard? Do you have your own
      #       templates? Any clauses you routinely push back on?]
      #
      #   - q: Do you carry professional indemnity insurance?
      #     a: >-
      #       [Insurer, cover level, and whether you can provide a certificate
      #       on request. Enterprise procurement asks for this by default.]
      #
      #   - q: Who owns the IP in what you build?
      #     a: >-
      #       [Standard position: client owns deliverables on final payment?
      #       Any retained rights to generic tooling or boilerplate?]
      #
      #   - q: What are your payment terms?
      #     a: >-
      #       [Deposit up front? Milestone billing? Net 30? Currency?]
      #
      #   - q: Do any of our documents reach third-party AI services?
      #     a: >-
      #       [Your own tooling policy during an engagement - which AI tools you
      #       use on client material, and under what terms. Buyers in this
      #       segment increasingly ask.]
      # ==================================================================

  # Sits between the light Proof section and the dark About section, so the band
  # reads as its own block. A dark band here would blend into both neighbours.
  - type: crosslink.html
    section_id: engineering-crosslink
    eyebrow: Hands-on engineering
    title: Already know what you need built?
    text: >-
      If you are past the strategy question and need cloud architecture,
      migration, DevOps, or Kubernetes delivery, that work runs through the
      main site rather than these packages.
    action:
      label: See engineering services
      url: /

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
        url: mailto:ivan@prlic.io?subject=AI Advisory enquiry
      - title: LinkedIn
        icon: fa-linkedin
        icon_type: fab
        url: https://www.linkedin.com/in/iprlic/
---
