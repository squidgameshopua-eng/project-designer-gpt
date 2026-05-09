Use this file only for architecture and domain-boundary decisions. Main Project Instructions control behavior.

Architecture decision must precede prompt writing. Compare Custom GPT, ChatGPT Project, Project plus GPT, several GPTs, GPT plus files/actions/tests, checklist/SOP, decision matrix, or no-GPT/human workflow.

Choose Custom GPT when behavior must be reusable as standalone assistant and Knowledge/reference files are enough. Choose ChatGPT Project when work needs shared context, multiple chats, iterative files, and project-level instructions. Choose Project plus GPT when durable assistant and project workspace both add value.

Split systems when one assistant would be too broad, unsafe, contradictory, untestable, source-conflicted, jurisdiction-conflicted, audience-conflicted, tool-heavy, or maintenance-heavy.

Use no-GPT/SOP when task is deterministic, high-liability without sufficient verification, better handled by human review, or not improved by language-model interaction.

For non-trivial GPT/Project packages define: purpose; target user; real use cases; inputs; outputs; scope; non-goals; boundaries; assumptions; files; sources; tools/capabilities; safety/refusals; clarification; format; tests; deployment verdict.

Full child GPT package normally includes: name; description; target user; core use cases; non-goals; boundaries; main instruction; starters; recommended files; capabilities/tools; source policy; safety rules; formats; clarification/refusal rules; test prompts; checklist; version notes; verdict.

Domain rule: high-stakes legal, medical, psychiatric, financial, regulatory, safety, or platform-compliance GPTs require jurisdiction/context, current source policy, escalation/professional-review boundaries, and refusal rules. For Ukraine/Kryvyi Rih legal/local matters, require current local source verification when material.

File architecture rule: create a new file when a responsibility has its own owner-rule, source freshness, test protocol, child propagation, domain boundary, or reusable reference purpose. Split bloated mixed-purpose files. Merge overlapping files only when one owner-rule controls behavior without reducing testability. Delete only after Patch Lock/deletion burden.

Source architecture: source facts belong in source files with date checked, scope, freshness notes, official links. Source files do not replace behavior in main instruction.

Testing architecture: every system that creates or changes deliverables needs pre-delivery tests. Every system that creates child systems must propagate applicable tests, Patch Lock, and governance.

Decision matrix fields: quality gain; reliability; safety; source honesty; testability; maintainability; user effort; cost/load; reversibility; drift risk; child propagation.

Verdicts: Ready; Ready With Minor Risks; Not Ready; Split Required; More Source Material Required; Unsafe; Invalid Delivery.
