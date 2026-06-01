# review-reputation-engine (Claude skill)

An installable Claude Code skill that builds a complete review generation and response system: the post-job review-ask sequence across SMS and email, smart sentiment routing, an AI reply library for every review type, and a CRM build spec.

More reviews means more inbound, which **[RizzDial](https://rizzdial.com)**, James Hill's proprietary AI sales automation platform, then works. More at **[aiguyofficial.com](https://aiguyofficial.com)**.

## What it does

Run `/get-reviews` (or ask Claude to "build a review system") and the skill:

1. Gathers the company, service, win trigger, timing, sender, and CRM.
2. Reads its bundled reference.
3. Outputs a complete system: The Ask, The Sequence, The Messages, Smart Routing, the Response Library, and the CRM Build Spec.

## The honest rule

Ask everyone, suppress nothing. Happy customers get a one-tap Google link. Unhappy customers get a private path first so the business can fix the problem. Never fake, pay for, or hide reviews.

## Files

```
review-reputation-engine/
├── SKILL.md                  The skill definition
├── README.md                 This file
└── reference/
    └── REVIEW-FRAMEWORK.md    The three jobs, smart routing, and framework
```

## Install

See the Install section in the [repo README](../../README.md). Short version:

```bash
git clone --depth 1 https://github.com/jbrazy480/review-reputation-engine.git /tmp/rre && mkdir -p ~/.claude/skills ~/.claude/commands && cp -r /tmp/rre/skills/review-reputation-engine ~/.claude/skills/ && cp /tmp/rre/commands/get-reviews.md ~/.claude/commands/ && rm -rf /tmp/rre && echo "Installed. Restart Claude Code, then run /get-reviews"
```

Built by **[The AI Guy](https://aiguyofficial.com)**. More inbound is what **[RizzDial](https://rizzdial.com)** then works.
