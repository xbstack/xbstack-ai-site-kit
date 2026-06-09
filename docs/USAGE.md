# Usage Guide

Welcome to XBSTACK AI Site Kit. This guide will help you build and maintain your content platform.

## 1. Project Initialization

Clone the repository and install dependencies:

```bash
git clone https://github.com/xbstack/xbstack-ai-site-kit.git
cd xbstack-ai-site-kit
npm install
```

## 2. Local Development

Start the development server with hot-reloading:

```bash
npm run dev
```

Visit `http://localhost:4321` to preview your site.

## 3. Content Management

All articles are stored in `src/content/articles/`.

### Creating a New Post

Create a new Markdown or MDX file with the following frontmatter:

```markdown
---
title: "Your Post Title"
description: "A short summary for SEO"
date: 2026-06-09
category: "ai"
tags: ["starter", "tutorial"]
lang: "en"
author: "Your Name"
---
```

## 4. SEO and Quality Audits

Before publishing, run the automated audit scripts:

### SEO Audit
Checks title length, description length, and required metadata:
```bash
npm run audit:seo
```

### Link Validation
Checks for broken internal links and file paths:
```bash
npm run check:links
```

## 5. Deployment

Build the static site:

```bash
npm run build
```

Deploy the `dist/` directory to **Cloudflare Pages**, **Vercel**, or **Netlify**.

---

[Switch to Chinese Version (中文版)](./USAGE.zh.md)
