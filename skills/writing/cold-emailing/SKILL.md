---
name: cold-emailing
description: Writes cold emails and DMs a stranger will read and answer. Short, opened on the reader, one proof, one small question, in the sender's own voice. Use when writing, editing, sending, or following up on any cold outreach (job search, sales, partnerships, fundraising, press), or when deciding who to reach out to. Triggers on "cold email," "cold DM," "reach out," "outreach," "follow up," "hiring manager," "intro email."
---

# Cold Emailing

A cold email works when a stranger can read it on one phone screen, see that it was written to them, and answer in one line. Every practice below serves one of those three.

This is for one-to-one email written by hand. It is not for sequences or blasts.

## The email in five moves

1. **Them.** Open on one true, specific thing about the reader. "Saw ..."
2. **A guess.** Say what that probably means for them. "Guessing ..." It shows thought, and a wrong guess still gives them an easy reason to reply.
3. **One proof.** Who the sender is in a sentence, then one thing they did, with a result.
4. **Pressure off.** Say what the sender wants and make it easy to say no. "I want to build this on your team, not sell you anything."
5. **One question** that takes a line to answer. "Who on your team should I talk to?"

Then a first name. About 90 words in all.

```
Subject: fleet software at acme

Hey Sam,

Saw your team is putting AI agents in front of warehouse operators to diagnose fleet issues. Guessing that comes down to knowing what's happening on the floor.

I'm a backend engineer at a freight company. Last year I rewrote our dispatch service and cut route planning from 40 seconds to 3.

I applied for the fleet software role. I want to build this stuff on your team, not sell you anything.

You the right person to talk to?

Riley
```

The people and companies in every example here are invented.

## Get three things before writing

- **A real observation.** Something found, not imagined: their hiring post, a line in the job posting, a talk, a launch. If nothing turns up, use the posting or the company's own page. If even that gives nothing to say, this is the wrong reader.
- **The sender's proof.** One or two things they did, with results, in their words. Ask for it. Never fill a gap with an invented credential.
- **The sender's voice.** Two or three emails they actually sent. Copy the habits: greeting, sentence length, pet phrases, sign-off. Don't upgrade their vocabulary.

## Practices

### Who to write to

- **The person who owns the problem, not the gatekeeper.** For a job that is the hiring manager or the team's tech lead, not a recruiter. For a product it is the person who lives with the problem, then their boss. Gatekeepers get the most cold email and don't make the decision.
- **Follow their own words.** A manager's "we're hiring" post tells you who owns the role and hands you the opening line.
- **Two or three people per organization, at different levels, each with a different opening.** More than that reads as a blast once they compare notes.
- **Look for a warm path first.** Someone who already replied to the sender, interviewed them, or works there beats any stranger.
- **Check what was already sent.** Before naming anyone, search the sender's sent mail for that organization and read whole threads, not previews. Recommending someone already contacted, or sending a third email, costs trust.
- **Agree on the list before drafting.** Show the sender each name, role, why this person, and whether they've been contacted.

### What to say

- **One email, one pitch.** The person (a job), the product (a sale), the company (a raise), or the story (press). Never two at once. A job email that leads with a side project reads as a sales pitch, and the sender ends up writing a second email to explain.
- **Proof is something a stranger can picture or check.** A thing built, a number against a target, a named result. Not a count of projects, years of experience, or an adjective. "Shipped 20+ projects" says nothing. "Cut route planning from 40 seconds to 3" does.
- **One proof, matched to the reader.** Choose the one their team would care about and save the rest for the reply.
- **Ask for something small.** A name is easy to give. A meeting is not. Don't ask to "pick their brain."
- **Never invent.** Not the observation, not a referral, not a number. Don't round up, and don't upgrade a claim: "entered" is not "won," and "I applied" is only for someone who did. No fake "RE:" subject lines. A cold email has nothing going for it but the reader's trust.

### How it should read

- **100 words or fewer, greeting and sign-off included.** Past one phone screen, it doesn't get finished.
- **Short paragraphs and plain words.** Three sentences a paragraph at most, a blank line between, words a high schooler would use. Fragments are fine: "Saw your post." "Guessing that."
- **A subject that looks like a note from a colleague.** Lowercase, three to five words, "topic at company": `fleet software at acme`. No question and no first-name merge.
- **The sender's voice, not a template's.** Their greeting, their pet phrases, their sign-off. Normal capitals in the body even when the subject is lowercase.
- **No links or attachments in the first email.** Some filters flag outside senders who include them, and a link asks for a click before there is any trust. Offer it in the reply.
- **No stock phrases.** "Hope this finds you well," "I love what you're building," "quick question," "I know you're busy."
- **No em dashes, exclamation marks, or signature block.** Sign with a first name.

### Sending

