# Intake

Reference file for `research-conventions`. Load it before asking the user anything at the start of a task, and when deciding whether to ask at all.

This file governs clarifying questions only. Checkpoints are different. A pause that a calling skill declares (such as `initiating-coverage`'s one-task-per-request rule) or a review stop that an agent's guardrails require always holds. Nothing here shortens either.

## Read what is already known before composing a question

Before asking, read:

- the conversation so far;
- the project's instructions;
- any memory the host keeps;
- the files the user supplied.

Together they usually settle most of the mandate:

- **mandate and vehicle**
- **benchmark**
- **horizon**
- **risk posture and sizing norms**
- **sectors and geographies in and out of scope**
- **delivery preferences**: format, template, house style, rating ladder

Ask only about the forks they leave open. When the host keeps memory and the user volunteers a durable preference or asks you to remember one, save it, so the next skill inherits it instead of asking again. Starting a task does not count as a reason to save anything. A missing profile never delays the first answer.

## Question limits

Ask at most three questions before substantial work begins, and fewer is better. Each question:

- offers two or three options, with the recommended one first and labelled as recommended;
- says in the option text what the choice changes about the output;
- leaves free text to the interface rather than spending an option on "something else".

Use the host's structured question tool when it has one. When the user skips a question, take the recommended option and disclose it as an assumption.

A calling skill's parameter list says what to settle. It does not make every item a question. Settle what the request and the context already answer, ask about the rest within the limit, and default and disclose anything left over.

## Running headless

In a managed-agent session no one is there to answer. Ask nothing: take the recommended defaults, disclose them in the delivery, and stop wherever the agent's guardrails say to stop.

## Ask once

A preference resolved once holds for the rest of the run and for every skill downstream of it. A skill running as an input to another workflow does not prompt at all. It inherits the caller's answers and returns what it was asked for.

## Present, do not block

Between checkpoints, work in stages. Present each stage as it finishes, say what you are about to build next, and carry on unless the user objects. A finished stage with its assumptions stated gives the user a better place to step in than a question does, and it costs them nothing when the defaults were right.

## Forks worth asking about

Ask when the answer changes what gets built:

- **Workflow.** Which of two plausible deliverables the request means: a screen or a full initiation, a preview or a model update.
- **An artifact the user already has.** Whether to extend their file, rebuild it, or produce a companion. This bears on every workbook and deck task, and guessing wrong wastes the whole build.
- **Mode.** Which mode of a multi-mode skill: a new thesis or a refresh of one, a calendar build or a weekly preview.
- **Scope.** The universe, the peer set, the segment boundary.
- **Horizon.** The valuation or thesis horizon, when the context does not fix it.
- **Framing.** Whether the user wants the case made, the case tested, or both.

Everything outside that list is a default you take and disclose.

## Disclose the defaults you took

Put assumed defaults in the message that delivers the artifact, not inside it. For each one, name the default, say why it was taken, and give the one-line change if it was wrong. Assumptions that bear on the numbers also stay in the artifact, labelled per `evidence.md`.
