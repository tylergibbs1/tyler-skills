---
name: cold-emailing
description: Finds the right person, drafts a short cold email or DM in the user's own voice, and sends from Gmail only on their say-so. Use for any cold outreach, a follow-up on unanswered emails, or a "who should I reach out to" question, whether the pitch is a job or a product. Triggers on "cold email," "cold DM," "reach out," "hiring manager," "outreach," "follow up."
---

# Cold Emailing

A good cold email is about 90 words from one specific person to another. It opens on the reader, gives one piece of proof, and ends on one question that takes a line to answer. The steps below protect that, and make sure nothing goes out that the user has not read.

## Workflow

Copy this checklist and check items off as you go:

```
Cold email progress:
- [ ] 1. Decide the pitch
- [ ] 2. Pick the readers
- [ ] 3. Check what the user already sent
- [ ] 4. Find the address and one real observation
- [ ] 5. Write the email
- [ ] 6. Run the email checks
- [ ] 7. Save Gmail drafts and read each one back
- [ ] 8. Send only when the user says to
- [ ] 9. Confirm delivery
- [ ] 10. Follow up once
```

- **New outreach?** Run all ten steps.
- **Follow-up on earlier emails?** Run step 3, then step 10, then steps 6 to 9.
- **Wording help on a draft the user wrote?** Run steps 5 and 6 only.

Steps 1 to 6 are judgment. Steps 7 to 9 are fragile, so run them exactly as written. If a connector (Gmail, Clay, Exa) is missing, say which one and keep going with what you have: web search for hiring posts, and the email text in chat for the user to send themselves.

## The user's profile

The email is only as good as what you know about the person sending it. Before step 5, read `references/profile.md`. It holds who the user is in one sentence, their proof lines, emails they have sent, and what must not be said. The file is gitignored, so it can name a real employer and real numbers without publishing them.

If it is missing, ask the user for the items in `references/profile.example.md`, draft from their answers, and offer to save them as `references/profile.md`. Never fill a gap with an invented credential.

## 1. Decide the pitch

One email carries one pitch.

- **Job outreach pitches the person.** Anything they built is one line of proof, and the closing question is about the role or who to talk to. No demo offers. A job email that leads with a side project reads as a sales pitch, and the user ends up writing a second email to say they wanted a job.
- **Product outreach pitches the product.** The user is the credential, and the question is about the reader's problem.

If you can't tell which one this is, ask before drafting.

## 2. Pick the readers

For a job, email the people who feel the open role. Skip recruiters: they get the most cold email and can only route it.

1. The manager who owns the role. Look for their own "I'm hiring" post.
2. The tech lead or a senior engineer on that team.
3. The director or head of the org.
4. A senior engineer one team over, who can give a name.

For a product, email the person who lives with the problem, then their manager.

Pick two or three readers per company, at different levels. More than that looks like a blast once they compare notes. Find them with `Exa:web_search_exa` (people search and LinkedIn posts), and use `Clay:search-contacts-by-name` when Exa can't open a profile. If the user shares an application tracker, start from the roles still pending, and write "I applied" only when the tracker or a confirmation email shows it.

## 3. Check what the user already sent

Do this before recommending anyone. A list that includes someone the user already emailed costs their trust in the rest of it.

- Run `Gmail:search_threads` with `in:sent to:company.com`, then `Gmail:get_thread` on every hit. Search previews show only the oldest messages in a thread, so a preview can hide a follow-up or a reply.
- Search the inbox for replies, bounces, and auto-replies from the same domain. An auto-reply saying someone left often names the team to ask for.

| What Gmail shows | Status |
|---|---|
| Nothing sent | New |
| One email, under five days old | Wait |
| One email, five or more days old, no reply | Follow-up due |
| Two emails, no reply | Stop. Pick someone else on the team |
| A bounce, or "no longer here" | Dead address. Pick someone else |

## 4. Find the address and one real observation

**Address.** `Clay:add-contact-data-points` with the Email data point spends the user's Clay credits, so tell them how many lookups you ran. Apollo quotes a credit cost before it spends: pass that to the user and wait for a yes. These addresses are reported, not verified. Flag the ones that look like guesses. Only a reply or an auto-reply proves an address is live. Keep the user's own email address and personal details out of lookup tools unless they approve.

