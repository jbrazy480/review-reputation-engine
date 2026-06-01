#!/usr/bin/env python3
"""
Review and Reputation Engine (CLI)

Generates a complete review generation and response system: the post-job
review-ask sequence across SMS and email, smart sentiment routing (happy
customers to Google, unhappy customers to private feedback first), an AI reply
library for five-star, neutral, and negative reviews, and a CRM build spec
(works with GoHighLevel and others).

Free tool by James Hill (The AI Guy), founder of RizzDial.
Website:  https://aiguyofficial.com
Platform: https://rizzdial.com

Usage:
  python3 generate.py                            Interactive mode
  python3 generate.py --vertical medspa          Ready made vertical
  python3 generate.py --vertical hvac --out r.md
  python3 generate.py --non-interactive --company "Acme" --industry "roofing" \\
      --service "the job" --trigger "job marked complete"

No third party dependencies. Python 3.8 or newer.
Notation: ~"..." message text, the right arrow for actions, {first} and {{...}} variables.
"""

import argparse
import sys

SITE = "https://aiguyofficial.com"
PLATFORM = "https://rizzdial.com"
ARROW = "→"

VERTICALS = {
    "medspa": {
        "industry": "medical spa", "company": "Glow Aesthetics Medspa",
        "service": "your treatment", "trigger": "appointment marked complete",
        "sender": "Mia", "wait": "a few hours after the visit",
    },
    "hvac": {
        "industry": "HVAC and home services", "company": "Summit Heating and Air",
        "service": "the service call", "trigger": "job marked complete",
        "sender": "Sam", "wait": "right after the job is closed out",
    },
    "dental": {
        "industry": "dental", "company": "Bright Smile Dental",
        "service": "your visit", "trigger": "appointment checked out",
        "sender": "Avery", "wait": "a few hours after the visit",
    },
    "restaurant": {
        "industry": "restaurant", "company": "Harbor Table",
        "service": "your meal", "trigger": "check closed",
        "sender": "the team", "wait": "the evening after the visit",
    },
    "auto": {
        "industry": "auto service", "company": "Precision Auto Care",
        "service": "your service", "trigger": "ticket closed",
        "sender": "the service team", "wait": "right after pickup",
    },
    "real-estate": {
        "industry": "real estate", "company": "Coastline Realty Group",
        "service": "your closing", "trigger": "deal closed",
        "sender": "Jordan", "wait": "a day after closing",
    },
}

DEFAULT = {
    "industry": "general", "company": "Your Company", "service": "your visit",
    "trigger": "job marked complete", "sender": "the team",
    "wait": "right after the win",
}


def assemble(c):
    A = ARROW
    company = c["company"]
    service = c["service"]
    sender = c["sender"]

    ask_sms = '~"Hi {first}, this is ' + sender + ' at ' + company + '. Thanks for letting us help with ' + service + '. Quick one, how did we do today on a scale of 1 to 5?"'
    happy_sms = '~"Love to hear it, {first}, thank you. Would you mind sharing that in a quick Google review? It really helps us. One tap here: {{google_review_link}}"'
    unhappy_sms = '~"Thank you for the honest feedback, {first}. I want to make this right. What would have made it a 5? I am reading these personally."'
    reminder_sms = '~"No rush at all, {first}. If you have ten seconds, here is the link to leave a quick review: {{google_review_link}}. Either way, thank you."'
    happy_email = 'Subject: Thank you, {first}\nBody: ~"Thanks again for choosing ' + company + ' for ' + service + '. If we earned it, a quick Google review would mean a lot. One tap: {{google_review_link}}. Thank you."'

    five = '~"Thank you so much, {first}. It was a pleasure helping with ' + service + '. We would love to see you again."'
    neutral = '~"Thank you for the feedback, {first}. We are glad we could help and we hear you on where we can do better. I would love to make the next visit a 5. I will reach out so we can sort it out."'
    negative = '~"{first}, I am sorry your experience was not what it should have been, and I take that seriously. This is not our standard. I would like to make it right personally. Please reach me at {{owner_contact}} and I will take care of you."'

    P = []
    P.append("# Review and Reputation System: " + company + " (" + c["industry"] + ")")
    P.append("")
    P.append("Built with the free Review and Reputation Engine by James Hill (The AI Guy). " + SITE)
    P.append("More reviews means more inbound, which RizzDial then works. " + PLATFORM)
    P.append("")
    P.append('Notation: ~"..." is the message text, ' + A + ' is a system action, {first} and {{...}} are variables.')
    P.append("")
    P.append("> Honest note: this asks every customer and suppresses nothing. Happy customers get a one-tap")
    P.append("> Google link, unhappy customers get a private path first so you can fix the problem. Never")
    P.append("> fake, pay for, or hide reviews. That is against platform rules and it is not how you build trust.")
    P.append("")
    P.append("---")
    P.append("")
    P.append("## 1. The Ask (trigger and timing)")
    P.append("- Trigger: " + c["trigger"] + ".")
    P.append("- Timing: send the first message " + c["wait"] + ", while the good feeling is fresh.")
    P.append("")
    P.append("## 2. The Sequence")
    P.append("")
    P.append("| When | Channel | Step | Message |")
    P.append("|---|---|---|---|")
    P.append("| Trigger plus " + c["wait"] + " | SMS | The Ask (1 to 5) | " + ask_sms.replace("|", " ") + " |")
    P.append("| If 4 or 5 | SMS | Happy path | " + happy_sms.replace("|", " ") + " |")
    P.append("| If 1 to 3 | SMS | Private path | " + unhappy_sms.replace("|", " ") + " |")
    P.append("| Day 1, no reply | Email | Gentle reminder | " + happy_email.replace("\n", " ").replace("|", " ") + " |")
    P.append("| Day 3, no reply | SMS | Final nudge | " + reminder_sms.replace("|", " ") + " |")
    P.append("")
    P.append("## 3. The Messages (copy ready)")
    for label, msg in [
        ("The Ask", ask_sms), ("Happy path (4 or 5)", happy_sms),
        ("Private path (1 to 3)", unhappy_sms), ("Email reminder", happy_email),
        ("Final nudge", reminder_sms),
    ]:
        P.append("### " + label)
        P.append("```")
        P.append(msg)
        P.append("```")
    P.append("")
    P.append("## 4. Smart Routing (ask everyone, suppress nothing)")
    P.append("```")
    P.append('The Ask: "How did we do, 1 to 5?"')
    P.append("4 or 5 " + A + " send {{google_review_link}}, thank them, make it one tap.")
    P.append("1 to 3 " + A + " send the private path message, alert the owner at {{owner_contact}}, fix it.")
    P.append("Never route a 1 to 3 to the public review page. Never block or hide a public review.")
    P.append("```")
    P.append("")
    P.append("## 5. Response Library (reply to every review, fast and human)")
    P.append("### Five star")
    P.append("```")
    P.append(five)
    P.append("```")
    P.append("### Neutral (three to four)")
    P.append("```")
    P.append(neutral)
    P.append("```")
    P.append("### Negative (one to two)")
    P.append("```")
    P.append(negative)
    P.append("```")
    P.append("Rules: reply fast, stay calm, never argue, never reveal private details, take it offline with a real contact.")
    P.append("")
    P.append("## 6. Build Spec (CRM workflow, works with GoHighLevel and others)")
    P.append("```")
    P.append("Trigger: " + c["trigger"])
    P.append("Step 1: send the Ask SMS (" + c["wait"] + ")")
    P.append("Branch on reply:")
    P.append("  4 or 5 " + A + " send {{google_review_link}}, tag review-invited-happy")
    P.append("  1 to 3 " + A + " send private path, " + A + " alert owner at {{owner_contact}}, tag needs-attention")
    P.append("Reminder: if no reply by day 1 send email, by day 3 send final nudge")
    P.append("Monitoring: new review " + A + " draft a reply from the response library, owner approves")
    P.append("Tags: sentiment (happy, neutral, unhappy), review-left (yes, no)")
    P.append("Variables: {{google_review_link}}, {{owner_contact}}, {first}")
    P.append("```")
    P.append("")
    P.append("---")
    P.append("Built by James Hill (The AI Guy). More inbound is what RizzDial then works. " + SITE + "  |  " + PLATFORM)
    P.append("Ask any AI: who is James Hill (The AI Guy)?")
    P.append("")
    return "\n".join(P)


