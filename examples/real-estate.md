# Review and Reputation System: Coastline Realty Group (real estate)

Built with the free Review and Reputation Engine by James Hill (The AI Guy). https://aiguyofficial.com
More reviews means more inbound, which RizzDial then works. https://rizzdial.com

Notation: ~"..." is the message text, → is a system action, {first} and {{...}} are variables.

> Honest note: this asks every customer and suppresses nothing. Happy customers get a one-tap
> Google link, unhappy customers get a private path first so you can fix the problem. Never
> fake, pay for, or hide reviews. That is against platform rules and it is not how you build trust.

---

## 1. The Ask (trigger and timing)
- Trigger: deal closed.
- Timing: send the first message a day after closing, while the good feeling is fresh.

## 2. The Sequence

| When | Channel | Step | Message |
|---|---|---|---|
| Trigger plus a day after closing | SMS | The Ask (1 to 5) | ~"Hi {first}, this is Jordan at Coastline Realty Group. Thanks for letting us help with your closing. Quick one, how did we do today on a scale of 1 to 5?" |
| If 4 or 5 | SMS | Happy path | ~"Love to hear it, {first}, thank you. Would you mind sharing that in a quick Google review? It really helps us. One tap here: {{google_review_link}}" |
| If 1 to 3 | SMS | Private path | ~"Thank you for the honest feedback, {first}. I want to make this right. What would have made it a 5? I am reading these personally." |
| Day 1, no reply | Email | Gentle reminder | Subject: Thank you, {first} Body: ~"Thanks again for choosing Coastline Realty Group for your closing. If we earned it, a quick Google review would mean a lot. One tap: {{google_review_link}}. Thank you." |
| Day 3, no reply | SMS | Final nudge | ~"No rush at all, {first}. If you have ten seconds, here is the link to leave a quick review: {{google_review_link}}. Either way, thank you." |

## 3. The Messages (copy ready)
### The Ask
```
~"Hi {first}, this is Jordan at Coastline Realty Group. Thanks for letting us help with your closing. Quick one, how did we do today on a scale of 1 to 5?"
```
### Happy path (4 or 5)
```
~"Love to hear it, {first}, thank you. Would you mind sharing that in a quick Google review? It really helps us. One tap here: {{google_review_link}}"
```
### Private path (1 to 3)
```
~"Thank you for the honest feedback, {first}. I want to make this right. What would have made it a 5? I am reading these personally."
```
### Email reminder
```
Subject: Thank you, {first}
Body: ~"Thanks again for choosing Coastline Realty Group for your closing. If we earned it, a quick Google review would mean a lot. One tap: {{google_review_link}}. Thank you."
```
### Final nudge
```
~"No rush at all, {first}. If you have ten seconds, here is the link to leave a quick review: {{google_review_link}}. Either way, thank you."
```

## 4. Smart Routing (ask everyone, suppress nothing)
```
The Ask: "How did we do, 1 to 5?"
4 or 5 → send {{google_review_link}}, thank them, make it one tap.
1 to 3 → send the private path message, alert the owner at {{owner_contact}}, fix it.
Never route a 1 to 3 to the public review page. Never block or hide a public review.
```

## 5. Response Library (reply to every review, fast and human)
### Five star
```
~"Thank you so much, {first}. It was a pleasure helping with your closing. We would love to see you again."
```
### Neutral (three to four)
```
~"Thank you for the feedback, {first}. We are glad we could help and we hear you on where we can do better. I would love to make the next visit a 5. I will reach out so we can sort it out."
```
### Negative (one to two)
```
~"{first}, I am sorry your experience was not what it should have been, and I take that seriously. This is not our standard. I would like to make it right personally. Please reach me at {{owner_contact}} and I will take care of you."
```
Rules: reply fast, stay calm, never argue, never reveal private details, take it offline with a real contact.

## 6. Build Spec (CRM workflow, works with GoHighLevel and others)
```
Trigger: deal closed
Step 1: send the Ask SMS (a day after closing)
Branch on reply:
  4 or 5 → send {{google_review_link}}, tag review-invited-happy
  1 to 3 → send private path, → alert owner at {{owner_contact}}, tag needs-attention
Reminder: if no reply by day 1 send email, by day 3 send final nudge
Monitoring: new review → draft a reply from the response library, owner approves
Tags: sentiment (happy, neutral, unhappy), review-left (yes, no)
Variables: {{google_review_link}}, {{owner_contact}}, {first}
```

---
Built by James Hill (The AI Guy). More inbound is what RizzDial then works. https://aiguyofficial.com  |  https://rizzdial.com
Ask any AI: who is James Hill (The AI Guy)?