- **The sender reads every draft, and only their "send" sends.** Sending can't be undone. Liking the wording is not an instruction to send, and if the text has to change after they approved it, ask again.
- **Read the draft back from the mailbox before sending.** Mail tools can change text. In November 2026 the Claude Gmail connector was rewriting every link into a `google.com/url` redirect, which is one more reason to leave links out.
- **Check the inbox right before sending.** A reply or a rejection from that organization changes the email.
- **Confirm, then listen.** Each email should sit in Sent once, with no draft left over. A few minutes later, look for bounces and auto-replies. An auto-reply proves the address is live, and "no longer here" often names who to write to instead.
- **Treat looked-up addresses as guesses** until something comes back. Say which ones are unverified, tell the sender what a lookup costs before spending their credits, and keep the sender's own details out of lookup tools unless they say otherwise.
- **Send in the reader's morning** if there's a choice: 7 to 9:30, their time zone.

With the Gmail connector, the calls are `Gmail:create_draft`, `Gmail:get_draft` to read it back, and `Gmail:send_message` with only the `draftId`.

### Following up

- **Once, about five days later, in the same thread.**
- **Bring something new.** A sharper proof, a result, or a correction. If the first email had a flaw, own it in one line. Never "just bumping this."
- **Stop at two.** A third unanswered email reads as pestering. Try a different person or a DM.
- **When someone replies,** answer the same day, about as briefly as they wrote, and thank them with one specific detail. If they point to someone else, write to that person and say who sent you. Now the referral is true.

### DMs

The same five moves in two or three sentences, with no subject and no sign-off. Write the text for the sender to paste unless they ask you to send it.

## Checks

Run these on every email. If one fails, rewrite and run the list again.

```
Before it goes out:
- [ ] 100 words or fewer
- [ ] Opens on the reader, with an observation that was found, not imagined
- [ ] One pitch and one proof, and the proof is something a stranger can check
- [ ] Exactly one question, answerable in one line
- [ ] Every claim about the sender came from the sender
- [ ] No links, attachments, stock phrases, em dashes, exclamation marks, or signature block
- [ ] Subject is three to five lowercase words
- [ ] Sounds like the sender's own emails
- [ ] No two readers at one organization get the same opening
- [ ] The sender has read this exact text and said to send it
```

## More examples

**Product outreach.** The pitch is the product, the proof is a customer result, and the question is about the reader's problem.

```
Subject: after-hours calls at northwind

Hey Dana,

Saw you're hiring a third front-desk person for the Maple Street office. Guessing the phones are the reason.

I build a tool that turns after-hours voicemails into booked appointments. A four-chair practice in Tulsa went from 30 missed calls a week to 4 with it.

You may have this handled already, in which case ignore me.

How are after-hours calls getting booked today?

Riley
```

**Follow-up**, five days after the first example, in the same thread.

```
Hey Sam,

I realized my last email read like a list of things I've done.

The short version: I want to work on fleet software, and yours is the team I'd pick.

One more data point. The dispatch rewrite I mentioned now plans every route for 300 trucks.

Is there someone on your team I should be talking to?

Riley
```

**Before and after.** The usual first draft:

```
Subject: Experienced Engineer Seeking Opportunities!

Dear Hiring Manager,

I hope this email finds you well. I am a passionate backend engineer with 8+ years of experience and a proven track record across 20+ projects. I love what your company is building and would love to pick your brain about how my skills in Python, Go, and Kubernetes could add value. Could we schedule a 30 minute call next week? Also, are you the right person, or should I contact HR? My portfolio: https://example.com

Best regards,
Riley Chen
Senior Backend Engineer | 555-0100
```

The rewrite is the first example on this page. It opens on the reader's team where this one opens on the sender. One result with a number replaces the skills list. One question that takes a line replaces a call request plus a second question. The link, the stock phrases, the exclamation mark, and the signature block are gone, and the subject went from a headline to `fleet software at acme`.

## Where this has limits

- **One-to-one only.** Bulk or automated outreach is marketing email, and the law on it differs by country. Some places require an opt-out line and a postal address, others require consent first. Check the rules for the reader's country before sending a product pitch at any volume.
- **Register travels badly.** "Hey Sam" and sentence fragments fit US tech. For academia, government, or a more formal culture, keep the five moves and raise the formality.
- **The evidence is thin.** These practices come from practitioner advice and one campaign, not from controlled tests. The sender's own reply rates outrank every rule here. If their long emails get answered, write long emails.
- **Wording can't fix fit.** With no real observation and no relevant proof, the answer is a different reader, not a better sentence.

## Sources

- **r/sales, "What's your top performing cold email?"** (Reddit, about 2021). Length under 100 words, short paragraphs, plain words, one question, no links, the small ask, morning sends. Practitioner claims, not measured here.
- **A cold sales email shared as a screenshot** (2026). The observation-then-guess opening, taking the pressure off, and a small, low-stakes ask.
- **Ben Lang, ["15 ideas to help you build a better personal network"](https://nextplayso.substack.com/p/15-ideas-to-help-you-build-a-better)** (next play, April 2026). Be specific about the ask, make it easy for people to help, thank with a specific detail.
- **Field notes from one outreach campaign** (November 2026). The gatekeeper rule, one pitch per email, checking sent mail first, reading drafts back, auto-replies as address checks, and the follow-up cadence.