**Observation.** One true, specific thing about the reader's team that you found in this session: their hiring post, a line in the job posting, a talk, a launch. Never invent one, and never imply a referral or a relationship that isn't real. If nothing turns up, use the job posting.

Before drafting, show the user a table: name, title, why this reader, address or profile, and status.

## 5. Write the email

Five moves, in order:

1. **Them.** "Saw ..." and the observation.
2. **A guess.** "Guessing ..." and what that probably means for them. It shows the user thought about their problem, and it invites a correction.
3. **One proof.** Who the user is in a sentence, then one thing they did, with a result. Take both from the profile, word for word where it gives a line.
4. **Pressure off.** What the user wants, and that they aren't selling. "I applied for the fleet software role. I want to build this stuff on your team, not sell you anything."
5. **One question** that takes a line to answer. "You the right person to talk to?" "Who on your team should I talk to?" A name is easy to give. A meeting is not.

End with the user's first name on its own line and nothing after it.

**Subject.** Lowercase, three to five words, in the form "topic at company": `fleet software at acme`. A capital on the company name is fine. No question, no first name, no fake "RE:".

**Voice.** The profile's samples come first. Copy the user's greeting, sentence length, pet phrases, and sign-off, and don't upgrade their vocabulary. Where the samples are silent, default to:

- "Hey {first name}," using the name the reader goes by, then a blank line.
- Short paragraphs, three sentences at most, with a blank line between. The whole email fits on one phone screen.
- Contractions and fragments. "Saw your post." "Guessing that."
- Words a high schooler would use.
- Normal capitals in the body. Only the subject is lowercase, even when another style rule says to write everything in lowercase.
- No em dashes and no exclamation marks.

**Keep out of the email:**

- Links and attachments. Some corporate filters flag outside senders who include them, and the Gmail connector mangles links (step 7). If the user wants a link in the email, they type it in Gmail themselves.
- Resume-speak. Counts of projects, years of experience, "passionate," "proven track record." A line like "shipped 20+ projects across the stack" is trite and bland. Proof is something a stranger can picture or check.
- Stock phrases. "Hope this finds you well," "I love what you're building," "pick your brain," "quick question," "I know you're busy."
- A second question, a second proof, or a list of skills.
- A signature block, title, or phone number.

**Proof rules.** One proof per email, matched to the reader's team. Don't round a number, upgrade a claim ("entered" is not "won"), or add a time word that isn't true.

## 6. Run the email checks

```
Email checks:
- [ ] 100 words or fewer, greeting and sign-off included
- [ ] First paragraph is about the reader, and the observation was found this session
- [ ] One proof that a stranger can picture or check
- [ ] Exactly one question mark, on a question that takes a line to answer
- [ ] No links, attachments, em dashes, exclamation marks, or signature block
- [ ] No resume-speak or stock phrases
- [ ] Subject is three to five words, lowercase apart from the company name
- [ ] No two readers on the same team get the same opening
- [ ] Every claim about the user comes from the profile or from the user
```

If a check fails, rewrite and run the whole list again. Move on only when every box is checked.

## Examples

The sender, readers, and companies here are invented.

**Example 1: job outreach.** Reader: tech lead on a warehouse fleet software team. Observation: the job posting says the team is putting AI agents in front of operators.

Subject: `fleet software at acme`

```
Hey Sam,

Saw your team is putting AI agents in front of warehouse operators to diagnose fleet issues. Guessing that comes down to knowing what's happening on the floor.

I'm a backend engineer at a freight company. Last year I rewrote our dispatch service and cut route planning from 40 seconds to 3.

I applied for the fleet software role. I want to build this stuff on your team, not sell you anything.

You the right person to talk to?

Riley
```

**Example 2: product outreach.** Reader: operations manager at a dental group who posted a third front-desk opening.

Subject: `after-hours calls at northwind`

```
Hey Dana,

Saw you're hiring a third front-desk person for the Maple Street office. Guessing the phones are the reason.

I build a tool that turns after-hours voicemails into booked appointments. A four-chair practice in Tulsa went from 30 missed calls a week to 4 with it.

You may have this handled already, in which case ignore me.

How are after-hours calls getting booked today?

Riley
```