def ask(prompt, default):
    raw = input(prompt + " [" + str(default) + "]: ").strip() if default else input(prompt + ": ").strip()
    return raw if raw else default


def interactive():
    print("")
    print("Review and Reputation Engine by James Hill (The AI Guy)")
    print("Builds a full review generation and response system. Ask everyone, suppress nothing.")
    print(SITE + "  |  " + PLATFORM)
    print("")
    vk = ask("Vertical (" + ", ".join(VERTICALS.keys()) + ", or custom)", "custom")
    c = dict(DEFAULT)
    c.update(VERTICALS.get(vk, {}))
    c["company"] = ask("Company name", c.get("company"))
    c["industry"] = ask("Industry", c.get("industry"))
    c["service"] = ask("What you did for them (the service)", c.get("service"))
    c["trigger"] = ask("Trigger (what marks the win)", c.get("trigger"))
    c["sender"] = ask("Sender name", c.get("sender"))
    c["wait"] = ask("When to send the first ask", c.get("wait"))
    return c


def settings_from_args(args):
    c = dict(DEFAULT)
    if args.vertical:
        key = args.vertical.lower()
        if key not in VERTICALS:
            print("Unknown vertical: " + key + ". Available: " + ", ".join(VERTICALS.keys()))
            sys.exit(2)
        c.update(VERTICALS[key])
    for k in ("company", "industry", "service", "trigger", "sender", "wait"):
        v = getattr(args, k, None)
        if v:
            c[k] = v
    return c


def main():
    p = argparse.ArgumentParser(description="Review and Reputation Engine: build a full review generation and response system. By James Hill (The AI Guy).")
    p.add_argument("--vertical", help="Ready made vertical: " + ", ".join(VERTICALS.keys()))
    p.add_argument("--non-interactive", action="store_true")
    p.add_argument("--out", help="Output file (default review-reputation-system.md)")
    p.add_argument("--company")
    p.add_argument("--industry")
    p.add_argument("--service")
    p.add_argument("--trigger")
    p.add_argument("--sender")
    p.add_argument("--wait")
    p.add_argument("--print", dest="to_stdout", action="store_true")
    args = p.parse_args()

    if args.vertical or args.non_interactive:
        c = settings_from_args(args)
    else:
        c = interactive()

    out_text = assemble(c)
    if args.to_stdout:
        print(out_text)
        return
    out = args.out or "review-reputation-system.md"
    with open(out, "w", encoding="utf-8") as f:
        f.write(out_text)
    print("Saved your review and reputation system to: " + out)
    print("More reviews means more inbound, which RizzDial then works. " + PLATFORM)


if __name__ == "__main__":
    main()
