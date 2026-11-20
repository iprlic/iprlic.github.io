---
layout: home
permalink: /training/claude-confusions/
lang: en
ref: training-claude-confusions
last_updated: 2026-11-20
sticky_cta:
  label: Book a call
  url: https://calendly.com/prlic/15min
image:
  path: /assets/img/og-image.png
  width: 1200
  height: 630
locale: en_US
title: "Claude Concepts That Get Mixed Up: 14 Pairs Explained"
description: >-
  Caching vs compaction, streaming vs batches, Skills vs MCP, hooks vs permissions: 14 Claude concepts people confuse, with which exam tests each.

header:
  compact: true
  title: Claude concepts that get mixed up
  subtitle: Fourteen pairs that look alike, when to use which, and which exam tests them
  text: >-
    Most wrong answers on the Claude certification exams are not about
    unknown features. They come from two real features that sound alike,
    where the scenario fits one and not the other. Here are the pairs that
    most often decide practice questions, each with a rule of thumb, a short
    example and the exams that test it.
  action:
    label: Start with the API
    url: '#api'
  proof:
    - Checked against Anthropic's documentation
    - Updated 20 November 2026
    - Independent guide, not affiliated with Anthropic

sections:
  - type: course-overview.html
    section_id: api
    background_style: bg-subtle
    title: Calling the Claude API
    text: >-
      Exam codes: CCAO-F Associate, CCDV-F Developer – Foundations, CCAR-F
      Architect – Foundations, CCDV-P Developer – Professional, CCAR-P
      Architect – Professional ([compare them](/training/claude-certifications/)).
    columns:
      - title: Streaming or Message Batches
        text: >-
          **Stream** when a person is waiting: text appears as it is
          generated, and long responses do not hit HTTP timeouts. Normal
          price, normal rate limits.


          **Batch** when nobody is waiting: up to 100,000 requests per batch,
          results within 24 hours (most batches finish within an hour), at
          half the normal price.


          *Example:* the support chat streams; tonight's classification of
          40,000 tickets goes in a batch.


          **Tested in:** CCDV-F, CCAR-F, CCDV-P

      - title: The six stop reasons that matter
        text: >-
          **end_turn**: Claude is done, use the answer. **tool_use**: run
          the tool and send a `tool_result` back. **max_tokens**: your output
          limit cut the answer; raise it or continue. **pause_turn**: a
          server tool loop such as web search hit its iteration limit; send
          the assistant content back unchanged so Claude can continue.
          **refusal**: Claude declined for safety reasons; it arrives as a
          normal response, not an error. **model_context_window_exceeded**:
          the context window is full; treat the output as truncated, and
          shrink the context instead of raising `max_tokens`.


          *Example:* an agent loop that only checks for `end_turn` and
          `tool_use` silently drops work when web search returns `pause_turn`.


          **Tested in:** CCDV-F, CCAR-F, CCDV-P

      - title: "tool_choice: auto, any, tool or none"
        text: >-
          **auto** (the default with tools): Claude decides whether to call a
          tool. **any**: it must call one of your tools. **tool**: it must
          call the one you name. **none**: no tool calls.


          **The caveats:** a forced call (`any` or `tool`) starts the response
          with the tool call, so no text and no thinking come before it.
          Manual extended thinking accepts only `auto` and `none`, and some
          current models reject forced tool use altogether; there, use `auto`
          with strict tools, or structured outputs.


          *Example:* "always call `record_invoice`" is `tool`, where the model
          allows it; otherwise get the record through structured outputs.


          **Tested in:** CCDV-F, CCAR-F

      - title: Prompt caching, context editing or compaction
        text: >-
          **Prompt caching** when the same long prefix (tools, system prompt,
          documents) is sent again within minutes: re-reading it costs a
          fraction of the price and is faster. It changes neither the output
          nor how much of the context window you use.


          **Context editing** when an agent's context fills with old tool
          results or thinking it no longer needs: the API clears them by rule
          before the request reaches Claude.


          **Compaction** when the conversation itself is too long but its
          substance matters: older turns are replaced with a summary Claude
          writes.


          Clearing or summarising changes the prompt prefix, so the cache is
          invalidated from that point; that is the trade-off.


          *Example:* a coding agent caches its tools and instructions, clears
          old file reads, and compacts when the session runs for hours.


          **Tested in:** CCDV-F, CCDV-P, CCAR-P

      - title: Structured outputs or tool use for JSON
        text: >-
          **Structured outputs** (a JSON schema in `output_config.format`)
          when you want Claude's answer itself as JSON: the response is
          constrained to the schema, so it always parses.


          **Strict tool use** (`strict: true` on a tool) when Claude is
          choosing actions and the arguments of each tool call must match the
          tool's schema.


          Forcing a single "fake" tool to get JSON is the older workaround;
          you still meet it in exam scenarios.


          *Example:* extracting fields from an invoice is structured outputs;
          an agent calling `issue_refund` with an amount is a strict tool.


          **Tested in:** CCDV-F, CCAR-F

      - title: Retrieval (RAG), long context or the Files API
        text: >-
          **Long context** when the material fits comfortably in the window
          and the task needs all of it: one contract, one report. Pair it
          with caching if you ask about it repeatedly.


          **Retrieval** when the collection is far larger than the window or
          changes often: fetch only the relevant passages per question, and
          cite them.


          **The Files API** is not a third way to find information. It lets
          you upload a file once and refer to it by `file_id`; its content is
          still billed as input tokens and must fit in the context window.


          *Example:* questions over 20,000 policy documents need retrieval; a
          summary of one 80-page PDF needs long context, uploaded once through
          the Files API if several requests use it.


          **Tested in:** CCDV-F, CCDV-P, CCAR-P

  - type: course-overview.html
    section_id: agents
    title: Agents and extensions
    columns:
      - title: Agent or workflow
        text: >-
          **Workflow** when you can write the steps down in advance: your code
          decides the path (chain, route, run in parallel) and Claude does
          each step. Predictable, cheaper, easier to test.


          **Agent** when the steps depend on what Claude finds along the way:
          Claude chooses the next tool call and decides when it is done. Worth
          it when flexibility matters more than predictability; give it clear
          tools, limits and a stopping condition.


          *Example:* extract, validate and post an invoice is a workflow;
          "find out why this customer's sync fails" is an agent.


          **Tested in:** CCDV-F, CCAR-F, CCAR-P, CCDV-P

      - title: Tool, Skill, MCP server or plugin
        text: >-
          **Tool**: one function Claude can call, defined by a name, a
          description and an input schema.


          **MCP server**: a separate service that exposes tools (and
          resources and prompts) through the Model Context Protocol, so one
          integration with an external system works in any MCP client.


          **Skill**: a folder with a `SKILL.md` and optional scripts and
          files; Claude loads it when the task calls for it. It adds know-how,
          not connectivity.


          **Plugin** (Claude Code): packaging. It bundles skills, subagents,
          hooks and MCP servers into one installable unit, shared through a
          marketplace.


          *Example:* an MCP server connects Claude to Jira, a skill holds your
          ticket triage rules, a plugin ships both to every engineer.


          **Tested in:** CCDV-F, CCAR-F

      - title: Subagent, agent team or Managed Agents session
        text: >-
          **Subagent** when a focused task should run in its own context
          window and only the result matters: it reports a summary back to
          the agent that started it, which keeps the main context clean.


          **Agent team** (Claude Code, experimental) when several workers must
          share findings and challenge each other: a lead, a shared task list,
          teammates messaging each other directly. It uses far more tokens.


          **Managed Agents session** when your product needs a long-running
          agent in hosted infrastructure: you start a session of an agent you
          defined through the API and exchange events with it, without
          building the loop or the sandbox yourself.


          *Example:* compare three libraries in parallel with subagents; let
          five reviewers argue about a root cause as a team; run a nightly
          unattended agent for your customers on Managed Agents.


          **Tested in:** CCAR-F, CCDV-F, CCDV-P

  - type: course-overview.html
    section_id: claude-code
    background_style: bg-subtle
    title: Configuring Claude Code
    columns:
      - title: Hooks, permission rules or the sandbox
        text: >-
          **Permission rules** (allow, ask, deny) decide whether a tool call
          may run at all. They cover every tool and are checked before the
          call.


          **Hooks** run your own command at a lifecycle event, such as before
          or after a tool call, every time and without Claude deciding. Use
          them for what must always happen: block an edit, run the formatter,
          log.


          **The sandbox** limits what Bash commands and their child processes
          can reach on the file system and the network while they run,
          enforced by the operating system. It does not cover the built-in
          file tools, MCP servers or hooks.


          *Example:* deny reading `.env` with a permission rule, run the
          linter after each edit with a hook, stop a build script from
          calling unknown hosts with the sandbox.


          **Tested in:** CCAR-F, CCDV-F, CCDV-P

      - title: CLAUDE.md, rules, Skills or settings.json
        text: >-
          **CLAUDE.md**: instructions loaded in every session, such as build
          commands and conventions. Claude follows them as guidance; nothing
          enforces them.


          **.claude/rules/**: the same kind of instructions in separate files;
          with `paths` in their front matter they load only when Claude works
          on matching files.


          **Skills**: knowledge or workflows loaded on demand, or run with
          `/name`.


          **settings.json**: configuration Claude Code enforces, such as
          permissions, hooks, environment variables and the model.


          *Example:* "use pnpm" goes in CLAUDE.md, test conventions for
          `src/api/**` in a rule, the release checklist in a skill, and "never
          push" as a deny rule in settings.json.


          **Tested in:** CCAR-F, CCDV-F

  - type: course-overview.html
    section_id: quality
    title: Claude apps, quality and the exam itself
    columns:
      - title: Projects, Skills or connectors in Claude
        text: >-
          **Project** when a team works on one topic over time: its
          instructions and knowledge files are there in every chat in that
          project.


          **Skill** when it is a procedure you want in any chat, loaded only
          when the task needs it: your report format, your brand rules.


          **Connector** when Claude needs current data from another
          application or should act in it.


          *Example:* a project for the Q4 tender with the tender documents, a
          skill for your proposal format, a connector to pull this week's
          price list from the shared drive.


          **Tested in:** CCAO-F

      - title: Code-graded, LLM-judged or human evals
        text: >-
          **Code-graded** when a rule can decide: exact match, valid JSON, a
          passing test. Fast, cheap, repeatable; use it wherever you can.


          **LLM as judge** when quality is a matter of judgment but you can
          write it down as a rubric: faithfulness to the source, tone. It
          scales, but calibrate it against human ratings first.


          **Human review** for high stakes, new tasks, and building the
          reference set the other two are checked against.


          *Example:* ticket classification accuracy is graded by code; "is
          this summary faithful to the contract?" by an LLM judge with a
          rubric, spot-checked by the legal team.


          **Tested in:** CCAO-F, CCDV-F, CCDV-P, CCAR-P

      - title: Scaled score or percentage correct
        text: >-
          **The scaled score** decides pass or fail: 100 to 1,000, pass at
          720. Scaling evens out small differences in difficulty between exam
          forms, so 720 is not 72% correct.


          **Percentages** appear on the score report per exam section. Use
          them to find weak domains, not to work out whether you passed.
          Unscored items (10 of 70 on the newer exams, not identified) count
          towards neither.


          *Example:* two candidates with the same number of correct answers
          on different exam forms can get different scaled scores.


          **Tested in:** all five exams (it is how they are scored)
    note: >-
      Practise the pairs on real exam-style questions: the
      [free practice questions on CertDrill](https://certdrill.io/exams/)
      cover every exam. Exam formats change; see the
      [dated log of program changes](/training/claude-certification-changes/).
      Feature details checked against Anthropic's documentation on
      20 November 2026.

  - type: faq.html
    section_id: faq
    background_style: bg-subtle
    title: Questions about these concepts
    items:
      - q: What is the difference between prompt caching, context editing and compaction?
        a: >-
          Prompt caching makes re-sending the same prompt prefix cheaper and
          faster but removes nothing from the context. Context editing clears
          specific content, such as old tool results or thinking blocks, by
          rule before the request reaches Claude. Compaction replaces older
          conversation turns with a summary Claude writes. Caching saves
          money; the other two save context space, and both invalidate the
          cache from the point where they change the prompt.

      - q: Which stop reasons does an agent loop need to handle?
        a: >-
          At least `end_turn` (finished), `tool_use` (run the tool and return
          the result), `max_tokens` (output cut off by your limit),
          `pause_turn` (a server tool loop paused; send the response back to
          continue), `refusal` (Claude declined) and
          `model_context_window_exceeded` (the context window is full, so the
          output is truncated). `stop_sequence` matters only if you set stop
          sequences.

      - q: When should I use the Message Batches API instead of streaming?
        a: >-
          When no one is waiting for the answer. Batches cost half the normal
          price and accept up to 100,000 requests, but results can take up to
          24 hours. Streaming is for interactive use, where the user should
          see the answer as it is written.

      - q: What is the difference between a Skill, an MCP server and a plugin?
        a: >-
          An MCP server connects Claude to an external system and gives it
          tools. A Skill gives Claude instructions and know-how, loaded when a
          task needs them. A plugin, in Claude Code, packages skills,
          subagents, hooks and MCP servers so a team can install them in one
          step.

      - q: Is 720 on a Claude exam the same as 72% correct?
        a: >-
          No. 720 is a scaled score on a range of 100 to 1,000. Scaling
          adjusts for small differences in difficulty between exam forms, so
          there is no fixed percentage that equals a pass. The per-section
          percentages on the score report show where you were weak.

      - q: Is a Claude Academy certificate the same as a Claude certification?
        a: >-
          No. A certificate of completion from Anthropic's public Claude
          Academy shows you finished a course and passed its quiz. A Claude
          certification is a proctored exam at Pearson VUE, scored from 100 to
          1,000 with 720 to pass, valid for 12 months and open only to people
          at Claude Partner Network companies. See
          [who can take the exams](/training/claude-exam-eligibility/).

  - type: contact.html
    section_id: contacts
    title: Learn it properly
    watermark: CLAUDE
    text: >-
      Each of my prep courses covers these distinctions with hands-on labs,
      not slides alone. Tell me which exam your team is aiming for.
    actions:
      - title: Book a Call
        icon: fa-calendar-alt
        url: https://calendly.com/prlic/15min
      - title: ivan@prlic.io
        icon: fa-envelope
        url: mailto:ivan@prlic.io?subject=Claude%20certification%20training
      - title: LinkedIn
        icon: fa-linkedin
        icon_type: fab
        url: https://www.linkedin.com/in/iprlic/
---
