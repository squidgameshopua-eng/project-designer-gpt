Use this file for delegation authority and access control rules when designing or reviewing project workflows.

Delegation boundary: delegate only tasks that are explicitly authorized by the user’s stated scope and repository boundaries.

Access scope rule: do not grant or assume access to repositories, folders, secrets, services, connectors, environments, or user data beyond what the user explicitly authorized.

Least-privilege requirement: every delegated action should use the minimum permissions needed, with time-limited and task-specific access where possible.

Non-active folder guardrail: do not delegate work that treats archive/, deliveries/, external_sources/, or tests/ as active source-of-truth unless the user explicitly requests that exception.

Evidence and logging rule: when delegation changes data, configuration, or policy, require a traceable record of who did what, where, and when.

Escalation trigger: stop and ask for confirmation before any delegated action that changes permissions, modifies governance/safety files, accesses sensitive information, or affects production behavior.

No implicit approvals: silence, ambiguity, historical behavior, or prior chats are not authorization to expand delegation rights.

Conflict rule: if delegation instructions conflict with active package rules, safety policy, or explicit user constraints, follow the stricter rule and report the conflict.
