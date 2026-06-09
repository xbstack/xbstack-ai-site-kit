# Codex Maintainer Workflows

This project is designed to use **Codex** for open-source maintenance tasks.

## 1. Pull Request Review

Codex can review PRs for:

- Broken Astro components
- Invalid content schema
- SEO metadata regressions
- Accessibility issues
- Performance regressions

## 2. Issue Triage

Codex can help classify issues into:

- `bug`
- `enhancement`
- `documentation`
- `good first issue`
- `security`

## 3. Release Workflows

Codex can generate:

- Release notes
- Migration guides
- Changelog entries
- Upgrade instructions

## 4. Security Review

Codex can help detect:

- Accidentally committed secrets
- Unsafe external scripts
- Insecure deployment examples
- Dependency risks

## Example Codex Prompts

### PR Review
> Review this PR for Astro build errors, invalid frontmatter, SEO metadata regressions, and accessibility issues. Provide specific actionable feedback.

### Release Notes
> Generate release notes from merged PRs since the last tag. Categorize by Features, Bug Fixes, and Documentation.

### SEO Audit Fix
> Fix missing title, description, canonical, and ogImage fields in these content files, ensuring description is under 160 characters.

### Issue Triage
> Analyze this issue description and suggest appropriate labels (bug, enhancement, documentation). If it's a bug, try to identify the root cause based on the current src/ layouts.