**Example 3: follow-up**, five days after Example 1, in the same thread.

```
Hey Sam,

I realized my last email read like a list of things I've done.

The short version: I want to work on fleet software, and yours is the team I'd pick.

One more data point. The dispatch rewrite I mentioned now plans every route for 300 trucks.

Is there someone on your team I should be talking to?

Riley
```

## 7. Save Gmail drafts and read each one back

1. Call `Gmail:create_draft` with `to`, `subject`, and a plain-text `body`. One reader per draft, no cc or bcc, no Markdown, and no `htmlBody`.
2. Call `Gmail:get_draft`, then compare the `to` address, subject, and body against what you wrote.
3. To fix a draft, call `Gmail:update_draft` with the `draftId` and the new `body` (the address and subject carry over), then read it back again.

**Known problem, observed November 2026.** The Claude Gmail connector rewrites any URL or bare domain in a draft into a `google.com/url?q=...` redirect. In `body`, the redirect URL replaces the visible text. In `htmlBody`, the text looks right but the link points at a Google redirect carrying a token that expires in about a day, which a corporate filter or a careful reader can take for phishing. So drafts carry no links, and disguising the domain to slip past the rewrite is not an option. Before trusting a link again, test it on one draft and look for `google.com/url` in the read-back.

Tell the user the drafts are in Gmail and show them the text of each. They read every one before anything goes out.

## 8. Send only when the user says to

A sent email can't be pulled back, so sending needs a clear instruction from the user in the conversation, like "send them." Liking the wording is not that instruction.

Right before sending:

1. Search the inbox for anything new from the readers' domains. A reply or a rejection changes the email.
2. Call `Gmail:get_draft` on each draft one last time.
3. Call `Gmail:send_message` with only the `draftId`.

If the text has to change from what the user approved, tell them what and why, and get a yes first.

Suggest 7 to 9:30 AM in the reader's time zone, when most people clear their inbox. Say so once. If the user says now, send now.

## 9. Confirm delivery

1. Call `Gmail:search_threads` with `in:sent` and each reader's address. Each email should appear once.
2. Call `Gmail:list_drafts`. Nothing should be left over.
3. Wait two or three minutes, since a bad address usually bounces within a minute or two. Then search the inbox with today's date: `{from:mailer-daemon from:postmaster subject:"Automatic reply" from:company.com} after:YYYY/MM/DD -in:sent`.
4. Read every auto-reply and check its dates against a calendar. A stale out-of-office still proves the address is live.

Report to the user in this order: who it went to, anything that differs from what they approved, bounces, auto-replies, and the follow-up date.

## 10. Follow up once

About five days after the first email, or on the user's own cadence if the profile gives one, reply in the same thread.

- Draft it with `Gmail:create_draft`, with `replyToMessageId` set to the id of the user's first message and `to` set to the same reader. Read it back and confirm it goes to the reader and not to the user.
- Three or four short paragraphs. If the first email had a flaw, own it in one line. Add one new thing, such as a sharper proof or a result, and end on one question. Example 3 is the model.
- Skip "just bumping this" and "circling back."
- Run the step 6 checks, except the one about the opening. A follow-up can open on the earlier email instead of an observation.
- Two emails per reader is the limit, because a third unanswered email reads as pestering. After that, pick someone else on the team or write a DM.

**When someone replies,** tell the user right away and draft an answer the same day, about as short as theirs. Thank them with one specific detail from what they said. If they point to someone else, email that person and say who sent the user, since now the referral is true. If they ask something personal, such as a side company, a notice period, or pay, ask the user how they want to answer.

## DMs

For LinkedIn or X, use the same five moves in two or three sentences, with no subject and no sign-off. Write the text for the user to paste. Don't send a DM through a browser unless they ask.

## Reference files

- **`references/profile.example.md`**: The template for the user's profile, filled with invented details. Copy it to `references/profile.md` and replace every line.
- **`references/profile.md`**: The real profile. Gitignored and never committed. Read it before writing any email.
