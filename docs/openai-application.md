# OpenAI Codex for OSS Application Data

This document contains the suggested answers for the OpenAI Codex for OSS application form.

## GitHub Repository URL
`https://github.com/xbstack/xbstack-ai-site-kit`

## Describe your role
I am the founder and primary maintainer of XBSTACK AI Site Kit. I designed the architecture, maintain the Astro codebase, manage releases, triage issues, review contributions, and maintain the documentation, deployment workflow, SEO utilities, and content automation scripts.

## Why does this project meet the criteria?
XBSTACK AI Site Kit is an actively maintained open-source Astro starter kit for AI engineers and indie developers. It provides reusable templates, content taxonomy, Cloudflare deployment, SEO validation, and maintainer automation workflows. It aims to lower the barrier for technical creators to build fast, SEO-friendly platforms while documenting best practices in AI-native publishing.

## How do you plan to use OpenAI API credits?
I will use API credits for core OSS maintainer workflows: 
1. **Automated Code Review**: Using Codex to review PRs for component regressions and accessibility.
2. **SEO Auditing**: Automating the validation of metadata and frontmatter schemas.
3. **Issue Triage**: Using AI to classify and label community issues.
4. **Release Notes**: Automatically generating high-quality changelogs from commit history.
5. **Security Checks**: Detecting accidentally committed secrets or insecure deployment patterns.
6. **Documentation**: Helping generate and update technical documentation based on code changes.

### Example Codex Prompts
**PR Review**
> Review this PR for Astro build errors, invalid frontmatter, SEO metadata regressions, and accessibility issues. Provide specific actionable feedback.

**Release Notes**
> Generate release notes from merged PRs since the last tag. Categorize by Features, Bug Fixes, and Documentation.

**SEO Audit Fix**
> Fix missing title, description, canonical, and ogImage fields in these content files, ensuring description is under 160 characters.

## Anything else we should know?
The project is connected to the live engineering site xbstack.com, serving as a real-world testing ground for the templates and scripts provided in the kit. We are committed to an "AI-assisted maintenance" philosophy, using Codex to keep the codebase clean, secure, and performant with minimal manual overhead.
