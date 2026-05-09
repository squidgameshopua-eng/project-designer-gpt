Use this file only for OpenAI GPT/Project/source facts and freshness notes. Main Project/GPT Instructions control behavior. Verify current official sources again when material, because OpenAI product limits and UI behavior can change.

Date checked: 2026-05-08.

Official source: OpenAI Help, “Projects in ChatGPT”
URL: https://help.openai.com/en/articles/10169521-projects-in-chatgpt
Checked facts: Projects have project-level instructions; project file limits vary by plan. The article currently says only 10 files can be uploaded at the same time; Free 5 files per project; Go/Plus 25 files; Edu/Pro/Business/Enterprise 40 files. The article describes project memory and that project instructions apply inside projects.
Usage rule: use for current Project behavior/limits only after rechecking if the exact limit matters.

Official source: OpenAI Help, “Creating and editing GPTs”
URL: https://help.openai.com/en/articles/8554397-creating-and-editing-gpts
Checked facts: GPT Instructions define how a GPT behaves. Knowledge files provide source/reference material, not the main behavioral rules. GPT Knowledge supports up to 20 files; each file up to 512 MB. OpenAI recommends explicit step structure for multi-step workflows and testing GPTs in Preview.
Usage rule: behavior belongs in GPT Instructions; Knowledge files may support facts, examples, templates, and reference material.

Official source: OpenAI Help, “File Uploads FAQ”
URL: https://help.openai.com/en/articles/8555545-file-uploads-faq
Checked facts: all files uploaded to GPT or ChatGPT conversation have hard 512 MB per-file limit; text/document files are capped at 2M tokens; CSV/spreadsheets about 50 MB depending on row size; images 20 MB. This article also currently says updated Project file limits include Plus up to 20 files per project and Pro/Team/Education/Business up to 40.
Usage rule: because this conflicts with “Projects in ChatGPT” on Plus project-file count, state the conflict and prefer the more conservative limit when designing packages unless current UI confirms otherwise.

Official source: OpenAI Help, “File storage and Library in ChatGPT”
URL: https://help.openai.com/en/articles/20001052-file-storage-and-library-in-chatgpt
Checked facts: confirms 512 MB file limit; 2M-token text/document cap; ~50 MB spreadsheet limit; 20 MB image limit; library/storage behavior may vary by region/plan.
Usage rule: use for file-size claims, not as authority for instruction behavior.

Instruction limit note: The user provided UI screenshot evidence that the project instruction field rejects text over 8000 characters. No official public source was found in this package proving the exact 8000-character Project Instruction limit. Treat 8000 as UI/account evidence, not universal OpenAI documentation.

Package design implication for this project: keep active source files comfortably under 20 files when possible because official sources conflict between 20 and 25 Plus project files. Current package uses 13 active source files plus Project Instructions, under both limits.
